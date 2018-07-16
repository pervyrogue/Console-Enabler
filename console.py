#  Pervy Rogues, 2018
#
# This walks all directoriesin a folder,
# starting from where the file is located,
# looking for Renpy games and
# enables the game console.
#

import fnmatch
import os

# Starts in directory it is ran from
rootDir = '.'
numFiles = 0

# Loops through directories looking for folder called renpy.
for root, subdirs, files in os.walk(rootDir):
    for dir in subdirs:
        for file in files:
            # Find file 00console.rpy
            if fnmatch.fnmatch(file, '00console.rpy'):
                s = open(os.path.join(root, file)).read()
                # Check the file first before changing.
                if s.find('    config.console = False') != -1:
                    s = s.replace('    config.console = False', '    config.console = True')
                    f = open(os.path.join(root, file), 'w')
                    f.write(s)
                    f.close()
                    numFiles += 1
                    print(os.path.join(root, file), " was edited.")
                # File was already edited, do nothing.
                else:
                    print(os.path.join(root, file), " was already edited.")
                # Clear this directory so os.walk moves on and break from file loop.
                subdirs[:] = []
                break

if numFiles > 0:
    print(numFiles, " files were changed.")
else:
    print("No files were changed.")
