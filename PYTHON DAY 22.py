#!/usr/bin/env python
# coding: utf-8

# ### CONTROL FLOW STATEMENTS
# 

# 

# ### if condition
# 
#   

# In[ ]:


x=10
if(x<15):
    print("the number is less than 15")


# In[ ]:





# In[ ]:


x=10
if(x>15):
    print("x is greater than 10")


# In[ ]:


x=10
if(x<15):
    print("x is lesser vthan 15")
    


# ### example 3

# 
# 

# In[ ]:


x=10
if(x>15):
   print("HELLO GOODMORNING")
else:
   print("HELLO GOOD AFTERNOON")


# ### example 4
# #### x and  y is the input and we have to find out the larger number between two numbers

# In[ ]:


x=30
y=20
if(x>y):
    print("x is greater than y")
else:
    print("y is greater than x")


# #  example 5
# ### need 2 numbers as input andif tboth the numbers are same then the output must be square of 1st number if not the output must be the multiplicationof both the numbers 

# In[ ]:


x=15
y=20
if(x==y):
    print(x*x)
else:
    print(x*y)


# # example 6
# ### only one number as input and we are looking for whether the number is  zero,positive,negetive

# In[ ]:


x=0
if(x<0):
    print("It is negetive")
elif(x>0):
    print("it is positive")
elif(x==0):
    print("it is Zero")


# # Loop Statements
# ## while(condition):
# ##       statements
# ##        inc/dec
# #### the loopiwill get executed as long as the condition returns true and the condition will terminate if the conditionsi false
# 

# In[ ]:


n=1
while(n<=10):
    print(n)
    n=n+1


# ## example 2
# ### print the numbers from10 to 1
# 

# In[ ]:


n=10
while(n>=1):
    print(n)
    n=n-1


# #  example 3
# ## print the numbers from-22 to-45

# In[ ]:


n=-22
while(n>=-45):
    print(n)
    n=n-1


# # Example 4
# ### print the even numbers between 1 to 100

# In[3]:


a=1
b=100
sum=0
while(a!=b):
    if(a%2==0):
        sum=sum+a
    a=a+1
print(sum)
        


# # example 5
# ## extract the digits of the number from the right side direction
# 

# In[23]:


x=123
y=0

while(x!=0):
    y=x%10
    sum=(sum*10)+y
    x=x//10
print(sum)
    


# # example 6
# 

# In[1]:


x=14534
y=0
z=0
while(x>10):
    y=x%10
    if(y%2==0):
        z=z+y
    x=x//10
print(z)


# # example 7
# ### respective name of digit

# In[ ]:





# In[8]:


x=123
y=0
sum=0
while(x!=0):
    y=x%10
    if(y==0):
        print("zero ",end="")
    elif(y==1):
        print("one ",end="")
    elif(y==2):
        print("two ",end="")
    elif(y==3):
        print("three ",end="")
    elif(y==4):
        print("four ",end="")
    elif(y==5):
        print("five ",end="")
    elif(y==6):
        print("six ",end="")
    elif(y==7):
        print("seven ",end="")
    elif(y==8):
        print("eight ",end="")
    elif(y==9):
        print("nine ",end="")
    x=x//10
    sum=sum*10+y
        
print(sum)        
        


# # example 8
# ### input  a number 
# ### output  how many times the first digit is repeated between the second and thirdnumber 

# In[1]:


a=6
b=60
c=65
i=b
count=0
while(i!=c):
    buffer=i
    while(i!=0):
        r=i%10
        if(r==a):
            count=count+1
        i=i//10
    i=buffer
    i=i+1
print(count)
        
    


# # functional programming in python

# ## functionalprogramming to print first nNaturalnumbers

# In[6]:


def printnaturalnumber(n):
    count=1
    while(count!=n):
        print(count,end=" ")
        count=count+1
        print(count)
print()       
    
printnaturalnumber(9)
printnaturalnumber(16)


# # example  1

# In[12]:


def findfact(n):
    fact=1
    while(n!=0):
        fact=fact*n
        n=n-1
    return fact

print(findfact(10))


# # example 3
# ### exampleto find the palindromes between two limits 

# In[5]:


def palindrome(n1,n2):
    count=0
    while(n1!=n2):
        sum=0
        buffer=n1
        while(n1!=0):
            r=n1%10
            sum=(sum*10)+r
            n1=n1//10
        if(buffer==sum):
            count=count+1
        n1=buffer
        n1=n1+1
    return count
print(palindrome(1,100))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




