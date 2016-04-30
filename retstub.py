#!/usr/local/bin/python
# coding: utf-8
import re
#from re import findall, search ,S

secret_code = 'hadddjkjkxxxIxx123xxlovexxwerwwrxxyouxxdfsafsa324'

a = 'xy123'
b = re.findall('x.?',a)
print b

class RegStub(object):
    def __init__(self):
        print "init"

    '''.   匹配任意字符,换行符除外'''
    def dottest(self,s=secret_code):
        b = re.findall('xx.', s)
        return b

    '''*   匹配前一个字符的0次或无限次'''
    def asterisk(self,s=secret_code):
        return re.findall('kx*',s)

    '''?   匹配前一个字符的0次或1次'''
    def ask(self,s=secret_code):
        return re.findall('kx?',s)

    '''.*  贪心算法'''
    def dotasterisk(self,s=secret_code):
        return re.findall('xx.*',s)

    '''.*? 非贪心算法'''
    def dotasteriskask(self,s=secret_code):
        return re.findall('xx.*?',s)

    @classmethod
    def searchtest(cls):
        print re.search('xx(.*?)xx123xx(.*?)xx',secret_code).group(2)

    @staticmethod
    def findalltest():
        #()  括号内的数据作为结果返回
        ret = re.findall('xx(.*?)xx',secret_code)
        print ret
        for i in ret:
            print i

    def sub(self,s=secret_code):
        return re.sub('123(.*?)123','ben%sben'%'li',s)

    @staticmethod
    def digtest():
        s = 'adfaa1231313jkjadf23424lkj'
        return re.findall('(\d+)',s)


if __name__=='__main__':

    test = RegStub()
    print ".匹配任意字符  ",test.dottest()
    print "*匹配前一字符的任意次  ",test.asterisk()
    print "?匹配前一个字符的0次或1次 ",test.ask()
    print ".*贪心算法 ",test.dotasterisk()
    print ".*? 非贪心算法 ",test.dotasteriskask()

    RegStub.findalltest()
    RegStub.searchtest()
    s = '123abcssfasdfas123'
    print "test for sub ",test.sub(s)

    print "test for digit ",RegStub.digtest()



