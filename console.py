#  James D Isaacks, 2018
#
# This walks all directories in a folder looking
# for Renpy games and enables the game console.
#
#
#

import mmap
import os

# Starts in directory it is ran from
rootDir = '.'
numFiles = 0

# Loops through directories looking for folder called renpy.
for root, dirs, files in os.walk(rootDir):
    for dir in dirs:
        for file in files:
            # Find file console.rpy with a path check to ensure proper file.
            if os.path.isfile('*/renpy/common/console.rpy'):
                s = mmap.mmap("console.rpy").read()
                # Check the file first before changing.
                if s.find('config.console = False') != -1:
                    s = s.replace('config.console = False', 'config.console = True')
                    f = open("console.rpy". 'w')
                    f.write(s)
                    f.close()
                    numFiles += 1
                    print os.path.join(root, file) " was edited."
                # File was already edited, do nothing.
                else:
                    print os.path.join(root, file) " was already edited."

if numFiles > 0:
    print numFiles " were changed."
else:
    print "No files were changed."
