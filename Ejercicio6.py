#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from turtle import *
import math as m
a=int(input("numero de filas de la piramide: "))
T1=Turtle()
T2=Turtle()
T1.hideturtle()
T2.hideturtle()
d=0
for j in range(a,0,-1):
    c=0
    while c<j:
        T1.penup()
        T1.seth(90-180/a)
        T1.fd(25/m.sqrt(1/a)+20)
        T1.seth(0)
        T1.pendown()
        for l in range(a+2,2,-1):
            if l==j+2:
                for i in range(l):
                    y=-180+(l-2)*180/l
                    g=2*40*m.sin(m.pi/l)
                    T1.fd(g)
                    T1.rt(y)
                    f=T1.pos()
        h=T1.pos()
        T1.penup()
        h = h+(g/2,-g/5)
        T2.penup()
        T2.goto(h)
        T2.circle(40)
        s = T2.pos()
        T1.right(90+180/a)
        T1.fd(25/m.sqrt(1/a)+20)
        T1.seth(0)
        T1.fd(88)
        c += 1    
    T1.setposition((d+1)*40,((d+1)*100))    #el d para subirlo   
    d +=  1
exitonclick()
