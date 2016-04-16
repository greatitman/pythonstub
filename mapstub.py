"""
dict = {}
dict = dict(arg)
dict = {}.fromkeys(arg)
copy clear
get
setdefault
items/iteritems,keys iterkeys values/itervalues
pop popitem
update
has_key
"""

class DictTest(object):
    def __init__(self):
        print "init"

    def test(self):
        print "test dict begin"
        d = {"key": "value", "key1":"VALUE"}
        D = {}
        D['nanjing']="jiangsu"
        D['hefei'] = 'anhui'
        web = (["lxs", 10],['ben',6])
        web = dict(web)
        book = {}.fromkeys(("python","author"),"lxs")
        city_codes = {"nanjing":"025", "guangzhou":"020"}
        city_codes["beijing"]= "010"
        print d
        print D.__len__()
        print D
        print web
        print book
        print city_codes["nanjing"]
        print city_codes
        print "beijing code is %(beijing)s"% city_codes
        print len(city_codes)
        print "nanjing" in city_codes
        del city_codes["nanjing"]
        print "nanjing" in city_codes
        city_codes["nanjing"]="026"
        print city_codes
        f = city_codes.copy()
        e = city_codes
        city_codes["aa"]="bb"
        print id(city_codes["nanjing"])
        print id(f["nanjing"])
        print id(city_codes)
        print id(f)
        # city_codes["nanjing"].remove("026")
        print city_codes

        # print f.clear()
        # city_codes.clear()
        # del city_codes
        # city_codes = {}
        print city_codes.get("beijing")
        city_codes.setdefault("nanjing", 025)
        print city_codes
        print city_codes.items()
        d_iter = city_codes.iteritems()
        print list(d_iter)
        print city_codes.keys()
        print city_codes.iterkeys()
        print city_codes.itervalues()
        print city_codes["nanjing"]
        print city_codes.popitem()
        print city_codes

if __name__ == "__main__":
    d = DictTest()
    d.test()