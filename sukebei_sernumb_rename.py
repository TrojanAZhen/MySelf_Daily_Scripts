#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 车：https://sukebei.nyaa.si/?f=0&c=0_0&q=%E6%A5%B5%E5%93%81%E8%BB%8A%E7%89%8C

import os
import re
import shutil

re_names = []

SN_PATH = '/home/xxxx/Desktop/Serial_number'


def read_file_rename(file_path, root_path):
    with open(file_path,'r') as file_data:
        tmp_data = re.search(r'(.*):piece length', str(file_data.readline()), re.M|re.I)
        try:
            tmp_data = tmp_data.group()
            tmp_name = re.search(r'name[a-zA-Z0-9]+:(\[.*?\]?)?([a-zA-Z0-9]+-?\d+[a-zA-Z0-9]+)', str(tmp_data))
            tmp_name = tmp_name.group()
            print(tmp_name[7:-1])
            if tmp_name[7:-1] not in re_names:
                os.rename(file_path, root_path+'/'+tmp_name[7:-1]+'.torrent')
                re_names.append(tmp_name[7:-1])
        except:
            # 种子内无内容，即扔到另一文件夹
            shutil.move(file_path, root_path[:-13]+"bak")


for root, dirs, files in os.walk(SN_PATH, topdown=False):
    for name in files:
        try:
            # 正常用工具在sukebei下载的种子是全数字名
            if int(name[:-8]):
                print(name)
                tmp_file_path = os.path.join(root, name)
                read_file_rename(tmp_file_path, root)
        except:
            pass
