#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Hustlion (1114128525@qq.com)
# Date:     10/06/2016
# Usage: 
# ./ubmTrainer.py featurePath ubmOutputPath
# python ./ubmTrainer.py ~/20161006-500K/20161006-500K ~/20161006-500K/20161006-500K 

import os
import sys
import ubm_train

noiseFeaturePath = sys.argv[1]
ubmOutputPath = sys.argv[2]

print "脚本名：", sys.argv[0]
print "MFCC路径：", noiseFeaturePath
print "UBM模型输出路径", ubmOutputPath


if (os.path.isdir(ubmOutputPath)):
        print "UBM模型输出路径已经存在"
else:
    os.mkdir(ubmOutputPath)

ubm_train.main(noiseFeaturePath, ubmOutputPath)