import numpy as np
import random

numList = np.random.randint (1,100, size=200)
print(numList)

uniqueList= []

for number in numList:
    if number in uniqueList:
         pass
    else:
         uniqueList.append(number)

print(uniqueList)


uniqueList2 = []
for number in numList:
    if number not in uniqueList2:
        uniqueList2.append(number)
print("unique2:", uniqueList2)