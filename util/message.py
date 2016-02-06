#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals


def is_osx():
    import platform
    system_name = platform.system()
    return "Darwin" in system_name


EN = 1
CHT = 2


class Msg(object):
    @staticmethod
    def get(lang_type, msg_id):
        assert lang_type in msg_id
        return msg_id[lang_type]

    acquired_url_count = {
      EN: "acquired url count",
      CHT: "獲得url筆數"
    }
    cache_file_does_not_exist = {
      EN: "cache file does not exist:",
      CHT: "不存在快取檔案："
    }
    cannot_create_directory = {
      EN: "cannot create program directory, program exits:",
      CHT: "無法新增資料夾，程式即將結束："
    }
    cannot_fetch_image_url = {
      EN: "cannot fetch newer image url list:",
      CHT: "無法擷取最新的圖片網址："
    }
    cannot_lower_down_rank_as_it_is_already_the_lowest = {
      EN: "cannot lower down rank as it is already the lowest!",
      CHT: "已經是最低等級，無法再降低！"
    }
    cannot_read_pickle_file = {
      EN: "cannot read pickle file:",
      CHT: "pickle檔案無法讀取："
    }
    change_rank_to = {
      EN: "change rank to ",
      CHT: "更改等級至"
    }
    check_network_connection = {
      EN: "check network connection...",
      CHT: "檢查網路連線..."
    }
    create_new_cache_file_for_directory = {
      EN: "create a new cache file for directory:",
      CHT: "建立一個新的資料夾快取檔案："
    }
    current_url_count = {
      EN: "current url count:",
      CHT: "現有url個數："
    }
    day = {
      EN: "day(s)",
      CHT: "天"
    }
    decrease_rank = {
      EN: "decrease rank:",
      CHT: "減少等級："
    }
    directory = {
      EN: "directory",
      CHT: "資料夾"
    }
    error = {
      EN: "error",
      CHT: "錯誤"
    }
    error_message = {
      EN: "error:",
      CHT: "錯誤訊息："
    }
    fail_to_convert_image_to_fullscreen = {
      EN: "fail to convert image to fullscreen:",
      CHT: "將圖片轉換成全畫面失敗："
    }
    fail_to_open_image = {
      EN: "fail to open image:",
      CHT: "無法打開圖片："
    }
    fail_read_file = {
      EN: "fail to read file",
      CHT: "無法讀取檔案"
    }
    fail_to_write_cache = {
      EN: "fail to write cache",
      CHT: "寫入快取失敗"
    }
    failed_url = {
      EN: "failed url:",
      CHT: "無法由url儲存圖片："
    }
    fetch_image = {
      EN: "fetch image:",
      CHT: "擷取圖片於："
    }
    fetch_image_fail = {
      EN: "fetch image fail",
      CHT: "圖片擷取不成功"
    }
    fetch_succeed = {
      EN: "fetch succeeded",
      CHT: "擷取成功！"
    }
    give_up_acquired_image_with_size = {
      EN: "give up acquired image with size:",
      CHT: "放棄獲得的圖片，其大小為："
    }
    give_up_fetch_image = {
      EN: "give up fetching image (due to no network connection):",
      CHT: "放棄擷取圖片（由於無網路連線）"
    }
    has_changed_update_cache_file = {
      EN: "has changed, update cache file",
      CHT: "已改變，更新快取檔案"
    }
    delete_button = "delete" if is_osx() else "backspace"
    help_message = {
      EN: "[esc]switch fullscreen, [" + delete_button + "]remove image, [h]help, [i]info, [->]next, [<-]prev, [q]quit",
      CHT: "[esc]切換全畫面, [" + delete_button + "]刪除圖片, [h]求助, [i]訊息, [->]下一張, [<-]上一張, [q]離開"
    }
    hour = {
      EN: "hour(s)",
      CHT: "時"
    }
    increase_rank = {
      EN: "increase rank:",
      CHT: "增加等級："
    }
    information = {
      EN: "info",
      CHT: "訊息"
    }
    location = {
      EN: "location",
      CHT: "位置"
    }
    minute = {
      EN: "minute(s)",
      CHT: "分"
    }
    network_status_fail = {
      EN: "status: not connected",
      CHT: "狀態：連線失敗"
    }
    network_status_succeed = {
      EN: "status: connected",
      CHT: "狀態：連線正常"
    }
    no_available_image_wait_10_minutes = {
      EN: "no available image now, will wait for ten minutes...",
      CHT: "現在無可使用的圖片，等待十分鐘..."
    }
    no_search_due_to_no_api_key_and_cx = {
      EN: "as api_key and cx for Google custom search is not available, no image search will be issued",
      CHT: "沒有指定Google custom search需要的api_key及cx，將不進行圖片搜尋"
    }
    not_any_image_specified_program_exit = {
      EN: "not any image is specified, program exits",
      CHT: "沒有指定圖片，程式即將結束"
    }
    obtain_unrecognized_status_code = {
      EN: "obtain unrecognized status code:",
      CHT: "獲得無法辨識的狀態碼："
    }
    rank = {
      EN: "rank",
      CHT: "等級"
    }
    remove_image = {
      EN: "remove image:",
      CHT: "刪除圖片："
    }
    search_target = {
      EN: "search target:",
      CHT: "查詢標的："
    }
    search_engine_err_msg = {
      EN: "search engine error:",
      CHT: "搜尋引擎傳回錯誤訊息："
    }
    second = {
      EN: "second(s)",
      CHT: "秒"
    }
    size = {
      EN: "size",
      CHT: "大小"
    }
    suggest_re_fetch_pickle_file = {
      EN: ", suggest re-fetch the pickle file",
      CHT: "，建議重新擷取pickle檔案"
    }
    target = {
      EN: "target",
      CHT: "標的"
    }
    timestamp = {
      EN: "timestamp",
      CHT: "時間"
    }
    to_next_search = {
      EN: "to next search:",
      CHT: "距離下次搜尋："
    }
    total_data_count = {
      EN: "total data count:",
      CHT: "全部資料筆數："
    }
    try_fetch_image_again = {
      EN: "try fetch image again",
      CHT: "再次嘗試獲取圖片"
    }
    use_previous_search_result = {
      EN: "use previous search result (due to no network connection)",
      CHT: "使用上一次的搜尋結果（由於無網路連線）"
    }
