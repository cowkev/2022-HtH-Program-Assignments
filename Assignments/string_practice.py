#STring Ex Using Operators
fname= "Kevin "
mname= "Andrew "
lname= "Mata"

myname= fname + mname + lname


print ("My first name is: " + str(fname))
print ("My middle name is: " + str(mname))
print ("My last name is: " + str(lname))

print ("Hello my full name is " + (myname))

#String Ex Using str.join()
listOfStrings = [fname, lname]
finalstring = "".join(listOfStrings)
print(" The appended string is: "+ finalstring)

#STring Ex USing f-strings
fstring = f"{fname}{lname}"
print ("The append sting is: " + fstring)

#SLicing string examples
string1 = "This is my string"
print (string1[0:4])
print (string1[5:7])
print (string1 [8:10])
print (string1 [11:len(string1)])

#list exmaples
ex = [1,6,3,9,5,4,7,2,8,0]
ex.remove (1)
ex.remove (3)
ex.remove (5)
ex.remove (7)
ex.remove (8)
print (ex)

even = [1,3, 5]
even.pop (1)
print (even)