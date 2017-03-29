# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

def GetFileList(dir):
    newDir = dir
    if os.path.isfile(dir):
        namelist=os.path.basename(dir)
        newname_list=namelist.replace(' ','_')
        newname_list=newname_list.replace('（','_')
        newname_list=newname_list.replace(' ）','_')
        newname_list=newname_list.replace('(','_')
        newname_list=newname_list.replace(')','_')
        #old_name = os.path.join(dir,namelist)
        #new_name = os.path.join(dir,newname_list)
        path = os.path.split(dir)[0]
        os.chdir(path) 
        cmd = "mv '"+namelist+"' "+newname_list
#        print cmd
        os.system(cmd)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
            # continue
            newDir = os.path.join(dir, s)
#	  newDir = newDir.encode("utf-8")
            GetFileList(newDir)
    return "Susscess !"
    
def create_file(dir):
    newDir = dir
    print 'file or dir',os.path.isfile(dir)
    if os.path.isfile(dir):
        [file_name_path,file_name] = os.path.split(dir)
        [shotname,extension] = os.path.splitext(file_name)
        if extension.find(".mfcc")  != -1 :
#            file_name=os.path.basename(dir)
            os.mkdir(os.path.join(file_name_path,shotname))
            print "The dir is ",dir,"The file_name is ",os.path.join(file_name_path,shotname)
            cmd = "mv "+dir+" "+os.path.join(file_name_path,shotname)
            print "The cmd is ",cmd
            os.system(cmd)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
#	  newDir = newDir.encode("utf-8")
            create_file(newDir)
    return "Sucess !"    
    
def create_mix_errNor_Noise(feature_path):
    os.listdir(feature_path)
    des_path = os.path.split(feature_path)[0]
    destination_path = os.path.join(des_path,"mixture_err_nor_Noise")
    os.mkdir(destination_path)
    for j in os.listdir(feature_path):
        if j == "errNoise":
            new_path = os.path.join(feature_path,"errNoise")
            num = 1
            for i in os.listdir(new_path):
                if num <= 2000:
                    old_name_path = os.path.join(new_path,i)
                    old_file = os.listdir(old_name_path)[0]
                    old_name = os.path.join(old_name_path,old_file)
                    new_name = os.path.join(destination_path,str(num))
                    os.mkdir(new_name)
                    cmd = "cp   "+ old_name+"  "+new_name
                    os.system(cmd)
                    num = num + 1
                elif num > 2000:
                    print "The errdata is more than 2000"
            print "errNoise Sucess !"
        if j == "norNoise":
            new_path = os.path.join(feature_path,"norNoise")
            num_nor = 2001
            for i in os.listdir(new_path):
                if num_nor <= 3000:
                    old_name_path = os.path.join(new_path,i)
                    old_file = os.listdir(old_name_path)[0]
                    old_name = os.path.join(old_name_path,old_file)
                    new_name = os.path.join(destination_path,str(num_nor))
                    os.mkdir(new_name)
                    cmd = "cp   "+ old_name+"  "+new_name
                    os.system(cmd)
                    num_nor = num_nor + 1
                elif num_nor > 3000:
                    print "The errdata is more than 3000"
            print "norNoise Sucess !"
            return destination_path
    
    
    
    
#if  __name__  == 'main':
#dir1 = sys.argv[0]
#    dir='/home/390771/Project/noise/audiolib_feature/hh'
#    dir1='/home/390771/Project/noise/audiolib_feature/hh/14_名义制冷  风机60Hz，压机1 20Hz，压机2 34Hz      右面.mfcc'
#GetFileList(dir)

