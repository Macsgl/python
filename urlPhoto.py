import urllib2
import re
req = urllib2.urlopen('http://www.mantusy.com')
buf = req.read()
listurl = re.findall(r'/.+\.jpg',buf)
def add(x):
    return 'http://www.mantusy.com'+x
listurl = map(add,listurl)
i = 0
for url in listurl:
    f = open(str(i)+'.jpg','wb')
    req = urllib2.urlopen(url)
    buf = req.read()
    f.write(buf)
    f.close()
    i += 1

