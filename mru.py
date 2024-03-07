#matt's renaming utility: quickly renames files en masse or lets you rename them quicker than you could in a GUI
#also works as a file converter if you're into that

#NOTE : please place this program in the folder you plan to modify before doing anything

#NOTE2 : this program has only been tested in the windows 11 file system

import random
import os

filetype = ''
router = ''

#Home folder
while router == '':
    router = input('\nBefore starting, please enter the exact location of the folder you are going to be editing\n')
    if router == '':
        continue
    else:
        break
    
folder = os.listdir(router)

#1 2 3... renamer
def looper_numbers():
    newnamernum =  0
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    while indexer < length:
        name = folder[indexer]
        if name != 'mru.py':
            os.rename(str(name), str(newnamernum) + str(filetype))
            newnamernum += 1
        indexer += 1

#individual renamer
def looper_individual():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    while indexer < length:
        name = folder[indexer]
        if name != 'mru.py':
            newnamer = input('\nPlease input your name here\n')
            os.rename(str(name), str(newnamer) + str(filetype))
        indexer += 1
        
#prefix adderoner
def looper_prefix():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    prefixer = input('\nPlease input your prefix here\n')
    while indexer < length:
        name = folder[indexer]
        if name != 'mru.py':
            os.rename(str(name), str(prefixer + name) + str(filetype))
        indexer += 1

#Main program
while True:
    prompt = int(input('Welcome to matt\'s file utility: Please choose one of the following:\n1 to rename files\n2 for other fun utilities\n0 to quit\n'))

    #Program quit
    if prompt == 0:
        print('Goodbye')
        break
    
    #File renamer    
    elif prompt == 1:
        renamer = int(input('\n1 to rename a single file\n2 to rename an entire folder of files starting from 1 to X\n3 rename each file individually\n4 to add a prefix to the name of each file\n'))
        if renamer == 1:
            namefile = input('\nWhat is the name of the file you would like to rename?\n')
            newnamefile = input('\nWhat would you like to rename the file to?\n')
            filetype = str(input('\nPlease enter a file type (ex - .txt)\n'))
            os.rename(namefile, newnamefile + filetype)
            folder = os.listdir(router)
        elif renamer == 2:
            filetype = str(input('\nPlease enter a file type (ex - .txt)\n'))
            looper_numbers()
            print('\nTask completed!\n')
            folder = os.listdir(router)
        elif renamer == 3:
            filetype = str(input('\nPlease enter a file type (ex - .txt)\n'))
            looper_individual()
            print('\nNo more files to rename!\n')
            folder = os.listdir(router)

        elif renamer == 4:
            filetype = str(input('\nPlease enter a file type (ex - .txt)\n'))
            looper_prefix()
            print('\nTask completed!\n')
            folder = os.listdir(router)

        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
