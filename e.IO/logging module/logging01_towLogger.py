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

# LOGGER 1 - INFO ==============================================================
# Create logger
logger01 = logging.getLogger(__name__ + '.A')

# Set level
logger01.setLevel(logging.INFO)

# Logger Formating
formatter01 = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# File handler
file_handler01 = logging.FileHandler('test_info.log')
file_handler01.setFormatter(formatter01)

# Add Handler to logger
logger01.addHandler(file_handler01)

# LOGGER 2 - ERROR =============================================================
# Create logger
logger02 = logging.getLogger(__name__ + '.B')

# Set level
logger02.setLevel(logging.ERROR)

# Logger Formating
formatter02 = logging.Formatter('[%(lineno)d] %(asctime)s:%(levelname)s:%(name)s:%(message)s')

# File handler
file_handler02 = logging.FileHandler('test_error.log')
file_handler02.setFormatter(formatter02)

# Add Handler to logger
logger02.addHandler(file_handler02)


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
        logger02.error('Iteration # {}'.format(i))
#        logger02.error('Division by zero !!')    # UNCOMMENT <2>
#        logger02.exception('Division by zero !!') # UNCOMMENT <3>

    logger01.info('Iteration # {}'.format(i + 1))
    logger01.info('Add:      {} + {} = {}'.format(x[i], y[i], add))
    logger01.info('subtract: {} + {} = {}'.format(x[i], y[i], subtract))
    logger01.info('multiply: {} + {} = {}'.format(x[i], y[i], multiply))
    logger01.info('division: {} + {} = {}'.format(x[i], y[i], division))
