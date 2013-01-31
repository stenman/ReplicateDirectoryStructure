#coding=UTF-8
import os
import sys
import UserDialogue

print (os.getcwd())

#TODO: L�gg dessa i en config?
error_message_directory_already_exists = "The destination directory you want to replicate to already exist!"
error_message_folder_to_be_replicated_does_not_exist = "The folder you want to replicate does not exist!"
replicateFolderStructureQuestion = "Are you sure you want to replicate the cwd structure recursively?"
defaultAnswerToReplicateFolderStructureQuery = "no"
folderToBeReplicated = "/test/FolderToBeReplicated"
defaultReplicationDestinationDirectory = "/ReplicatedFolderStructure"
defaultWindowsRootFolder = "/"

#Temporary test commit comment 1

def checkDir():
	if os.path.isdir(defaultReplicationDestinationDirectory):
		raise OSError(error_message_directory_already_exists)
	if not os.path.isdir(folderToBeReplicated):
		raise OSError(error_message_folder_to_be_replicated_does_not_exist)
	
def testDirectoryAccess():
	print("method not yet defined")

def createFolderList():
	print("method not yet defined")

def replicateFolderStructure():
	print("\nReplicating folder structure in", os.getcwd(), "recursively.")
	print("\nYou will find the root of the replicated folder structure here:\n", defaultReplicationDestinationDirectory, "\n")
	print("method not yet defined")
	
def main():
	try:
		userDialogue = UserDialogue.UserDialogue()
		if userDialogue.QueryYesNo(replicateFolderStructureQuestion, defaultAnswerToReplicateFolderStructureQuery):
			
			#Verify directory existences
			checkDir()
			
			#TODO: TESTA att en återskapning av folderstrukturen är möjlig med os.access
			testDirectoryAccess()
			
			#TODO: starta replikeringen (skapa en lista (eller n�t) �ver mappstrukturen)
			#TODO: kolla upp os.walk()!
			createFolderList()
			
			os.chdir(folderToBeReplicated)
			os.mkdir(defaultReplicationDestinationDirectory)

			#TODO: skapa replikan i defaultReplicationDestinationDirectory (anv�nd listan som skapades)
			replicateFolderStructure()
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
		#Test:
		if os.path.isdir(defaultReplicationDestinationDirectory):
			os.removedirs(defaultReplicationDestinationDirectory)
			print("Test: removed defaultReplicationDestinationDirectory")
		sys.exit(1)

if __name__ == "__main__":
	main()


