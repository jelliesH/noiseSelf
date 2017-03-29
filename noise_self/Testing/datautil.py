#!/usr/bin/python2
# -*- coding: utf-8 -*-
# $File: datautil.py
# $Author: yjunlei

import os
import glob
import random

import numpy as np
from numpy import loadtxt

def read_raw_data(pattern):
    """:return X"""
    if isinstance(pattern, basestring):
        fpaths = glob.glob(pattern)
    elif isinstance(pattern, list):
        fpaths = pattern

    X = []
    for fpath in fpaths:
        print 'loading file {} ... ' . format(fpath)
        X.extend(loadtxt(fpath))
    return X

def read_data(pattern):
    """ 获取每个类别下的特征向量 """
    X_train, y_train = [], []
    if isinstance(pattern, basestring):
        fpaths = sorted(glob.glob(pattern))
    elif isinstance(pattern, list):
        fpaths = pattern

    for fpath in fpaths:
        if fpath[-1] == "/":
            fpath = fpath[0:-1]
        featurefiles = glob.glob(os.path.join(fpath,"*.mfcc"))
        x_train = []
        for featurefile in featurefiles:
            print 'reading {} ...' . format(fpath)
            classname = os.path.basename(fpath) # 类别名称
            x_train.extend(np.loadtxt(featurefile))
        X_train.append(x_train)
        y_train.append(classname)

    return X_train, y_train

def read_test_data(pattern):
    """ 获取每个类别下的特征向量 """
    X_test, y_test = [], []
    filenames = []
    if isinstance(pattern, basestring):
        fpaths = sorted(glob.glob(pattern))
    elif isinstance(pattern, list):
        fpaths = pattern

    for fpath in fpaths:
        if fpath[-1] == "/":
            fpath = fpath[0:-1]
        featurefiles = glob.glob(os.path.join(fpath,"*.mfcc"))
        for featurefile in featurefiles:
            print 'reading {} ...' . format(fpath)
            classname = os.path.basename(fpath) # 类别名称
            filename = os.path.basename(featurefile)
            X_test.append(np.loadtxt(featurefile))
            y_test.append(classname)
            filenames.append(filename)

    return X_test, y_test,filenames
