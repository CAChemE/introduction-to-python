# Logging - Example 2 

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


class Person:
    def __init__ (self, fullname,  e_mail = '' ):
        self.name = fullname
        self.email = e_mail
        print('Record: {} | {}'.format(self.name, self.email))

    def printp (self):
        print( 'Name = ', self.nombre)
        print( 'E-mail = ', self.email)

person_1 = Person('first1 last1', 'last1.first1@mail.com')
person_2 = Person('first2 last2', 'last2.first2@mail.com')
person_3 = Person('first3 last3', 'last3.first3@mail.com')
