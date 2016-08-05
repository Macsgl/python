
#coding = utf-8
import re
import MySQLdb
import urllib2
import time
import logging
from bs4 import BeautifulSoup
#log_filename = 'error.log'
#log_format = '%(asctime)s - %(filename) - %(levelname)'
#logging.basicConfig(filename=log_filename,format=log_format,filemode='a',level=logging.DEBUG)
while True:
	#try:
	i = 0
	addUrlNum = 0
	req = urllib2.urlopen('http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%9D%AD%E5%B7%9E&kw=php%E5%AE%9E%E4%B9%A0%E7%94%9F&sm=0&p=1')
	buf = req.read()
	soup = BeautifulSoup(buf,"html5lib")
	links = soup.find_all('a',href=re.compile(r'http://jobs.zhaopin.com/\d+\.htm'))
	conn = MySQLdb.connect(host='localhost',port=3306,user='mac',passwd='123654',db='test')
	cur = conn.cursor()
	for link in links:
		sql = "SELECT URL FROM urls WHERE URL = '%s' LIMIT 1" %(link['href'])
		if cur.execute(sql) == 0:
			sql = "INSERT INTO urls (URL) VALUES ('%s')" %(link['href'])
			cur.execute(sql)
			conn.commit()
			addUrlNum += 1
	if addUrlNum == 0:
		f = open('record.log','a')
		note = "It's all in db. " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		f.write(note+'\r\n')
		#f.write("\n")
		f.close()
		#print "It's all in db."
	else:
		f = open('record.log','a')
		note = "Add %d urls.     " %(addUrlNum) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		f.write(note+'\r\n')
		#f.write("\n")
		f.close()
		#print "Add %d urls" %(addUrlNum)
	cur.close()
	conn.commit()
	conn.close()
	time.sleep(60)
	#except:
		#logging.exception("Exception Logged")