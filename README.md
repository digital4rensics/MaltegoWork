MaltegoWork
===========

This repo holds work I've done with Maltego (by Paterva). Transforms will require the Python library (MaltegoTransform) available here: http://paterva.com/web6/documentation/developer-local.php


Both Passive DNS scripts require a copy of the ISC provided script (available at: ftp://ftp.isc.org/isc/nmsg/misc/isc-dnsdb-query) and specifying your api key in the isc-dnsdb-query.conf file.
  * Domain2IPs_pDNS.py - This transform takes a domain and uses the ISC PassiveDNS service to identify known                 associated IP addresses.
  * IP2Domains_pDNS.py - This transform takes an IP address and uses the ISC PassiveDNS service to identify known associated domains.

The Following scripts require BeautifulSoup 3 and Mechanize Python libraries.
  * malwr_hash2ip.py - This transform takes an MD5 hash and searches Malwr.com for a report. If one is found, it returns IP addresses from the report.
  * threatexpert_hash2ip.py - This transform takes an MD5 hash and searches ThreatExpert.com for a report. If one is found, it returns IP addresses from the report.
  * threatexpert_hash2mutex.py - Takes an MD5 hash and searches ThreatExpert.com for a report. If one is found, it returns all mutexes in the report.

All feedback, bug reports, enhancements, etc. are greatly appreciated.



Maltego is a registered trademark of Paterva (Pty) Ltd.