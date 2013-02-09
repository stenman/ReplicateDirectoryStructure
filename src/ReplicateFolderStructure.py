'''
Created on 3 feb 2013

@author: Gildur
'''
#coding=UTF-8
import os
import sys
import UserDialogue
import shutil

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

def check_destination_dir(dir):
    if os.path.isdir(dir):
        raise OSError(error_message_directory_already_exists)

def check_source_dir(dir):
    if not os.path.isdir(dir):
        raise OSError(error_message_directory_to_be_replicated_does_not_exist)
    
#TODO: Make sure that a replication of the directory structure even is possible, use os.access
def test_directory_access():
    print("method not yet defined")

def replicate_directory_structure(src, dst):
    print("\nReplicating directory structure in "+src+" recursively.")
    print("\nYou will find the root of the replicated directory structure here:\n"+dst+"\n")
    #TODO: there should be some error handling here!
    shutil.copytree(src, dst, ignore=ignored_files)

def ignored_files(adir,filenames):
    filenames = []
    for filename in os.listdir(adir):
        if os.path.isfile(adir+"/"+filename):
            filenames.append(filename)
            continue
        else:
            continue
    return filenames

def main():
    #TODO: make this a user choice!
    source_directory = "c:/test/a"
    destination_directory = "c:/test/b"
    try:
        user_dialogue = UserDialogue.UserDialogue()
        if user_dialogue.query_yes_or_no(question_replicate_directory_structure, default_answer_to_replicate_directory_structure_query):
            check_source_dir(source_directory)
            check_destination_dir(destination_directory)
            test_directory_access()
            replicate_directory_structure(source_directory, destination_directory)
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
        sys.exit(1)

if __name__ == "__main__":
    main()


