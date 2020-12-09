import sys
import os

check_exit = False

def checkExit(exit):
    return exit() or None

if len(sys.argv) < 3:
    print('Missing params!')
    print('Help: python copy_files.py <source file> <target file>')
    check_exit = True

checkExit(check_exit)

source_file_name = sys.argv[1]
dest_file_name = sys.argv[2]

if source_file_name == dest_file_name:
    print('Source file is the Target file. Copy unsuccessful')
    exit()
if not os.path.exists(source_file_name):
    print('Source file don`t exists. Copy unsuccessful')
    exit()

if not os.path.exists(dest_file_name):
    print('Target file don`t exists. Copy unsuccessful')
    exit()

source_file = open(source_file_name, 'r')
dest_file = open(dest_file_name, 'w')

for source_line in source_file:
    dest_file.write(source_line)

source_file.close()
dest_file.close()

print('Copy successful.')
