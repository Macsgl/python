#coding = utf-8
import urllib2
import MySQLdb
import time
from bs4 import BeautifulSoup
while True:
	conn = MySQLdb.connect(host='localhost',port=3306,user='mac',passwd='123654',db='test',charset='utf8')
	cur = conn.cursor()
	cur.execute('SET NAMES utf8')
	sql = "SELECT URL FROM urls WHERE IsUsed = 0 LIMIT 1"
	cur.execute(sql)
	if cur.execute(sql) == 1:
		x = cur.fetchall()
		z = list(x)
		y = list(z[0])
		url = str(y[0])
		sql = "UPDATE urls SET IsUsed = 1 WHERE URL = '%s'" %(url)
		cur.execute(sql)
		conn.commit()
		req = urllib2.urlopen(url)
		buf = req.read()
		soup = BeautifulSoup(buf,'html5lib')
		txts = soup.find('ul',{'class':'terminal-ul clearfix'}).find_all('li')
		txt = []
		i = 0
		while i<8:
			txts[i] = str(txts[i])
			k = BeautifulSoup(txts[i],'html5lib')
			txt.append(k.strong.get_text())
			i+=1
		texts = soup.find('div',{'class':'fixed-inner-box'})
		texts = str(texts)
		p = BeautifulSoup(texts,'html5lib')
		txt.append(p.h1.get_text())
		txt.append(p.h2.get_text())
		#txts[0] = str(txts[0])
		#soup = BeautifulSoup(txts[0],"html5lib")
		#txt = soup.strong.get_text()
		sql = "INSERT INTO php_job (jobNAME,jobCOM,jobMON,site,rel_date,nature,jobEXP,minEDU,jobNUM,jobCLASS) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(txt[8],txt[9],txt[0],txt[1],txt[2],txt[3],txt[4],txt[5],txt[6],txt[7])
		cur.execute(sql)
		conn.commit()
		cur.close()
		conn.commit()
		conn.close()
	else:
		cur.close()
		conn.commit()
		conn.close()
		time.sleep(60)


