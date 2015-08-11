# encoding: utf-8

import logging

logging.basicConfig(format='%(asctime)s [%(levelname)-5s] %(message)s', level=logging.INFO)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('requests').setLevel(logging.WARNING)

log = logging.getLogger()
