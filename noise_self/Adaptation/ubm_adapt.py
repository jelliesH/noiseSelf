#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: adapt-ubm.py
# $Author: yjunlei

import sys
sys.path.append("..")
#sys.path.append('/home/390771/Project/noise/proNoise/pro_Noise/')
import os
import glob

from gmm.python.pygmm import GMM
# import config
import datautil
import dirutils
import time

# 模型存放位置名称
#model_dir_name = "model"

def get_training_data_fpaths(datapath):
    """ 获取各个类别文件夹 """
    path_name = dirutils.getdirnames(datapath)
    fpaths = []
    for fpath in path_name:
        fpaths.append(os.path.join(datapath,fpath))
    print(fpaths)
    return fpaths

def main(datapath,ubmpath, gmmPath):
    fpaths = get_training_data_fpaths(datapath)
#    print "The fpath is :",fpaths
    X_train, y_train = datautil.read_data(fpaths)
    ubm = GMM.load(ubmpath)
    for x, y in zip(X_train, y_train):
        gmm = GMM(concurrency=8,
                threshold=0.01,
                nr_iteration=100,
                verbosity=1)
        start = time.time()
        gmm.fit(x, ubm=ubm)
        # score = gmm.score(X_train[0])
        # print(gmm.weights_)
        # score_ubm = ubm.score(X_train[0])
        # print(sum(score))
        # print(sum(score_ubm))
        # score_all = gmm.score_all(X_train[6])
        # score_all_ubm = ubm.score_all(X_train[6])
        # print(str(score_all) + " score_all")
        # print(str(score_all_ubm) + " score_all")
        # print(str(score_all/score_all_ubm) + " score_all")
        end = time.time()
        print(str(end - start) + " seconds")
        gmm.dump(os.path.join(gmmPath, y + ".model"))
        print(os.path.join(gmmPath, y + ".model"))

if __name__ == '__main__':
    if not os.path.exists(model_dir_name):
        os.mkdir(model_dir_name)
    main(data_path,ubm_path)

# vim: foldmethod=marker
