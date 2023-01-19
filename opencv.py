# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:19:53 2022

@author: jasee
"""


import cv2
Img=cv2.imread('image.jpg',1)
cv2.imshow('image',Img)
cv2.waitKey(0)
cv2.destroyAllWindows()