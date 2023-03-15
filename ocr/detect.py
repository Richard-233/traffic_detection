# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 18:24:10 2021

@author: luohenyueji
"""

from PIL import Image, ImageDraw, ImageFont
import os, shutil

provincelist = [
    "皖", "沪", "津", "渝", "冀",
    "晋", "蒙", "辽", "吉", "黑",
    "苏", "浙", "京", "闽", "赣",
    "鲁", "豫", "鄂", "湘", "粤",
    "桂", "琼", "川", "贵", "云",
    "藏", "陕", "甘", "青", "宁",
    "新"]

wordlist = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "J", "K",
    "L", "M", "N", "P", "Q",
    "R", "S", "T", "U", "V",
    "W", "X", "Y", "Z", "0",
    "1", "2", "3", "4", "5",
    "6", "7", "8", "9"]


# --- 绘制边界框


def DrawBox(im, box):
    draw = ImageDraw.Draw(im)
    draw.rectangle([tuple(box[0]), tuple(box[1])], outline="#FFFFFF", width=3)


# --- 绘制四个关键点


def DrawPoint(im, points):
    draw = ImageDraw.Draw(im)

    for p in points:
        center = (p[0], p[1])
        radius = 5
        right = (center[0] + radius, center[1] + radius)
        left = (center[0] - radius, center[1] - radius)
        draw.ellipse((left, right), fill="#FF0000")


# --- 绘制车牌


def DrawLabel(im, label):
    draw = ImageDraw.Draw(im)
    # draw.multiline_text((30,30), label.encode("utf-8"), fill="#FFFFFF")
    font = ImageFont.truetype('simsun.ttc', 64)
    draw.text((30, 30), label, font=font)


# --- 图片可视化


def ImgShow(imgpath, box, points, label):
    # 打开图片
    im = Image.open(imgpath)
    DrawBox(im, box)
    DrawPoint(im, points)
    DrawLabel(im, label)
    # 显示图片
    im.show()
    im.save('result.jpg')


def move(path, numberdict):
    # 图像路径
    imgpath = path

    # 图像名
    imgname = os.path.basename(imgpath).split('.')[0]

    # 根据图像名分割标注
    try:
        _, _, box, points, label, brightness, blurriness = imgname.split('-')
    except:
        return

    # --- 边界框信息
    # box = box.split('_')
    # box = [list(map(int, i.split('&'))) for i in box]

    # --- 关键点信息
    # points = points.split('_')
    # points = [list(map(int, i.split('&'))) for i in points]
    # 将关键点的顺序变为从左上顺时针开始
    # points = points[-2:] + points[:2]
    # --- 读取车牌号
    label = label.split('_')

    # 统计省份
    if provincelist[int(label[0])] in numberdict:
        numberdict[provincelist[int(label[0])]] = numberdict[provincelist[int(label[0])]] + 1
    else:
        numberdict[provincelist[int(label[0])]] = 1

    # 省份缩写
    # if int(label[0]) != 0 and numberdict[provincelist[int(label[0])]]<=1500:
    # if int(label[0]) == 0 and numberdict[provincelist[int(label[0])]]<=1026:
    #     print(path)
    #     try:
    #         shutil.move(path, r"D:\Users\Richard_Young\Desktop\data\blue")
    #     except:
    #         os.remove(path)
    #         numberdict[provincelist[int(label[0])]] = numberdict[provincelist[int(label[0])]] - 1
    #     return 0

    # else:
    #     numberdict[provincelist[int(label[0])]] = 0
    #     return 1

    # province = provincelist[int(label[0])]
    # print(province)
    # 车牌信息
    # words = [wordlist[int(i)] for i in label[1:]]
    # 车牌号
    # label = province + ''.join(words)

    # --- 图片可视化
    # ImgShow(imgpath, box, points, label)
    # return 0


def main():
    # file_path = r'D:\Users\Richard_Young\Desktop\数据集\CCPD2019'
    file_path = r'D:\Users\Richard_Young\Desktop\data\blue'
    numberdict = dict()
    for root, dirs, files in os.walk(file_path):
        for file in files:
            path = os.path.join(root, file)
            i = move(path, numberdict)
            if i == 1:
                break
    print(numberdict)


main()
