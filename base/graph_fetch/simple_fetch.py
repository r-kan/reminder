#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import os
import urllib2

url = "http://xxx.com/yyy.jpg"
abs_graph_file = "foo.jpg"
try:
    f = open(abs_graph_file, 'wb')
    print("擷取圖片於：", url)
    f.write(urllib2.urlopen(url, timeout=3).read())
    f.close()
    # image.retrieve(url, abs_graph_file)
    assert os.path.exists(abs_graph_file)
    print("擷取成功！")
except IOError as e:
    print("無法由url儲存圖片：", url)
