import random

randomList = []
for i in range(100):
    n = random.randint(1, 20)
    randomList.append(n)
print(randomList)

count = 0
for number in randomList:
    if number == 19:  # So sánh với biến number, không phải n
        count += 1

print(count, "số 19")


s = " hello anh thu."
print(s[3:])
