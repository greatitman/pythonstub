#! /usr/bin/env python  
# coding=utf-8  
from bottle import *  
import hashlib  
import xml.etree.ElementTree as ET  
import urllib2  
# import requests  
import json
@get( "/ ")
def checkSignature():
		"""
		    这里是用来做接口验证的，从微信Server请求的URL中拿到&ldquo;signature&rdquo;,&ldquo;timestamp&rdquo;, "nonce "和&ldquo;echostr&rdquo;，  
		    然后再将token, timestamp, nonce三个排序并进行Sha1计算，并将计算结果和拿到的signature进行比较，  
		    如果相等，就说明验证通过。  
		    话说微信的这个验证做的很渣，因为只要把echostr返回去，就能通过验证，这也就造成我看到一个Blog中，  
		    验证那儿只返回了一个echostr，而纳闷了半天。  
		    附微信Server请求的Url示例：http://yoursaeappid.sinaapp.com//?signature=730e3111ed7303fef52513c8733b431a0f933c7c  
		    &amp;echostr=5853059253416844429&amp;timestamp=1362713741&amp;nonce=1362771581  
		     """ 
	token =  "******* "  # 你在微信公众平台上设置的TOKEN  
	signature = request.GET.get('signature', None)  # 拼写不对害死人那，把signature写成singnature，直接导致怎么也认证不成功  
	timestamp = request.GET.get('timestamp', None)  
	nonce = request.GET.get('nonce', None)  
	echostr = request.GET.get('echostr', None)  
	tmpList = [token, timestamp, nonce]  
	tmpList.sort()  
	tmpstr =  "%s%s%s " % tuple(tmpList)  
	hashstr = hashlib.sha1(tmpstr).hexdigest()  
	if hashstr == signature:
		return echostr
	else:
		return None

def test():
	print "test"

def parse_msg():
	recvmsg = request.body.read()
	root = ET.fromstring(recvmsg)
	msg = {}
	for child in root:  
		msg[child.tag] = child.text  
	return msg

def query_movie_info():
	"""
    这里使用豆瓣的电影search API，通过关键字查询电影信息，这里的关键点是，一是关键字取XML中的Content值，  
    二是如果Content中存在汉字，就需要先转码，才能进行请求  
	"""
	
	movieurlbase =  "http://api.douban.com/v2/movie/search "  
	DOUBAN_APIKEY =  "************** "  # 这里需要填写你自己在豆瓣上申请的应用的APIKEY  
	movieinfo = parse_msg()  
	searchkeys = urllib2.quote(movieinfo[ "Content "].encode( "utf-8 "))  # 如果Content中存在汉字，就需要先转码，才能进行请求  
	url = '%s?q=%s&amp;apikey=%s' % (movieurlbase, searchkeys, DOUBAN_APIKEY)  
	# return  "<p>{'url': %s}</p> " % url  
	# url = '%s%s?apikey=%s' % (movieurlbase, id[ "Content "], DOUBAN_APIKEY)  
	# resp = requests.get(url=url, headers=header)  
	resp = urllib2.urlopen(url)  
	movie = json.loads(resp.read())  
	# return  "<p>{'movie': %s}</p> " % movie  
	# info = movie[ "subjects "][0][ "title "] + movie[ "subjects "][0][ "alt "]  
	# info = movie['title'] + ': ' + ''.join(movie['summary'])  
	return movie  
	# return info  
		  
		  
def query_movie_details():
	"""
    这里使用豆瓣的电影subject API，通过在query_movie_info()中拿到的电影ID，来获取电影的summary。
     """
	movieurlbase =  "http://api.douban.com/v2/movie/subject/ "
	DOUBAN_APIKEY =  "**************** "  # 这里需要填写你自己在豆瓣上申请的应用的APIKEY
	id = query_movie_info()
	url = '%s%s?apikey=%s' % (movieurlbase, id[ "subjects "][0][ "id "], DOUBAN_APIKEY)
	resp = urllib2.urlopen(url)
	description = json.loads(resp.read())
	description = ''.join(description['summary'])
	return description
		  
		  
@post( "/ ")
def response_msg():
	"""
	这里是响应微信Server的请求，并返回数据的主函数，判断Content内容，如果是&ldquo;Hello2BizUser&rdquo;，就
	表明是一个新注册用户，调用纯文本格式返回，如果是其他的内容就组织数据以图文格式返回。

	基本思路：
	# 拿到Post过来的数据
	# 分析数据（拿到FromUserName、ToUserName、CreateTime、MsgType和content）
	# 构造回复信息（将你组织好的content返回给用户）
		"""

	msg = parse_msg()

	textTpl =  """<xml>
				<ToUserName><![CDATA[%s]]></ToUserName>
				<FromUserName><![CDATA[%s]]></FromUserName>
				<CreateTime>%s</CreateTime>
				<MsgType><![CDATA[%s]]></MsgType>
				<Content><![CDATA[%s]]></Content>
				<FuncFlag>0</FuncFlag>
				</xml>"""

	pictextTpl =  """<xml>
		<ToUserName><![CDATA[%s]]></ToUserName>
		<FromUserName><![CDATA[%s]]></FromUserName>
		<CreateTime>%s</CreateTime>
		<MsgType><![CDATA[news]]></MsgType>
		<ArticleCount>1</ArticleCount>
		<Articles>
		<item>
		<Title><![CDATA[%s]]></Title>
		<Description><![CDATA[%s]]></Description>
		<PicUrl><![CDATA[%s]]></PicUrl>
		<Url><![CDATA[%s]]></Url>
		</item>
		</Articles>
		<FuncFlag>1</FuncFlag>
	</xml> """

	#判断Content内容，如果等于 "Hello2BizUser "，表明是一个新关注用户，如果不是，就返回电影标题，电影简介
	#和电影海报组成的图文信息
	if msg[ "Content "] ==  "Hello2BizUser ":
		echostr = textTpl % (
	        msg['FromUserName'], msg['ToUserName'], str(int(time.time())), msg['MsgType'],
	        u "欢迎关注豆瓣电影，输入电影名称即可快速查询电影讯息哦！ ")
		return echostr
	else:
		Content = query_movie_info()
		description = query_movie_details()
		echostr = pictextTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())),
		                        Content[ "subjects "][0][ "title "], description,
		                        Content[ "subjects "][0][ "images "][ "large "], Content[ "subjects "][0][ "alt "])
		return echostr
		  
if __name__ ==  "__main__ ":
	# Interactive mode
	debug(True)
	run(host='10.66.40.57', port=8888, reloader=True)
else:
	# Mod WSGI launch
	import sae
	debug(True)
	os.chdir(os.path.dirname(__file__))
	app = default_app()
	application = sae.create_wsgi_app(app)