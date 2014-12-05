Cisco CDR to ES Parser
==========

Small Python Script to Parse Cisco CDR Records into ElasticSearch/Kibana

This script set has limited testing.  It worked but was not tested over a long period as it was decided we would keep using a
commercial product.  I wouldn't consider it complete but might make a nice starting point for someone...

Configure an FTP server such as VSFTP and point your CUCM server to FTP CDR records to it.  This script will demonize and 
process those CDR files upon arrival.  It will send the CDR information to your ElasticSearch server and move the CDR file from 
the FTP root directory to an archive directory which can be purged as you see fit.

Script requires the official ElasticSearch python module and python-daemon (tested with 1.6.1).
