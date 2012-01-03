import os
import sys

print (os.getcwd())

replicateFolderStructureQuestion = "Are you sure you want to replicate the cwd structure recursively?"
defaultAnswerToReplicateFolderStructureQuery = "no"
defaultReplicationDestinationDirectory = "/ReplicatedFolderStructure"
defaultWindowsRootFolder = "/"

def QueryYesNo(question, default="no"):
    valid = {"yes": True, "y": True, "Y":True, "YES":True, "Yes":True, 
             "no":False, "n":False, "N":False, "NO":False, "No":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("Invalid default answer: '%S'" % default)
        
    while True:
        sys.stdout.write(replicateFolderStructureQuestion + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

if QueryYesNo(replicateFolderStructureQuestion, defaultAnswerToReplicateFolderStructureQuery):
    #TODO: Kontrollera att den nya root-katalogen inte finns, 
    #TODO: om den inte redan finns - fortsätt till själva replikeringen (skapa inte mappen förrän replikeringen gick bra!)
    #TODO: om den redan finns - avsluta programmet
    os.mkdir(defaultReplicationDestinationDirectory)
    os.chdir("/test/FolderToBeReplicated") #TODO: Byt detta statement till os.chdir(defaultReplicationFolder)
    print("Replicating folder structure in ", os.getcwd, " recursively.")
    print("You will find the root of the replicated folder structure here:\n", defaultReplicationDestinationDirectory)
    #TODO: starta replikeringen (skapa en lista (eller nåt) över mappstrukturen genom att först TESTA att det ens är möjligt med os.access)
        #TODO: kolla upp os.walk()!
    #TODO: skapa replikan i defaultReplicationDestinationDirectory (använd listan som skapades)
    
     
else:
    print("Terminating program.")    



