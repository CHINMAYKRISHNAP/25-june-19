#!/usr/bin/env python
# coding: utf-8

# # example1 
# ## print sumof even numbers 

# In[3]:


def even(n):
    count=0
    sum=0
    while(count!=n):
        if(count%2==0):
            sum=sum+count
        count=count+1
    return sum
print(even(20))


# # example 2
# ## print factors ofnumbers 

# 

# In[10]:


def factor(n):
    count=1
    while(count!=n):
        if(n%count==0):
            print(count,end=" ")
        count=count+1
    return count
print(factor(10))
        


# # lists 
# 

# ## example 1

# In[12]:


list1=[1,2,3,4,5]
print(list1)
print(list1[0])


# # example 2
# 
# 

# In[14]:


list1=["chinmay","rohan","charith"]
for x in list1:
    print(x)


# # example3

# In[25]:


list1=[1,2,3,4,5,6,7,8,9,10]
for x in list1:
         print(x,end="")
print()
print(list1[5])
print(list1[2:5])
print(list1[0:3])
print(list1[:3])
print(list1[3:7])


# #  example 4
# 

# 

# In[31]:


list1=[1,2,3,4,5,6,7,8,9,10]
for x in list1:
         print(x,end=" ")
print()
print(list1[1:-1])
print(list1[::3])
print(list1[::2])


# # example 5\
# 

# In[33]:


list1=["chinmay","rohan","charithg","manish"]
print(list1)
list1[2]=15
print(list1)
del list1[3]
print(list1)


# # example 6

# In[42]:


list1=["chinmay","rohan","charithg","manish",4,5,4,5,4,5,4]
print(list1)
list1[2]=15
print(list1)
del list1[3]
print(list1)
list1.append(16)
print(list1)
print(list1.count(5))
print(list1.count(4))


# # list methods

# In[46]:


list1=["gitam","chinmay","rohan","charith",1,2,3,4,1,2,3,4]
print(list1)
print(list1.index("chinmay"))
list1.index("chinmay")
list1.index(2)


# # insert(index,obj)

# In[48]:


list1=["gitam","chinmay","rohan","charith",1,2,3,4,1,2,3,4]
print(list1)
list1.index("chinmay")
list1.index(2)
list1.insert(4,20)
print(list1)


# # remove(obj)
# 

# In[51]:


list1=["gitam","chinmay","rohan","charith",1,2,3,4,1,2,3,4]
print(list1)
list1.remove("chinmay")
print(list1)


# # reverse
# 
# 

# In[52]:


list1=["gitam","chinmay","rohan","charith",1,2,3,4,1,2,3,4]
print(list1)
list1.remove("chinmay")
print(list1)
list1.reverse()
print(list1)


# # DATA STRUCTURS

# #### SEARCHINMG THE DATA
# #### STORE THE DATA
# #### SORT THE DATA
# #### BINARY SEARCH
# #### LINEAR SEARCH
# #### SAVE THE DATA 

# # LINEARSEARCH
# 

# In[ ]:


## 


# In[ ]:





# In[62]:


def linearsearch(a,taritem):
    flag=0
    for i in range(len(a)):
        if a[i] == taritem:
            flag=1
            break
    if(flag!=0):
        print("target itemisfound")
    else:
        print("atrget iteam is not found")
        
a=[16,43,5,6,7,8,9,9,877,6,5]
linearsearch(a,6)


# ## linearsearchduplicate

# In[64]:


def linearsearchduplicate(a,taritem):
    flag=0
    for i in range(len(a)):
        if a[i] ==taritem:
            flag=flag+1
    print(flag)
    
a=[1,2,3,4,5,6,7,8,9,8,7]
linearsearchduplicate(a,9)


# # linear search example
# 

# In[67]:


def linearexample(a,taritem):
    flag=0
    for i in range(len(a)):
        if a[i]==taritem:
            
            flag=flag+1
            print(i)
 
    
a=[1,3,4,5,6,7,6,5,4,5,4,6,5]
linearexample(a,5)


# # example 2
# ### sequence of charecters

# In[82]:


def seqchar(a,taritem):
    flag=0
    c=0
    for i in range(len(a)): 
        if a[i]==taritem:
            flag=flag+1
    while(c<=i):
        print("!",end=" ")
        c=c+1

        
a=[1,2,3,2,3,2,5,3,4]
seqchar(a,2)


# # example 3
# ### multiples of 3 and 5

# In[87]:


def linearmultiple(a):
    flag=0
    sum=0
    for i in range(len(a)):
        if((a[i]%3==0)and(a[i]%5==0)):
            sum=sum+a[i]
            flag=flag+1
    print(sum)

a=[1,30,45,25,61]
linearmultiple(a)


# # example 4
# ### linearsearch formatted output

# In[6]:


def linearformat(a):
    i=0
    while i!=len(a):
            if a[i]==a[0] or a[i]==a[len(a)-1]:
                print(a[i],end=" ")
            else:
                print ((a[i-1]*a[i+1]),end=" ")
            i=i+1
            
            
a=[1,2,3,4,5]
linearformat(a)


# # example 5

# In[12]:


def linearsearch(a):
    for i in range(len(a)):
        if(a[i-1]%2==0)and(a[i+1]%2==0):
            print(a[i],end=" ")
            i=i+1
        
a=[1,2,3,4,5,6,7,8,9,10]
linearsearch(a)


# In[19]:


def list(n):
    list=[]
    while n!=0:
        r=n%10
        list.append(r)
        n=n//10
        
    list.reverse()
    print(list)
    
    
n=int(input("enter a number"))        
list(n)

        


# # example 7
# ### list to number conversion

# In[20]:


def even(a):
    i=0
    for i in range(len(a)):
        if a[i]%2==0:
            print(a[i],end=" ")
          
        
a=[1,2,3,4,5,6,7,8,9]
even(a)            


# # example 8
# ## print even

# In[21]:



def even(a):
    i=0
    for i in range(len(a)):
        
            print(a[i],end=" ")
a=[1,2,3,4,5,6,7,8,9]
even(a)                      


# # example 9

# In[29]:


def list(a):
    list=[]
    while a!=0:
        r=a%10
        a=a//10
        if r%2==0:
            list.append(r)
    
    list.reverse()
    return list

a=int(input("enter a numnber"))
list(a)


# In[ ]:





# In[ ]:




