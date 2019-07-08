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

# IMPLEMENTAR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Command-line Interface
def check_args(args = None):

# IMPLEMENTAR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	

# MAIN
if __name__ == '__main__':

	# Call check_args
    n_max, output_file = check_args(sys.argv[1:])

	
	# Call prime algorithm
    results = sieve_Eratosthenes(n_max)
    print('{0} prime numbers up to {1} have been found in {2:0.2f} seconds using the Sieve of Eratosthenes Algorithm'.format(len(results[0]), n_max, results[1]))
    print('Results are saved in {:s}'.format(output_file))
	
	# Call print_primes
    print_primes (output_file, results, n_max )


