import os
import datetime

def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + "_" + str(counter) + extension
        counter += 1

    return path

overwrite = False  # True is dangerous 

target_folder = f'CONTEST_{datetime.date.today()}'

if overwrite == False:
    target_folder = uniquify(target_folder)
    
target_template = 'zcp_template.cpp'

suffix = '.cpp'
preffix = ''
start_index = 'A'
end_index = 'H'

if not os.path.isdir(target_folder): 
    os.mkdir(target_folder)

with open(target_template, 'r') as template_file:
    template = template_file.read()

# ord <-> chr
for index in range(ord(start_index), ord(end_index)+1):
    filename = f'{target_folder}/{preffix}{chr(index)}{suffix}'
    if (not os.path.isfile(filename) or overwrite):
        with open(filename, 'w') as f:
            f.write(template)
    
