d = {"a": 0, "b": 1, "c": 2}
keyvalue = dict()
print(d)

for key, value in d.items():
    #print(key,value)
    print (f"{key} : {value}")
print (d['a'], d['c'])

d['a'] +=10
d['c'] +=20
print (d['a'], d['c'])

kv = {10: 0, 20: 0, 30:"hello"}
print ("key", kv.key())
print ("value:", kv.value())

string= "this is a string"


def getUniqueLetter(filename):
uniqueLetter = set()
filename= "pg1342.txt"
with open(filename, "r") as filehandler:
    n=0
    while True:
        line = filehandler.readline()
        if not line:
            break
        n += 1
        for letter in line:
            uniqueLetter.add(letter)
        
return uniqueLetter
