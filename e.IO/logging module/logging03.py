# Logging - Example 3

"""
Level    Description
--------------------------------------------------------------------------------
DEBUG    Detailed information, typically of interest only when diagnosing
         problems.

INFO     Confirmation that things are working as expected.

WARNING  An indication that something unexpected happened, or indicative of
         some problem in the near future (e.g. ‘disk space low’).
         The software is still working as expected. (DEFAULT LEVELLOGGING.debug)

ERROR    Due to a more serious problem, the software has not been able to
         perform some function.

CRITICAL A serious error, indicating that the program itself may be unable
         to continue running.

Python documentation for logging facility
https://docs.python.org/3/howto/logging.html

https://docs.python.org/3/library/logging.html
"""

import logging
import datetime
import time


# Create logger
logger = logging.getLogger(__name__)

# Set logger level
logger.setLevel(logging.INFO)

# Create File and Console handler and set level (if required)
file_handler    = logging.FileHandler('test.log')
console_handler = logging.StreamHandler()

# Create formatter
formatter_f = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
formatter_c = logging.Formatter('%(message)s')

# Add formatter to file_handler and console_handler
file_handler.setFormatter(formatter_f)
console_handler.setFormatter(formatter_c)


# Add File and Console handler to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

time_start = datetime.datetime.now()
time_stop = time_start + datetime.timedelta(seconds = 5, minutes = 0)

def f():
    cont = 0
    while True:
        cont += 1
        time.sleep(0.5)
        logger.info('A Sample Log Statement Number {}'.format(cont))

        tnow = datetime.datetime.now()
        if tnow > time_stop:
            logger.info('** The time limit has been reached')
            break

# Run function f()
print(__name__)
f()
