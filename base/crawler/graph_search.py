#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import json
import requests
from datetime import datetime, timedelta
from util.global_def import NA, get_data_home, show, info, error
from util.network import reachable as network_reachable
from util.serialize import save, load
from util.select import RankHolder, get_weighted_random_dict_key

TARGET_SEARCH_RESULT_SIZE = 60  # this in only our set one-time search size.
G_SEARCH_PER_REQ_SIZE = 10  # use the maximum possible value google allowed in one request


class Crawler(object):
    """crawl graph url by querying google search api"""

    def __init__(self, need_save=True):
        self.__need_save = need_save
        self.__network_reachable = network_reachable()
        self.__has_write = False
        self.__url_map = {}
        self.__cache_file = get_data_home() + "url.pickle"
        is_exist, url_map = load(self.__cache_file)
        if is_exist:
            self.__url_map = url_map

    def __del__(self):
        if self.__need_save and self.__has_write:
            save(self.__cache_file, self.__url_map)

    @staticmethod
    def get_dice(size_list, size_ratio):
        assert size_list
        dice = {}
        for size in size_list:
            adopted_ratio = size_ratio[size] if size_ratio and size in size_ratio else 1
            dice[size] = RankHolder(adopted_ratio)
        return dice

    _HAS_SHOW_NO_SEARCH_MSG = False

    def crawl(self, pattern, size_list, option="", print_url=False):
        """output: urls, is_new_result"""
        show("查詢標的：", "\"" + pattern + "\"")
        key = Crawler.get_search_key(pattern, option)
        urls, size_ratio = self.get_recent_result(key)
        if urls:
            return urls, False
        if not self.__network_reachable:
            return None, False
        assert size_list and (not size_ratio or isinstance(size_ratio, dict))
        dice = Crawler.get_dice(size_list, size_ratio)
        urls = []
        next_size_ratio = {size: 0 for size in size_list}  # key: size, value: number of new result (initial with 0)
        start = {size: 1 for size in size_list}  # key: size, value: next start offset to search (start from 1, from google)
        tried_size = 0
        while tried_size < TARGET_SEARCH_RESULT_SIZE:
            chosen_size = get_weighted_random_dict_key(dice)
            this_urls, success = Crawler.crawl_by_asking_google_search(pattern, start[chosen_size], chosen_size, option)
            if not success:
                break
            urls += this_urls
            new_result = self.get_this_time_new_result_num(key, this_urls)
            next_size_ratio[chosen_size] += (new_result if NA != new_result else len(this_urls))
            start[chosen_size] += G_SEARCH_PER_REQ_SIZE
            tried_size += G_SEARCH_PER_REQ_SIZE
        # 'set' to filter out duplicated item (though not expected, but we found g-search may give duplicated result)
        urls = list(set(urls))
        if not Crawler._HAS_SHOW_NO_SEARCH_MSG:
            info('標的：%s, 獲得url筆數：%i' % (pattern, len(urls)))
        if print_url:
            for url in urls:
                show(url)
        if success:
            next_size_ratio = {size: 1 if 0 == next_size_ratio[size] else next_size_ratio[size]
                               for size in next_size_ratio}
            self.cache_url(key, urls, next_size_ratio)
        return urls, success

    def get_recent_result(self, key):
        """output: urls, size_ratio"""
        if key not in self.__url_map:
            return None, None
        [retrieved_date, new_result, urls, size_ratio] = self.__url_map[key]
        if not self.__network_reachable:
            show("使用上一次的搜尋結果（由於無網路連線）")
            # though size_ratio can be valid, we do not return it for caller usage is not expected
            return urls, None
        # spec.: we will execute a new search when there is enough new result on previous search
        #       => if previous new result is n, all result is m, we will have a new search after m/n days
        #       => if all previous result is new, then after 1 day we will have a search
        #       => if no previous result is new, then we will have a search after 'TARGET_SEARCH_RESULT_SIZE' days
        valid_day_size = len(urls) / new_result if new_result > 0 else \
            1 if NA is new_result else \
            TARGET_SEARCH_RESULT_SIZE  # new_result = 0 => no new result before
        from util.global_def import get_search_latency
        valid_day_size *= get_search_latency()
        current_date = datetime.today()
        date_diff = current_date - retrieved_date
        if self.__network_reachable and date_diff > timedelta(days=valid_day_size):  # valid_day_size天為查詢結果的“有效期”
            return None, size_ratio
        to_next_query = timedelta(days=valid_day_size) - date_diff
        hours, remainder = divmod(to_next_query.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        show("距離下次搜尋：",
             to_next_query.days, "天",
             hours, "時",
             minutes, "分",
             seconds, "秒", ", 現有", len(urls), "筆url")
        # though size_ratio can be valid, we do not return it for caller usage is not expected
        return urls, None

    def get_this_time_new_result_num(self, key, urls):
        if key not in self.__url_map:
            return NA  # means this is a new query, all results are new
        new_result = 0
        [_, _, cached_urls, _] = self.__url_map[key]
        for url in urls:
            if url not in cached_urls:
                new_result += 1
        return new_result

    def cache_url(self, key, urls, next_size_ratio):
        self.__has_write = True
        self.__url_map[key] = [datetime.today(), self.get_this_time_new_result_num(key, urls), urls, next_size_ratio]

    @staticmethod
    def crawl_by_asking_google_search(pattern, start, size, option=""):
        assert type(pattern) in [str, unicode]
        from util.global_def import get_api_key, get_cx
        api_key = get_api_key()
        cx = get_cx()
        if not api_key or not cx:
            if not Crawler._HAS_SHOW_NO_SEARCH_MSG:
                Crawler._HAS_SHOW_NO_SEARCH_MSG = True
                info("沒有指定Google custom search需要的api_key及cx，將不進行圖片搜尋")
            return [], False
        size_option = "&imgSize=" + size if size else ""
        full_option = size_option + (option if option else "")
        base_url = 'https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&searchType=image&num=%d' \
                   '&q=' + pattern + '&start=%d' + full_option
        request_str = base_url % (api_key, cx, G_SEARCH_PER_REQ_SIZE, start)
        urls = []
        success = True
        try:
            r = requests.get(request_str)
            res = json.loads(r.text)
            if "error" in res:
                Crawler.print_error(res["error"])
                return urls, False
            for image_info in res['items']:
                assert 'link' in image_info
                url = image_info['link']
                urls.append(url)
        except TypeError as e:  # for unhandled error...
            info("無法擷取最新的圖片網址：", str(e))
            success = False
        return urls, success

    @staticmethod
    def get_search_key(pattern, option):
        return pattern  # TODO:

    @staticmethod
    def print_error(data):
        assert isinstance(data, dict) and "message" in data
        error("搜尋引擎傳回錯誤訊息：", data["message"])


if __name__ == '__main__':
    from util.global_def import config_action
    config_action()
    # name '_' before the 'obj' to let python not free imported module before __del__ is called
    # (or we will have something like 'NoneType' object has no attribute 'dump' for cPickle.dump)
    _obj = Crawler(need_save=True)
    size = ["large", "xlarge", "xxlarge", "huge"]
    _obj.crawl("Inside Out", size_list=size, print_url=True)
