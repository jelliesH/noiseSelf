#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 09:21:05 2016

@author: 390771
"""
"""
    提取特征处理
"""
import sys
import random
sys.path.append("/home/390771/Project/noise_self")
import os
from mfccExtractors import mfcc_feature
from data_preprocessing import rename_preprocessing
from UBM import ubm_trainer
from Adaptation import adapters
from Testing import tests
import pandas as pd

def data_star(path):
#    mfcc提取特征
#    path = "/home/390771/Project/noise/audiolib"
    mfcc_feature(path)
    
    #------数据预处理----
    """
        重命名处理.mfcc文件
    """
    feature_path = "/home/390771/Project/noise/audiolib_feature"
    rename_preprocessing.GetFileList(feature_path)
    
    """
        把每个文件放在独立的文件夹下
    """
    rename_preprocessing.create_file(feature_path)
    """
        每个文件夹放到一个混合的文件中作训练数据 文件命名为：mixture_err_nor_Noise
    """
    rename_preprocessing.create_mix_errNor_Noise(feature_path)
    
def train_test_model(mix_feature_path):
    #----数据与处理结束----
    """
        模型训练
              总共343文件夹：300个文件夹做训练，43个文件夹作测试
              train : 300 test: 43
    """
#    mix_feature_path ="/home/390771/Project/noise/mixture_err_nor_Noise"
    mix_feature_path_list = os.listdir(mix_feature_path)
    test_feature_dir_path = mix_feature_path+"/test_data"
    train_feature_dir_path = mix_feature_path+"/train_data"
    os.mkdir(test_feature_dir_path)
    os.mkdir(train_feature_dir_path)
    list_dir_mix_feature_file = os.listdir(mix_feature_path)
    list_dir_mix_feature_file.remove('test_data')
    list_dir_mix_feature_file.remove('train_data')
    num = random.sample(list_dir_mix_feature_file,43)
    for index_num in num:
        targ_mv_file = os.path.join(mix_feature_path,index_num)
        cmd = "mv "+targ_mv_file+" "+test_feature_dir_path
        os.system(cmd)
    list_dir_mix_feature_file = os.listdir(mix_feature_path)
    list_dir_mix_feature_file.remove('test_data')
    list_dir_mix_feature_file.remove('train_data')
    for index_list_dir_mix_feature_file in list_dir_mix_feature_file:
        targ_mv_file = os.path.join(mix_feature_path,index_list_dir_mix_feature_file)
        cmd = "mv "+targ_mv_file+" "+train_feature_dir_path
        os.system(cmd)
    #数据所在目录
    #mix_feature_path ="/home/390771/Project/noise/mixture_err_nor_Noise"
    ubm_path = train_feature_dir_path
    ubm_path_file = ubm_trainer(train_feature_dir_path,ubm_path)
    
    #训练每个类别的模型
    adapters_model_path = adapters(train_feature_dir_path,ubm_path)
    
    #adapters_model_path="/home/390771/Project/noise/mixture_err_nor_Noise_model"
#    ubm_path_file = "/home/390771/Project/noise/mixture_err_nor_Noise/train_data/ubm.mixture-32.model"
    ubm_path_file = mix_feature_path+"/train_data/ubm.mixture-32.model"
    """
        测试精度
    """
    return tests(test_feature_dir_path,adapters_model_path,ubm_path_file)

def summry_text(all_text):
    if len(all_text.split()) == 3:
        if all_text.split()[0] == all_text.split()[1] :
            return 1            
        elif all_text.split()[0] != all_text.split()[1] :
            print all_text
            return 0
    elif  len(all_text.split()) != 3:
        return "Null"
"""
    正确异常的识别率
"""
def er_nor_rate(all_text):
    if len(all_text.split()) == 3:
        if int(all_text.split()[0]) <= 2000:
            if int(all_text.split()[1]) <= 2000:
                return 4
            elif int(all_text.split()[1]) > 2000:
                    return 2
        elif int(all_text.split()[0]) > 2000:
            if int(all_text.split()[1])  >2000:
                return 1
            elif int(all_text.split()[1])  <=2000:
                return 3
                
def result_analysis(file_text_path):
#    file_text_path = "/home/390771/Project/result-noise.txt"
    """
        结果集分析
    """
    file_object = open(file_text_path)
    all_text = file_object.readlines( )
    file_object.close( )
    result = map(summry_text,all_text)
    print "每个类别识别率为： "+ str(float(result.count(1))/(result.count(1)+result.count(0)))    
    result_err_nor = map(er_nor_rate,all_text)
    a11 = result_err_nor.count(1)
    a12 = result_err_nor.count(2)
    a21 = result_err_nor.count(3)
    a22 = result_err_nor.count(4)
    #列联表
    data_frame = pd.DataFrame({'nor':[a11,a21],'err':[a12,a22]},index = ['nor','err'],columns = ['nor','err'])
    print 'The second classification result is'
    print data_frame