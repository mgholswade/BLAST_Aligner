##This contains all of the basic functions used in the main program for blast alignment.
import numpy as np
import pandas as pd
from os.path import exists
import itertools

#Basic steps for BLAST Alignment
#Start with query sequence (q) and heuristics:
#   scoring matrix (M)
#   word length (w)
#   word score threshold (t)
#   segment score threshold (s)

#Steps
#1. Determine words of length w in the sequence q
#2. Compare all words to scoring matrix, return all that score at least t
#2. Scan database for matches from list generated by 2
#3. Extend matches to find high scoring alignments
#4. Return all alignments scoring over S



def word_list(w,q):
    word_list = []

    for i in range(0,len(q)-w):
        word_list.append(q[i:(i+w)])

    return word_list


#Function to import chosen scoring matrix 
def score_choose():
    matrixName = input('Enter Scoring Matrix: ')
    path = '../data/{}.csv'.format(matrixName)
    
    if exists(path):
        matrix = pd.read_csv(path)
    else:
        print('ERROR: Not a valid scoring matrix.')
        matrix = score_choose()

    return matrix

#Function to score a word using the chosen scoring matrix
def word_score(word,matrix,T):

    wordList = []
    for i in range(0,len(word)):
        wordList.append(word[i])
    
    #Pull the first column of the scoring matrix to determine strings
    wordMat = pd.DataFrame()
    for ch in wordList:
         #Pull each column from the scoring matrix, add to new matrix
        wordMat = wordMat.append(matrix[ch])
    
    #Add up each combination of row entries of the scoring matrix, if it is over T then add to wordList


    for t in itertools.product(*iterables):
        print t
    return wordMat #FIXME# Temp variable for testing purposes
    #return wordList
