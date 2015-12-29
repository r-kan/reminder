#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from PIL import Image, ImageTk
import Tkinter


# TODO: the following image cannot be shown even in Image.show()
graph_file = "/Users/rodion/dev/reminder/base/graph_fetch/picture/インサイドヘッド/image_71.jpg"
# this one has strange result
graph_file2 = "/Users/rodion/dev/reminder/base/graph_fetch/picture/believe/image_66.jpg"
image = Image.open(graph_file)
print(image.width, image.height)
print(image.format, image.mode)
image.show()

root = Tkinter.Tk()
tmp = None
try:
    image = Image.open(graph_file)  # .convert("RGB")
    tmp = image
except IOError as e:
    # some image cannot be opened (maybe it's not image format?), err msg is 'cannot identify image file'
    print("無法打開圖片：", str(e))
root.geometry('%dx%d+0+0' % (image.size[0], image.size[1]))
tk_image_obj = ImageTk.PhotoImage(tmp)
label_image = Tkinter.Label(root, image=tk_image_obj)
label_image.place(x=0, y=0, width=image.size[0], height=image.size[1])
label_image.pack()
# root.mainloop()
