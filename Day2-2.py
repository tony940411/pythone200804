# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:45:14 2020

@author: user
"""

import random
X=random.randint(1,10)
while True:
    x=input("請輸入數字")
    x = int(x)
    if x>10 or x<0:
        print("輸入錯誤")
    elif x==X:
        print("答對了")
    elif x<X:
        print("大一點")
    else:
        print("小一點")