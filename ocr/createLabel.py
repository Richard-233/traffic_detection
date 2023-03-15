# -*- coding: utf-8 -*-
"""
Based on filename to create label for training
"""

import os

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


def create(file_path,label_file,state_file):
    # 图像路径
    imgpath = file_path
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
    points = points.split('_')
    points = [list(map(int, i.split('&'))) for i in points]
    # 将关键点的顺序变为从左上顺时针开始
    # points = points[-2:] + points[:2]
    # --- 读取车牌号
    label = label.split('_')

    province = provincelist[int(label[0])]
    # 车牌信息
    words = [wordlist[int(i)] for i in label[1:]]
    # 车牌号
    label = province + ''.join(words)

    label_content = 'blue/'+os.path.basename(file_path) + '	[{"transcription": "' + label + '", "points": ' + str(
        points) + ', "difficult": false}]'

    label_file.write(label_content+'\n')

    state_content = file_path + '	1'

    state_file.write(state_content+'\n')


def main():
    file_path = r'D:\Users\Richard_Young\Desktop\final_design\data\blue'
    label_file_path = file_path + '\\Label.txt'
    state_file_path = file_path + '\\fileState.txt'
    label_file = open(label_file_path,'w')
    state_file = open(state_file_path,'w')
    for root, dirs, files in os.walk(file_path):
        for file in files:
            file_path = os.path.join(root, file)
            create(file_path,label_file,state_file)
    label_file.close()
    state_file.close()

main()
