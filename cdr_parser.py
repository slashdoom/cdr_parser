###############################################################################
#
# Cisco CDR to ES Parser (cdr_parser)
#
# FILENAME:    cdr_parser.py
# DESCRIPTION: Main app file to control parser as daemon
#
# AUTHOR:      Patrick K. Ryon (slashdoom)
# COPYWRITE:   Copyright (c) 2016, Patrick Ryon (Slashdoom) All rights reserved.
# LICENSE:     3 clause BSD (see LICENSE file)
#
################################################################################

import logging, time
from daemon import runner

import mod_conf
from mod_cdr_main import (
  initial_program_setup,
  do_main_program,
  program_cleanup,
  reload_program_config,
  )

class App():
    
  def __init__(self):
    self.stdin_path      = '/dev/null'
    self.stdout_path     = '/dev/tty'
    self.stderr_path     = '/dev/tty'
    self.pidfile_path    = '{0}cdr_parser.pid'.format(mod_conf.pid_path)
    self.pidfile_timeout = 5

  def run(self):
    logger.info("cdr_parser started")

    while True:
      # Call Main Program
      do_main_program(logger)
      
app = App()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Logger Console Handler
ch = logging.StreamHandler() # StreamHandler logs to console
ch.propagate = False
ch.setLevel(logging.DEBUG)
ch_format = logging.Formatter('%(asctime)s - %(levelname)-8s - %(message)s')
ch.setFormatter(ch_format)
logger.addHandler(ch)

# Logger File Handler
fh = logging.FileHandler('{0}{1}.log'.format(mod_conf.log_path,__name__))
fh.propagate = False
fh.setLevel(logging.INFO)
fh_format = logging.Formatter('%(asctime)s - %(levelname)-8s - %(message)s')
fh.setFormatter(fh_format)
logger.addHandler(fh)

daemon_runner = runner.DaemonRunner(app)
# Don't close logging files during daemonization
daemon_runner.daemon_context.files_preserve=[fh.stream]
daemon_runner.do_action()

logger.info("cdr_parser stopped")
