import os

fileCount = 0
folderCount = 0

def walk(directory, spaceCount = 0):
    global fileCount, folderCount
    dirList = os.listdir(directory)
    dirList.sort()

    for path in dirList:

        joinDir = os.path.join(directory, path)
        
        if os.path.isfile(joinDir):
            print spaceCount * ' ' + '- ' + path
            fileCount += 1
            
        elif os.path.isdir(joinDir):
            print spaceCount * ' ' + '* ' + path
            folderCount += 1
            walk(joinDir, spaceCount + 1)

        else:
            print 'SOMETHING IS BROKEN, path is = ' + path

walk(os.getcwd())
print '%d Files & %d Folders' % (fileCount, folderCount)
