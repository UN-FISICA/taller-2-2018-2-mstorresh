#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from turtle import *
T1=Turtle()
T2=Turtle()
T2.pensize(5)
T1.hideturtle()
T2.hideturtle()
a=int(input("numero de lados: "))
D1=100  #dimension del cuadrado grande
d2=20   #dimension de las figuras en los bordes
d3=d2/2
for j in range(a):
    if a==2+j:
        y=-180+(a-2)*180/a            
def figura(x):
    for i in range(a):
        T2.fd(x)
        T2.rt(y)
def cuadro(z):
    for i in range(4):
        T1.penup()
        T1.fd(z)
        T2.pendown()
        b=T1.pos()
        c=b-(d3,d3)
        T2.penup()
        T2.goto(c)
        T2.pendown()
        figura(d2)
        T1.rt(-90)        
cuadro(D1)
exitonclick()