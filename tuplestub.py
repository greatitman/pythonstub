
class TupleTest(object):
    def __init__(self):
        print "init"

    def test(self):
        a = (1,3,4)
        b = [1,2,3]
        temp = list(a)
        temp[2]=100
        a = tuple(temp)
        print a
        print (1)
        print (1,)
        print "count {0}".format(a.count(1))
        print "index {0}".format(a.index(1))

if __name__=='__main__':
    arr = TupleTest()
    arr.test()
