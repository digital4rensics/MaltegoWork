#!/usr/bin/python

# Domain2IPs_pDNS.py
# Author: Keith Gilbert - www.digital4rensics.com - @digital4rensics
# Version: 1.1
# Date: November, 2012

# This script will retrieve IPs associated with a given domain
# from the ISC pDNS service. IPs will be added as entities to the graph.
# The script requires copying the ISC provided script from https://www.farsightsecurity.com/Services/DNSDB/
# and specifying your api key in the isc-dnsdb-query.conf file.

from MaltegoTransform import *
import sys
import subprocess

badDomain = sys.argv[1] + "/A"
xform = MaltegoTransform()

out = subprocess.Popen(["/bin/bash", "isc-dnsdb-query.sh", "rrset", badDomain], shell=False, stdout=subprocess.PIPE)
results, err = out.communicate()

entries = results.splitlines()
for line in entries:
	if line.startswith(';'):
		pass
	else:
		if len(line) == 0:
			pass
		else:
			IP = line.split()[3]
			if IP == "127.0.0.1" or IP == "0.0.0.0":
				pass
			else:
				entity = xform.addEntity("maltego.IPv4Address", IP)
	
xform.returnOutput()
