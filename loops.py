n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    for j in range(1,i+1):
        print("*",end="")

    print()

fruits=["Ganesh","ravi","Kiran","akash"]
for i in range(len(fruits)):
    print(fruits[i])

name="Ganesh" 
for ch in name:
    print(ch,end=" ")
print()

for i in range(12,0,-3):
    print(i,end=",")

fruits=["Ganesh","ravi","Kiran","akash"]
for i in range(len(fruits)):
    print(fruits[i])

print("hell{0[0]}{0[1]}".format(fruits))
#output:

x=9
y=41
print(x or y,x and y)