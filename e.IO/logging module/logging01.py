# Logging - Example 1 

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


    print('Iteration # {}'.format(i + 1))
    print('Add:      {} + {} = {}'.format(x[i], y[i], add))
    print('subtract: {} + {} = {}'.format(x[i], y[i], subtract))
    print('multiply: {} + {} = {}'.format(x[i], y[i], multiply))
    print('division: {} + {} = {}'.format(x[i], y[i], division))
