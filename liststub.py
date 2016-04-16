"""
len
+
*
in
max() min()
cmp()
append
extend
count
index
reverse
sort
insert
pop
remove
"""
class ListTest(object):
    def __init__(self):
        print "init"

    def test(self):
        print "begin to test"
        a = ["lxs", 2, 3]
        b = [a,33,32,31]
        print a,b
        print b[0][1]
        print a.index("lxs")
        lst = [1,2,3,4,5,6]
        print lst
        print lst[::-1]
        print lst[0:4]
        print lst[0:4:2]
        print lst[5:3:-1]
        print lst[::-2]
        print list(reversed(lst))
        print "len is {0}".format(len(lst))
        print lst*3
        print "max is {0}".format(max(lst))
        print min(lst)
        lsttmp=[2,3,4]
        print cmp(lst,lsttmp)
        print id(lst)

        # lst.append(lsttmp)
        lst.extend(lsttmp)
        # lst.extend("str")
        print lst
        print hasattr("str", '__iter__')
        print hasattr(lst,'__iter__')
        print list.count(lst,9)
        print lst.count(3)
        print list.index(lst,4)
        print lst.index(4)
        lst.insert(0,99)
        print lst
        lst.pop()
        print lst
        lst.pop(3)
        print lst
        lst.remove(99)
        print lst
        lst.reverse()
        print lst
        # lst.sort()
        lst.sort(reverse=True)
        print lst
        print list("string")
        a = "python is good"
        slist = a.split(" ")
        print slist

if __name__=='__main__':
    mylist = ListTest()
    mylist.test()