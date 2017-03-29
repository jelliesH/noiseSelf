#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: dirutils.py
# $Date: Wed Jun 15 20:07:41 PDT 2016
# $Author: yjunlei

import os

def getdirnames(rootdir):
    """ 获取目录下的所有文件夹名 """
    dirs = []
    for f in os.listdir(rootdir):
        if os.path.isdir(os.path.join(rootdir, f)):
            dirs.append(f)
    return dirs

