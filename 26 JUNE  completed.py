#!/usr/bin/env python
# coding: utf-8

# # upper lower functions

# In[9]:


text="chinmay"
text1="My Name Is Chinmay"
print(text.islower())
print(text1.islower())


# #### isupper()--- true or false

# In[10]:


s="application"
s1="PYTHON"
print(s.isupper())
print(s1.isupper())


# In[13]:


s='23456'
s1="abc123"
print(s.isnumeric())
print(s1.isnumeric())


# In[14]:


s="Application"
s1="App1899"
print(s.isalpha())
print(s1.isalpha())


# In[16]:


s="python programming"
s1="Python Programming"
print(s.istitle())
print(s1.istitle())


# In[18]:


s="python is a programming language"
s1="pythonisprogramming"
print(s.isspace())
print(s1.isspace())


# # string methods
# ##  join()
# ## replace()
# ## 

# In[21]:


str="python"
print(" ".join(str))


# # join

# In[38]:


print(",".join([" python","programming","is","easy"]))


# # replace

# In[29]:


str="python"
str=(str.replace('python','java'))
str


# # SPLIT

# In[37]:


S="C***H***I***N***M***A***Y"
print(S.split("***"))


# # list

# In[39]:


s="python is a very intresting language"
lst=list(s)
print(lst)


# In[40]:


# repalce


# In[42]:


s=("python programming")
print(s.replace("gra","application"))


# In[48]:


s=" ROHAN is goodboy"
print(s.replace("goodboy","MASS LESS"))


# # python tuples

# In[49]:


s=("python","programming",1989,2019,"machine learning")
s1=(1,2,3,4,5,)
print(s)
print(s1)


# In[52]:


s=("python","programming",1989,2019,"machine learning")
print("t1[0] = ",s[0])
print("t1[1]= ",s[1])


# In[53]:


s=("python","programming",1989,2019,"machine learning")
print(s)
del s
print(s)


# In[54]:


s=("python","programming",1989,2019,"machine learning")
s1=12,13,"ai","bi"
s2=s+s1
print(s2)


# # python directory

# In[65]:


user={"name" : "chinmay","age" : "19","address" : "dubai","email id" : "chinmaykrishna999@gmail.com","phone nmber" : "9030997968"}
user["email id"]="CHINMAYKRISHNA@gmail.com"
print("user[email id]")
user["address"]="LAS VEGAS"
print("user[address]")
print("user[name] = " ,user["name"])
print("user[age] = " , user["age"])
print("user[address]= ",user["address"])
print("user[email id]= ",user["email id"])


# In[70]:


user={"name" : "chinmay","age" : "19","address" : "dubai","email id" : "chinmaykrishna999@gmail.com","phone nmber" : "9030997968"}
del user["age"]
print(user)
user.clear()
del user


# # len of dicf

# In[71]:


user={"name" : "chinmay","age" : "19","address" : "dubai","email id" : "chinmaykrishna999@gmail.com","phone nmber" : "9030997968"}
print(len(user))


# # add and modify

# In[78]:




user={"name" :"chinmay","age" :"19","address" :"dubai","email id" :"chinmaykrishna999@gmail.com","phone nmber" :"9030997968"}
user2=user.copy()
print(user)
print(user2)
user["address"] = "LAS VEGAS"
print(user)
print(user2)


# # values

# In[77]:




user={"name" : "chinmay","age" : "19","address" : "dubai","email id" : "chinmaykrishna999@gmail.com","phone nmber" : "9030997968"}
print(user.values())
user1=user.copy()
print(user1.values())


# # items

# In[76]:


user={"name" : "chinmay","age" : "19","address" : "dubai","email id" : "chinmaykrishna999@gmail.com","phone nmber" : "9030997968"}
print(user.items())


# In[79]:


list=["python","programming"]
print("{0} {1}".format(list[0],list[1]))


# In[81]:


list=["python","programming"]
print("%s %s" %(list[0],list[1]))


# # cojntact application
# ## creat contact

# In[15]:


contacts = {}
def addcontact(name,phone):
    if name not in contacts:
        contacts[name]=phone
        print("contact %s   added"  %  name)
    else: 
        print("contact  %s  already exists"  %   name)
    return

addcontact("chinmay",9030997968)
print(contacts)
addcontact("chinmay",9030997968)
print(contacts)
addcontact("charith",9304567876)
print(contacts)
addcontact("rohan",9876543456)
print(contacts)


# # search

# In[17]:


def searchcontact(name):
    if name in contacts:
        print(name,  " : " ,contacts[name])
    else:
        print(" %s contact does not exists"% name)
        
    return
searchcontact("chinmay")
searchcontact("rohan")
searchcontact("charith")
searchcontact("maneesh")


# # adding contacts

# In[22]:


def importcontact(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()), "contact added successfully")
    return
newcontacts={ " shashank":90273645435,"abhi shake":9876576879}
importcontact(newcontacts)


# # delete contact

# In[24]:


def deletecontact(name):
    if name is contacts:
        del contacts[name]
        print(name," : is deleted from the contacts")
    else:
        print(name," do not exists in the contscts")
    return

deletecontact("maneesh")
deletecontact("manish")


# In[25]:


print(contacts)


# # update contact

# In[27]:


def updatecontact(name,phone):
    if name in contacts:
        contacts[name]=phone
        print(name,"updated")
    else:
        print(name,"donot exists")
    return

updatecontact("charith",4564564563)
print(contacts)


# In[30]:


lst=[1,2,3,4]
print("%d %d %d %d"%(lst[0],lst[1],lst[2],lst[3]))


# In[31]:


lst=[1,2,3,4]
print("value at: {0} value at:{1}".format(lst[0],lst[1]))
print("value at: {0} value at:{1}".format(lst[2],lst[3]))


# # python packages and modules

# In[32]:


from math import floor as f1 
f1(546587.6574657)


# In[34]:


from math import factorial as fact
fact(5)


# In[36]:


import math
math.factorial(5)


# ###### generate tyhe random numbers between twolimits

# In[39]:


import random
def generaterandomnumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end=" ")
    return
generaterandomnumbers(100,23,89)


# In[ ]:




