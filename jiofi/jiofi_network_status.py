import requests

from bs4 import BeautifulSoup

res = requests.get('http://jiofi.local.html/cgi-bin/en-jio/mStatus.html').text

soup = BeautifulSoup(res,'html.parser')

RSRP = soup.find(id='pDashEngineerInform_rsrpValue').decode_contents()


if int(RSRP[:-3]) >= -100:
	print(RSRP, 'Good')
else:
	print(RSRP, 'Normal')
