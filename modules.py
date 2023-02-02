#   ====Modules_____Call=====
""""
===== We have three(3) ways to improt Modules======

1. Improt module_name
2. form mudule_name import (any funcation  class  name  without brakit and you also use (*) )
3.  if you module name is  to long  when you use [ improt module_name (as) any short name N]
"""

# #==============================
# from mofile20 import *

# print(sum(500,20)) 
# #==============================
# from mofile20 import sum,mul ,my_fun

# print(mul(30,10))
# #===============================
# import mofile20

# print(mofile20.my_fun(10))

# #================================
# import mofile20 as H

# print(H.sum(30,55))

# import calendar as cal

# year=int(input("enter the year"))

# cal.setfirstweekday(cal.SUNDAY)

# cale=cal.calendar(year)
# print(cale)

# print(cal(year,month))

# n=int(input("enter the number"))
# i=1
# while i<11:
#     a=n*i
#     print(f"{n}X{i} =",a)
#     i+=1
# x=int(input("enter nay number"))
# y=int(input("enter nay number"))

# k=lambda x,y:y*x

# print(k(x,y))
# size=5
# for i in range(size):
#     for j in range(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')

#     print()
# size = 5

# # Create a list of rows
# for i in range(0, size):
#     # Create a list of columns
#     for j in range(0, size):
#         print("*", end="")
#     print()  
# import math as m
# x=3.5
# print(m.ceil(x))

# import datetime as d

# print(d.date.today())

# print(m.log10(50))

# print(m.log(10))



# import pyautogui as pt
# import time

# time.sleep(3)

# limit=int(input("enter the limit"))
# msg=input("enter the msg")
# i=0



# while i<=int(limit):
#     pt.typewrite(msg)
#     pt.press("enter")
#     i+=1

import turtle 
t = turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(2)
t.color('green')
t.left(90)
t.backward(100)
t.speed(200)
t.shape('turtle')

def tree(i):
    if i<10:
        return
    else:
        t.forward(i)
        t.color('orange')
        t.circle(2)
        t.color('brown')
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)

tree(100)
turtle.done()