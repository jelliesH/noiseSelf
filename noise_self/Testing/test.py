#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Hustlion (1114128525@qq.com)
# Date:     10/07/2016
# E.g: python test.py ~/20161007/500K ~/20161007/500Kmodel ~/20161007/500K/ubm.mixture-32.model

import ubm_predict
import os
import sys

noiseFeaturePath = sys.argv[1]
modelPath = sys.argv[2]
ubmPath = sys.argv[3]


if __name__ == '__main__':
    ubm_predict.main(noiseFeaturePath, modelPath,ubmPath)
