 #list

stud=["Ganesh","chndra","ravi","kiran"]

print(stud)
print(type(stud))

list3=list("ganesh")
print(list3)

list4=list((3,4,"Ganesh"))
print(list4)

l1=[3,4,5,9,1,6,7,8]
l1.append(32)
print(l1)
 
li=[1,2]
l2=["Ganesh","mani"]
li.extend(l2)
print(li)

li.insert(1,3)
print(li)

li1=[5,4,3,8,6,1]
# li1.remove(1)
# li1.pop(1)  
print(li1)

li1[1:4]=19,20
print(li1)