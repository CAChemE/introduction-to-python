import subprocess


# GET MEDIA METADATA - OPTION I
# (instalar hachoir: pip install hachoir, https://pypi.org/project/hachoir/)



inputFile = 'IMG01.jpg'
exe = 'hachoir-metadata'

process = subprocess.check_output([exe, inputFile], shell = True, universal_newlines = True)

text = process.strip().split('\n')

metadata = {}
for line in text:
    x = line.split(':')
    metadata[x[0][2:]]=x[1:]

creation_date = metadata['Creation date']
print('Creation date:', (':').join(creation_date).strip())



# GET MEDIA METADATA - OPTION II

inputFile = 'IMG01.jpg'
exe = 'hachoir-metadata'

process = subprocess.Popen([exe, inputFile], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines = True)

#for output in process.stdout:
#    print(output)

metadata = {}
for output in process.stdout:
    line = output.strip().split(':')
    metadata[line[0]] = line[1].strip()
print(metadata)
