"""
Created on Sun Jan 21 22:39:46 2022

@author: FELF3L
"""

s=0.05
x1=0.0
i=1

class Pas_fixe_acc():

    def __init__(self):
        self.i = i
        self.x1 = x1
        self.s = s

    def x(self,i,s,x1):
        if i>0:
            return x1 + (i-1) *s
        else:
            return x1 - (i+1) *s


    def f(self,i,s,x1):
        return self.x(i,s,x1)**5 - self.x(i,s,x1)**3 - 20*self.x(i, s, x1) + 5

    def pas_fixe_acc(self,i,s,x1):
        
        x1=0.0       
        s=0.05
        i=1
        if self.f(2,s,x1)<self.f(1,s,x1) :
            
            while self.f(i+1,s,x1)<self.f(i,s,x1): 
                i+=1
                s=2*s
                a=self.x(i-1,s,x1)
                b=self.x(i,s,x1)
       
        if self.f(2,s,x1)>self.f(1,s,x1):
            while self.f(i+1,s,x1)>self.f(i,s,x1):
                i-=1
                s=2*s
                a=self.x(i-1,s,x1)
                b=self.x(i,s,x1)
        elif self.f(2,s,x1)==self.f(3,s,x1):
            a=self.x(1,s,x1)
            b=self.x(2,s,x1)
        elif self.f(2,s,x1)>self.f(1,s,x1) and self.f(2,s,x1)>self.f(1,s,x1):
            a=self.x(-2,s,x1)
            b=self.x(2,s,x1)
        
        return i,a,b,s

Test = Pas_fixe_acc()
results = Test.pas_fixe_acc(i, s, x1) 
i=results[0]
a=results[1]
b=results[2]   
s=results[3]
print("Le point de minimum x* est compris entre ",a," et ",b, "de plus f(x*) = ,",s)
