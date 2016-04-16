# hello  test
# coding=utf-8
# #import User from hellotest

# a = User("a")
from mylib import Compute
import requests

class User(object):
    name = "lxs"
    password = "123"
    arr = {1, 2, 3}

    def __init__(self, name, password=122):
        User.name = name
        User.password = password
        User.xy = "xxx"
        print "hello init"

        # def __new__(cls, *args, **kwargs):
        #   print "hello new "

    def about(self):
        print "name:", User.name
        print "password:", User.password
        print "xxxx : ", self.xy
        print "array :", self.arr

class Student(User):
    def __init__(self):
        print ("son student name {0}".format(Student.name))

    def study(self):
        print ("study hard")


def testSen(score=90):
    # score = 90
    if score >= 80:
        print ("good")
    elif score >= 60:
        print ("及格")
    else:
        print("bad")

    for i in range(1, 9):
        print ("item{0},{1}".format(i, "hello"))

if __name__ == '__main__':
    user = User("bb")
    # a = 21
    # print "hello test", a
    #user.about()
    #testSen(40)
    s = Student()
    s.study()
    h = Compute()
    a = 3
    b = 5
    print ("max of {0} and {1} is {2} ".format(a,b,h.max(a,b)))
    payload = {'category':0,'city':0,'otherFilter':0, 'rows':20}
    r = requests.get("http://www.yunkanli.com",params=payload)
    print(r.url)
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'}
    r = requests.get('http://localhost:5000/index',headers= headers)
    print(r.text)