#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:47:38 2016

@author: 390771
"""
import os
import ubm_train

def ubm_trainer(noiseFeaturePath,ubmOutputPath):
    noiseFeaturePath = noiseFeaturePath+"/"
    ubmOutputPath = ubmOutputPath+"/"
    print "MFCC路径：", noiseFeaturePath
    print "UBM模型输出路径", ubmOutputPath
    if (os.path.isdir(ubmOutputPath)):
            print "UBM模型输出路径已经存在"
    else:
        os.mkdir(ubmOutputPath)
    print "Sucess !"
    return ubm_train.main(noiseFeaturePath, ubmOutputPath)
   