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
    
    def display_successful_replication_message(self, destination_directory):
        print("\nDirectory structure replicated to: {0}\n".format(destination_directory))

    
    def replicate_directory_structure(self, src, dst):
        print("\nReplicating directory structure in {0} recursively...".format(src))
        shutil.copytree(src, dst, ignore=self.ignored_files)
    
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