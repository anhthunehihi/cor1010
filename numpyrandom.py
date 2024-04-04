import numpy as np

numArray = np.random.randint(0,100, size=20)
print(numArray)

#to make a group of unique number
#[ 0 67 83 80  0 53 67 33 34 93 49 81 29 29 75  3  5 56  8 79]
#unique_A = [ 0 67 83 80  0 53 67 33 34 93 49 81 29 29 75  3  5 56  8 79]

#1
unique = []
for number in numArray:
    if number in unique:
        pass #do nothing
    else:
        unique.append(number)
print("unique:", unique)

#2
uniqueList2 = []
for number in numArray:
    if number not in uniqueList2:
        uniqueList2.append(number)
print("unique:", uniqueList2)

#uniqueList3 = [ number for number in numArray if number not in uniqueList2]

myList = []
myList2= list()

uniqueSet= set()
for num in numArray:
    uniqueSet.add(num)

print(uniqueSet)
for elem in uniqueSet:
    print(elem, end=" ")
print()
