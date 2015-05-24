import os

def walk(directory = os.getcwd(), spaceCount = 0):
    dirList = os.listdir(directory)

    for path in dirList:

        joinDir = os.path.join(directory, path)
        
        if os.path.isfile(joinDir):
            print spaceCount * ' ' + '- ' + path
            
        elif os.path.isdir(joinDir):
            print spaceCount * ' ' + '* ' + path
            walk(joinDir, spaceCount + 1)

        else: # else not needed, in for debug
            print 'SOMETHING IS BROKEN, path is = ' + path
walk()
