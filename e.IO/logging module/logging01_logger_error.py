# Logging - Example 1 | Logger

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
https://docs.python.org/3/library/logging.html
https://docs.python.org/3/howto/logging.html
"""

import logging
import logging02_logger


# Create logger
logger = logging.getLogger(__name__)

# Set level
logger.setLevel(logging.DEBUG)

# Logger Formating
formatter = logging.Formatter(' %(asctime)s:%(levelname)s:%(name)s:%(message)s')

# File handler
file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.DEBUG) # UNCOMMENT <1>
file_handler.setFormatter(formatter)

#NOTE:
# Why are there two setLevel() methods? The level set in the logger determines
# which severity of messages it will pass to its handlers. The level set in each
# handler determines which messages that handler will send on.


# Sream handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.ERROR) # UNCOMMENT <1>

# Add Handler to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler) # UNCOMENT <4>


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 2, 2, 2, 2, 2, 2, 2, 2, 0]

for i in range(len(x)):
    add      = x[i] + y[i]
    subtract = x[i] + y[i]
    multiply = x[i] * y[i]
    try:
        division = x[i] / y[i]
    except ZeroDivisionError:
        division = 'division by zero !!!'
#        logger.error('Division by zero !!')    # UNCOMMENT <2>
        logger.exception('Division by zero !!') # UNCOMMENT <3>

    logger.debug('Iteration # {}'.format(i + 1))
    logger.debug('Add:      {} + {} = {}'.format(x[i], y[i], add))
    logger.debug('subtract: {} + {} = {}'.format(x[i], y[i], subtract))
    logger.debug('multiply: {} + {} = {}'.format(x[i], y[i], multiply))
    logger.debug('division: {} + {} = {}'.format(x[i], y[i], division))
