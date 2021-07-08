# encoding=utf-8

import jieba
import wordcloud
from imageio import imread

def main():
    mask = imread("chinamap.jpg")
    excludes = {}
    f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
    t = f.read()
    f.close()
    ls = jieba.lcut(t)
    txt = " ".join(ls)
    w = wordcloud.WordCloud(width=1000, height=700, background_color="white", font_path="msyh.ttc", mask=mask)
    w.generate(txt)
    w.to_file("grwordcloudm2.png")

def main1():
    txt = open("threekingdoms.txt", "r", encoding='utf-8').read()
    words = jieba.lcut(txt)
    result = " ".join(words)
    w = wordcloud.WordCloud(width=1000, height=1000, background_color="white", font_path="msyh.ttc")
    w.generate(result)
    w.to_file("grwordcloudm1.png")


if __name__ == '__main__':
    main1()