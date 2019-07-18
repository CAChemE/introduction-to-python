# Logging - Example 1 | Logger

import logging
import winsound
import time
import datetime
import numpy as np
from multiprocessing import Process, current_process


# Create logger
logger = logging.getLogger(__name__)

# Set level
logger.setLevel(logging.INFO)

# Logger Formating
formatter = logging.Formatter(' %(asctime)s:%(levelname)s:%(name)s:%(message)s')

# File handler
file_handler = logging.FileHandler('numbers.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# Sream handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.ERROR)

#NOTE:
# Why are there two setLevel() methods? The level set in the logger determines
# which severity of messages it will pass to its handlers. The level set in each
# handler determines which messages that handler will send on.

# Add Handler to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# ALARM FUNCTION ---------------------------------------------------------------
def alarm(timeLimit = 5):
    time_start = datetime.datetime.now()
    time_stop = time_start + datetime.timedelta(seconds = timeLimit, minutes = 0)
    while True:
        winsound.PlaySound('mario-bros tuberia.wav', winsound.SND_ASYNC)
        time.sleep(1)

        tnow = datetime.datetime.now()
        if tnow > time_stop:
#            print('** Alarm time limit has been reached')
            break
#-------------------------------------------------------------------------------




# BASIC OPERATION FUNCTION -----------------------------------------------------
def basic_operations(x, y):

    add      = x + y
    subtract = x - y
    multiply = x * y
    try:
        division = x / y
    except ZeroDivisionError:
        division = None
        logger.exception('Division by zero !!')
    return add, subtract, multiply, division
#-------------------------------------------------------------------------------



def my_process():
    iter = 0
    process = []
    while True:
        time.sleep(0.4)
        x = np.random.randint(10)
        y = np.random.randint(10)
        print(f'{x} [.] {y}')


        add, subtract, multiply, division = basic_operations(x,y)

        if division is None:
            process = Process(target = alarm, args = (5,))
            division = 'division by zero !!!'
            process.start()




        logger.info('Iteration # {}'.format(iter + 1))
        logger.info('Add:      {} + {} = {}'.format(x, y, add))
        logger.info('subtract: {} - {} = {}'.format(x, y, subtract))
        logger.info('multiply: {} * {} = {}'.format(x, y, multiply))
        logger.info('division: {} / {} = {}'.format(x, y, division))

if __name__ == '__main__':
    my_process()
