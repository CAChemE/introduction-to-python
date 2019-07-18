# SUBPROCESS

import subprocess
import sys


process = subprocess.Popen('ping 172.16.96.1 -n 10' , shell = True,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE,
                            universal_newlines = True)
#process.wait()

 for output in process.stdout:
     print(output)


# while process.poll() is None:
    # output = process.stdout.readline().strip()
    # print(output)


# while True:
#     try:
#         print ( process.stdout.readline() )
#     except:
#         break
