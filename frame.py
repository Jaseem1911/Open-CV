# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:40:03 2022

@author: jasee
"""

import cv2
vid=cv2.VideoCapture(0)
 
for i in range(0,1000):
    ret,frame=vid.read()
    cv2.imshow("frame",frame)
    #print(i)
    cv2.imwrite(r"C:\Users\jasee\Downloads\open Cv-20221101T060441Z-001\open Cv\test/"+str(i)+".jpg",frame)
     
     
vid.release()
cv2.destroyAllWindows()