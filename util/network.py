#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import urllib2


def check_access_status():
    print("檢查網路連線...")
    try:
        urllib2.urlopen('http://google.com', timeout=3)
        print("狀態：連線正常")
        return True
    except urllib2.URLError:
        pass
    print("狀態：連線失敗")
    return False


__CHECKED = False
__REACHABLE = False


def reachable():
    global __CHECKED, __REACHABLE
    if not __CHECKED:
        __REACHABLE = check_access_status()
        __CHECKED = True
    return __REACHABLE


if __name__ == '__main__':
    print(reachable())
