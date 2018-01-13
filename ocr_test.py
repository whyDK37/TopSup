# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/8 20:38
# @desc    : 答题闯关辅助，截屏 ，OCR 识别，百度搜索


from PIL import Image
from common import screenshot, ocr, methods
from threading import Thread
import time

img = Image.open("./15158331854303.png")

# 文字识别
text = ocr.ocr_img_all(img)

print(text)
