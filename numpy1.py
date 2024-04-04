#random_numbers!

import random
import numpy as np #pip install numpy
number = random.randint(1, 100) #lệnh ra số random
print(number)

################################

listOfRandomNumber = [ ] #tạo tập trống
for i in range(10): #tạo vòng lặp = 10 lần
     n = random.randint(1, 20) # ra số ngẫu nhiên từ 1-20 => 10 số
     listOfRandomNumber.append #add "n" vào tập trống

###################################    
#sum
     
total = 0 # lisOfRandomNumber [0] + listOfRandomNumber
for number in listOfRandomNumber:
     total = total + number
print("total:", total)

print(listOfRandomNumber)

#
totalsum = sum(listOfRandomNumber)
print("total:", total, totalsum)




