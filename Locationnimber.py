import phonenumbers

import folium
import results as results

from myNumber import number

from phonenumbers import geocoder

Key = '.........................'

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

## get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

requests = geocoder.geocode(query)
##print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat,lng)

myNumber folium,Map(location=[lat, lng], zoom_start_=_9)


folium.Marker([lat, lng],popup=yourLocation).add_to((myMap))

## save map in html file

myMap.save("mylocation.html")
