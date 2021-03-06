#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from ConfigParser import ConfigParser
from util.global_def import set_phrase_appear_ratio, get_phrase_appear_ratio, \
    set_slideshow_frequency, get_slideshow_frequency, \
    set_search_latency, get_search_latency, \
    set_api_key, set_cx, get_api_key, get_cx, \
    set_verbose, get_verbose, \
    set_data_home, get_data_home, \
    set_lang, get_lang, \
    set_fullscreen_mode2, get_fullscreen_mode2
from util.message import EN, CHT


class Config(object):

    def __init__(self, config_file):
        import os
        if not os.path.exists(config_file):
            print("config file \"%s\" does not exist, program exits..." % config_file)
            import sys
            sys.exit()
        self.__config = ConfigParser()
        self.__config.read(config_file)

    def set_general_setting(self):
        lang = get_lang() if not self.__config.has_option("reminder", "lang") else \
            self.__config.get("reminder", "lang")
        if type(lang) is str:
            lang = EN if "EN" == lang else CHT if "CHT" == lang else None
        assert lang is not None
        data_home = get_data_home() if not self.__config.has_option("reminder", "data_location") else \
            self.__config.get("reminder", "data_location")
        slideshow_frequency = get_slideshow_frequency() if not self.__config.has_option("image", "slideshow_frequency") else \
            float(self.__config.get("image", "slideshow_frequency"))
        phrase_appear_ratio = get_phrase_appear_ratio() if not self.__config.has_option("phrase", "ratio") else \
            float(self.__config.get("phrase", "ratio"))
        api_key = get_api_key() if not self.__config.has_option("search", "api_key") else \
            self.__config.get("search", "api_key")
        cx = get_cx() if not self.__config.has_option("search", "cx") else \
            self.__config.get("search", "cx")
        search_latency = get_search_latency() if not self.__config.has_option("search", "search_latency") else \
            float(self.__config.get("search", "search_latency"))
        fullscreen_mode2 = get_fullscreen_mode2() if not self.__config.has_option("reminder", "fullscreen_mode2") else \
            "True" == self.__config.get("reminder", "fullscreen_mode2")
        verbose = get_verbose() if not self.__config.has_option("reminder", "verbose") else \
            "True" == self.__config.get("reminder", "verbose")
        set_lang(lang)
        set_data_home(data_home)
        set_slideshow_frequency(slideshow_frequency)
        set_phrase_appear_ratio(phrase_appear_ratio)
        set_search_latency(search_latency)
        set_api_key(api_key)
        set_cx(cx)
        set_fullscreen_mode2(fullscreen_mode2)
        set_verbose(verbose)
        print("=======  reminder setting  =============")
        print("data home:       ", data_home)
        print("slideshow:       ", slideshow_frequency)
        print("phrase ratio:    ", phrase_appear_ratio)
        print("search latency:  ", search_latency)
        print("api key:         ", api_key if "" != api_key else "None")
        print("cx:              ", cx if "" != cx else "None")
        print("========================================")

    def get_setting(self, section, option):
        if self.__config.has_option(section, option):
            return self.__config.get(section, option)
        else:
            return None
