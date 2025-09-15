# #sum of even numver between 1 to 21
# sum=0
 
# for i in range(1,21):
#     if(i%2==0):
#         print(i,end=" ")
        
#         sum+=i
    
# print("\n",sum)

# str=input("enter a string:")
# count=0

# for i in str:
#     if(i=="a" or i=="i"or i=="o" or i=="e"or i=="u"):
#         count+=1
         
# print(count)
# print(i)
#or

# str=input("Enter a string:")
# count=0
# str1=[]

# for ch in str:
#     if ch.lower() in ('a','i','e','o','u'):
#         count+=1
#         str1.append(ch)
# print("Number of vowels:", count)
# print(" :",''.join(str1))

'''
Write a Python program to print the Fibonacci series up to n terms.

1 , 1 , 2, 3, 5, 8, 13 ...

'''

n = int(input("Please enter the value of n - upto which we want the fibonacci series"))
print(n)
if (n <=0):
  print("Number entered is not correct. It should be > 0. Entered num", n)

print(1, end=",")
if(n==1):
  pass
else :
  print(1, end=",")
  if(n==2):
    pass
  else:
    #print the remaining part of the series
    prev = 1
    prev_prev=1
    for num in range(3, n+1):
      print(prev+prev_prev, end=",")
      prev, prev_prev = prev+prev_prev , prev
