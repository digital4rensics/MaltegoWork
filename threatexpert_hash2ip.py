#!/usr/bin/python

# threatexpert_hash2ip.py
# Author: Keith Gilbert - www.digital4rensics.com - @digital4rensics
# Version: 1.0
# Date: November, 2012

# This script will retrieve ip addresses from reports on threatexpert.com if the
# file has been uploaded and the report is present.

import sys
import mechanize
import re
from MaltegoTransform import *
from BeautifulSoup import BeautifulSoup

def getreport(hash):
	url = 'http://threatexpert.com/report.aspx?md5=' + hash
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
	
	try:
		for element in page.findAll(text=re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")):
			entity = xform.addEntity("maltego.IPv4Address", element)
	except:
		sys.exit("Report contains no IPs.")
			
	xform.returnOutput()

def main():
	hash = sys.argv[1]
	
	source = getreport(hash)
	parsereport(source)

if __name__ == '__main__':
	main()