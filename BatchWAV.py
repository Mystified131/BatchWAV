#This code imports the necessary modules

import os
import re
import collections
import operator
import librosa
 
for subdir, dirs, files in os.walk('C:\\Users\\mysti\\thomasoriginalcode\\Git\\BatchWAV'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".wav")) :
            instr = str(file)
            outstr = "RB" + str(file)
            pubstr = instr + ": " + outstr
            print(pubstr)
            y, s = librosa.load(instr, sr = 44100)
            librosa.output.write_wav(outstr, y, s)


print("")

print("The designated files have been converted. Thank you.")

print("")