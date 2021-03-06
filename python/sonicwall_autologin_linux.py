#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import sys
import time

def main() :
	display = Display(visible=0, size=(800, 600))
	display.start()
	authurl = "https://firewall.amritanet.edu:8443/auth1.html"
	delay = 3
	print "\n\n[*]  Opening a New Session.."
	driver = webdriver.Firefox()
	driver.get(authurl)

	assert "Sonic" in driver.title

	print "\n\n[*] Enumerating Login Page.."
	user = driver.find_element_by_name("userName")
	passwd = driver.find_element_by_name("pwd")

	print "\n\n[*] Sending Credentials .. "
	user.send_keys("<user_name_here>")
	passwd.send_keys("<password_here>")
	passwd.send_keys(Keys.RETURN)

	driver.get("http://www.msftncsi.com/ncsi.txt")

	print "\n\n[*] Login Done!"
	driver.quit()
	display.stop()

main()
