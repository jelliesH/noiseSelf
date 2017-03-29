#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: adapt-ubm.py
# $Author: yjunlei

import sys
sys.path.append("..")
#sys.path.append("/home/390771/Project/noise/proNoise/pro_Noise")
import os
#sys.path.append(os.getcwd())
import glob

from gmm.python.pygmm import GMM
# import config
import datautil
import dirutils
import time

# 数据位置
data_path = "/home/yjunlei/Desktop/mnoise_test_feature"

# ubm 位置
ubm_path = "./model/ubm.mixture-32.model"

# 输出结果
output_filename = "result-noise.txt"
# 模型存放位置名称
model_dir_name = "model"
def get_predict_data_fpaths(path):
    """ 获取各个特征文件 """
    path_name = dirutils.getdirnames(path)
    fpaths = []
    for fpath in path_name:
        # fpath = glob.glob(os.path.join(data_path,fpath,"*.mfcc"))
        fpaths.append(os.path.join(path,fpath))
    return fpaths

def get_model_fpath(path):
    result = []
    result_classname = []
    mpaths = glob.glob(os.path.join(path,"*.model"))
    for mpath in mpaths:
        basename = os.path.basename(mpath)
        namesplit  = basename.split(".")
        classname = namesplit[0]
        if classname != "ubm":
            result.append(mpath)
            result_classname.append(classname)
        
    return (result,result_classname)

def main(datapath,modelpath,ubmpath):
    fpaths = get_predict_data_fpaths(datapath)
#    print "The fpath is ",fpaths
    mpaths,model_name = get_model_fpath(modelpath)
    # print(mpaths)
    X_test, y_test,filenames = datautil.read_test_data(fpaths)
#    print "X_test is",X_test
#    print "Y_test is",y_test
    # print(len(X_test[0]))
    # return
    ubm = GMM.load(ubmpath)
    model = []
    for mname,cname in zip(mpaths,model_name):
        model.append(GMM.load(mname))
    
    # ouputfile = open(output_filename)
    resultlines = []
    correct_count = 0
    count_all = 0
    resultdict={}
    for y in y_test:
        resultdict[y] = (0,0)   # (正确数,总数)

    for x, y,z in zip(X_test, y_test,filenames):
        ubm_score_all = ubm.score_all(x)
        score_list = []
        for m in model:
            score_list.append(m.score_all(x))
        max_index = score_list.index(max(score_list))
        print(max(score_list) / ubm_score_all)
        count_all = count_all + 1
#        print "The y is",y,"The Max_index is ",max_index,"The Model name is",model_name[max_index]
        if y == model_name[max_index]:
            correct_count = correct_count+1
        # resultstr = y + " " + model_name[max_index] + " " + z + " " + str(maxscore) + " " + str(ubm_score_all) + " " + str(maxscore / ubm_score_all)+ "\n" 
        resultstr = y + " " + model_name[max_index] + " " + z + "\n" 
        resultlines.append(resultstr)

        temp = resultdict[y]
        classall = temp[1] + 1
        classcorrect = temp[0]
        if y == model_name[max_index]:
            classcorrect = classcorrect + 1
        resultdict[y] = (classcorrect,classall)

    resultdict["all"] = (correct_count,count_all)
    print(correct_count)
    print(count_all)
    for k, v in resultdict.items():
        print k, " ", v
    output_filename_path = datapath+"/"+output_filename
    outputfile = open(output_filename_path,"w")
    # for line in resultlines:
    outputfile.writelines(resultlines)
    for k, v in resultdict.items():
        outputfile.writelines(k + "\n")
        for item in v:
            outputfile.writelines(str(item) + "\n")

    outputfile.close()
    return output_filename_path
    
def predict(data):
    """ 
    parameters
    ==========
        data : mfcc 数组
    """
    mpaths,model_name = get_model_fpath(model_dir_name)
    ubm = GMM.load(ubm_path)
    model = []
    for mname,cname in zip(mpaths,model_name):
        model.append(GMM.load(mname))

    ubm_score_all = ubm.score_all(data)

    score_list = []
    for m in model:
        score_list.append(m.score_all(data))

    max_index = score_list.index(max(score_list))
    return model_name[max_index]
    

if __name__ == '__main__':
    main(data_path,model_dir_name,ubm_path)

# vim: foldmethod=marker
