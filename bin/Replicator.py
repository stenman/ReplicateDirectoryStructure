'''
Created on 10 feb 2013

@author: Gildur
'''

import os
import shutil
import ReplicatorConfig

class Replicator(object):
    '''
    Takes care of user dialogues
    '''

    def __init__(self):
        self
    
    def replicate_directory_structure(self, src, dst):
        print("\nReplicating directory structure in "+src+" recursively.")
        print("\nYou will find the root of the replicated directory structure here:\n"+dst+"\n")
        shutil.copytree(src, dst, ignore=self.ignored_files)
    
    #TODO: Make test cases to check for possible errors while traversing directories. Maybe make a "test_directory_access" function?
        #TODO: Errors found so far:
        #TODO: [Errno 13]: Permission denied. Example: C:\Windows\System32\winevt\Logs\system.evtx
        #TODO: [WinError 5]: Access Denied. Example: C:\Windows\SysWOW64\com\dmp\*.*
    #TODO: Create a logging function    
    def replicate(self, src, dst):
        self.check_source_dir(src)
        self.check_destination_dir(dst)
        self.replicate_directory_structure(src, dst)

    def check_destination_dir(self, directory):
        if os.path.isdir(directory):
            raise OSError(ReplicatorConfig.error_message_directory_already_exists)
    
    def check_source_dir(self, directory):
        if not os.path.isdir(directory):
            raise OSError(ReplicatorConfig.error_message_directory_to_be_replicated_does_not_exist)
    
    def ignored_files(self, adir,filenames):
        filenames = []
        for filename in os.listdir(adir):
            if os.path.isfile(adir+"/"+filename):
                filenames.append(filename)
                continue
            else:
                continue
        return filenames