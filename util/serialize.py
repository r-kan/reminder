#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import cPickle
import errno
from cPickle import UnpicklingError
from util.global_def import show, error


def load(pickle_file):
    """output: is_exist, value"""
    try:
        pickle_fd = open(pickle_file, "r")
    except IOError as err:
        if errno.ENOENT == err.errno:
            show("不存在快取檔案：", pickle_file)
            return False, None
        assert False
    try:
        value = cPickle.load(pickle_fd)
        return True, value
    except (ValueError, UnpicklingError, EOFError):
        error("pickle檔案無法讀取：", pickle_file, "，建議重新擷取pickle檔案")
        assert False


def save(pickle_file, value):
    pickle_fd = open(pickle_file, "w")
    try:
        cPickle.dump(value, pickle_fd)
    except AttributeError as msg:
        error("寫入快取失敗", str(msg))
    pickle_fd.close()
