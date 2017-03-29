#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Hustlion (1114128525@qq.com)
# Date:     10/06/2016
# Usage: 
# ./ubmTrainer.py featurePath ubmPath
# python ./adapter.py ~/20161006-500K/20161006-500K ~/20161006-500K/20161006-500K/

import os
import sys
import ubm_adapt

noiseFeaturePath = sys.argv[1]
ubmPath = sys.argv[2]
gmmPath = noiseFeaturePath + "_model/"

print "脚本名：", sys.argv[0]
print "MFCC路径：", noiseFeaturePath
print "GMM模型输出路径", gmmPath

if (os.path.isdir(gmmPath)):
    print "GMM文件夹已经存在"
else:
    os.mkdir(gmmPath)

ubm_adapt.main(noiseFeaturePath,ubmPath + "ubm.mixture-32.model", gmmPath)
