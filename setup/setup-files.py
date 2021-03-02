import os
import sys # to exit properly
import platform # to check the OS
# import subprocess # to call batch files
import shutil # to clean the destination
from zipfile import ZipFile
from lib import ask # to declutter the code
from lib import copy # to declutter the code

# define error handling
global fuckups
fuckups = 0

def stop(fuckup_count):
    print("Total fuckups so far: " + str(fuckup_count))
    print("Stopping file setup. \n")
    sys.exit()
    exit()
    quit()

# run setup
print("Your detected OS is " + platform.system())
os.chdir("..") ## go one dir level up
cwd = os.getcwd() ## save cwd to dodge path-fuckups

## generate and assign paths
if platform.system() == 'Windows':
    source = cwd + "\www\*"
    destination = "C:\MAMP\htdocs"
    pathto_mamp = "C:\MAMP\MAMP.exe"
    pathto_indexhtml = destination + "\index.html"
    pathto_php = destination + "\*.php"
    pathto_w3folder = cwd + "\www"
    pathto_w3zip = cwd + "\www.zip"

if platform.system() == 'Darwin':
    source = cwd + "/www/*"
    destination = "/Applications/MAMP/htdocs"
    pathto_mamp = "/Applications/MAMP/conf/ssl/*.*"
    pathto_indexhtml = destination + "/index.html"
    pathto_php = destination + "/*.php"
    pathto_w3folder = cwd + "/www"
    pathto_w3zip = cwd + "/www.zip"

## if you managed to run the script on linux, you probably dont need it
if platform.system() == 'Linux':
    source = cwd + "/www/*"
    destination = "/var/www/html"
    pathto_mamp = "THERE IS NO MAMP ON LINUX"
    pathto_indexhtml = destination + "/index.html"
    pathto_php = destination + "/*.php"
    pathto_w3folder = cwd + "/www"
    pathto_w3zip = cwd + "/www.zip"
    print("Have fun debugging this \n :) \n")


# define actions
def printPaths():
    print("current directory is " + cwd)
    print("source www directory is " + source)
    print("destination directory is " + destination)
    print("\n")
    if ask.yesno("Print path debug infos?", "no") == True:
        print("source is: '" + source + "'")
        print("destination is: '" + destination + "'")
        print("pathto_mamp is: '" + pathto_mamp + "'")
        print("pathto_indexhtml is: '" + pathto_indexhtml + "'")
        print("pathto_php is: '" + pathto_php + "'")
        print("pathto_w3folder is: '" + pathto_w3folder + "'")
        print("pathto_w3zip is: '" + pathto_w3zip + "'")

## test if some dirs and files exists
def checkDir():
    fine = 1
    print("Testing Directories...")
    if os.path.isfile(pathto_mamp): print("Check: MAMP seems to be installed")
    else: 
        if platform.system() == 'Linux': 
            print(":) \n")
        else:
            print("Error: Install MAMP.")
            fine -1
            fuckups +1

    if os.path.isfile(pathto_indexhtml): print("Check: htdocs folder looks good")
    else: 
        print("Note: Original MAMP files are (partially) removed.")
        fine -1
        fuckups +1

    ### this one is fucked up
    if os.path.isfile(pathto_php): print("Check: htdocs folder seems otherwise clean")
    else: 
        print("Note: There are some php files, which indicate an existing CMS install. \n" 
        + "You should clean up the folder.")
        fine -1
        fuckups +1
    # for File in os.listdir(destination):
    # if File.endswith(".php"):
    #     print("Note: There are some php files, which indicate an existing CMS install. \n" 
    #     + "You should clean up the folder.")
    #     fine -1
    #     fuckups +1
    # else:
    #     print("Check: htdocs folder seems otherwise clean")
    
    if os.path.exists(destination):
        print("\n")
        if ask.yesno("Do you want to clean it now?") == True:
            shutil.rmtree(destination)
            print("Deleted everything in htdocs.")
            print("Moving on then \n")
        else: 
            print("Moving on then \n")

    return fine

# def setupDir(destination):
#     print("Setting up Directorys...")
#     subprocess.call([r'setup-dir.bat'])

def unpackW3dir(pathto_w3folder, pathto_w3zip):
    if os.path.isdir(pathto_w3folder): print("Check: 'www' folder exists already")
    # to-do: folder can exist, but be empthy.

    else:
        print("Error: 'www' folder not found. Attemting to create it...")

        if os.path.isfile(pathto_w3zip): 
            print("Unpacking files. Thing might take long, DO NOT QUIT!")
            with ZipFile(pathto_w3zip, 'r') as zipObj:
                # Extract all the contents of zip file in different directory
                zipObj.extractall(pathto_w3folder)
                print("\n 'www.zip' extracted. Moving on... \n")
        else:
            print("'www.zip' not found.")
            stop(fuckups+1)

def copyFiles(from_path, to_path):    
    print("Starting copytree...")
    if platform.system() == 'Windows':
        copy.win32_shell(from_path, to_path)
    if platform.system() == 'Darwin':
        copy.darwin_shell(from_path, to_path)
    if platform.system() == 'Linux':
        copy.linux(from_path, to_path)

    print("Copy filetree should be done now")



# run actions
## check paths
printPaths()

if ask.yesno("Are those correct?") == True:
    if checkDir() < 1:
        print("Pathcheck failed.")
        stop(fuckups+1)

else:
    print("Well then modify the paths in './setup/setup-files.py'. \n")
    stop(fuckups+1)

## do the actual work
unpackW3dir(pathto_w3folder, pathto_w3zip)
copyFiles(source, destination)

## guess what this will do
exit()