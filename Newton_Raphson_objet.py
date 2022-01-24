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

x1=1
eps=0.001
x = Symbol('x')
f = x**3 - x-1
df = f.diff(x)
ddf = df.diff(x)
eps = 0.1

class Newton_Raphson():


    
    def __init__(self):
        self.x1 = x1
        self.eps = eps
        self.y = f
        self.yprime = f.diff(x)
        self.yprime2 = self.yprime.diff(x)
        
    def derive(self,x):
        
        x = Symbol('x')    
        self.y = x**3 - 7*x**2 + 8*x - 3
        self.yprime = self.y.diff(x)
        self.yprime2 = self.yprime.diff(x)
    
    def f(self):
        return self.y
        # return self.x**3-self.x-1

    def df(self,x):
        return self.yprime
        # return (3*(x**2))-1

    def ddf(self,x):
        return self.yprime2
        # return 6*x
    
    def x(self,i,df,ddf,x1):
        
        if i==1:
            return x1
        
        else:
            return self.x(i-1,df,ddf,x1)-(self.df(self.x(i-1,df,ddf,x1))/self.ddf(self.x(i-1,df,ddf,x1)))
        self.test = abs(self.df(self.x(i,df,ddf,x1)))
        
    
    def NewtonR(self,df,ddf,x1,eps):
        i=1
        while abs(self.df(self.x(i,df,ddf,x1)))>eps:            
            i= i + 1            
        return self.x(i,df,ddf,x1)   
        
    # print (NR(self,x1,eps))


Test = Newton_Raphson()
tes = Test.NewtonR(df,ddf,x1,eps)
