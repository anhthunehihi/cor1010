filename= "pg1342.txt"

filehandler = open(filename,"r", encoding="latin-1")

n=0
while True:
    line= filehandler.readline()
    n +=1
    print(n, line)
    if n >10:
        break


#####################
f2 = open("longstring0.py", "r")
n= 0
ulist =[]
while True:
    line = filehandler.readline()
    if not line:
        break #get out of the loop
    n +=1
    for letter in line:
        if letter not in ulist:
            ulist.append(letter)
filehandler.close() #close the file
print(n, len(ulist), ulist)





