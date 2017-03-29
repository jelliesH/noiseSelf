#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:47:38 2016

@author: 390771
"""
import ubm_predict
import os
import sys
def tests(noiseFeaturePath,modelPath,ubmPath):
    return ubm_predict.main(noiseFeaturePath, modelPath,ubmPath)