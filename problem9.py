#first_case:
for i in range(10):
    for j in range(10-i):
        print(j, end=" ")
    print()


    
#second_case:
for i in range(10):
    for j in range(i):
        print(" ", end = " ")
    for j in range(10-i):
        print (j, end=" ")
    print()