import os

print(os.getcwd())
print(os.listdir())
print(os.listdir('C:\\Users\\150987\\Documents\\Workspace'))

import shutil

# shutil.move('practice.txt','C:\\Users\\150987\\Documents')

# Deletes the file permanently!
# os.unlink('C:\\Users\\150987\\Documents\\example.txt')

# Deletes an entire folder permanently!
# os.rmdir('C:\\Users\\150987\\Documents\\example')

# DANGER! Removes all folder and files with it, DO NOT RUN THIS
# shutil.rmtree('C:\\Users\\150987\\Test\\example')

import send2trash

send2trash.send2trash(os.getcwd()+'\\practice.txt')

file_path = 'C:\\Users\\150987\\Documents'

for folder, sub_folders, files in os.walk(file_path):

    print(f'Currently looking at {folder}')
    print('\n')
    print('The subfolder are: ')

    for sub_fold in sub_folders:
        print(f'\t Subfolder: {sub_fold}')
    
    print('\n')
    print('The files are: ')

    for f in files:
        print(f'\t File: {f}')
    print('\n')