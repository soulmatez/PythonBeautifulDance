import os
import re
import cv2
import jieba
import requests
import moviepy
import pandas as pd
import numpy as np
from PIL import Image
from lxml import etree
from two.wordcloud import WordCloud
import matplotlib.pyplot as plt
from fake_useragent import UserAgent

# 安装you-get
# pip install you-get

# 下载视频
# you-get -i https://www.bilibili.com/video/BV11C4y1h7nX

# 更多访问you-get官网
# https://blog.csdn.net/dreamer0823/article/details/89438512

# 词云制作
# https://mp.weixin.qq.com/s/ZAYb7rjS5-kOFUsY2PAA5Q