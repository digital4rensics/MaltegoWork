#!/usr/bin/python

# malwr_hash2ip.py
# Author: Keith Gilbert - www.digital4rensics.com - @digital4rensics
# Version: 1.0
# Date: November, 2012

# This script will retrieve ip addresses from reports on malwr.com if the
# file has been uploaded and the report is present.

import sys
import mechanize
from MaltegoTransform import *
from BeautifulSoup import BeautifulSoup

def getreport(hash):
	url = 'http://malwr.com/analysis/' + hash + '/'
	browser = mechanize.Browser()
	
	try:
		report = browser.open(url)
		html = report.read()
		page = BeautifulSoup(html)
		return page
	except:
		sys.exit("Report does not exist.")
			
def parsereport(page):
	xform = MaltegoTransform()
	
	table = page.find("div", {"id" : "network_hosts"}).findNext('table')
	elements = table.findAll('td', {"class" : "row"})
	for element in elements:
		text = element.find(text=True)
		entity = xform.addEntity("maltego.IPv4Address", text)
		
	xform.returnOutput()

def main():
	hash = sys.argv[1]
	
	source = getreport(hash)
	parsereport(source)

if __name__ == '__main__':
	main()