#Author: Sunil Suthar

import requests
import json
from bs4 import BeautifulSoup


url_home = "http://jiofi.local.html"
url_status = "http://jiofi.local.html/cgi-bin/en-jio/mStatus.html";
url_login = "http://jiofi.local.html/cgi-bin/en-jio/login_check.html";
url_login_check = "http://jiofi.local.html/cgi-bin/en-jio/login_Query.html";
url_devices_connected = "http://jiofi.local.html/cgi-bin/en-jio/mConnected_Devices.html";
url_wificonfig = "http://jiofi.local.html/cgi-bin/en-jio/mWiFi_Config.html";
url_reboot = ["http://jiofi.local.html/cgi-bin/en-jio/mSoftUpdate_Reboot.html","http://jiofi.local.html/cgi-bin/en-jio/reboot.html"]
url_block_mac=["http://jiofi.local.html/cgi-bin/en-jio/mWMAC.html","http://jiofi.local.html/cgi-bin/en-jio/mWMAC_Apply.html"]

class JioFi:

	def __init__(self,username,password):
		self.session = requests.Session()
		params={
			"act": username,
			"pwd": password,
			"RequestVerifyToken": self.fetch_token(url_home)
		}
		self.session.post(url_login,params).text

	def fetch_token(self,url):
		soup = BeautifulSoup(self.session.get(url).text, 'html.parser')
		token = soup.find(id='RequestVerifyToken').get('value')
		return token

	def is_loggedin(self):
		login = json.loads(self.session.get(url_login_check).text)['login']
		if login == '1':
			return True
		else:
			return False

	def get_ssid(self):
		soup = BeautifulSoup(self.session.get(url_status).text, 'html.parser')
		ssid = soup.find(id='lWirelessNwValue').text
		return ssid
	def get_battery_status(self):
		soup = BeautifulSoup(self.session.get(url_status).text, 'html.parser')
		battery_status = soup.find(id='lDashBatteryQuantity').text
		return battery_status
	
	def connected_devices(self):
		devices_json="["+self.session.get(url_devices_connected).text.splitlines()[9][24:-2]+"]"
		devices=json.loads(devices_json)
		return devices

	def reboot(self):
		token=self.fetch_token(url_reboot[0])
		response = self.session.get(url_reboot[1]+"?RequestVerifyToken="+token).text
		result = json.loads(response)
		return result['result']





try:
	my_jiofi= JioFi("sunil","9950169194")
except Exception as e:
	input("Can't connect to jiofi")
	exit()


if my_jiofi.is_loggedin():
	print("SSID:   ",my_jiofi.get_ssid())
	print("Battery:",my_jiofi.get_battery_status())
	devices=my_jiofi.connected_devices()
	
	print("----------------------------connected devices----------------------------")
	for device in devices:
		print(device['IP_address']," >> ",device['MAC'],"[",device['Host_name'],"]")

	print("\n")
	print("Enter 'r' to reboot JioFi")
	print("Or press any other key to exit")

	console_input=input(">>")
	if console_input == 'r':
		my_jiofi.reboot()
		print("Rebooting...")
else:
	input("You are not logged in!!!")
