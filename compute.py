from __future__ import division
from decimal import Decimal as D
import math
#coding:utf-8

"""
compute function

"""

class Compute(object):
    a = 3
    b = 4
    def __init__(self):
        print "init a={0},b={1}".format(self.a,self.b)
    def add(self,a,b):
        a = D(a)
        b = D(b)
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):

        return a/b

if __name__=='__main__':
    c = Compute()
    print "compute test {0}".format(c.div(6,3))
    print "compute 0.3 add 0.4 = {0}".format(c.add(D("0.1"),D("0.2")))
    a = divmod(5,2)
    print a[1]