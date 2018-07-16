#  James D Isaacks, 2018
#
# This walks all directories in a folder looking
# for Renpy games and enables the game console.
#
#
#

import fnmatch
import mmap
import os

# Starts in directory it is ran from
rootDir = '.'
numFiles = 0

# Loops through directories looking for folder called renpy.
for root, subdirs, files in os.walk(rootDir):
    for dir in subdirs:
        for file in files:
            if fnmatch.fnmatch(file, '00console.rpy'):
            # Find file console.rpy with a path check to ensure proper file.
#            if file == 'console.rpy':
                print("Found a file.")
                s = open(os.path.join(root, file)).read()
                # Check the file first before changing.
                if s.find('    config.console = False') != -1:
                    s = s.replace('    config.console = False', '    config.console = True')
                    f = open(os.path.join(root, file), 'w')
                    f.write(s)
                    f.close()
                    numFiles += 1
                    print(os.path.join(root, file), " was edited.")
                    break
                # File was already edited, do nothing.
                else:
                    print(os.path.join(root, file), " was already edited.")

if numFiles > 0:
    print(numFiles, " were changed.")
else:
    print("No files were changed.")
