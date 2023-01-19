# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:41:26 2022

@author: jasee
"""

import cv2

Img=cv2.imread('image.jpg',0)
img_resized=cv2.resize(Img,(780,540),interpolation=cv2.INTER_NEAREST)
img_resized2=cv2.resize(Img,(255,255),interpolation=cv2.INTER_NEAREST)
cv2.imshow('image',img_resized)
cv2.imshow('image',img_resized2)
cv2.waitKey(1)
cv2.destroyAllWindows()