#coding=UTF-8
import os
import sys

print (os.getcwd())

#TODO: L�gg dessa i en config?
replicateFolderStructureQuestion = "Are you sure you want to replicate the cwd structure recursively?"
defaultAnswerToReplicateFolderStructureQuery = "no"
defaultReplicationDestinationDirectory = "/ReplicatedFolderStructure"
defaultWindowsRootFolder = "/"

#Create a platform independent ClearScreen-function
if sys.platform.startswith("win"):
	def ClearScreen():
		subprocess.call(["cmd.exe", "/C", "cls"])
else:
	def ClearScreen():
		subprocess.call(["clear"])

def QueryYesNo(question, default="no"):
	ClearScreen()
	valid = {"yes": True, "y": True, "Y":True, "YES":True, "Yes":True, "no":False, "n":False, "N":False, "NO":False, "No":False}
	if default == None:
		prompt = " [y/n] "
	elif default == "yes":
		prompt = " [Y/n] "
	elif default == "no":
		prompt = " [y/N] "
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

try:
	if QueryYesNo(replicateFolderStructureQuestion, defaultAnswerToReplicateFolderStructureQuery):
        #TODO: Kontrollera att den nya root-katalogen inte finns, 
        #TODO: om den inte redan finns - forts�tt till sj�lva replikeringen (skapa inte mappen f�rr�n replikeringen gick bra!)
        #TODO: om den redan finns - avsluta programmet
		os.mkdir(defaultReplicationDestinationDirectory)
		os.chdir("/test/FolderToBeReplicated") #TODO: Byt detta statement till os.chdir(defaultReplicationFolder)
		print("Replicating folder structure in", os.getcwd(), " recursively.\n")
		print("You will find the root of the replicated folder structure here:\n", defaultReplicationDestinationDirectory)
        #TODO: starta replikeringen (skapa en lista (eller n�t) �ver mappstrukturen genom att f�rst TESTA att det ens �r m�jligt med os.access)
        #TODO: kolla upp os.walk()!
        #TODO: skapa replikan i defaultReplicationDestinationDirectory (anv�nd listan som skapades)
        
	else:
		print("Terminating program.")    

except:
	print("Something went wrong")

finally:
    #Test:
	os.removedirs(defaultReplicationDestinationDirectory)
	print("Test: removed defaultReplicationDestinationDirectory")



