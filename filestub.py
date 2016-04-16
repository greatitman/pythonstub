import os
import fileinput
import random
"""

"""
class FileTest(object):
    one = 0
    def __init__(self):
        print "init"

    def test(self):
        print "begin"
        fs = "/Users/benbenlee/PycharmProjects/teststub/filestub.py"
        with open(fs) as f:
            for line in f:
                print line
            f.seek(0)
            f.readline()
            f.tell()

        with open("/Users/benbenlee/PycharmProjects/teststub/filestub1.py","a") as f1:
         f1.write("hello test")
         f1.read()
        # f1.close()
    def pingjunshu(self):
        lst = [random.randint(0,10) for i in range(11)]
        s = sum(lst)
        length = len(lst)
        average = s*1.0/length
        print "average {0}".format(average)
        lst.sort()
        middle = lst[length/2]
        print "middle ", middle
        m = {}
        for i in lst:
            if i in m:
                m[i] +=1
            else:
                m[i] = 1

        print m

        max_num = max(m.values())
        print "max ", max_num

    @classmethod
    def get_class_attr(clss):
        return clss.one

if __name__=='__main__':
    f = FileTest()
    # f.test()
    f.one = 8
    FileTest.one = 9
    print f.one
    print f.get_class_attr()
    print FileTest.get_class_attr()