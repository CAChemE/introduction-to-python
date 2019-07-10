# ARGPARSE MODULE - argp06.py | Argument Groups


"""
#-----------------------------------------------------------------------------------
#                          ### INTRODUCTION TO ARGPARSE ###
#-----------------------------------------------------------------------------------

The argparse module makes it easy to write user-friendly command-line interfaces. 
The program defines what arguments it requires, and argparse will figure out how to 
parse those out of sys.argv. The argparse module also automatically generates help 
and usage messages and issues errors when users give the program invalid arguments.

https://docs.python.org/3/library/argparse.html
#-----------------------------------------------------------------------------------
"""


"""

The add_argument() method

ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])


1.  name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
2.  action        - The basic type of action to be taken when this argument is encountered at the command line.
3.  nargs         - The number of command-line arguments that should be consumed.
4.  const         - A constant value required by some action and nargs selections.
5.  default       - The value produced if the argument is absent from the command line.
6.  type          - The type to which the command-line argument should be converted.
7.  choices       - A container of the allowable values for the argument.
8.  required      - Whether or not the command-line option may be omitted (optionals only).
9.  help          - A brief description of what the argument does.
10. metavar       - A name for the argument in usage messages.
11. dest          - The name of the attribute to be added to the object returned by parse_args().

https://docs.python.org/3/library/argparse.html#the-parse-args-method
"""

import argparse
import sys

print('\nPath of Python executable binary: {}'.format(sys.executable))
print('Python version: {}\n '.format (sys.version))

# 01 List of Command line arguments ------------------------------------------------ 
print('Number of command-line arguments: {} '.format( len(sys.argv)) )
print('List of arguments: {} \n\n '.format( str(sys.argv)))
#-----------------------------------------------------------------------------------




# 06 ARGPARSE: Argument Groups #---------------------------------------------------

parser = argparse.ArgumentParser(description = 'Introduction to ARGPARSE Module')

group1 = parser.add_argument_group('group1', 'group1 description')
group2 = parser.add_argument_group('group2', 'group2 description')

# Group 1 
#	> Positional arguments
group1.add_argument('arg1', help = 'First positional argument, group1 (str)',  type = str)
group1.add_argument('arg2', help = 'Second positional argument, group1 (str)', type = str)


# Group 2 
#	> Positional argument
group2.add_argument('arg3', help = 'Third positional argument, group1 (str)', 
                     type = str)

#	> Optional argument
group2.add_argument('-opt1', '--option1', help = 'Upper or Lower Case  optional argument, group2 (str)',
					type = str,
					nargs = '?',
					choices = ['cap', 'low'],
					default = 'low')


# Optional Arguments
parser.add_argument('-p', '--printr', help = 'Print results',
					action = 'store_true')


args = parser.parse_args()

if args.printr:
	if args.option1 == 'cap':
		print('First  positional argument: {}'.format(args.arg1).upper())
		print('Second positional argument: {}'.format(args.arg2).upper())
		print('Third  positional argument: {}'.format(args.arg3).upper())
	else:
		print('First  positional argument: {}'.format(args.arg1).lower())
		print('Second positional argument: {}'.format(args.arg2).lower())
		print('Third  positional argument: {}'.format(args.arg3).lower())
else:	
	print('Print option: {}'.format(args.printr))

































