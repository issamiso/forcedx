W = '\33[0m'
R = '\33[1;31m'
G = '\033[1;32m'
O = '\33[1;33m'
B = '\33[1;34m'
P = '\33[1;35m'
C = '\33[1;36m'
#GR = '\33[1;37m'
GR="\033[40m\033[1;30m"
list=[]
error=f'{W}[{R} ! {W}]{R} Error{GR} '
done=f'{W}[{P} + {W}]{G} '
ty=f'{W}[{R} *{W} ]{W} '
import os
import sys
import time
import random
try:
	import argparse
	import mechanize
	import requests
	from bs4 import BeautifulSoup as bs
	import user_agent
except KeyboardInterrupt:
	sys.exit()
except:
	os.system('pip install mechanize && pip install requests && pip install bs4 && pip install user-agent && pip install argparse ')
try:
	from data import login
	from data import UP
	from data import Pu
	from data import U_p
except:
	print(error+'data not found')
	sys.exit()
from data import login
from data import UP
from data import Pu
from data import U_p

try:
	import argparse
	import mechanize
	import requests
	from bs4 import BeautifulSoup as bs
	import user_agent
except KeyboardInterrupt:
	sys.exit()
except:
	print(error+'failed to install library '+W+'requests , mechanize , bs4 , user-agent , argparse')
	sys.exit()

import argparse
import mechanize
import requests
from bs4 import BeautifulSoup as bs
import user_agent

user_=user_agent.generate_user_agent(os=('android'))

def ban():
	print(f'''{R}
    ____                         __   _  __
   / __/___  _____________  ____/ /  | |/ /
  / /_/ __ \/ ___/ ___/ _ \/ __  /   |   / 
 / __/ /_/ / /  / /__/  __/ /_/ /   /   |  
/_/  \____/_/   \___/\___/\__,_/   /_/|_| 

{W}[{R}*{W}]{G} forced X {R}Brute force {P}v1{W}\033[40m\033[1;30m Bay issam iso
''')
def bannerarg():
	print(f'''{R}
    ____                         __   _  __
   / __/___  _____________  ____/ /  | |/ /
  / /_/ __ \/ ___/ ___/ _ \/ __  /   |   / 
 / __/ /_/ / /  / /__/  __/ /_/ /   /   |  
/_/  \____/_/   \___/\___/\__,_/   /_/|_| {G}{{✓}} {P}v1{W}   

{W}[{R}?{W}] {G}use{O} python3 forced.py --help {W}
{W}[{R}?{W}] {G}or use{O} python3 forced.py --yho	{GR} The best{W}
''')



def yhos():
	os.system('clear')
	ban()
	print(f'''
{W}[{R} 1 {W}] Brute force username PasswordList
{W}[{R} 2 {W}] Brute force UsernameList password
{W}[{R} 3 {W}] Brute force UsernameList PasswordList
{W}[{R} 4 {W}] Login one Username password
{W}[{R} 5 {W}] Reach with me 
	''')
	cmd=input(done+f'choice :{W} ')
	cmd=cmd.strip()
	if cmd == "1":
		url=input(ty+'url : ').strip()
		username=input(ty+'username : ').strip()
		password=input(ty+'passwordList : ').strip()
		formuser=input(ty+'username form name (or enter) : ').strip()
		if formuser == "":
			formuser=0
		formpass=input(ty+'password form name (or enter) : ').strip()
		if formpass == "":
			formpass=0
		keyfalse=input(ty+'key false ex(login error) : ').strip()
		if keyfalse == "":
			print(error+'enter key false')
			keyfalse=input(ty+'key false ex(login error) : ').strip()
		keytrue=input(ty+'key true or enter : ').strip()
		if keytrue == '':
			keytrue="akeifjcnfkskwoeifjfjfjeksifi﷼«♕%_+$"
		os.system('clear')
		try:
			Pu.Pu(url,username,password,formuser,formpass,keyfalse,keytrue)
		except KeyboardInterrupt:
			sys.exit()
		except Exception as ex:
			print(R)
			print(ex)
	if cmd == "2":
		url=input(ty+'url : ').strip()
		username=input(ty+'usernamelist : ').strip()
		password=input(ty+'password : ').strip()
		formuser=input(ty+'username form name (or enter) : ').strip()
		if formuser == "":
			formuser=0
		formpass=input(ty+'password form name (or enter) : ').strip()
		if formpass == "":
			formpass=0
		keyfalse=input(ty+'key false ex(login error) : ').strip()
		if keyfalse == "":
			print(error+'enter key false')
			keyfalse=input(ty+'key false ex(login error) : ').strip()
		keytrue=input(ty+'key true or enter : ').strip()
		if keytrue == '':
			keytrue="akeifjcnfkskwoeifjfjfjeksifi﷼«♕%_+$"
		os.system('clear')
		try:
			U_p.Up(url,username,password,formuser,formpass,keyfalse,keytrue)
		except KeyboardInterrupt:
			sys.exit()
		except Exception as ex:
			print(R)
			print(ex)
	if cmd == "3":
		url=input(ty+'url : ').strip()
		username=input(ty+'usernamelist : ').strip()
		password=input(ty+'passwordlist : ').strip()
		formuser=input(ty+'username form name (or enter) : ').strip()
		if formuser == "":
			formuser=0
		formpass=input(ty+'password form name (or enter) : ').strip()
		if formpass == "":
			formpass=0
		keyfalse=input(ty+'key false ex(login error) : ').strip()
		if keyfalse == "":
			print(error+'enter key false')
			keyfalse=input(ty+'key false ex(login error) : ').strip()
		keytrue=input(ty+'key true or enter : ').strip()
		if keytrue == '':
			keytrue="akeifjcnfkskwoeifjfjfjeksifi﷼«♕%_+$"
		os.system('clear')
		try:
			UP.UsernamePassword(url,username,password,formuser,formpass,keyfalse,keytrue)
		except KeyboardInterrupt:
			sys.exit()
		except Exception as ex:
			print(R)
			print(ex)
	if cmd == "4":
		url=input(ty+'url : ').strip()
		username=input(ty+'username : ').strip()
		password=input(ty+'password : ').strip()
		formuser=input(ty+'username form name (or enter) : ').strip()
		if formuser == "":
			formuser=0
		formpass=input(ty+'password form name (or enter) : ').strip()
		if formpass == "":
			formpass=0
		keyfalse=input(ty+'key false ex(login error) : ').strip()
		if keyfalse == "":
			print(error+'enter key false')
			keyfalse=input(ty+'key false ex(login error) : ').strip()
		keytrue=input(ty+'key true or enter : ').strip()
		if keytrue == '':
			keytrue="akeifjcnfkskwoeifjfjfjeksifi﷼«♕%_+$"
		os.system('clear')
		try:
			login.login(url,username,password,formuser,formpass,keyfalse,keytrue)
		except KeyboardInterrupt:
			sys.exit()
		except Exception as ex:
			print(R)
			print(ex)
	if cmd == '5':
		print(f'''
{R}Facebook :{W} https://www.facebook.com/issamiso4
{R}Github :{W} https://github.com/issamiso
{R}Telegram :{W} @issamiso4
		''')
		
		
	
	
	
	
	
	
def argss():
	parse=argparse.ArgumentParser()
	parse.add_argument('--url',dest='url')
	parse.add_argument('--username',dest='username')
	parse.add_argument('--password',dest='password')
	parse.add_argument('--keyfalse',dest='keyfalse',help=' Key Error ex ( login error )')
	parse.add_argument('--keytrue',dest='keytrue',help="Key True ex ( login successfully  ) ")
	parse.add_argument('--formuser',dest='formuser',help=' username form name or not choose ')
	parse.add_argument('--formpass',dest='formpass',help='password form name or not choose')
	parse.add_argument('--userlist',dest='userlist',help='username list')
	parse.add_argument('--passlist',dest='passlist',help='password list')
	parse.add_argument('--yho',dest='yho',action='store_true',help='The best')
	arg=parse.parse_args()
	if arg.url:
		url=arg.url
		if arg.username and arg.password:
			username=arg.username
			password=arg.password
			if arg.keyfalse:
				keyfalse=arg.keyfalse
			if not arg.keyfalse:
				print(error+'keyfalse not select')
				sys.exit()
			if arg.formuser:
				formuser=arg.formuser
			if not arg.formuser:
				formuser=0
			if arg.formpass:
				formpass=arg.formpass
			if not arg.formpass:
				formpass=0
			if arg.keytrue:
				keytrue=arg.keytrue
			if not arg.keytrue:
				keytrue="QWERTYUIOSJDDJWKSKFKFJNCNDJSJDJ"
			try:
				login.login(url,username,password,formuser,formpass,keyfalse,keytrue)
			except KeyboardInterrupt:
					sys.exit()
			except Exception as ex:
				print(R)
				print(ex)
		if arg.userlist and arg.passlist:
				username=arg.userlist
				password=arg.passlist
				if arg.keyfalse:
					keyfalse=arg.keyfalse
				if not arg.keyfalse:
					print(error+'keyfalse not select')
					sys.exit()
				if arg.keytrue:
					keytrue=arg.keytrue
				if not arg.keytrue:
					keytrue='QWERYJEKXJFJDKSKDKCKCNRNSKXKCKKF'
				if arg.formuser:
					formuser=arg.formuser
				if not arg.formuser:
					formuser=0
				if arg.formpass:
					formpass=arg.formpass
				if not arg.formpass:
					formpass=0
				try:
					UP.UsernamePassword(url,username,password,formuser,formpass,keyfalse,keytrue)
				except KeyboardInterrupt:
					sys.exit()
				except Exception as ex:
					print(R)
					print(ex)
		if arg.passlist and arg.username:
				username=arg.username
				password=arg.passlist
				if arg.keyfalse:
					keyfalse=arg.keyfalse
				if not arg.keyfalse:
					print(error+'keyfalse not select')
					sys.exit()
				if arg.keytrue:
					keytrue=arg.keytrue
				if not arg.keytrue:
					keytrue='QWERYJEKXJFJDKSKDKCKCNRNSKXKCKKF'
				if arg.formuser:
					formuser=arg.formuser
				if not arg.formuser:
					formuser=0
				if arg.formpass:
					formpass=arg.formpass
				if not arg.formpass:
					formpass=0
				try:
					Pu.Pu(url,username,password,formuser,formpass,keyfalse,keytrue)
				except KeyboardInterrupt:
					sys.exit()
				except Exception as ex:
					print(R)
					print(ex)
		if arg.userlist and arg.password:
				username=arg.userlist
				password=arg.password
				if arg.keyfalse:
					keyfalse=arg.keyfalse
				if not arg.keyfalse:
					print(error+'keyfalse not select')
					sys.exit()
				if arg.keytrue:
					keytrue=arg.keytrue
				if not arg.keytrue:
					keytrue='QWERYJEKXJFJDKSKDKCKCNRNSKXKCKKF'
				if arg.formuser:
					formuser=arg.formuser
				if not arg.formuser:
					formuser=0
				if arg.formpass:
					formpass=arg.formpass
				if not arg.formpass:
					formpass=0
			#	Pu.Pu(url,username,password,formuser,formpass,keyfalse,keytrue)
				try:
					U_p.Up(url,username,password,formuser,formpass,keyfalse,keytrue)
				except KeyboardInterrupt:
					sys.exit()
				except Exception as ex:
					print(R)
					print(ex)
	elif arg.yho:
		try:
			yhos()
		except:
			print(error+'exit tool')
	else:
		bannerarg()
	
	
argss()











