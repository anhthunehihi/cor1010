import numpy as np 
print ("my numpy version:", np.__version__)

#print 1 million numbers from 1-20:
randomList= []
for i in range (100):
     n= np.random.randint(1,20)
     randomList.append(n)


print ("randomList:", randomList)



#nrandom = 19 then count=count+1
count = 0 
for number in randomList:
    print(number)
    if number == 19:
         count +=1


print("finish")
print("the list contain", count, "19")

#print(f"the list contain {count} 19s.")
