# -*- coding: utf-8 -*-
"""

@author: Faris
"""

from sympy import *

#La bibliothèque sympy permet de calculer une dérivée d'une fonction


# def f(x):
#     return x**3-x-1

# def df(x):
#     return (3*(x**2))-1

# def ddf(x):
#     return 6*x

def derive(x):
    x = Symbol('x')    
    y = x**3 - x-1
    yprime = y.diff(x)
    yprime2 = yprime.diff(x)
    
def f(x):
    return x**3-x-1

def df(x):
    return (3*(x**2))-1

def ddf(x):
    return 6*x
    

x1=1
eps=0.001

def x(i,df,ddf,x1):
    if i==1:
        return x1
    else:
        return x(i-1,df,ddf,x1)-(df(x(i-1,df,ddf,x1))/ddf(x(i-1,df,ddf,x1)))
    
def NR(x1,eps):
    i=1
    while abs(df(x(i,df,ddf,x1)))>eps:
        i+=1
    return x(i,df,ddf,x1)   
    
print (NR(x1,eps))
 
# def x(i,x1):
#     if i == 1:
#         return x1
#     else: 
#         return x()