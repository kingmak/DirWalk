# note: if we need to change the value of a var outside func
# then we use the global keyword

import os, sys, platform

fileCount = 0
folderCount = 0

fileColor = ''
folderColor = ''
statColor = ''
_os = platform.platform()

if 'Linux' in _os or 'Darwin' in _os:
    fileColor = '"\033[34m'
    folderColor = '"\033[32m'
    statColor = '"\033[36m'

# too lazy to do the logic in one function
def walkOne(directory = os.getcwd()):
    global fileCount, folderCount
    dirList = os.listdir(directory)

    for path in dirList:

        joinDir = os.path.join(directory, path)

        if os.path.isfile(joinDir):
            os.system('echo ' + fileColor + '- ' + path + '"')
            fileCount += 1
            
        else:
            os.path.isdir(joinDir)
            os.system('echo ' + folderColor + '* ' + path + '"')
            folderCount += 1

        #else: print 'SOMETHING IS BROKEN, path is = ' + path

def walk(directory = os.getcwd() , spaceCount = 0):
    global fileCount, folderCount
    dirList = os.listdir(directory)

    for path in dirList:

        joinDir = os.path.join(directory, path)
        
        if os.path.isfile(joinDir):
            os.system('echo ' + fileColor + (spaceCount * ' ') + '- ' + path + '"')
            fileCount += 1
            
        else:
            os.path.isdir(joinDir)
            os.system('echo ' + folderColor + (spaceCount * ' ') + '* ' + path + '"')
            folderCount += 1
            walk(joinDir, spaceCount + 1)

args = sys.argv

if len(args) == 1:
    walk(os.getcwd())

elif len(args) == 2:
    if args[1] == "-c":
        walkOne()
    else:
        walk(args[1])

elif len(args) == 3:
    walkOne(args[1])

else:
    sys.exit('error')

os.system('echo ' + statColor + ('\n%d Files & %d Folders in total' % (fileCount, folderCount)) + '"')
