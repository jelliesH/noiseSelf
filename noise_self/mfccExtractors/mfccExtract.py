#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Hustlion (1114128525@qq.com)
# Date:     10/04/2016
# Usage: 
# ./mfccExtract.py dataPath
# ./mfccExtract.py /Volumes/Knowledge/Projects/tmp/training

import os
import sys
import mfcc_extract

trainingFilesPath = sys.argv[1]
noise_feature_output_dir = trainingFilesPath + "_feature"

print "脚本名：", sys.argv[0]
print "训练数据路径：", trainingFilesPath
print "MFCC输出路径：", noise_feature_output_dir
if (os.path.isdir(noise_feature_output_dir)):
        print "MFCC文件夹已经存在"
else:
    os.mkdir(noise_feature_output_dir)

mfcc_extract.main(trainingFilesPath, noise_feature_output_dir)
