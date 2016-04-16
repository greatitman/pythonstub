"""
split()
join()
s.split
S.upper()
S.lower()
S.capitalize()
S.islower
S.istitle()
dir(str)
help(str.split)
"""
class StrTest(object):
    str = 'hello'
    len = 0
    dit = 0
    c = ['i','love','u']
    url = 'www.baidu.com'
    def __init__(self,s):
        self.str=s
        self.len = len(s)
    def test(self):
        print self.str
        print self.str * 2
        print str(250)
        print ord('a')
        print chr(98)
        print (cmp('a','b'))
        print (cmp('ad','a'))
        print (cmp("123",'23'))

        print ('a' in self.str)
        print "len is {0}".format(len(self.str))
        print "last char is {0}".format(self.str[self.len-1])

        print self.str.split(",")
        print '-'.join(self.c)
        print '-'.join(self.url.split('.'))
        print " lxs ".lstrip()
        print r"c:\new world"
        t = "i am %d , i like %s"
        ii = "i am %d"
        print t % (23,self.url)
        print ii % 15
        print "Today temp is %+.2f" % 11.239

        s = "i like {0} {1}"
        print s.format("li", "ben")


if __name__=='__main__':
    ss = "hello world"
    # ss = raw_input("please input :")
    so = StrTest(ss)
    so.test()