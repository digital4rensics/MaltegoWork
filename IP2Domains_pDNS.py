#!/usr/bin/python

# IP2Domains_pDNS.py
# Author: Keith Gilbert - www.digital4rensics.com - @digital4rensics
# Version: 1.1
# Date: November, 2012

# This script will retrieve domains associated with a given IP
# from the ISC pDNS service. Domains will be added as entities to the graph.
# The script requires copying the ISC provided script from https://www.farsightsecurity.com/Services/DNSDB/
# and specifying your api key in the isc-dnsdb-query.conf file.

from MaltegoTransform import *
import sys
import subprocess

badIP = sys.argv[1]
xform = MaltegoTransform()

out = subprocess.Popen(["/bin/bash", "isc-dnsdb-query.sh", "rdata", "ip", badIP], shell=False, stdout=subprocess.PIPE)
results, err = out.communicate()

entries = results.splitlines()
for line in entries:
	domain = line.split()[0].rstrip('.;')
	if len(domain) == 0:
		pass
	else:
		entity = xform.addEntity("maltego.Domain", domain)
	
xform.returnOutput()
