# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:18:03 2017

@author: karja
"""
import os
from pathlib import Path
from textwrap import fill
# Geting users home directory
h_path = str(Path.home())

# Set Choices for the class Story
choices = ('A', 'B', 'C')

# Story attributes
class S_at:
    pass
    
# Storie's variables
class C_st(S_at):
    def __init__(self):
        super().__init__()
        self.ch_st = self.ch_st
        self.docr = self.docr
        self.fix_1 = self.fix_1
        self.fix_2 = self.fix_2
        
# Class story to help the s_story() run smoothly
class Story(C_st):

    def __init__ (self,ans=None,part=None):
        super().__init__()
        self.ans = ans
        self.part = part
    
    def choice(self):
        while True:
            try:
                self.ans = str(input('Please choose! A/B/C').upper())
            except:
                print ('Please choose accordingly!')
                continue
            else:
                c = enumerate(choices)
                c = {a:b for b,a in c} 
                if self.ans == 'A':
                    return c['A']
                    break
                elif self.ans == 'B':
                    return c['B']
                    break
                elif self.ans == 'C':
                    return c['C']
                    break
                else:
                    print ('Please choose accordingly!')
                    continue
                    
    def get_ans(self):
        if self.part == 1:
            if self.ans == 0:
                print (fill(self.q1_ansA))
            elif self.ans == 1:
                print (fill(self.q1_ansB))
            elif self.ans == 2:
                print (fill(self.q1_ansC),'\nThe End'.upper())
                
        elif self.part == 2:
            if self.ans == 0:
                print (fill(self.q2_ansA))
            elif self.ans == 1:
                print (fill(self.q2_ansB))
            elif self.ans == 2:
                print (fill(self.q2_ansC),'\nThe End'.upper()) 

# Create Story Attributes
def check_s():
    
    # Checking the existence of the directory
    try:
        os.chdir('%s/Documents/Bless_Story' %h_path)
    except:
        print('Please create story first!')
        input('Check the folder "Bless_Story" in default local "Documents" folder!' +
              ' If it is not exist, you should find it in your OneDrive(cloud) "Documents"' +
              ' Please copy the folder to local "Documents" folder!')
    else:
        
        # Cheking library for stories
        num_f = len([name for name in os.listdir()])
        if num_f is 0:
            print('Please create story first!')
            #break
        else:
            Story.ch_st = []
            for name in os.listdir():
                Story.ch_st.append(name)
            
            # Create dictionary to key the choices
            Story.ch_st = dict(enumerate(Story.ch_st))
            print('List of stories', Story.ch_st)
            
            # Unravel the chosen Story
            while True:
                try:
                    print()
                    story_ch = Story.ch_st[int(input('Please choose a story from the list.'
                                 + ' Choose number: '))]
                except:
                    print('The story you have chosen is not exist!')
                    continue
                else:
                    
                    # Unpacked story that has been chosen
                    Story.docr = []
                    file_op = open(story_ch, 'r')
                    file_op.seek(0)
                    Story.docr = file_op.readlines()
                    ch1 = Story.docr[1]
                    ch2 = Story.docr[2]
                    
                    # Fixing the choices list 
                    Story.fix_1=[]
                    Story.fix_2=[]
                    post_1 = ''
                    for appen in ch1:
                        if appen != '[' != ']':
                            post_1 += appen
                            if appen == ',':
                                Story.fix_1.append(post_1)
                                post_1 = ''
                    Story.fix_1 = [Story.fix_1[i].replace(',','') 
                             for i in range(len(Story.fix_1))] 
                    
                    post_2 = ''
                    for appen in ch2:
                        if appen != '[' != ']':
                            post_2 += appen
                            if appen == ',':
                                Story.fix_2.append(post_2)
                                post_2 = ''
                    Story.fix_2 = [Story.fix_2[i].replace(',','') 
                             for i in range(len(Story.fix_2))] 
                    file_op.close()
    
                    # Setting up story to be run later on 
                    S_at.pre = Story.docr[0]    
                    
                    S_at.q1 = Story.fix_1
                    
                    S_at.q2 = Story.fix_2
                    
                    S_at.q1_ansA = Story.docr[3]
                    
                    S_at.q1_ansB = Story.docr[4]
                    
                    S_at.q1_ansC = Story.docr[5]
                    
                    S_at.q2_ansA = Story.docr[6]
                    
                    S_at.q2_ansB = Story.docr[7]
                    
                    S_at.q2_ansC = Story.docr[8]
                    break
                
# Run the story that has been chosen
def s_story():
    
    # First part of the story
    print (fill(Story.pre),'\n')
    for i in Story.q1:
        print (i)
    s =Story().choice()
    print()
    Story(s,1).get_ans() 
    print()
    
    # Second part of the story
    if s != 2:
        for i in Story.q2:
            print (i)
        s =Story().choice()
        print()
        Story(s,2).get_ans()
        
        # Ending part of the story
        if s == 0:
            w = Story.docr[9] 
            print()
            print (fill(w.upper(),73))
        elif s == 1:
            w = Story.docr[10]
            print()
            print (fill(w.upper(),73))

# Start the story and running until end
def start_story():
    check_s()
   
    # Initial starting
    while True: 
        if len(Story.docr) > 0:
            print() 
            s_story()
            print()
            aq = str(input('[C]ontinue, [R]estart, [E]nd ? ' ).upper())
            
            # Choosing the continuation
            if aq == 'C':
                print()
                continue
            elif aq == 'R':
                print()
                Story.docr = []
                continue
            elif aq == 'E':
                print()
                input('God bless you')
                Story.docr = []
                break
        else:
            
            # Restarting and checking the availability of Stories
            print()
            check_s()
            if len(Story.ch_st) > 0:
                continue
            else:
                input('Check the folder "Bless_Story" in default local "Documents" folder!' +
                      ' If it is not exist, you should find it in your OneDrive(cloud) "Documents"' +
                      ' Please copy the folder to local "Documents" folder!')
                break

start_story()
