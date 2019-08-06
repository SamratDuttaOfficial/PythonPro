import subprocess as sp
sp.call('cls',shell=True) #clears the screen in cmd (windows only)
t=()
print (t)
t1=('element1','element2') #this is a tuple.
print(t1)
t2='element1','element2','element3' #this is also a tuple.
print(t2)
print(t2[-1])
t3=1,2,3,4
print(2 in t3)
l1=['element 1','element 2','element 3']
t4=tuple(l1)
print(t4)
t5=1,5,6
v1,v2,v3=t5
print(v1+v2+v3)
t6=t5+(8,) #the comma indicates it's a tuple. otherwise it is not considered as a tuple.
print(t6)
T1=1,2,3,4,5,6,7,8
T2=10,11,12
T=T1[0:3]+T2+T1[3:]
print(T)
# T2[2]=6 #we can't change any element in a tuple
L=list(T)
L[3]=15
L.append(20) #changed tuple to list to perform some operations on it.
T=(L)
print(T)
numberofelements = len(T)
print(numberofelements)
countnumber=T.count(5) #counts how many times an element appears.
print(countnumber)
s1=set() #this is the set constructor. creates an empty set.
print(s1)
set1={1,2,3,4,5,6,7} #This is a set. it's unordered and all the elements must be distinct.
print(set1)
set2=set(l1)
print(set2)
for i in set2:
    print(i)
set1.add(12) #inserting a single element in the set
print(set1)
set1.update([15,20]) #inserting multiple elements in the set.
print(set1)
set1.pop() #pops a specific element, not the element in that perticular index because set is unordered.
print(set1)
set1.remove(4) #removes a specific element. removes a specific element, not the element in that perticular index because set is unordered.
print(set1)
set1.discard(2) #discards an element. remove() will throw an error message when the element which we are trying to remove is not there in the set, whereas, discard() will not intimate the absence of element which we try to remove.
print(set1)
set3={15,20,53,51,52}
SET1 = set1&set3 #intersecton of sets.
print(SET1)
SET2=set1|set3 #union of sets
print(SET2)
SET3=set1-set3 #difference between two sets.
print(SET3)
set4={15,20}
subset1=set4<=set1 #checks if the first set is a subset of the second set or not
print(subset1)
superset1= set4>=set1 #checks if the first set is a superset of the second set or not
print(superset1)

