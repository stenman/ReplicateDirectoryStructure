'''
Created on 3 feb 2013

@author: Gildur
'''
#coding=UTF-8
import os
import sys
import argparse
import UserDialogue
import Replicator
import ReplicatorConfig

def main(argv):
    parser = argparse.ArgumentParser(description=ReplicatorConfig.program_description)
    parser.add_argument("src", help="Source Directory")
    parser.add_argument("dst", help="Destination Directory")
    args = parser.parse_args(argv)
    replicate_directories(args.src, args.dst)

def replicate_directories(source_directory, destination_directory):
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
    sys.exit(main(sys.argv[1:]))


