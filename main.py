#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import sys
from argparse import ArgumentParser
from gui.graph_view.multi_viewer import MultiGraphViewer
from util.global_def import get_msg
from util.message import Msg


class Reminder(object):

    def __init__(self):
        arg_parser = ArgumentParser(description='reminder --- brings you a better reminder')
        arg_parser.add_argument('config_file')
        args = arg_parser.parse_args()
        if not args.config_file:
            args.print_help()
            sys.exit()
        self.__image_setting = []
        self.__phrase_setting = []
        self.__parse_config(args.config_file)

    def __parse_config(self, config_file):
        from util.config import Config
        config = Config(config_file)
        config.set_general_setting()
        image_target = config.get_setting("image", "target")
        if not image_target:
            print(get_msg(Msg.not_any_image_specified_program_exit))
            sys.exit()
        phrase_target = config.get_setting("phrase", "target")
        import glob
        self.__image_setting += glob.glob(image_target)
        self.__phrase_setting += (glob.glob(phrase_target) if phrase_target else [])

    def show(self):
        MultiGraphViewer(self.__image_setting, self.__phrase_setting).view()


if __name__ == '__main__':
    Reminder().show()
