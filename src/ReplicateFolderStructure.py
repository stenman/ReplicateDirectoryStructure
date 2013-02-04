'''
Created on 3 feb 2013

@author: Gildur
'''
#coding=UTF-8
import os
import sys
import UserDialogue

print (os.getcwd())

#TODO: Put these variables in a config?
error_message_directory_already_exists = "The destination directory you want to replicate to already exist!"
error_message_directory_to_be_replicated_does_not_exist = "The directory you want to replicate does not exist!"
question_replicate_directory_structure = "Are you sure you want to replicate this directory structure recursively?"
default_answer_to_replicate_directory_structure_query = "no"
#TODO: make this directory and location a user choice
directory_to_be_replicated = "/test/DirectoryToBeReplicated"
#TODO: make this directory name and location a user choice
default_replication_destination_directory = "/ReplicatedDirectoryStructure"
default_root_directory_windows = "/"

def checkDir():
    if os.path.isdir(default_replication_destination_directory):
        raise OSError(error_message_directory_already_exists)
    if not os.path.isdir(directory_to_be_replicated):
        raise OSError(error_message_directory_to_be_replicated_does_not_exist)
    
def testDirectoryAccess():
    print("method not yet defined")

def createDirectoryList():
    print("method not yet defined")

def replicateDirectoryStructure():
    print("\nReplicating directory structure in", os.getcwd(), "recursively.")
    print("\nYou will find the root of the replicated directory structure here:\n", default_replication_destination_directory, "\n")
    print("method not yet defined")
    
def main():
    try:
        userDialogue = UserDialogue.UserDialogue()
        if userDialogue.QueryYesNo(question_replicate_directory_structure, default_answer_to_replicate_directory_structure_query):
            
            #Verify directory existences
            checkDir()
            
            #TODO: Make sure that a replication of the directory structure is possible, use os.access
            testDirectoryAccess()
            
            #TODO: start the replication. Eg. - create a list over the directory structure.
            #TODO: check out os.walk()!
            createDirectoryList()
            
            os.chdir(directory_to_be_replicated)
            os.mkdir(default_replication_destination_directory)

            #TODO: create the replication in default_replication_destination_directory (use the above mentioned list)
            replicateDirectoryStructure()
        else:
            print("\nTerminating program.")
            sys.exit(0)

    except OSError as error:
        print("\nOSError: %s" % str(error))
        sys.exit(1)

    except Exception as error:
        print("\nAn unexpected exception was encountered: %s" % str(error))
        sys.exit(1)

    finally:
        #TODO: Test (remove me)
        if os.path.isdir(default_replication_destination_directory):
            os.removedirs(default_replication_destination_directory)
            print("Test: removed default_replication_destination_directory")
        sys.exit(1)

if __name__ == "__main__":
    main()

