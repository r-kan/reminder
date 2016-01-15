#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import urllib2
from util.global_def import get_msg
from util.message import Msg


def check_access_status():
    print(get_msg(Msg.check_network_connection))
    try:
        urllib2.urlopen('http://google.com', timeout=3)
        print(get_msg(Msg.network_status_succeed))
        return True
    except urllib2.URLError:
        pass
    print(get_msg(Msg.network_status_fail))
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
