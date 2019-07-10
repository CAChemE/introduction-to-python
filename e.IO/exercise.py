import time
import argparse
import sys
import os

# Prime Algorithm
def sieve_Eratosthenes(nmax):

	start = time.clock()
	L = []

	for n in range(2, nmax):
		for factor in L:
			if n % factor == 0:
				break
		else: # no break
			L.append(n)
	cpu_time = (time.clock() - start)
	
	return(L, cpu_time)

# Print results in a txt file
def print_primes (fileName, prime_list, n_max):
	prime_numbers = results[0]
	elapsed_time  = results[1]
	file_object = open(fileName, 'w')
	file_object.write('{0} prime numbers up to {1} have been found in {2:0.2f} seconds using the Sieve of Eratosthenes Algorithm \n\n'
                       .format(len(prime_numbers), n_max, elapsed_time))
	file_object.write('List of prime numbers: \n')
	
	for i in prime_numbers:
		file_object.write(str(i) + '\n')
	file_object.close()


# Command-line Interface
def check_args(args = None):

    parser = argparse.ArgumentParser(description = 'Finding prime numbers check argument')
	
    parser.add_argument('n_max',
                        type = int,
                        nargs = '?',
						default = 100,
                        help = 'Upper Limit')
                        
    parser.add_argument('output_file', type = str, nargs = '?', default = 'List_primes.txt', help = 'txt file with prime numbers')
	
    results = parser.parse_args()
    return (results.n_max, results.output_file)
	

# MAIN
if __name__ == '__main__':

	# Call check_args
    n_max, output_file = check_args(sys.argv[1:])
	
	# Call prime algorithm
    results = sieve_Eratosthenes(n_max)
    print('{0} prime numbers up to {1} have been found in {2:0.2f} seconds using the Sieve of Eratosthenes Algorithm'
           .format(len(results[0]), n_max, results[1]))
           
    print('Results are saved in {:s}'.format(output_file))
	
	# Call print_primes
    print_primes (output_file, results, n_max )
