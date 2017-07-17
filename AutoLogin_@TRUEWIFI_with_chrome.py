import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time


# def createSession():
# 	try:
# 		# binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')
# 		# driver = webdriver.Firefox(firefox_binary=binary)
# 		# profile = webdriver.FirefoxProfile(os.path.expanduser("~/Library/Application Support/Firefox/Profiles/Selenium/"))
# 		chromedriver = "chromedriver"
# 		driver = webdriver.Chrome(chromedriver)

# 		driver.implicitly_wait(10)
# 		# WebDriverWait(driver , 10)
# 		print "Page already"
# 		return driver
# 	except Exception as e:
		

def auto_login(chromedriver , userName , passWord):
	try:
		# chromedriver = r"/Users/l31ank5pace/Desktop/PyScripts/chromedriver"
		driver = webdriver.Chrome(chromedriver)

		driver.implicitly_wait(5)
		# time.sleep(1)

		print "Now to go..."
		driver.get("https://portal.trueinternet.co.th/wifiauthen/web/wifi-login.php")
		# time.sleep(1)
		print "finding usernameFill..."
		user = driver.find_element_by_name("username")
		user.send_keys(userName)
		pwd = driver.find_element_by_name("password")
		pwd.clear()
		pwd.send_keys(passWord)
		submit = driver.find_element_by_id("confirm").click()
		print "Finished on!!!!"
		# time.sleep(2)
		driver.quit()
	except Exception as e:
		raise e

######################### Main Function #############################

os.chdir(os.path.dirname(__file__))
path = os.getcwd()
ope = open("user.txt" , "r")
keep = ope.read().split('\n')
while(1):
	print "Test Connection...."
	chNet = os.system("ping www.google.com")
	if(chNet > 0):
		print "Internet disconnect try to Login .@TRUEWIFI"
		############## to Different for anyone #############################
		uName = keep[0]
		pWord = keep[1]
		chromedriver = path + "/chromedriver.exe"
		####################################################################
		auto_login(chromedriver , uName , pWord)
	else:
		print "Now you connected to Internet..."
		pass
	time.sleep(7)
