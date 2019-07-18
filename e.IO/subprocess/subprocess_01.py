# SUBPROCESS

import subprocess


"""
Communicate from the script to the shell and get the output
"""


"""
The subprocess module allows you to spawn new processes, connect to their
input/output/error pipes, and obtain their return codes.

https://docs.python.org/3/library/subprocess.html

"""


"""
A continuación, se muestran varios ejemplos con el módulo  "subprocess" que genera un nuevo proceso para
ejecutar el comando permitiendo controlar su ejecución y obtener su  salida y/o errores que pudieran darse.

"""


# SUBPROCESS: run
print(subprocess.run('dir', shell = True))




# SUBPROCESS: check_output
# Communicate Script with Shell. Get outputs from the shell
output = subprocess.check_output('dir', shell = True, universal_newlines = True)
print(output)


# SUBPROCESS: Popen Constructor
# It offers a lot of flexibility so that developers are able to handle the less
# common cases not covered by the convenience functions.

#"""
process = subprocess.Popen('dir', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines = True)
error = process.stderr.read()
output = process.stdout.read()
process.stderr.close()
process.stdout.close()

print("Errors:\n")
print(error)


print("Command output:\n")
print(output)
#"""





