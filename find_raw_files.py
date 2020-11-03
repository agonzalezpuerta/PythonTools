# IMPORT STATEMENTS
import pathlib, os, glob, shutil

# FILE OPERATIONS
scriptName = "find_raw_files.py"

databasePath = "D:\\OneDrive\\04 Fotografias\\Otros\\RAW\\"

currentPath = __file__.replace(scriptName,'') 

outputPath = currentPath + "FoundRawFiles\\"

# CREATE LIST OF FILES TO SEARCH
listOfFilesToSearch = []
os.chdir(currentPath)
for fileToSearch in glob.glob("DSC*.JPG"):
    listOfFilesToSearch.append(fileToSearch.replace(".JPG",''))                                 # Remove .JPG extension for file search to work

# ITERATE THROUGH DATABASE OF RAW FILES
os.chdir(databasePath)
for dbFileToSearch in glob.glob("DSC*.ARW"):
    isFileInDatabase = listOfFilesToSearch.__contains__(dbFileToSearch.replace(".ARW",''))      # Remove .ARW extension for file search to work
    if isFileInDatabase:
        shutil.copyfile(src= databasePath+dbFileToSearch,dst=outputPath+dbFileToSearch)
