#pylint:disable=E0001
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
O = '\33[1;33m'
N = '\x1b[0m'
GR="\033[40m\033[1;30m"
error=f"{R}[ ! ]{W} {GR}"
done=f"{G}[ + ]{W} "
start=f"{B}[ * ]{W} "
import os
try:
	import requests
	import mechanize
	import bs4
	import argparse
except:
	os.system("pip install requests && pip install mechanize && pip install bs4 && pip install argparse")
import requests
import mechanize
import sys
import time
import random
import os
import json
from bs4 import BeautifulSoup as bs
import argparse
from source import userword_password
from source import username_wordpass
from source import worduser_pass
from source import user_pass
def bannerarg():
	print(f'''{R}
    ____                         __   _  __
   / __/___  _____________  ____/ /  | |/ /
  / /_/ __ \/ ___/ ___/ _ \/ __  /   |   / 
 / __/ /_/ / /  / /__/  __/ /_/ /   /   |  
/_/  \____/_/   \___/\___/\__,_/   /_/|_| {P}v2{W}   

{W}[{R}?{W}] {G}use{O} python3 forcedx2.py --help {W}
{W}[{R}?{W}] {G}or use{O} python3 forcedx2.py --yho	{GR} The best{W}
''')
def ban():
	print(f'''{R}
    ____                         __   _  __
   / __/___  _____________  ____/ /  | |/ /
  / /_/ __ \/ ___/ ___/ _ \/ __  /   |   / 
 / __/ /_/ / /  / /__/  __/ /_/ /   /   |  
/_/  \____/_/   \___/\___/\__,_/   /_/|_| 

{W}[{R} * {W}]{G} forced X {R}Brute force {P}v2{W}\033[40m\033[1;30m by issam iso{W}''')
def txt(v):
	for i in v:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.1)
def txt2(v):
	for i in v:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0)




def yho():
	os.system('clear')
	ban()
	txt2(f'{W}[{R} * {W}]{G} ')
	txt(B+f'Welcome to forcedx{R} v2')
	print(f'''
{R}--------------------------------------------
{W}[{G} 1 {W}] Brute force username PasswordList
{W}[{G} 2 {W}] Brute force UsernameList password
{W}[{G} 3 {W}] Brute force UsernameList PasswordList
{W}[{G} 4 {W}] Login one username password
{W}[{G} 5 {W}] Reach with me 
{R}--------------------------------------------''')
	try:
		cmd=input(done+f'choice :{W} ')
		cmd=cmd.strip()
	except:sys.exit()
	if cmd=='1' or cmd =='01':
		try:
			url=input(start+"Enter url : ").strip()
			username=input(start+"Enter username : ").strip()
			passlist=input(start+"Enter password file : ").strip()
			formuser=input(start+"Enter formuser or Enter :").strip()
			if len(formuser) ==0:
				formuser=0
			formpass=input(start+'Enter formpass or Enter : ').strip()
			if len(formpass)==0:
				formpass=0
			keytrue=input(start+'Enter keytrue ex"Login succeeded" or Enter :').strip()
			if len(keytrue)==0:
				keytrue='00iso'
			keyfalse=input(start+'Enter keyfalse ex"login error" or Enter :').strip()
			if len(keyfalse) ==0:
				keyfalse='00iso'
			proxy=input(start+f'Enter proxy list{R} .txt{W} or proxy ip or Enter : ').strip()
			if len(proxy) ==0:
				proxy="Null"
			os.system('clear')
			username_wordpass.user_wordpass(url,formuser,formpass,keyfalse,keytrue,username,passlist,proxy)
		except KeyboardInterrupt:sys.exit()
		except Exception as ex:print(error+str(ex))
	if cmd=='2' or cmd=='02':
		try:
			url=input(start+"Enter url : ").strip()
			userlist=input(start+"Enter username file : ").strip()
			password=input(start+"Enter password : ").strip()
			formuser=input(start+"Enter formuser or Enter :").strip()
			if len(formuser) ==0:
				formuser=0
			formpass=input(start+'Enter formpass or Enter : ').strip()
			if len(formpass)==0:
				formpass=0
			keytrue=input(start+'Enter keytrue ex"Login succeeded" or Enter :').strip()
			if len(keytrue)==0:
				keytrue='00iso'
			keyfalse=input(start+'Enter keyfalse ex"login error" or Enter :').strip()
			if len(keyfalse) ==0:
				keyfalse='00iso'
			proxy=input(start+f'Enter proxy list{R} .txt{W} or proxy ip or Enter : ').strip()
			if len(proxy) ==0:
				proxy="Null"
			os.system('clear')
			worduser_pass.wordsusers_passw(url,formuser,formpass,keyfalse,keytrue,userlist,password,proxy)          #  # # # # # # #;#;;#;#;#
		except KeyboardInterrupt:sys.exit()
		except Exception as ex:print(error+str(ex))

	if cmd=="3" or cmd=='03':
		try:
			url=input(start+"Enter url : ").strip()
			userlist=input(start+"Enter username file : ").strip()
			passlist=input(start+"Enter password file : ").strip()
			formuser=input(start+"Enter formuser or Enter :").strip()
			if len(formuser) ==0:
				formuser=0
			formpass=input(start+'Enter formpass or Enter : ').strip()
			if len(formpass)==0:
				formpass=0
			keytrue=input(start+'Enter keytrue ex"Login succeeded" or Enter :').strip()
			if len(keytrue)==0:
				keytrue='00iso'
			keyfalse=input(start+'Enter keyfalse ex"login error" or Enter :').strip()
			if len(keyfalse) ==0:
				keyfalse='00iso'
			proxy=input(start+f'Enter proxy list{R} .txt{W} or proxy ip or Enter : ').strip()
			if len(proxy) ==0:
				proxy="Null"
			os.system('clear')
			userword_password.user_pass(url,formuser,formpass,keyfalse,keytrue,userlist,passlist,proxy)
		except KeyboardInterrupt:sys.exit()
		except Exception as ex:print(error+str(ex))

	if cmd=='4' or cmd=="04":
		try:
			url=input(start+"Enter url : ").strip()
			username=input(start+"Enter username : ").strip()
			password=input(start+"Enter password : ").strip()
			formuser=input(start+"Enter formuser or Enter :").strip()
			if len(formuser) ==0:
				formuser=0
			formpass=input(start+'Enter formpass or Enter : ').strip()
			if len(formpass)==0:
				formpass=0
			keytrue=input(start+'Enter keytrue ex"Login succeeded" or Enter :').strip()
			if len(keytrue)==0:
				keytrue='00iso'
			keyfalse=input(start+'Enter keyfalse ex"login error" or Enter :').strip()
			if len(keyfalse) ==0:
				keyfalse='00iso'
			proxy=input(start+f'Enter proxy list{R} .txt{W} or proxy ip or Enter : ').strip()
			if len(proxy) ==0:
				proxy="Null"
			user_pass.user_passwd(url,formuser,formpass,keyfalse,keytrue,username,password,proxy)	
		except KeyboardInterrupt:sys.exit()
		except Exception as ex:print(error+str(ex))
	if cmd=="5" or cmd=='05':
		print(f"""
{R}Facebook : {G}https://www.facebook.com/issamiso4

{R}Github : {G}https://github.com/issamiso

{R}Page Facebook : {G}https://www.facebook.com/termuxpkg
		
		""")
def parsers():
	parse=argparse.ArgumentParser(description=f"{R}Forcedx V2 by issam iso{W}")
	parse.add_argument('--url',help='target url')
	parse.add_argument('--userlist',help="username worldlist")
	parse.add_argument('--passlist',help="password wordllist")
	parse.add_argument('--username',help="just username")
	parse.add_argument('--password',help="just password")
	parse.add_argument('--formuser',help='form username default auto')
	parse.add_argument('--formpass',help='form password default auto')
	parse.add_argument('--keyfalse',help='key false ex"login error"')
	parse.add_argument("--keytrue",help='key true ex"login succeeded"')	
	parse.add_argument('--proxy',help=f'proxy ip or file proxy {R}.txt')
	parse.add_argument('--yho',help=B+'The best',action='store_true')
	parse.add_argument('--rwm',help=G+"Reach with me ",action="store_true")
	arg=parse.parse_args()
	if arg.url:
		url=arg.url
		if arg.formuser:
			formuser=arg.formuser.strip()
		if not arg.formuser:
			formuser=0
		if arg.formpass:
			formpass=arg.formpass
		if not arg.formpass:
			formpass=0
		if arg.keytrue:
			keytrue=arg.keytrue.strip()
		if not arg.keytrue:
			keytrue="00iso"
		if arg.keyfalse:
			keyfalse=arg.keyfalse.strip()
		if not arg.keyfalse:
			keyfalse="00iso"
		if arg.proxy:
			proxy=arg.proxy
		if not arg.proxy:
			proxy="Null"
		if arg.userlist and arg.passlist:
			userlist=arg.userlist
			passlist=arg.passlist
			try:
				userword_password.user_pass(url,formuser,formpass,keyfalse,keytrue,userlist,passlist,proxy)
			except KeyboardInterrupt:sys.exit()
			except Exception as ex:print(error+str(ex))
		if arg.passlist and arg.username:
			username=arg.username
			passlist=arg.passlist
			try:
				username_wordpass.user_wordpass(url,formuser,formpass,keyfalse,keytrue,username,passlist,proxy)
			except KeyboardInterrupt:sys.exit()
			except Exception as ex:print(error+str(ex))
		
		if arg.userlist and arg.password:
			userlist=arg.userlist
			password=arg.password
			try:
				worduser_pass.wordsusers_passw(url,formuser,formpass,keyfalse,keytrue,userlist,password,proxy)          #  # # # # # # #;#;;#;#;#
			except KeyboardInterrupt:sys.exit()
			except Exception as ex:print(error+str(ex))
		if arg.username and arg.password:
			username=arg.username
			password=arg.password
			try:
				user_pass.user_passwd(url,formuser,formpass,keyfalse,keytrue,username,password,proxy)
			except KeyboardInterrupt:sys.exit()
			except Exception as ex:print(error+str(ex))
	elif arg.rwm:
		print(f"""
{R}Facebook : {G}https://www.facebook.com/issamiso4

{R}Github : {G}https://github.com/issamiso

{R}Page Facebook : {G}https://www.facebook.com/termuxpkg
		""")
		time.sleep(1)
		os.system('xdg-open https://www.facebook.com/issamiso4')
	elif arg.yho:
		try:
			yho()
		except:sys.exit()
	else:
		bannerarg()
		
try:
	parsers()
except KeyboardInterrupt:sys.exit()
except Exception as ex:print(error+str(ex))









