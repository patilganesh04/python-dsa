# #arithmetic

# num1=10
# num2=20
# print(num1+num2) #=>30

# print(num1-num2) #=>-10

# print(num1*num2) #=>200

# print(num2/num1) #=>2.0

# print(num2//num1) #=>2.0

# nan=float('nan')
# print(nan)

# pos_inf=float('inf')
# print(pos_inf)

# neg_inf=float('-inf')
# print(neg_inf)

# #comparison oprators

# print(num1==num2)
# print(num1!=num2)
# print(num1<=num2)


# #assignment oprators

# name="ganesh"
# x=5

# x=x+5
# print(x)
# x+=5
# print(x)
# x-=3
# print(x)

# #logical

# print(True and True)
# print(True and False)
# print(False and False)

# print(True or True)
# print(False or False)
# print(True or False)

# print(16^2)

a = float("-inf")
b = float("inf")
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# a=144
# print(a>>1,a>>2,a>>3,a>>4,a>>5)

# a=9
# print(a<<1,a<<2,a<<3,a<<4,a<<5)
a,b=14,6
print((a>>1)+3*(b)-36/12)


f=[]
n=int(input("enter a number"))
for i in range(n):
    val=int(input("enter elment:"))
    f.append(val)
print(f)
print(max(f))
print(min(f))
f.sort()
print(f)
