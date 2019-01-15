import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')
def createSession():
	try:
		driver = webdriver.Safari()
		driver.implicitly_wait(10)
		# WebDriverWait(driver , 10)
		print "[+] Page already"
	except:
		pass
	return driver

def auto_login(driver , userName , passWord):
	try:
		print "[+] Now to go"
		driver.get("http://1.1.1.1")
		time.sleep(7)
		print "[+] finding username field"
		user = driver.find_element_by_name("username")
		user.send_keys(userName)
		pwd = driver.find_element_by_name("password")
		pwd.clear()
		pwd.send_keys(passWord)
		submit = driver.find_element_by_id("confirm").click()
		print "[+] Finished on!!!!"
		time.sleep(10)
		driver.quit()
	except Exception as e:
		raise e

######################### Main Function #############################
trytoch = 0
os.chdir(os.path.dirname(__file__))
path = os.getcwd()
ope = open("user.txt" , "r")
keep = ope.read().split('\n')
while(1):
	cmd = 'networksetup -getairportnetwork en0 | awk -F \':\' \'{print $2}\''
	currentssid = os.popen(cmd).read()
	if(currentssid.find('.@ TRUEWIFI') == -1):
		print '[-] Now Current SSID is not .@ TRUEWIFI'
		os.system('networksetup -setairportnetwork en0 \'   .@ TRUEWIFI\'')
		print '[+] Change Network Airport to TRUEWIFI.'
	time.sleep(5)
	print "[+] Test Connection...."
	chNet = os.system("nc -z -G 1 www.google.com 443")
	if(chNet > 0):
		trytoch += 1
		print "[-] Check Fail count : " + str(trytoch) + "."
		if(trytoch >=3):
			print "[+] Internet disconnect try to Login .@TRUEWIFI"
			uName = keep[0]
			pWord = keep[1]
			auto_login(createSession() , uName , pWord)
			trytoch = 0
	else:
		print "[+] Now you connected to Internet..."
		time.sleep(5)
		os.system('clear')
		trytoch = 0
