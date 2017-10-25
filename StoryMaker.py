# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:37:04 2017

@author: karja
"""

from textwrap import fill
import os
import shutil
from pathlib import Path

# Geting users home directory
h_path = str(Path.home())

def make_s():
    # Checking the existence of a directory. If there is none
    # then make new one as default 
    try:
        os.chdir('%s/Documents/Bless_Story' %h_path)
    except:
        os.chdir('%s/Documents' %h_path)
        os.mkdir('Bless_Story')
        os.chdir('%s/Documents/Bless_Story' %h_path)
        
    # Creating new story file
    num_f = len([name for name in os.listdir()])
    # Process creating a file name and creating new one
    if num_f is 0: 
        n_st = open(
        'BlessingPro' + str(num_f + 1) + '.txt', 'w')
    else:
        for name in os.listdir(): 
            if name is None or name != 'BlessingPro' + str(num_f + 1) + '.txt':
                n_st = open('BlessingPro' + str(num_f + 1) + '.txt', 'w')
            else:
                print('BlessingPro' + str(num_f + 1) + '.txt'
                      ,'is already exist.', 
                      'Please naming file manually!')
                r_name = str(input('Naming File: '))
                n_st = open(r_name + '.txt', 'w')
    
    # Input the string without '' or ""
    # Input the choices in this format:
    ''' A. bla bla bla,B. bla bla bla,C. bla bla bla, '''
    # (Always remember to put ',' at the end of your last choices)
    part_1 = str(input('Please input Beginning of a story: '))
    part_2 = input('List of choices e.g. [A.,B...]: ')
    part_3 = input('List of choices e.g. [A.,B...]: ')
    part_4 = str(input('Please input middle of a story: '))
    part_5 = str(input('Please input middle of a story: '))
    part_6 = str(input('Please input middle of a story: '))
    part_7 = str(input('Please input end of a story: '))
    part_8 = str(input('Please input end of a story: '))
    part_9 = str(input('Please input end of a story: '))
    part_10 = str(input('Please input verse of a story: '))
    part_11 = str(input('Please input verse of a story: '))
    
    join_all = [part_1 + '\n',part_2 + '\n',part_3 + '\n'
                ,part_4 + '\n',part_5 + '\n',part_6 + '\n'
                ,part_7 + '\n',part_8 + '\n',part_9 + '\n'
                ,part_10 + '\n',part_11 + '\n']
    
    for line in join_all:
        n_st.write(line)
    n_st.close()

def start_m():
    while True:
        make_s()
        ask_q = str(input('Do you still want to make story?[Y]es / [Enter] for no ').upper())
        if ask_q == 'Y':
            continue
        else:
            break

            
start_m()
            