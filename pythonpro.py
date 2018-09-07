print "Hello World" #This is a print function

import keyword
print(keyword.kwlist) #To print the list of keywords

#Variables and Types:

myIntVar = 42 #declaring any variable
myFloatVar = 42.42
myStringVar = "Forty Two" #strings are declared inside quotations
myNumberString = "42" #python sees this as a string instead of number because of the quotation
print "Value of integer variable" + str(myIntVar) #str to print any declared variable
print "Value of float variable: " + str(myFloatVar)
print "Value of string variable: " + str(myStringVar)
print "Value of Number-String variable: " + str(myNumberString)

myListVar = [] #A list variable, declared by [], can contain any type of variable.
myListVar.append("First")
myListVar.append("Second")
myListVar.append("Third")
for Value in myListVar:
	print Value #To print the whole list. The tab (gap) before print is important.

#Basic operaters:

myExpressionValue = 5+4-3*2/7
print myExpressionValue

varRemainder = 10%3 # % sign means it shows the raminder if we devide 10 by 3
print varRemainder #Trivedy Bach Jayega

varPower = 10**2 # ** means power. So it means 10 tothe power 2.
print varPower

#Using operators with strings:
#Additional operators, '+' can be used to concatenate two or more strings.
#The multiplication, '*' operator can be used to form a repeating string sequence. 

varStringConcat = "bull" + " " + "dog"
varStringSequence = "Bark!" * 3
print "The wise old " + varStringConcat + "stoically replied, \n" + varStringSequence

# addition operator can also be used to join two or more lists.
#Multiplication operator can be used to form a repeating sequence of a list.

varList1 = [0,1]
varList2 = [2,3,4,5]
varListConcat = varList1 + varList2
varListSequence = varList1 * 3
print varListConcat
print varListSequence

#len() can be used to find the length of a string.

myString = "Elementary, my dear Watson!"
print len(myString)

#The index(0 method can be used to get the index(position) of the first occurence a character within a string.

print myString.index("d")

#count() method can be used to get the number of times a character occurs within a string.

print myString.count("a")

#By providing the start and end indexes one can easily extract a substring within a string.

print myString [3:15]

#The upper() and lower() method can be used to convert a string to all uppercase or lowercase.

print myString.upper()
print myString.lower()

#The split() method can be used to split a string by a given delimiter.

myList = myString.split(" ") #splits the sentence for all spaces.
print myList

#The startswith() and endswith() method can be used to check if a string starts/ends with the specifies string.

print myString.startswith("son!")
print myString.endswith("son!")

#Using the % operator, we can format a given set of variables together with a format string (normal text + argument specifiers).
#Argument specifiers are a set of special symbols which begin with a % sign like %s, %d etc. which indicate the type of data in the respective variable.
# %s=String %f=Floating point numbers %nf=Floating point numbers with 'n' digits to the right of the deciaml point %x/%X=Hexadecimal integers(lowercase or uppercase)

varCreature = "spider"
varLimbCount = 8
print "A %s has %d legs." %(varCreature, varLimbCount)

#Comparison operators: can be used to evaluate an expression. The result of a comparison operator is always a Boolean value, True or False.

myInt = 8
print myInt != 8 #not equals to?
print myInt ==8 #is equals to?
print myInt >7 #is greater than?

#Comparison operators can be built with the help of 'and' and 'or' Boolean operators.

varCarSpeed = 80
varCarLane = 1
if (varCarLane ==1 and varCarSpeed >60) or (varCarLane ==2 and varCarSpeed >100):
	print "Speed Violation!"
else:
	print "No speed violation"

#The 'in'operator can be used to check whether a specified object exists within an iteable object container. (eg: list)

varDesignation = "Project Manager"
if varDesignation in ["CEO", "VP", "Director"]:
	print "Access Granted."
else:
	print "You're not authorized."

#The 'is' operator can be used to check for equivalence like the '==' operator.
#Unlike the '==' operator, the 'is' operator matches the instances themselves rather than the values of the variable.

varName = "Darth Vader"
print varName is "Darth Vader"
print varName == "Darth Vader"


