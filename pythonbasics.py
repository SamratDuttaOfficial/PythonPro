print("Hello World")
print('another string')
a="abcd"
b='pqrs'
print(a+b)
c=15
print(str(c)+a+b)
d="""This is
a multiline
string"""
e='''This is
another multiline
string'''
print(d)
print(e)
year = 2019
text= "The curren year is ",year
print(text)
text2="The current year is {}"
print(text2.format(year))
f=20
g=70
h=30
text3="The variable1 = {} and variable2 = {} and variable3 = {}"
print(text3.format(f,g,h))
text4="The variable1 = {0} and variable2 = {1} and variable3 = {2}"
print(text4.format(f,g,h))
text5="The variable1 = {1} and variable2 = {0} and variable3 = {2}"
print(text5.format(f,g,h))
name="Samrat"
print(name[2])
print(name[-1])
print(name[2:-1])
print(name.lower())
print(name.upper())
print(len(name))
name2 = name.replace("S","b")
print(name2)
list1 = ["Apple","Banana","Mango"]
print(list1)
print("Printing the second element only:")
print(list1[1])
print("displaying all elements in the list:")
for x in list1:
    print (x)
list1[1] = "Another apple"
if "Apple" in list1:
    print("yes. Apple is in the list")
else:
    print("No. Apple is not in list")
print("displaying all elements in the list after modification:")
for x in list1:
    print (x)
    
print("Appending one element in the list:")
list1.append("Banana")
list1.insert(2,"Peach")
for x in list1:
    print (x)
    
print("Printing numbers from 0 to 4")
for y in range(5):
    print(y)
print("Printing numbers from 3 to 6")
for z in range(3,6):
    print(z)
print("Printing all odd numbers upto 20")
for i in range (1,21,2):
    print(i) #prints all odd numbers upto 20
    #The 2 in the end is the steps... so it increments 2 at a time after starting from 1

factorial = 1;
num = int(input("Enter a number: "))
for i in range (1,num+1):
    factorial = factorial*i
print("The factorial is: " + str(factorial))

#printing all odd numbers
num2 = int(input("Enter the first number: "))
num3 = int(input("Enter the second number: "))
if num2%2==1:
    start = num2
else:
    start = num2+1
for i in range (start,num3,2):
    print(i)


#PROGRAM FOR PRIME NUMBER
num1 = int(input("Enter a number: "))
num2 = int(input("Enter ending number: "))

for num in range(num1,num2+1):
    if num>1:
        for i in range (2,num):
            if (num%i)==0:
                break
        else:
                print(num)

# Program for armstrong number for 4 digits:
for num in range(num1,num2):
    sum = 0
    temp = num 
    while temp > 0:  
        digit = temp % 10  
        sum += digit ** 4  
        temp //= 10  
    if num == sum:
        print(num)
