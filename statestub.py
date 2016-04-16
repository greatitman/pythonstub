import  copy
import random
from math import *

"""

"""
class StateTest(object):
    def __init__(self):
        print "init"

    def test(self):
        a = 2
        b = 2
        print a==b
        print a is b
        print b is a
        c = copy.deepcopy(a)
        print c==a
        print c is a
        print a is c
        print bool(a)
        print bool(-1 and 0)
        print "begin test"
        for i in "cangloashi":
            print i
        lst = ['goole','aidu','biying']
        for i in lst:
            print i
        t = tuple(lst)
        for i in t:
            print i

        num = random.randint(1,100)
        # for i in range(0,100):
        #     input_num = int(raw_input("please input"))
        #     if num==input_num:
        #         print num
        #         break;
        #     elif input_num> num:
        #         print "larger"
        #     else:
        #         print "smaller"
        # i = 0
        # while i<10:
        #     print i
        #     input_num = int(raw_input("please input"))
        #     if input_num==num:
        #         print num
        #         break;
        #     elif input_num>num:
        #         print "bigger"
        #     else:
        #         print "samller"
        #     i = i+1
        for n in range(99,1,-1):
            root = sqrt(n)
            if root == int(root):
                print n
                break;

if __name__=="__main__":
    s = StateTest()
    s.test()