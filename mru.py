#matt's renaming utility: quickly renames files en masse or lets you rename them quicker than you could in a GUI

#NOTE : please place this program in the folder you plan to modify before doing anything

#NOTE2 : this program has only been tested in the windows 11 file system

import random
import os

filetype = ''
router = ''
bannedtypes = []

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
    filetype = folder[indexer]
    while indexer < length:
        name = folder[indexer]
        splitter = name.split('.')
        filetype = splitter[1]
        if name != 'mru.py':
            if filetype not in bannedtypes:
                os.rename(str(name), str(newnamernum) + '.' + str(filetype))
                newnamernum += 1
        indexer += 1

#individual renamer
def looper_individual():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    filetype = name.split('.')
    while indexer < length:
        name = folder[indexer]
        splitter = name.split('.')
        filetype = splitter[1]
        if name != 'mru.py':
            newnamer = input('\nPlease input your name here\n')
            os.rename(str(name), str(newnamer) + '.' + str(filetype))
        indexer += 1
        
#prefix adderoner
def looper_prefix():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    prefixer = input('\nPlease input your prefix here\n')
    while indexer < length:
        name = folder[indexer]
        splitter = name.split('.')
        filetype = splitter[1]
        if name != 'mru.py':
            if filetype not in bannedtypes:
                os.rename(str(name), str(prefixer + name + '.' + filetype))
        indexer += 1

#Main program
while True:
    prompt = int(input('Welcome to matt\'s file utility: Please choose one of the following:\n1 to rename files\n0 to quit\n'))

    #Program quit
    if prompt == 0:
        print('Goodbye')
        break
    
    #File renamer    
    elif prompt == 1:
        
        renamer = int(input('\n1 to rename an entire folder of files starting from 1 to X\n2 rename each file individually\n3 to add a prefix to the name of each file\n'))
        
        if renamer == 1:
            while True:
                bannedfile = str(input('\nPlease enter a file type to ignore\nPress enter to continue\n'))
                bannedtypes.append(bannedfile)
                if bannedfile == '':
                    break
            looper_numbers()
            print('\nTask completed!\n')
            folder = os.listdir(router)
            bannedtypes = []
            
        elif renamer == 2:
            looper_individual()
            print('\nNo more files to rename!\n')
            folder = os.listdir(router)

        elif renamer == 3:
            while True:
                bannedfile = str(input('\nPlease enter a file type to ignore\nPress enter to continue\n'))
                bannedtypes.append(bannedfile)
                if bannedfile == '':
                    break
            looper_prefix()
            print('\nTask completed!\n')
            folder = os.listdir(router)
            bannedtypes = []
            
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
