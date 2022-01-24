# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:39:46 2022

@author: FELF3L
"""



# s=float(input("entrez le pas :"))
# x1=float(input("entrez la position initiale :"))
# t_prb=input("quel est le type de probleme? (min ou max):")

s=0.05
x1=0.0
i=1

class Pas_fixe():
    
    def __init__(self):
        self.s = s
        self.x1 = x1
        self.i = i
    
    def x(self,i,s,x1):
    
        if i > 0:
            return x1 + (i-1) * s
        else:
            return x1 - (i-1) * s


    def f(self,i,s,x1):
        
        dex = self.x(i,s,x1)**5 - self.x(i,s,x1)**3 - 20*self.x(i, s, x1) + 5
        return dex

    def pas_fixe(self,i,s,x1):
        
        if self.f(2,s,x1) < self.f(1,s,x1) : # On est dans un problème de minimisation
    
            while self.f(i+1,s,x1)<self.f(i,s,x1): 
                i = i+1
                a = self.x(i-1,s,x1)
                b = self.x(i,s,x1)
    
        elif self.f(2,s,x1) > self.f(1,s,x1): #La recherche doit-être effectuée en sens inverse au points
        
            while self.f(i+1,s,x1) > self.f(i,s,x1):
                i = i-1
                a = self.x(i-1,s,x1)
                b = self.x(i,s,x1)
                
    
        elif self.f(1,s,x1) == self.f(2,s,x1):
        
            a = self.x(1,s,x1)
            b = self.x(2,s,x1)
    
        elif self.f(2,s,x1) > self.f(1,s,x1) and self.f(-2,s,x1) > self.f(1,s,x1):
           a = self.x(-2,s,x1)
           b = self.x(2,s,x1)
        return i,a,b


Test = Pas_fixe()
t = Test.pas_fixe(i, s, x1) 
i=t[0]
au=t[1]
bu=t[2]   
print("Le point de minimum x* est compris entre ",au," et ",bu,". On a f(x*)=",Test.f(i,s,x1))
             

    