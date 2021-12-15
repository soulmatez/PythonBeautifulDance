import os
import time
# libs = {"lxml","requests","pandas","numpy","you-get","opencv-python","pandas","fake_useragent","matplotlib","moviepy","opencv-contrib-python","WordCloud"}
liba = {"jieba"}
try:
    for lib in liba:
        os.system(f"pip3 install -i https://pypi.doubanio.com/simple/ {lib}")
        print(lib+"下载成功")
except:
    print("下载失败")
    