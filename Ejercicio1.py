# -*- coding: utf-8 -*-
from turtle import *
T1=Turtle()
T2=Turtle()
T2.pensize(5)
T1.hideturtle()
T2.hideturtle()
D1=100  #dimension del cuadrado grande
d2=20   #dimension de las figuras en los bordes
d3=d2/2
def cuadro(x):
    for i in range(4):
        T2.fd(x)
        T2.rt(-90)
def cuadrado(z):
    for i in range(4):
        T1.penup()
        T1.fd(z)
        T2.pendown()
        b=T1.pos()
        c=b-(d3,d3)
        T2.penup()
        T2.goto(c)
        T2.pendown()
        cuadro(d2)
        T1.rt(-90) 
cuadrado(100)
exitonclick()