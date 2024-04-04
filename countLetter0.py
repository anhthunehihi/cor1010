filename = "pg1342.txt"
# 1. make a list of unique letters

unqLetters = set()
with open(filename, "r", encoding='latin-1') as filehandler:
    n = 0
    while True:
        line = filehandler.readline()
        if not line:
            break
        n += 1
        for letter in line:
            unqLetters.add(letter)
        #print(n, line) 
        #if n > 3:
            #break
    #
#
print(f"Total {n} lines from {filename}: {len(unqLetters)} letters in the set {unqLetters}")

# 2. count each letter, going through the txt file from the beginning        

#2.1 initialize the dictionary
counts = {}
for letter in unqLetters:
    counts[letter] = 0
print(counts)

with open(filename, "r", encoding='latin-1') as file:
    n=0
    while True:
        line = file.read()
        if not line:
            break
        n += 1

        for letter in line:
            counts[letter] += 1 

        if n == 1:
            print(line)
            break

        
print(counts)
#
for key, value in counts.items():
    if value > 0:
        print(key, ":", value)