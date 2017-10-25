# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:18:03 2017

@author: karja
"""
from textwrap import fill
import os
import shutil
from pathlib import Path
from textwrap import fill
# Geting users home directory
h_path = str(Path.home())

# Checking the existence of a directory
ch_st = []
docr = []
fix_1 = []
fix_2 = []
pre = ''                   
q1 = []
q2 = []
q1_ansA = ''
q1_ansB = ''
q1_ansC = ''
q2_ansA = ''
q2_ansB = ''
q2_ansC = ''

def check_s():
    global ch_st, docr, fix_1, fix_2, pre, q1, q2, q1_ansA, q1_ansB, q1_ansC, q2_ansA, q2_ansB, q2_ansC
    try:
        os.chdir('%s/Documents/Bless_Story' %h_path)
    except:
        print('Please create story first!')
        #break
    else:
        
        # Cheking library for stories
        num_f = len([name for name in os.listdir()])
        if num_f is 0:
            print('Please create story first!')
            #break
        else:
            ch_st = []
            for name in os.listdir():
                ch_st.append(name)
            
            # Create dictionary to key the choices
            ch_st = dict(enumerate(ch_st))
            print('List of stories', ch_st)
    
            try:
                story_ch = ch_st[int(input('Please choose a story from the list.'
                             + ' Choose number: '))]
            except:
                print('The story you have chosen is not exist!')
                #break
            else:
                
                # Unpacked story that has been chosen
                docr = []
                file_op = open(story_ch, 'r')
                file_op.seek(0)
                docr = file_op.readlines()
                ch1 = docr[1]
                ch2 = docr[2]
                
                # Fixing the choices list 
                fix_1=[]
                fix_2=[]
                post_1 = ''
                for appen in ch1:
                    if appen != '[' != ']':
                        post_1 += appen
                        if appen == ',':
                            fix_1.append(post_1)
                            post_1 = ''
                fix_1 = [fix_1[i].replace(',','') 
                         for i in range(len(fix_1))] 
                
                post_2 = ''
                for appen in ch2:
                    if appen != '[' != ']':
                        post_2 += appen
                        if appen == ',':
                            fix_2.append(post_2)
                            post_2 = ''
                fix_2 = [fix_2[i].replace(',','') 
                         for i in range(len(fix_2))] 
                file_op.close()

                # Setting up story to be run later on 
                pre = docr[0]    
                
                q1 = fix_1
                
                q2 = fix_2
                
                q1_ansA = docr[3]
                
                q1_ansB = docr[4]
                
                q1_ansC = docr[5]
                
                q2_ansA = docr[6]
                
                q2_ansB = docr[7]
                
                q2_ansC = docr[8]

choices = ('A', 'B', 'C')

# Class story to help the s_story() run smoothly
class Story(object):

    def __init__ (self,ans=None,part=None):
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
                print (fill(q1_ansA))
            elif self.ans == 1:
                print (fill(q1_ansB))
            elif self.ans == 2:
                print (fill(q1_ansC),'\nThe End'.upper())
                
        elif self.part == 2:
            if self.ans == 0:
                print (fill(q2_ansA))
            elif self.ans == 1:
                print (fill(q2_ansB))
            elif self.ans == 2:
                print (fill(q2_ansC),'\nThe End'.upper())        
            
# Run the story that has been chosen
def s_story():
    global q1, q2
    print (fill(pre),'\n')
    for i in q1:
        print (i)
    s =Story().choice()
    print()
    Story(s,1).get_ans() 
    print()
    if s != 2:
        for i in q2:
            print (i)
        s =Story().choice()
        print()
        Story(s,2).get_ans()
        
        if s == 0:
            w = docr[9] 
            print()
            print (fill(w.upper(),73))
        elif s == 1:
            w = docr[10]
            print()
            print (fill(w.upper(),73))

# Start the story and running until end
def start_story():
    global docr, ch_st
    while True:       
        if len(docr) > 0:
           print() 
           s_story()
           print()
           aq = str(input('[C]ontinue, [R]estart, [E]nd ? ' ).upper())
           if aq == 'C':
               print()
               continue
           elif aq == 'R':
               print()
               docr = []
               continue
           elif aq == 'E':
               print()
               input('God bless you')
               docr = []
               break
        else:
            print()
            check_s()
            if len(ch_st) > 0:
                continue
            else:
                input('Check the folder "Bless_Story" in default local "Documents" folder!' +
                      ' If it is not exist, you should find it in your OneDrive(cloud) "Documents"' +
                      ' Please copy the folder to local "Documents" folder!')
                break
        
start_story()