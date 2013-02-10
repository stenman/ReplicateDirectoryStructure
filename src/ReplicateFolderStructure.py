'''
Created on 3 feb 2013

@author: Gildur
'''
#coding=UTF-8
import os
import sys
import UserDialogue
import Replicator
import ReplicatorConfig

print (os.getcwd())

#TODO: make this directory and location a user choice
source_directory = "c:/test/a"
destination_directory = "c:/test/b"

def main():
    try:
        replicator = Replicator.Replicator()
        user_dialogue = UserDialogue.UserDialogue()
        if user_dialogue.query_yes_or_no(ReplicatorConfig.question_replicate_directory_structure, ReplicatorConfig.default_answer_to_replicate_directory_structure_query):
            replicator.replicate(source_directory, destination_directory)
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


