#!/usr/bin/env python
'''
we have a dat file of the  database which will tell
the location of ip and many more things about the ip.
Database file is of geolitecity database.
'''

import pygeoip      #this library help us to extract the data from the dat file about the ip

ip_tocoun_db='/home/shikhar/Documents/python-cdac/geoip-dat/GeoLiteCity.dat'    #this will give the destination path of the dat file
gi = pygeoip.GeoIP(ip_tocoun_db)        #getting the object 'gi' from GeoIP class

def printRecord(tgt):                       #function will print the information related to the ip with help of dat file
	rec = gi.record_by_addr(tgt)        #rec get the information in the form of dictionary
	city = rec['city']
	region = rec['region_code']
	country = rec['country_name']
        time_zone = rec['time_zone']
	lon = rec['longitude']
	lat = rec['latitude']
	print '[*] Target: ' + tgt + ' Geo-located. '
	print '[+] '+str(city)+','+str(region)+', '+str(country)
	print '[+] Latitude: '+str(lat)+ ', Longitude: '+ str(lon)
        print '[*] Timezone: ' +str(time_zone)

IP=raw_input('enter the host name: ')       #code satrts from here and this will ask for user input of the host IP
printRecord(IP)                             #calling the function
