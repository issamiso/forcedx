import time
import os
import sys
R  = '\33[1;31m'
G  = '\33[1;32m'
P  = '\33[1;35m'
C  = '\33[1;36m'
def bnr():
	print(P+'''
  ____                 _           _     _     _
 / ___| ___   ___   __| |         | |   (_)___| |_
| |  _ / _ \ / _ \ / _` |  _____  | |   | / __| __|
| |_| | (_) | (_) | (_| | |_____| | |___| \__ \ |_
 \____|\___/ \___/ \__,_|         |_____|_|___/\__|
	''')
def list():
	file=input(R+'Enter The List Password : ')
	os.system('clear')
	bnr()
	#ff=open(file,'w')
	#ff.close()
	a=set([])
	may=set([])
	print(P+'-'*50)
	print(C+'Close Files : exit')
	print(P+'-'*50)
	oo=0
	while True:
		oo+=1
		cmd=input(G+f'Enter The Target Info {oo} :{R} ')
		if cmd == "exit":
			break;
		a.add(cmd)
	x=set([])
	m=set([])
	c=set([])
	for i in a:
		if i not in x:
			x.add(i)
			for l in x:
				finall=l+i
				#print(finall)
				recv=open(file,'a')
				recv.write(finall+'\n')
			if l not in m:
				m.add(l+i)
				for p in m:
					finall=set([])
					finall.add(i+l+p)
					for w in finall:
						time.sleep(0.02)
						if w not in c:
							c.add(w)
							for ss in c:
								recv.write(ss+'\n')
							#print(ss)
	recv.close()
	size=open(file,'r')
	kk=0
	for i in size.readlines():
		kk+=1
	print(C+'-'*50)
	print(R+'Sive Password List >> '+file+' Size '+str(kk))
	print(C+'-'*50)
								
try:
	list()
except:
	sys.exit()	