
#count the number of word and space
import numpy as np

longString = "Oh no, my regret and compassion are all done away by you so full of both."

print( len(longString) )


longString = longString.lower()
unique_letters = set(longString)
uniqueLetterList = list(unique_letters)
print("Unique letters:", uniqueLetterList)


#make a list of unique letter in longString
uniqueLetter = []
for letter in longString:
    if letter not in uniqueLetter:
        uniqueLetter.append(letter)
        
print("unique letter = ", len(uniqueLetter), uniqueLetter)

#######
print(uniqueLetter[0])
letterList = []
for elem in uniqueLetter:
    letterList. append(elem)


####
letterList2 = list (uniqueLetter)
print(uniqueLetter)
print(letterList2)

#####
