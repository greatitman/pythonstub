"""
issubset
issuperset
union
intersection
difference
"""

class SetTest(object):
    def __init__(self):
        print "init"

    def test(self):
        s = {1, "lxs"}
        s1 = set("string")
        s2 = set(["gogole","facebook", "twiter"])
        s3 = set([1,1,1])
        s4 = set({1,2,4})
        lst = [1,2,3,4,4,5,5]
        s5 = set(lst)
        lst1 = list(s5)
        s6 = frozenset(lst1)
        s7 = set()
        s7.add((1,2,3))
        print s
        print s1
        print s2
        print s3
        print s4
        print lst1
        print s7
        print hash(s6)

if __name__=="__main__":
    s = SetTest()
    s.test()

