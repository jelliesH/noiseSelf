#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:47:38 2016
     
@author: 390771
"""
import os
import mfcc_extract

def mfcc_feature(trainingFilesPath):
    noise_feature_output_dir = trainingFilesPath + "_feature"
#    print "脚本名：", sys.argv[0]
    print "训练数据路径：", trainingFilesPath
    print "MFCC输出路径：", noise_feature_output_dir
    if (os.path.isdir(noise_feature_output_dir)):
            print "MFCC文件夹已经存在"
    else:
        os.mkdir(noise_feature_output_dir)
    return mfcc_extract.main(trainingFilesPath, noise_feature_output_dir)
    