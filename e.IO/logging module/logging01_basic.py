# Logging - Example 1 | Basic Configuration

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
#import logging02_basic # UNCOMENT <1>

logging.basicConfig(filename = 'test.log', level=logging.INFO,
                    format = '[%(lineno)d]  %(asctime)s:%(levelname)s:%(name)s:%(message)s')
# datefmt ='%d-%m-%Y %H:%M:%S ',

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


    logging.info('Iteration # {}'.format(i + 1))
    logging.info('Add:      {} + {} = {}'.format(x[i], y[i], add))
    logging.info('subtract: {} + {} = {}'.format(x[i], y[i], subtract))
    logging.info('multiply: {} + {} = {}'.format(x[i], y[i], multiply))
    logging.info('division: {} + {} = {}'.format(x[i], y[i], division))
