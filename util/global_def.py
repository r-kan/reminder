#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import os
from util.message import EN, Msg


def get_delim():
    import platform
    system_name = platform.system()
    if "Darwin" in system_name:
        return "/"
    elif "Linux" in system_name:
        return "/"
    elif "Windows" in system_name:
        return "\\"
    return "/"  # default treats it an unix-like system


NA = -1
__DATA_HOME = (os.environ['HOME'] if 'HOME' in os.environ else '') + get_delim() + 'reminder' + get_delim()
__SLIDESHOW_FREQUENCY = 30  # the frequency in second to have slideshow
__PHRASE_APPEAR_RATIO = 50  # a fixed percentage ratio (0-100) to show phrase
__SEARCH_LATENCY = 1
__LANG = EN
__API_KEY = ''
__CX = ''
__FULLSCREEN_MODE2 = False


def set_fullscreen_mode2(fullscreen_mode2):
    global __FULLSCREEN_MODE2
    __FULLSCREEN_MODE2 = fullscreen_mode2


def get_fullscreen_mode2():
    return __FULLSCREEN_MODE2


def set_lang(lang):
    global __LANG
    __LANG = lang


def get_lang():
    return __LANG


def get_msg(msg_id):
    return Msg.get(__LANG, msg_id)


def set_api_key(api_key):
    global __API_KEY
    __API_KEY = api_key


def set_cx(cx):
    global __CX
    __CX = cx


def get_api_key():
    return __API_KEY if "" != __API_KEY else None


def get_cx():
    return __CX if "" != __CX else None


def set_search_latency(latency):
    assert latency >= 1
    global __SEARCH_LATENCY
    __SEARCH_LATENCY = latency


def get_search_latency():
    return __SEARCH_LATENCY


def get_slideshow_frequency():
    return __SLIDESHOW_FREQUENCY


def set_slideshow_frequency(slideshow_frequency):
    assert slideshow_frequency > 0
    global __SLIDESHOW_FREQUENCY
    __SLIDESHOW_FREQUENCY = slideshow_frequency


def set_phrase_appear_ratio(ratio):
    assert 0 <= ratio <= 100
    global __PHRASE_APPEAR_RATIO
    __PHRASE_APPEAR_RATIO = ratio


def get_phrase_appear_ratio():
    return __PHRASE_APPEAR_RATIO


def set_data_home(home):
    global __DATA_HOME
    __DATA_HOME = home
    assert len(__DATA_HOME) > 0
    if __DATA_HOME[-1] != get_delim():
        __DATA_HOME += get_delim()


def get_data_home():
    return __DATA_HOME


def get_user_config_file():
    return __DATA_HOME + "config.ini"


def config_action():
    config_file = get_user_config_file()
    if config_file:
        from util.config import Config
        Config(config_file).set_general_setting()


class CustomPrint(object):

    def __init__(self, verbose):
        self.verbose = verbose

    def set_verbose(self, verbose):
        self.verbose = verbose

    def show(self, *msg):
        if self.verbose:
            print(*msg)

    # noinspection PyMethodMayBeStatic
    def info(self, *msg):
        print("[" + get_msg(Msg.information) + "]", *msg)

    # noinspection PyMethodMayBeStatic
    def error(self, *msg):
        print("[" + get_msg(Msg.error) + "]", *msg)


__OUT = CustomPrint(False)


def set_verbose(verbose):
    global __OUT
    __OUT.set_verbose(verbose)


def get_verbose():
    return __OUT.verbose


def show(*msg):
    __OUT.show(*msg)


def info(*msg):
    __OUT.info(*msg)


def error(*msg):
    __OUT.error(*msg)
