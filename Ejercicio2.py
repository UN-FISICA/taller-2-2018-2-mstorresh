#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from turtle import *
colormode(1)
pensize(5)
hideturtle()
#a=int(input("numero de lados: "))
a=4
for j in range(a):
    if a==2+j:
        y=-180+(a-2)*180/a            
def figura(x):
    for i in range(a):
        fd(x)
        rt(y)
def cuadro(z):
    for i in range(4):
        fd(z)
        b=pos()
        c=b-(10,10)
        figura(20)
        rt(-90)        
cuadro(100)
print (a)
print (y)