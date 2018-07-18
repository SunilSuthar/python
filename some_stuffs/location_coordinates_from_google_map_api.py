import requests
URL = "http://maps.googleapis.com/maps/api/geocode/json"
PARAMS = {'address':'jodhpur'}
data = requests.get(url = URL, params = PARAMS).json()
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']
results="Latitude:%s\nLongitude:%s\nFormatted Address:%s" %(latitude, longitude,formatted_address)
print(results)
