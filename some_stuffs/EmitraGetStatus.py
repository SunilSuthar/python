import sys
import requests
import json

url = "http://reportsemitraapp.rajasthan.gov.in/emitraReportsRepository/mgetApplicationsStatusMobile"
receiptNumber = int(sys.argv[1])

data = json.loads(requests.post(url,{"receiptNumber":receiptNumber}).text)[0]
for x in data:
	print(x,':',data[x])
