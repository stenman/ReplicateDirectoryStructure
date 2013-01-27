#coding=UTF-8
import os
import sys

print (os.getcwd())

#TODO: L�gg dessa i en config?
replicateFolderStructureQuestion = "Are you sure you want to replicate the cwd structure recursively?"
defaultAnswerToReplicateFolderStructureQuery = "no"
folderToBeReplicated = "/test/FolderToBeReplicated"
defaultReplicationDestinationDirectory = "/ReplicatedFolderStructure"
defaultWindowsRootFolder = "/"

#Temporary test commit comment 1

#Create a platform independent ClearScreen-function
#TODO: Only for test (unless running program from shell)
if sys.platform.startswith("win"):
	def ClearScreen():
		# Use only if not running from shell
		os.system("cls")
else:
	def ClearScreen():
		os.system("clear")

def QueryYesNo(question, default="no"):
	ClearScreen()
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


def main():
	try:
		if QueryYesNo(replicateFolderStructureQuestion, defaultAnswerToReplicateFolderStructureQuery):
			if os.path.isdir(defaultReplicationDestinationDirectory):
				raise OSError("The destination directory you want to replicate to already exist!")
			if not os.path.isdir(folderToBeReplicated):
				raise OSError("The folder you want to replicate does not exist!")
			#TODO: starta replikeringen (skapa en lista (eller n�t) �ver mappstrukturen genom att f�rst TESTA att det ens �r m�jligt med os.access)
			#TODO: kolla upp os.walk()!
			
			os.chdir(folderToBeReplicated)
			
			os.mkdir(defaultReplicationDestinationDirectory)
			print("\nReplicating folder structure in", os.getcwd(), "recursively.")
			print("\nYou will find the root of the replicated folder structure here:\n", defaultReplicationDestinationDirectory, "\n")
			#TODO: skapa replikan i defaultReplicationDestinationDirectory (anv�nd listan som skapades)
			
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


