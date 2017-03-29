#!/usr/bin/python
# -*- coding: utf-8 -*-
# $File: train-ubm.py
# $Author:
import os
import sys
sys.path.append("..")
#sys.path.append("/home/390771/Project/noise/proNoise/pro_Noise")
#sys.path.append(os.getcwd())
import multiprocessing

import glob
import random
import datautil
import dirutils

from gmm.python.pygmm import GMM
# from sklearn.mixture import GMM


nr_mixture = 32

def get_gmm():
    # from sklearn.mixture import GMM as skGMM
    # from gmmset import GMM as pyGMM
    # if GMM == skGMM:
        # print 'using GMM from sklearn'
        # return GMM(nr_mixture)
    # else:
        # print 'using pyGMM'
        return GMM(nr_mixture=nr_mixture, nr_iteration=500,
                init_with_kmeans=0, concurrency=8,
                threshold=1e-15,
                verbosity=2)


def get_all_data_fpaths(path):
    fpaths = []
    fpathnames = dirutils.getdirnames(path)
    print "The fpathnames is",fpathnames
    # for style in ['Style_Reading', 'Style_Spontaneous', 'Style_Whisper']:
        # fpaths.extend(glob.glob('test-data/mfcc-lpc-data/{}/*.mfcc-lpc' .
            # format(style)))
    for fpath in fpathnames:
        fpath = glob.glob(os.path.join(path,fpath,"*.mfcc"))
        fpaths.extend(fpath)
    return fpaths


def train_all_together_ubm(path, ubmOutputPath):
    global nr_mixture
    # nr_utt_in_ubm = 300
    fpaths = get_all_data_fpaths(path)
    # random.shuffle(fpaths)
    # fpaths = fpaths[:nr_utt_in_ubm]
#    print "The path is ",fpaths
    X_train = datautil.read_raw_data(fpaths)
    gmm = get_gmm()
    gmm.fit(X_train)
    gmm.dump(ubmOutputPath+'ubm.mixture-{}.model'.format(
        nr_mixture))

def main(path, ubmOutputPath ):
    """
    @params: path: mfcc feature path
    e.g. mfcc_path = "/home/yjunlei/Desktop/mnoise_feature"
    """
    train_all_together_ubm(path, ubmOutputPath)
    return ubmOutputPath+'ubm.mixture-{}.model'.format(
        nr_mixture)


if __name__ == '__main__':
    main(mfcc_path)

# vim: foldmethod=marker
