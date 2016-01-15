#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import cPickle
import errno
from cPickle import UnpicklingError
from util.global_def import show, error, get_msg
from util.message import Msg


def load(pickle_file):
    """output: is_exist, value"""
    try:
        pickle_fd = open(pickle_file, "r")
    except IOError as err:
        if errno.ENOENT == err.errno:
            show(get_msg(Msg.cache_file_does_not_exist), pickle_file)
            return False, None
        assert False
    try:
        value = cPickle.load(pickle_fd)
        return True, value
    except (ValueError, UnpicklingError, EOFError):
        error(get_msg(Msg.cannot_read_pickle_file), pickle_file, get_msg(Msg.suggest_re_fetch_pickle_file))
        assert False


def save(pickle_file, value):
    pickle_fd = open(pickle_file, "w")
    try:
        cPickle.dump(value, pickle_fd)
    except AttributeError as msg:
        error(get_msg(Msg.fail_to_write_cache), str(msg))
    pickle_fd.close()
