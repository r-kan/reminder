#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import sys
from gui.graph_view.multi_viewer import MultiGraphViewer

DEFAULT_CONFIG_FILE = "config.ini"


class Reminder(object):

    def __init__(self):
        config_file = DEFAULT_CONFIG_FILE
        if len(sys.argv) >= 2:
            for argument in sys.argv[1:]:
                if "-" == argument[0]:
                    if argument in ["-h", "-help"]:
                        self.__help()
                        sys.exit()
                    else:
                        print("無法辨認的option：", argument)
                else:
                    config_file = argument
        self.__image_setting = []
        self.__phrase_setting = []
        self.__parse_config(config_file)

    def __parse_config(self, config_file):
        from util.config import Config
        config = Config(config_file)
        config.set_general_setting()
        image_target = config.get_setting("image", "target")
        if not image_target:
            print("沒有指定圖片，程式即將結束")
            sys.exit()
        phrase_target = config.get_setting("phrase", "target")
        import glob
        self.__image_setting += glob.glob(image_target)
        self.__phrase_setting += (glob.glob(phrase_target) if phrase_target else [])

    def show(self):
        MultiGraphViewer(self.__image_setting, self.__phrase_setting).view()

    @staticmethod
    def __help():
        help_msg = "reminder - usage\n" \
                   "\tmain.py [config_file]\n" \
                   "=============================\n" \
                   "config_file: a file that gives various setting to reminder\n" \
                   "             if not given, will search for \"%s\" at current directory" % DEFAULT_CONFIG_FILE
        print(help_msg)


if __name__ == '__main__':
    Reminder().show()
