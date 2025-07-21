# import logging

# logger = logging.getLogger(__name__)

# #create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# #level and the format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning("This is a warning")
# logger.error("This is an error")

import logging
import time
from logging .handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# #roll over after 2 KB , and keep backup logs app.log.1, app.log.2 , etc.
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

handler = TimedRotatingFileHandler('timed_test.log', when='s', interval = 5, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, World!')
    time.sleep(5)