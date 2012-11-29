#!/usr/bin/python

# threatexpert_hash2mutex.py
# Author: Keith Gilbert - www.digital4rensics.com - @digital4rensics
# Version: 1.0
# Date: November, 2012

# This script will retrieve mutexes from reports on threatexpert.com if the
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
		single = page.find(text='To mark the presence in the system, the following Mutex object was created:').findNext('ul').li.text
		multiple = page.find(text='To mark the presence in the system, the following Mutex objects were created:').findNext('ul')
				
		if single:
			entity = xform.addEntity("maltego.IPv4Address", single)
			if multiple:
				for mutex in multiple.findAll('li'):
					entity = xform.addEntity("maltego.Phrase", mutex.text)
		elif multiple:
			for mutex in multiple.findAll('li'):
					entity = xform.addEntity("maltego.Phrase", mutex.text)
		else:
			sys.exit("No Mutexes Reported")
	
	except:
		sys.exit("Error finding Mutexes.")
			
	xform.returnOutput()

def main():
	hash = sys.argv[1]
	
	source = getreport(hash)
	parsereport(source)

if __name__ == '__main__':
	main()