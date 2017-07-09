#!/usr/bin/env python
'''
through this script we can extract source ip
and destination ip from the pcap file of the
captured traffic.
'''

import dpkt             #this will help us to extract the source and destination ip from the pcap file
import socket           #this will help to check the socket through which the packet go from one device to other device
PACP_FILE='/home/shikhar/Documents/python-cdac/Lecture4-1(assignments_for_students)/Assignment4/firstTrafficCapture.pcap'   #path of pcap file

def printPcap(pcap):                                        #function will extract the source ip and destination ip
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			print 'source: '+str(src)+'  destination: '+str(dst)
		except:
			pass
def main():                                 #it will open the pcap file in read mode
	f=open(PACP_FILE,'r')
	pcap = dpkt.pcap.Reader(f)
	printPcap(pcap)
        f.close()
if __name__ == '__main__':      #code starts ffrom here
	main()

