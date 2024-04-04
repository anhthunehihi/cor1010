import numpy as np
import matplotlib.pyplot as plt



#function

def add(a, b, c):
    "a, b, c are all numbers: int, float"
    result= a +b + c
    return result

i = 1
j = 2
k = 3

z= add(i, j, k)

print(i, j, k, "=", z)


###### 



###c1

#begin function
def getUniqueLetters(string):
    "string: a str type input"
    listOfUniqueLetters = []
    for letter in string:

        if letter not in listOfUniqueLetters:
            listOfUniqueLetters.append(letter)

    return listOfUniqueLetters
#end function
 
myString = "toi la anh thu"
uniqueLtter = getUniqueLetters(myString)
print(uniqueLtter)



####c2
myString2= "spring is good"
uniqueLtter2 = getUniqueLetters(myString2)
print (uniqueLtter2)


###c3
uniqueLtter3= sorted (uniqueLtter2)
print (uniqueLtter3)


#### pip install matplotlib (1st step)
### import numpy as np (2nd step)
### import matplotlib.pyplot as plt (3rd step)

x = [1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y)
plt.show()



