#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: mfcc-data.py
# $Author: yjunlei
import os
import sys
#sys.path.append('/home/390771/Project/noise/proNoise/pro_Noise/feature')
#print os.getcwd()
#sys.path.append('../feature')
#print os.getcwd()
#sys.path.append(os.getcwd())
print sys.path
import wavio
import glob
from feature import MFCC
import multiprocessing
import numpy as np
import errno
import dirutils

concurrency = 8
# 声音文件根目录
wav_file_dir='/home/390771/Project/noise/audiolib/errNoise'
output_dir= wav_file_dir + '/mnoise_feature'

def mkdirp(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def get_mfcc_worker(params):
    fpath, outpath = params
    print('mfcc: ' + fpath)
    # fs, signal = wavfile.read(fpath)
    #import traceback
    try:
        wavobj = wavio.read(fpath)
        fs = wavobj.rate
        signal = wavobj.data
        mfcc = MFCC.extract(fs, signal)
        mkdirp(os.path.dirname(outpath))
        with open(outpath, 'w') as fout:
            for x in mfcc:
                print >> fout, " " . join(map(str, x))
    except:
        f=open(os.path.join(os.path.expanduser('~'),"gmm-ubm-log.txt"), 'a')
        #traceback.print_exc(file=f)
        print >> f, fpath, "\n"
        f.flush()
        f.close()
    finally:
        print('done: mfcc:' + fpath)

def extract_mfcc_data(data_dir,dirname, mfcc_output_dir):
    pool = multiprocessing.Pool(concurrency)
    files = glob.glob(os.path.join(data_dir,dirname, '*.[Ww][Aa][Vv]'))
    mfcc_files = map(lambda x: os.path.join(mfcc_output_dir, x[0] + ".mfcc"),
        map(os.path.splitext,
            map(os.path.basename, files)))
    result = pool.map(get_mfcc_worker, zip(files, mfcc_files))
    pool.terminate()

def extract(filename):
    """ 返回给定文件的 mfcc 特征 """
    wavobj = wavio.read(filename)
    fs = wavobj.rate
    signal = wavobj.data
    mfcc = MFCC.extract(fs, signal)
    return mfcc

def main(data_dir,outputdir):
    dirnames = dirutils.getdirnames(data_dir)
    for dirname in dirnames:
        print(os.path.join(data_dir,dirname))
        extract_mfcc_data(data_dir,dirname, os.path.join(outputdir,dirname))
    print 'Suceeses!'
    return outputdir

if __name__ == '__main__':
    main(wav_file_dir,output_dir)


# vim: foldmethod=marker
