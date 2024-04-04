#random_numbers!

import random
import numpy as np #pip install numpy
number = random.randint(1, 100) #lệnh ra số random
print(number)

################################

#IN RA 100 Số ngẫu nhiên 1-20
listOfRandomNumber = []  # Tạo một danh sách trống
for i in range(10):  # Lặp 10 lần
    for j in range(10):
        n = random.randint(1, 20)  # Tạo số ngẫu nhiên từ 1 đến 20
        listOfRandomNumber.append(n)  # Thêm số ngẫu nhiên vào danh sách

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




