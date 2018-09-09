#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from turtle import *
import math as m
a=int(input("numero de filas de la piramide: "))
hideturtle()
def figura(x):
    for l in range(a+2,2,-1):
        if l==j+2:
            for i in range(l):
                y=-180+(l-2)*180/l
                fd(x)
                rt(y)
                
d=0
for j in range(a,0,-1):
    c=0
    while c<j:
        penup()
        seth(90-180/a)
        fd(25/m.sqrt(1/a)+20)
        seth(0)
        pendown()
        figura(50)
        penup()
        right(90+180/a)
        fd(25/m.sqrt(1/a)+20)
        seth(0)
        fd(88)
        c += 1    
    setposition((d+1)*40,((d+1)*100))       
    d +=  1
exitonclick()