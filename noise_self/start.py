#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:18:25 2016

@author: 390771
"""
import os
import sys
sys.path.append(os.getcwd())
import model_main  

"""
----特征提取---- 
源数据目录结构
noise/
	  audiolib/ 
		      errNoise/
				***.WAV ...
		      norNoise/
				***.WAV ...
"""
path = "/home/390771/Project/noise/audiolib"
model_main.data_star(path)
"""
结果目录结构;文件名1-2000的属于异常数据，2000-3000属于正常数据
noise/
	  audiolib/ 
		      errNoise/
				***.WAV ...
		      norNoise/
				***.WAV ...
	  mixture_err_nor_Noise/

				2/				
				    ***.mfcc ...
				3/				
				    ***.mfcc ...
				...
				2001/				
				    ***.mfcc ...
				2002/				
				    ***.mfcc ...
				...			
"""
"""
训练与测试
    
        模型训练
              总共343文件夹：300个文件夹做训练，43个文件夹作测试
              train : 300 test: 43
    
"""
mix_feature_path ="/home/390771/Project/noise/mixture_err_nor_Noise"
file_text_path = model_main.train_test_model(mix_feature_path)
"""
输出结果是当前的star.py文件路径下的result-noise.txt文件
    结果中的result-noise.txt文件
    内容：每行三个字段：真实标签 判定标签 文件名
             后面几十行可能会乱序 
"""

"""
结果分析
"""
#file_text_path = "/home/390771/Project/noise/mixture_err_nor_Noise/test_data/result-noise.txt"
model_main.result_analysis(file_text_path)

