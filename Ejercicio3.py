#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from turtle import *
T1=Turtle()
T2=Turtle()
T2.pensize(5)
T1.hideturtle()
T2.hideturtle()
a=int(input("numero de lados de las figuras en los bordes : "))
l=int(input("numero de lados del poligono base "))
D1=100  #dimension del cuadrado grande 
d2=20   #dimension de las figuras en los bordes
d3=d2/2
for j in range(a): 
    if a==2+j:
        y=-180+(a-2)*180/a 
for j in range(l):
    if l==2+j:
        k=-180+(l-2)*180/l            
def figura(x):
    for i in range(a):
        T2.fd(x)
        T2.rt(y)
def fig(z):
    for i in range(l):
        T1.penup()
        T1.fd(z)
        T2.pendown()
        b=T1.pos()
        c=b-(d3,d3)
        T2.penup()
        T2.goto(c)
        T2.pendown()
        figura(d2)
        T1.rt(k)        
fig(D1)
exitonclick()