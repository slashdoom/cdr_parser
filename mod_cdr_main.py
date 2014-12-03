import csv, logging, os, shutil, time
import mod_conf, mod_cdr_decode

from datetime import datetime
from elasticsearch import Elasticsearch

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#Logger Console Handler
ch = logging.StreamHandler() #StreamHandler logs to console
ch.setLevel(logging.DEBUG)
ch_format = logging.Formatter('%(asctime)s - %(message)s')
ch.setFormatter(ch_format)
logger.addHandler(ch)

#Logger File Handler
fh = logging.FileHandler('/var/log/cdr_parser/{0}.log'.format(__name__))
fh.setLevel(logging.INFO)
fh_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s - %(message)s')
fh.setFormatter(fh_format)
logger.addHandler(fh)

def initial_program_setup():
  print "initial_program_setup"

def do_main_program():

  # by default connect to localhost:9200
  es = Elasticsearch()

  for file in os.listdir(mod_conf.cdr_path):
    # Get pathes from config file
    src_file = os.path.join(mod_conf.cdr_path, file)
    dest_file = os.path.join(mod_conf.archive_path,file)

    logger.debug("src_file = %s" % src_file)
    logger.debug("dest_file = %s" % dest_file)

    # Check for configured type, if none use filename
    if mod_conf.es_type == "":
      es_type = file
    else:
      es_type = mod_conf.es_type

    logger.debug("es_type = %s" % es_type)

    try:
      shutil.move(src_file, mod_conf.archive_path)
    except:
      logger.warning("Error moving file to archive.")
    
    time.sleep(.1)

    if os.access(dest_file, os.W_OK):
      # Open CDR Log File
      csv_file = open(dest_file, 'rb')
      csv_read = csv.reader(csv_file, delimiter=',', quotechar='"')

      # Read CDR header row
      csv_keys = next(csv_read)

      # Skip CDR types row
      csv_types = next(csv_read)      

      # Process actual CDR rows
      for csv_line in csv_read:
        # Combine headers with data
        csv_zip = zip(csv_keys, csv_line)

        # Check for empty lines
        if csv_zip:
          
          es_body = {}

          # Call Sequence Variables
          origNum = ""
          finNum = ""
          
          for csv_data in csv_zip:
            # Decode cdrRecordType
            if csv_data[0] == "cdrRecordType":
              es_body[csv_data[0]] = mod_cdr_decode.decode_RecordType(val=csv_data[1])
              # Check for configured type, if none use cdr/cmr-YYYY.MM.DD
              if mod_conf.es_index == "":
                if csv_data[1] == "1":
                  es_index = "cdr-%s" % datetime.utcnow().strftime("%Y.%m.%d")
                elif csv_data[1] == "2":
                  es_index = "cmr-%s" % datetime.utcnow().strftime("%Y.%m.%d")
                else:
                  es_index = "index_err"
              else:
                 es_index = mod_conf.es_index
            # Decode dateTimeStamp
            elif csv_data[0] == "dateTimeStamp":
              es_body[csv_data[0]] = mod_cdr_decode.decode_Time(val=csv_data[1])
              # Build @timestamp
              es_body['@timestamp'] = mod_cdr_decode.decode_Time(val=csv_data[1])
            # Decode dateTimeOrigination
            elif csv_data[0] == "dateTimeOrigination":
              es_body[csv_data[0]] = mod_cdr_decode.decode_Time(val=csv_data[1])
              # Build @timestamp
              es_body['@timestamp'] = mod_cdr_decode.decode_Time(val=csv_data[1])
            # Decode origIpAddr
            elif csv_data[0] == "origIpAddr":
              es_body[csv_data[0]] = mod_cdr_decode.decode_IP(val=csv_data[1])
            # Decode origCause_location
            elif csv_data[0] == "origCause_location":
              es_body[csv_data[0]] = mod_cdr_decode.decode_TermCauseCode(val=csv_data[1])
            # Decode origCause_value
            elif csv_data[0] == "origCause_value":
              es_body[csv_data[0]] = mod_cdr_decode.decode_TermCauseCode(val=csv_data[1])
            # Decode origPrecedenceLevel
            elif csv_data[0] == "origPrecedenceLevel":
              es_body[csv_data[0]] = mod_cdr_decode.decode_PrecedenceLevel(val=csv_data[1])
            # Decode origMediaTransportAddress_IP
            elif csv_data[0] == "origMediaTransportAddress_IP":
              es_body[csv_data[0]] = mod_cdr_decode.decode_IP(val=csv_data[1])
            # Decode origMediaCap_payloadCapability
            elif csv_data[0] == "origMediaCap_payloadCapability":
              es_body[csv_data[0]] = mod_cdr_decode.decode_CodecType(val=csv_data[1])
            # Decode origVideoCap_Codec
            elif csv_data[0] == "origVideoCap_Codec":
              es_body[csv_data[0]] = mod_cdr_decode.decode_CodecType(val=csv_data[1])
            # Decode origVideoCap_Resolution
            elif csv_data[0] == "origVideoCap_Resolution":
              es_body[csv_data[0]] = mod_cdr_decode.decode_VideoRes(val=csv_data[1])
            # Decode origRSVPAudioStat
            elif csv_data[0] == "origRSVPAudioStat":
              es_body[csv_data[0]] = mod_cdr_decode.decode_RSVPStat(val=csv_data[1])
            # Decode origRSVPVideoStat
            elif csv_data[0] == "origRSVPVideoStat":
              es_body[csv_data[0]] = mod_cdr_decode.decode_RSVPStat(val=csv_data[1])
            # Decode destIpAddr
            elif csv_data[0] == "destIpAddr":
              es_body[csv_data[0]] = mod_cdr_decode.decode_IP(val=csv_data[1])
            # Decode destCause_location
            elif csv_data[0] == "destCause_location":
              es_body[csv_data[0]] = mod_cdr_decode.decode_TermCauseCode(val=csv_data[1])
            # Decode destCause_value
            elif csv_data[0] == "destCause_value":
              es_body[csv_data[0]] = mod_cdr_decode.decode_TermCauseCode(val=csv_data[1])
            # Decode destPrecedenceLevel
            elif csv_data[0] == "destCause_value":
              es_body[csv_data[0]] = mod_cdr_decode.decode_PrecedenceLevel(val=csv_data[1])
            # Decode destMediaTransportAddress_IP
            elif csv_data[0] == "destMediaTransportAddress_IP":
              es_body[csv_data[0]] = mod_cdr_decode.decode_IP(val=csv_data[1])
            # Decode destMediaCap_payloadCapability
            elif csv_data[0] == "destMediaCap_payloadCapability":
              es_body[csv_data[0]] = mod_cdr_decode.decode_CodecType(val=csv_data[1])
            # Decode destVideoCap_Codec
            elif csv_data[0] == "destVideoCap_Codec":
              es_body[csv_data[0]] = mod_cdr_decode.decode_CodecType(val=csv_data[1])         
            # Decode destVideoCap_Resolution
            elif csv_data[0] == "destVideoCap_Resolution":
              es_body[csv_data[0]] = mod_cdr_decode.decode_VideoRes(val=csv_data[1])
            # Decode destVideoTransportAddressdest_IP
            elif csv_data[0] == "destVideoTransportAddress_IP":
              es_body[csv_data[0]] = mod_cdr_decode.decode_IP(val=csv_data[1])
            # Decode destRSVPAudioStat
            elif csv_data[0] == "destRSVPAudioStat":
              es_body[csv_data[0]] = mod_cdr_decode.decode_RSVPStat(val=csv_data[1])
            # Decode destRSVPVideoStat
            elif csv_data[0] == "destRSVPVideoStat":
              es_body[csv_data[0]] = mod_cdr_decode.decode_RSVPStat(val=csv_data[1])
            # Decode dateTimeConnect
            elif csv_data[0] == "dateTimeConnect":
              es_body[csv_data[0]] = mod_cdr_decode.decode_Time(val=csv_data[1])
            # Decode dateTimeDisconnect
            elif csv_data[0] == "dateTimeDisconnect":
              es_body[csv_data[0]] = mod_cdr_decode.decode_Time(val=csv_data[1])
            # Decode origDTMFMethod
            elif csv_data[0] == "origDTMFMethod":
              es_body[csv_data[0]] = mod_cdr_decode.decode_DTMFMethod(val=csv_data[1])
            # Decode destDTMFMethod
            elif csv_data[0] == "destDTMFMethod":
              es_body[csv_data[0]] = mod_cdr_decode.decode_DTMFMethod(val=csv_data[1])
            # Decode callSecuredStatus
            elif csv_data[0] == "callSecuredStatus":
              es_body[csv_data[0]] = mod_cdr_decode.decode_SecuredStatus(val=csv_data[1])
            # Link origLegCallIdentifier to callIdentifier
            elif csv_data[0] == "origLegCallIdentifier":
              es_body[csv_data[0]] = csv_data[1]
              es_body["callIdentifier"] = csv_data[1]
            # Decode duration
            elif csv_data[0] == "duration":
              es_body[csv_data[0]] = mod_cdr_decode.decode_duration(val=csv_data[1])
            # Save originalCalledPartyNumber for call sequence summary
            elif csv_data[0] == "originalCalledPartyNumber":
              origNum = csv_data[1]
              es_body[csv_data[0]] = csv_data[1]
            # Save finalCalledPartyNumber for call sequence summary
            elif csv_data[0] == "finalCalledPartyNumber":
              finNum = csv_data[1]
              es_body[csv_data[0]] = csv_data[1]
            # Write non-decoded values as is
            else:
              es_body[csv_data[0]] = csv_data[1]

          # Build call sequence summary if data is present
          if not origNum == "":
            if origNum == finNum:
              es_body["Call Sequence"] = "Call to: " + origNum
            else:
              es_body["Call Sequence"] = "Call to: " + origNum + " Forwarded to: " + finNum

          # Send CDR to ElasticSearch
          logger.debug(es.index(index=es_index,doc_type=es_type,body=es_body))

  time.sleep(.1)
  
def program_cleanup():
  print "program_cleanup - not implemented"
        
def reload_program_config():
  print "reload_program_config - not implemented"
