import os
import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


def plotCorrelation(lengths1, lengths2):
    plt.scatter(lengths1, lengths2)
    plt.xlabel('English')
    plt.ylabel('Japanese')  
    plt.show()

def plotLengths(lengths):
    axis = []
    for i in range(len(lengths)):
        axis.append(i)

    plt.scatter(axis, lengths)
    plt.show()


def getTextData(filename):
    types = set()
    lineLength = []
    tokens = 0
    with open(filename, 'r') as file:
        text = file.read()
        for line in text.splitlines():
            lineLength.append(len(line.split()))
            for word in line.split():
                types.add(word)
                tokens += 1  
    return types, lineLength, tokens     


types, lineLengths, tokens = getTextData(sys.argv[1])

print("Total tokens in ", sys.argv[1], ": ", tokens)
print("Total word types in ", sys.argv[1], ": ", len(types))
print("UNK values in ", sys.argv[1], ": ")

plotLengths(lineLengths)

if(len(sys.argv) == 3):
    types2, lineLengths2, tokens2 = getTextData(sys.argv[2])

    print("Total tokens in ", sys.argv[2], ": ", tokens)
    print("Total word types in ", sys.argv[2], ": ", len(types))
    print("UNK values in ", sys.argv[2], ": ")

    plotLengths(lineLengths2)
    plotCorrelation(lineLengths, lineLengths2)

