'''
Created on 3 feb 2013

@author: Gildur
'''
#coding=UTF-8
import sys
import argparse
import logging
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
            replicator.display_successful_replication_message(destination_directory)
        else:
            print("\nTerminating program.")
            sys.exit(0)
    except OSError as error:
        if(str(error) == ReplicatorConfig.error_message_directory_already_exists or str(error) == ReplicatorConfig.error_message_directory_to_be_replicated_does_not_exist):
            print("\nOSError: {0}".format(str(error)))
        else:
            logging.warning("\nOSError: {0}".format(str(error)))
            replicator.display_successful_replication_message(destination_directory)
            print("There were OSErrors while replicating the directory structure. Probably due to lack of access/permission rights to some of the folders.\nCheck errors.log for details.")
        sys.exit(1)
    except Exception as error:
        print("\nAn unexpected exception was encountered: {0}".format(str(error)))
        sys.exit(1)
    finally:
        sys.exit(1)

if __name__ == "__main__":
    logging.basicConfig(filename='errors.log',level=logging.WARNING)
    sys.exit(main(sys.argv[1:]))
    