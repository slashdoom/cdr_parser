###############################################################################
#
# Cisco CDR to ES Parser (cdr_parser)
#
# FILENAME:    mod_cdr_decode.py
# DESCRIPTION: Module that contains the parser's CUCM decoding information
#
# AUTHOR:      Patrick K. Ryon (slashdoom)
# COPYWRITE:   Copyright (c) 2016, Patrick Ryon (Slashdoom) All rights reserved.
# LICENSE:     3 clause BSD (see LICENSE file)
#
################################################################################

import time
import datetime
import mod_conf

def decode_RecordType(val):
  # Check val data type
  try:
    if type(val) == str or type(val) == int:
      val = int(val)
  except ValueError:
      return "decode_err"
  # Decode CDR Record Type
  if val == 1:
    return "CDR"
  elif val == 2:
    return "CMR"
  else:
    return "decode_err"

def decode_TermCauseCode(val):
  # Check val data type
  try:
    if type(val) == str or type(val) == int:
      val = int(val)
  except ValueError:
    return "decode_err"
  # Decode Termination Cause Code
  if val == 0:
    return "No error"
  elif val == 1:
    return "Unallocated (unassigned) number"
  elif val == 2:
    return "No route to specified transit network (national use)"
  elif val == 3:
    return "No route to destination"
  elif val == 4:
    return "Send special information tone"
  elif val == 5:
    return "Misdialed trunk prefix (national use)"
  elif val == 6:
    return "Channel unacceptable"
  elif val == 7:
    return "Call awarded and being delivered in an established channel"
  elif val == 8:
    return "Preemption"
  elif val == 9:
    return "Preemption-circuit reserved for reuse"
  elif val == 16:
    return "Normal call clearing"
  elif val == 17:
    return "User busy"
  elif val == 18:
    return "No user responding"
  elif val == 19:
    return "No answer from user (user alerted)"
  elif val == 20:
    return "Subscriber absent"
  elif val == 21:
    return "Call rejected"
  elif val == 22:
    return "Number changed"
  elif val == 26:
    return "Non-selected user clearing"
  elif val == 27:
    return "Destination out of order"
  elif val == 28:
    return "Invalid number format (address incomplete)"
  elif val == 29:
    return "Facility rejected"
  elif val == 30:
    return "Response to STATUS ENQUIRY"
  elif val == 31:
    return "Normal, unspecified"
  elif val == 34:
    return "No circuit/channel available"
  elif val == 38:
    return "Network out of order"
  elif val == 39:
    return "Permanent frame mode connection out of service"
  elif val == 40:
    return "Permanent frame mode connection operational"
  elif val == 41:
    return "Temporary failure"
  elif val == 42:
    return "Switching equipment congestion"
  elif val == 43:
    return "Access information discarded"
  elif val == 44:
    return "Requested circuit/channel not available"
  elif val == 46:
    return "Precedence call blocked"
  elif val == 47:
    return "Resource unavailable, unspecified"
  elif val == 49:
    return "Quality of Service not available"
  elif val == 50:
    return "Requested facility not subscribed"
  elif val == 53:
    return "Service operation violated"
  elif val == 54:
    return "Incoming calls barred"
  elif val == 55:
    return "Incoming calls barred within Closed User Group (CUG)"
  elif val == 57:
    return "Bearer capability not authorized"
  elif val == 58:
    return "Bearer capability not presently available"
  elif val == 62:
    return "Inconsistency in designated outgoing access information and subscriber class"
  elif val == 63:
    return "Service or option not available, unspecified"
  elif val == 65:
    return "Bearer capability not implemented"
  elif val == 66:
    return "Channel type not implemented"
  elif val == 69:
    return "Requested facility not implemented"
  elif val == 70:
    return "Only restricted digital information bearer capability is available (national use)"
  elif val == 79:
    return "Service or option not implemented, unspecified"
  elif val == 81:
    return "Invalid call reference value"
  elif val == 82:
    return "Identified channel does not exist"
  elif val == 83:
    return "A suspended call exists, but this call identity does not"
  elif val == 84:
    return "Call identity in use"
  elif val == 85:
    return "No call suspended"
  elif val == 86:
    return "Call having the requested call identity has been cleared"
  elif val == 87:
    return "User not member of CUG (Closed User Group)"
  elif val == 88:
    return "Incompatible destination" 
  elif val == 90:
    return "Destination number missing and DC not subscribed"
  elif val == 91:
    return "Invalid transit network selection (national use)"
  elif val == 95:
    return "Invalid message, unspecified"
  elif val == 96:
    return "Mandatory information element is missing"
  elif val == 97:
    return "Message type nonexistent or not implemented"
  elif val == 98:
    return "Message is not compatible with the call state, or the message type is nonexistent or not implemented"
  elif val == 99:
    return "An information element or parameter does not exist or is not implemented"
  elif val == 100:
    return "Invalid information element contents"
  elif val == 101:
    return "The message is not compatible with the call state"
  elif val == 102:
    return "Call terminated when timer expired; a recovery routine executed to recover from the error"
  elif val == 103:
    return "Parameter nonexistent or not implemented - passed on (national use)"
  elif val == 110:
    return "Message with unrecognized parameter discarded"
  elif val == 111:
    return "Protocol error, unspecified"
  elif val == 122:
    return "Precedence Level Exceeded"
  elif val == 123:
    return "Device not Preemptable"
  elif val == 125:
    return "Out of bandwidth (Cisco specific)"
  elif val == 126:
    return "Call split (Cisco specific)"
  elif val == 127:
    return "Interworking, unspecified"
  elif val == 129:
    return "Precedence out of bandwidth"
  elif val == 393216:
    return "Transfer/Conference"
  else:
    return "decode_err"

def decode_PrecedenceLevel(val):
  # Check val data type
  try:
    if type(val) == str or type(val) == int:
      val = int(val)
  except ValueError:
    return "decode_err"
  # Decode Precedence Level
  if val == 0:
    return "FLASH OVERRIDE/EXECUTIVE OVERRIDE"
  elif val == 1:
    return "FLASH"
  elif val == 2:
    return "IMMEDIATE"
  elif val == 3:
    return "PRIORITY"
  elif val == 4:
    return "ROUTINE"
  else:
    return "decode_err"

def decode_CodecType(val):
  # Check data type
  try:
    if type(val) == str or type(val) == int:
      val = int(val)
  except ValueError:
    return "decode_err"
  # Decode Codec Type
  if val == 0:
    return "N/A"
  elif val == 1:
    return "NonStandard"
  elif val == 2:
    return "G711Alaw 64k"
  elif val == 3:
    return "G711Alaw 56k"
  elif val == 4:
    return "G711mu-law 64k"
  elif val == 5:
    return "G711mu-law 56k"
  elif val == 6:
    return "G722 64k"
  elif val == 7:
    return "G722 56k"
  elif val == 8:
    return "G722 48k"
  elif val == 9:
    return "G7231"
  elif val == 10:
    return "G728"
  elif val == 11:
    return "G729"
  elif val == 12:
    return "G729AnnexA"
  elif val == 13:
    return "Is11172AudioCap"
  elif val == 14:
    return "Is13818AudioCap"
  elif val == 15:
    return "G.729AnnexB"
  elif val == 16:
    return "G.729 Annex AwAnnexB"
  elif val == 18:
    return "GSM Full Rate"
  elif val == 19:
    return "GSM Half Rate"
  elif val == 20:
    return "GSM Enhanced Full Rate"
  elif val == 25:
    return "Wideband 256K"
  elif val == 32:
    return "Data 64k"
  elif val == 33:
    return "Data 56k"
  elif val == 40:
    return "G7221 32K"
  elif val == 41:
    return "G7221 24K"
  elif val == 42:
    return "AAC"
  elif val == 80:
    return "GSM"
  elif val == 81:
    return "ActiveVoice"
  elif val == 82:
    return "G726_32K"
  elif val == 83:
    return "G726_24K"
  elif val == 84:
    return "G726_16K"
  elif val == 86:
    return "iLBC"
  elif val == 100:
    return "H261"
  elif val == 101:
    return "H263"
  elif val == 102:
    return "Vieo"
  elif val == 103:
    return "H264"
  elif val == 106:
    return "H224"
  else:
    return "decode_err"

def decode_VideoRes(val):
  # Check val data type
  try:
    if type(val) == str or type(val) == int:
      val = int(val)
  except ValueError:
    return "decode_err"
  # Decode CDR Video Resolution
  if val == 0:
    return "Media not established"
  elif val == 1:
    return "SQCIF"
  elif val == 2:
    return "QCIF"
  elif val == 3:
    return "CIF"
  elif val == 4:
    return "CIF4"
  elif val == 5:
    return "CIF16"
  else:
    return "decode_err"

def decode_RSVPStat(val):
  # Check val data type
  try:
    if type(val) == str or type(val) == int:
      val = int(val)
  except ValueError:
    return "decode_err"
  # Decode CDR RSVP Audio/Video Stat
  if val == 0:
    return "No reservation"
  elif val == 1:
    return "RSVP Reservation Failure condition at call setup or feature invocation"
  elif val == 2:
    return "RSVP Reservation Success condition at call setup or feature invocation"
  elif val == 3:
    return "RSVP Reservation No Response (RSVP Agent) condition at call setup or feature invocation"
  elif val == 4:
    return "RSVP Mid Call Failure Preempted condition (preempted after call setup)"
  elif val == 5:
    return "RSVP Mid Call Failure Lost Bandwidth condition (includes all mid-call failures except MLPP preemption)"
  else:
    return "decode_err"

def decode_DTMFMethod(val):
  # Check val data type
  try:
    if type(val) == str or type(val) == int:
      val = int(val)
  except ValueError:
    return "decode_err"
  # Decode CDR DTMF Method
  if val == 0:
    return "No DTMF"
  elif val == 1:
    return "OOB"
  elif val == 2:
    return "RFC2833"
  elif val == 3:
    return "OOB and RFC2833"
  elif val == 4:
    return "Unknown"
  else:
    return "decode_err"

def decode_SecuredStatus(val):
  # Check val data type
  try:
    if type(val) == str or type(val) == int:
      val = int(val)
  except ValueError:
    return "decode_err"
  # Decode CDR Secured Status
    if val == 0:
      return "Non-secured"
    elif val == 1:
      return "Authenticated"
    elif val == 2:
      return "Secured"
    else:
      return "decode_err"

def decode_Time(val):
  """ convert Unix epoch time to UTC timestamp """
  if val == "0":
    return val;
  else:
    # Convert from CUCM local time to UTC and format
    time_stamp = datetime.datetime.utcfromtimestamp(float(val))
    return time_stamp

###############################################################################
### decode_IP (int_to_ip) by Jerold Swan                                    ###
### https://gist.github.com/jayswan/1796357                                 ###
###############################################################################
def decode_IP(val):
  ### convert a 32-bit signed integer to an IP address ###
  # do preventative type checking because I didn't want to check inputs
  try:
    if type(val) == str or type(val) == int:
      val = long(val)
  except ValueError:
    return "decode_err"

  # CUCM occasionally creates CDRs with an IP of '0'. Bug or feature? Beats me.
  if val == 0:
    return "N/A"

  # hex conversion for 32-bit signed int; 
  # the slice at the end removes the '0x' and 'L' in the result
  h = hex(val & 0xffffffff)[2:-1] 

  if len(h) == 7: #pad initial zero if required
    h = '0' + h
 
  hex_ip = [h[6:8],h[4:6],h[2:4],h[:2]] # reverse the octets

  #put them back together in IPv4 format
  ip = '.'.join([str(int(n,16)) for n in hex_ip]) 

  return ip

def decode_duration(val):
  # Check val data type
  try:
    if type(val) == str or type(val) == int:
      val = int(val)
  except ValueError:
    return "decode_err"
  # Convert duration seconds to HH:MM:SS
  if val < 86400:
    return time.strftime('%H:%M:%S', time.gmtime(val))
  else:
    return val
