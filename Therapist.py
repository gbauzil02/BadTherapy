#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:08:27 2021

@author: gianna
"""

import time
import random

def shortPause():
    time.sleep(1.5)
    
def longPause():
    time.sleep(2.25)

def problem():
    problem = ["Okay so you're the problem, goodbye", "Congrats! You wasted my time...", 
               "You could've just looked in the mirror before wasting my time, peace..."]
    return random.choice(problem)
    
    
if __name__ == "__main__":
    #Variables
    end = False
    test = False
    
    #user name and welcome message
    name = input("Enter your name: ")
    print("\nHello "+name + "...\n")
    shortPause()
    print("Welcome to bad therapy")
    shortPause()
    print("This advice is not meant to be taken seriously because... ")
    longPause()
    print("I am not a licensed professional...")
    longPause()
    print("\njust a judgy person :))")
    
    longPause()
    shortPause()
    
    issue = input("So " + name + ", what seems to be the problem today? \n[1]Friend problems \n[2]Family Problems \n[3]Relationship Problems \n[4]Work Problems \n[5]School Problems \n[6]You're the problem \n\n")
    
    
    helpYou = True
    
    while helpYou == True:
        if issue == '6':
            print(problem())
            shortPause()
            break;
            
        shortPause()
        print("\nBefore I give you my advice...")
        shortPause()
        print("Please look at option 6 again before wasting my time...")
        shortPause()
        confirm = input("So are you absolutely sure you're not the problem? \n[1] Yes \n[2] No \n[3] You don't know \n\n")
        if confirm == '3':
            shortPause()
            print(problem)
            shortPause()
            break;
        elif confirm == '2':
            shortPause()
            print("\nWell you should figure that out. Goodbye")
            shortPause()
            break;
        else:
            shortPause()
            print("\nThat's what they all say...")
        shortPause()
        cause = input("\nSo how did this problem come about? ")
        
        shortPause()
        print("\nOh wow that sucks")
        shortPause()
        talking = input("Well have you tried talking to someone about it? \n[1]Yes \n[2]No \n[3]That's what I'm talking to you for \n\n")
        shortPause()
        if talking == '1':
            shortPause()
            print("\nOh well you should probably take their advice, and if you don't like it, they're either right...")
            shortPause()
            print("OR")
            shortPause()
            print("they're absolutely 100% wrong")
            shortPause()
        elif talking == '2':
            shortPause()
            print("\nWell you should probably talk to someone...")
            shortPause()
            print("Why are you talking to a python program LOL..")
            shortPause()
        else:
            shortPause()
            print("\nWhy would you talk to a python program about your issues? ")
            shortPause()
            print("Go see a professional...")
            shortPause()
            print("Expiditiously")
            shortPause()
        helpYou = False
        
    rate = input("So how did I do on a scale of 1-5? (1 being the worst and 5 being the best) ")
    if rate == '1':
        shortPause()
        print()
        print(problem())
        shortPause()
    elif rate == '2':
        shortPause()
        print()
        print(problem())
        shortPause()
    elif rate == '3':
        shortPause()
        print()
        print("Maybe you're the one who's mid...goodbye")
        shortPause()
    elif rate =='4':
        print()
        print("Everyone is entitled to their own opinion...you just so happen to be right ;)")
        shortPause()
    elif rate == '5':
        print()
        print("Wow...")
        shortPause()
        print("If you're in love with me...")
        shortPause()
        print("Just say that next time instead of wasting my time")
        shortPause()
    else:
        print("Well goodbye")
        
            
        
    
    
    
    
    
    