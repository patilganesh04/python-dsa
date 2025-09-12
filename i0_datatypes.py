#Assign 10 to variable length and 20 to variable breadth-
lenth = 10
breadth = 20

#- Assign the average of values of variables length and breadth to a variable sum-
sum=(lenth+breadth)/2

#<- Assign a list containing strings 'Paper', 'Gel Pen', and 'Eraser' to a variable stationery-
name = ["Mohan", "dash", "karam", "chandra","gandhi","Bapu"]
name.insert(0,"freedom_fighter")
print(name)


#name = ["Mohan", "dash", "karam", "chandra","gandhi","Bapu"]
#do the following operations in this list;
''':- add an element "freedom_fighter" in this list at the 0th index-
&- find the output of the following ,and explain how?'''
length1=len((name[-len(name)+1:-1:2]))
length2=len((name[-len(name)+1:-1]))
print(length1+length2)
name = ["Mohan", "dash", "karam", "chandra","gandhi","Bapu"]
name.extend(["NetaJi","Bose"])
print(name) #output:['Mohan', 'dash', 'karam', 'chandra', 'gandhi', 'Bapu', 'NetaJi', 'Bose']

#- what will be the value of temp:
 
temp=name[-1]
name[-1]=name[0]
name[0]=temp
print(name) #output:['Bose', 'dash', 'karam', 'chandra', 'gandhi', 'Bapu', 'NetaJi', 'Mohan']


# Find the output of the following.
animal = ['Human','cat','mat','cat','rat','Human', 'Lion']
print(animal.count('Human')) #output:2
print(animal.index('rat'))#output:4
print(len(animal))#output:7


tuple1=(10,20,"Apple",3.4,'a',["master","ji"],("sita","geeta",22),[{"roll_no":1},{"name":"Navneet"}])
print(len(tuple1)) #output:8
print(tuple1[-1][-1]["name"]) #output:Naveet
print(tuple1[-1][0]["roll_no"]) #output:1
print(tuple1[-3][1]) #output:ji
print(tuple1[-2][2]) #output:22