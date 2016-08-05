
#coding = utf-8
import re
import MySQLdb
import urllib2
import time
from bs4 import BeautifulSoup
while True:
	i = 0
	l = 0
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
			l += 1
	if l == 0:
		print "It's all in db."
	else:
		print "Add %d urls" %(l)
	cur.close()
	conn.commit()
	conn.close()
	time.sleep(60)