# Set location of CDR files
# Example: cdr_path = "/opt/cdr_ftproot/"
cdr_path = "/opt/cdr_ftproot/"

# Set location where CDR files are archived to after processing
# Example: archive_path = "/opt/cdr_archive/"
archive_path = "/opt/cdr_archive/"

# Set checking for files already existing in ElasticSearch
# Warning: Experimental
# Check for duplicates and don't write to ES:
# es_file_check = True
# Don't check for duplicates and write duplicate files to ES:
# es_file_check = False
es_file_check = False

# Set ElasticSearch Host
# Example: es_host = "192.168.1.100"
es_host = "localhost"

# Set ElasticSearch Port
# Example: es_port = "9200"
es_port = "9200"

# Set ElasticSearch Index
# Default normally recommended.  Uses cdr-[date] and cmr-[date]
# Example: es_index = "cdr"
es_index = ""

# Date format when default index used.  Requires valid PHP date format.
# Example: "%Y.%m.%d" = 2015.11.01
#          "%m.%d.%Y" = 11.01.2015
#          "%m%d%Y"   = 11012015
es_index_format = "%Y.%m.%d"

# Set ElasticSearch Type
# Will use CDR filename if none specified
# Example: es_type = "parsed_cdr"
es_type = ""
