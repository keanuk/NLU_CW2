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
    typeCounts = dict()
    with open(filename, 'r') as file:
        text = file.read()
        for line in text.splitlines():
            lineLength.append(len(line.split()))
            for word in line.split():
                types.add(word)
                tokens += 1
                if word not in typeCounts:
                    typeCounts[word] = 1
                else:
                    typeCounts[word] += 1
    
    unks = [k for k,v in typeCounts.items() if v == 1]
    unks = len(unks)

    return types, lineLength, tokens, unks     


types, lineLengths, tokens, unks = getTextData(sys.argv[1])

print("Total tokens in ", sys.argv[1], ": ", tokens)
print("Total word types in ", sys.argv[1], ": ", len(types))
print("UNK values in ", sys.argv[1], ": ", unks)

plotLengths(lineLengths)

if(len(sys.argv) == 3):
    types2, lineLengths2, tokens2, unks2 = getTextData(sys.argv[2])

    print("Total tokens in ", sys.argv[2], ": ", tokens2)
    print("Total word types in ", sys.argv[2], ": ", len(types2))
    print("UNK values in ", sys.argv[2], ": ", unks2)

    plotLengths(lineLengths2)
    plotCorrelation(lineLengths, lineLengths2)

