#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:47:38 2016

@author: 390771
"""
import os
import ubm_adapt
def adapters(noiseFeaturePath,ubmPath):
    ubmPath = ubmPath + "/"
    gmmPath = noiseFeaturePath + "_model"
    print "MFCC路径：", noiseFeaturePath
    print "GMM模型输出路径", gmmPath
    
    if (os.path.isdir(gmmPath)):
        print "GMM文件夹已经存在"
    else:
        os.mkdir(gmmPath)
    ubm_adapt.main(noiseFeaturePath,ubmPath + "ubm.mixture-32.model", gmmPath+"/")
    print "Sucess !"
    return gmmPath