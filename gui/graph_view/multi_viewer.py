#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from base.setting.image import Image as ImageObj, SettingLoader as ImageSettingLoader
from base.setting.phrase import SettingLoader as PhraseSettingLoader
from base.dir_handle.dir_handler import Status  # to let pickle can recognize Status


def get_setting(setting_file):
    if ".list" in setting_file:
        return get_list_setting(setting_file)
    elif ".json" in setting_file:
        return get_json_setting(setting_file)
    assert False


def get_list_setting(list_file):
    cur_option = None
    image_obj_list = []
    for pattern in open(list_file, 'r').readlines():
        raw_pattern = pattern.strip()
        option_str = "option="
        option_pos = raw_pattern.find(option_str)
        if 0 == option_pos:
            option_value = raw_pattern[len(option_str):]
            cur_option = option_value
            continue
        image_obj_list.append(ImageObj(raw_pattern, None, None, cur_option))
    return image_obj_list, None


def get_json_setting(json_file):
    image_obj_list = []
    images = ImageSettingLoader(json_file).images
    for pattern in images:
        image_obj_list.append(images[pattern])
    phrase_obj_list = []
    phrases = PhraseSettingLoader(json_file).phrases
    for phrase_group in phrases:
        phrase_obj_list.append(phrases[phrase_group])
    return image_obj_list, phrase_obj_list


class MultiGraphViewer(object):

    def __init__(self, image_setting_files=None, phrase_setting_files=None):
        if not image_setting_files:
            image_setting_files = []
        if not phrase_setting_files:
            phrase_setting_files = []
        self.__image_settings = []
        self.__phrase_settings = []
        for setting_file in image_setting_files + phrase_setting_files:
            image_setting, phrase_setting = get_setting(setting_file)
            self.__image_settings += image_setting
            self.__phrase_settings += phrase_setting if phrase_setting else []

    def init_from_command_line(self):
        import sys
        if len(sys.argv) >= 2:
            for setting_file in sys.argv[1:]:
                image_setting, phrase_setting = get_setting(setting_file)
                self.__image_settings += image_setting
                self.__phrase_settings += phrase_setting if phrase_setting else []

    def view(self):
        from viewer import GraphViewer
        GraphViewer().view(self.__image_settings, self.__phrase_settings)


if __name__ == '__main__':
    from util.global_def import config_action
    config_action()
    viewer = MultiGraphViewer()
    viewer.init_from_command_line()
    viewer.view()
