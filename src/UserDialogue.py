'''
Created on 31 jan 2013

@author: Gildur
'''
import sys
import os

class UserDialogue(object):
    '''
    Takes care of user dialogues
    '''

    def __init__(self):
        #Create a platform independent clear_screen-function
        #TODO: Only for test (unless running program from shell)
        if sys.platform.startswith("win"):
            def clear_screen(self):
        # Use only if not running from shell
                os.system("cls")
        else:
            def clear_screen(self):
                os.system("clear")

    def QueryYesNo(self, question, default="no"):
        self.clear_screen()
        valid = {"yes": True, "y": True, "Y":True, "YES":True, "Yes":True, "no":False, "n":False, "N":False, "NO":False, "No":False}
        if default == None:
            prompt = " [y/n]: "
        elif default == "yes":
            prompt = " [Y/n]: "
        elif default == "no":
            prompt = " [y/N]: "
        else:
            raise ValueError("Invalid default answer: '%S'" % default)
    
        while True:
            sys.stdout.write(question + prompt)
            #.rstrip('\r') is a fix to a bug in Python, causing a trailing '\r' in the resulting string
            choice = input().lower().rstrip('\r')
            if default is not None and choice == '':
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")
                

        
