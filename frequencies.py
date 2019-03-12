import os
import sys

with open(sys.argv[1], 'r') as file:
    text = file.read()
    for line in text.splitlines():
        for i in range(len(line.split())):
            # print(line.split()[i])
            with open(sys.argv[2], 'r') as dictionary:
                dText = dictionary.read()
                for dLine in dText.splitlines():
                    # print(dLine.split()[0], "+++++++", dLine.split()[1])
                    if(line.split()[i] == dLine.split()[0]):
                        print(line.split()[i], "-----", dLine.split()[1])
                        break
