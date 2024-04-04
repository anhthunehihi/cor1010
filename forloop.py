name = ["a", "b", "c", "d", "e"]
print( name[0] )
print( name[1] )
#
name.append("thư")
print(name)

#
second_name= ["chi"] + name
print(second_name)

#
for item in name:
    print(item[0]+ " the first letter of the name!")

    