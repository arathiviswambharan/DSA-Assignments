#!/usr/bin/env python
# coding: utf-8

# In[5]:


# question 1
   
from math import pi

r = float(input("Input the radius of the circle : "))
area = pi * r ** 2
print("The area of the circle with radius " + str(r) + " is: " + str(area))


# In[1]:


# question 2

Name = input("Enter the name")
print("Name :",Name)
Rollno = int(input("Enter the roll number"))
print("Roll no :", Rollno)
mark = int(input("Enter the mark"))
print("Marks :",mark)


# In[3]:


# question 3

list1 = [12,3,47,10]
list1.sort()
print("Largest number is:", list1[-1])


# In[4]:


# question 5

list = [10,20,33,46,55]

for num in list:
    
      if num % 5 == 0:
           print(num)


# In[4]:


# question 6

num = 10
i = 2
while i<=int(num/2):

    if num % i ==0:
        print(num , " is not a prime number")
        break
    else:
        print(num,"is a prime number")
        break


# In[5]:


# question 7

list = [10,40,30,70]
newlist=[]
for i in range(1,len(list)+1):
    newlist.append(list[-i])
print(newlist)


# In[6]:


# question 8

i = 1
while i<=4:
    j = 1
    while j<=i:
        print("*",end=' ')
        j = j+1
    print()
    i = i+1


# In[9]:


# question 9

def maximum(a, b, c): 
 
    if (a >= b) and (a >= c): 
        largest = a 
 
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
         
    return largest 
 
a = 34
b = 12
c = 7
print(maximum(a, b, c)) 


# In[10]:


# question 10

rows = 5

for i in range(0, rows):
    for j in range(0, i + 1):
        print('*', end = ' ')
    print()

for i in range(rows - 1, -1, -1):
    for j in range(0, i):
        print('*', end = ' ')
    print()


# In[ ]:


# Assignment set 2


# In[9]:


# question 2

def maximum(a, b, c): 
 
    if (a >= b) and (a >= c): 
        largest = a 
 
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
         
    return largest 
 
a = 34
b = 12
c = 7
print(maximum(a, b, c)) 


# In[2]:


# question 9

celsius = 5
fahrenheit = (celsius * 1.8) + 32
print(str(celsius )+ " degree Celsius is equal to " + str(fahrenheit )+ " degree Fahrenheit.")


# In[3]:


fahrenheit = 41
celsius = (fahrenheit-32)/1.8
print(str(fahrenheit) + "degree fahrenheit is equal to " + str(celsius)+" degree fahrenheit ")


# In[10]:


# question 8


i = 1
while i <= 15:
    if i%2==0:
        print(i,"-even")
       
    else:
            print(i,"- odd")
        
    
    i = i+1


# In[16]:


# question 7


list = [2,1,3,1]
print("The new list is: "+ str(list))
res = sum(map(lambda i: i * i, list))

print("The sum of squares of list is : " + str(res))


# In[17]:


# question 6

def most_frequent(List):
    return max(set(List), key = List.count)

List = [2,3,4,2,5,2]
print(most_frequent(List))



# In[25]:


# question 5
i = 1
while i <= 10:
    if i%2==0:
        print("Fizz")
    elif i%5==0 :
            print("Buzz")
   # elif i%=2==0 and i%=5==o:
           # print("FizzBuzz")

    else:
            print(" ")
        
    
    i = i+1


# In[29]:


# QUESTION 4


def sum_of_cubes(n):
    
    n -= 1
    
    total = 0
    
    while n > 0:
        
        total += n * n * n
        
        n -= 1
    
    
    return total


print("Sum of cubes smaller than the specified number: ", sum_of_cubes(4))


# 

# In[ ]:




