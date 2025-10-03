#read the file
f=open('file.txt','r')
data=f.read()
f.close()
print(data)

# for line in f:
#     print(line)


# #using with statement

# with open('','r') as file:
#     data=file.read()
#     print(data)

#read only first number of characters

# with open('file.txt','r') as file:
#     data=file.read(5)
#     print(data)


# file=open('file.txt1','w')
# file.write("Hellw eor")
# file.write("Ganesh ")
# file.close()

#code for pending file using with
with open('file.txt','w') as file:
    file.write("hello Everyone")

import os

os.remove('file.txt1')