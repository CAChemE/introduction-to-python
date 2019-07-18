# Logging - Example 2 | Logger

import logging

# Create logger
logger = logging.getLogger(__name__)

# Set level
logger.setLevel(logging.INFO)

# Logger Formating
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# File handler
file_handler = logging.FileHandler('person_records.log')
file_handler.setFormatter(formatter)

# Add Handler to logger
logger.addHandler(file_handler)



#logging.basicConfig(filename = 'record.log', level = logging.INFO,
#                    format = '%(levelname)s:%(name)s:%(message)s')


class Person:
    def __init__ (self, fullname,  e_mail = '' ):
        self.name = fullname
        self.email = e_mail
        logger.info('Record: {} | {}'.format(self.name, self.email))

    def printp (self):
        print( 'Name = ', self.nombre)
        print( 'E-mail = ', self.email)

person_1 = Person('first1 last1', 'last1.first1@mail.com')
person_2 = Person('first2 last2', 'last2.first2@mail.com')
person_3 = Person('first3 last3', 'last3.first3@mail.com')
