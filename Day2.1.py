# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:47:59 2020

@author: user
"""

import random
X=random.randint(1,3)
a=0
while a<6:
    x=input("請輸入數字")
    x = int(x)
    if x>20 or x<0:
        print("輸入錯誤")
    elif x==X:
        print("答對了")
        a=a+1
        print("答題次數:")
        print(a)
    elif x<X:
        print("大一點")
        a=a+1
    else:
        print("小一點")
        a=a+1
