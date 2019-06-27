#!/usr/bin/env python
# coding: utf-8

# In[38]:


# function to creat file and write some data
def createfile(filename):
    f=open(filename,"w")
    for i in range(10):
        f.write(" This is %d line \n" % i)
    print("The file is created and data is stored Successfully")
    f.close()
    return
createfile("chinmay.txt")
createfile("rohan.txt")
createfile("charith.txt")    


# In[39]:


## function to read the file 
def readfile(filename):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        print(x)
    f.close()
    return
readfile("chinmay.txt")
    


# In[40]:


# function to append the datatexixting file
def appenddata(filename):
    f=open(filename,"a")
    f.write("new line 1\n")
    f.write("newline")
    print("The data is appended")
    return
appenddata("chinmay.txt")
readfile("chinmay.txt")


# In[41]:


# count of charecters in a file
def countcharecter(filename):
    f=open(filename)
    if f.mode =="r":
        x=f.read()
        lst=list(x)
    return len(lst)
print(countcharecter("chinmay.txt"))


# In[42]:


# count the capital charecters in a file
def countcapital(filename):
    countupper=0
    f=open(filename)
    if f.mode=="r": 
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.isupper():
            countupper +=1
    return countupper
    
print(countcapital("chinmay.txt"))


# In[47]:


def countsmall(filename):
    countlower=0
    f=open(filename)
    if f.mode=="r": 
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.islower():
            countlower +=1
    return countlower
    
print(countsmall("chinmay.txt"))


# In[50]:


# to find the count theloines ofthe file
def countline(filename):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=x.split("\n")
    return len(lst)
countline("chinmay.txt")


# In[56]:


# regular expressions
import re
def phonenumbervalidate(phone):
    pattern="^[6-9][0-9]{9}$"
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phonenumbervalidate(9030997968))
print(phonenumbervalidate(5553900396))


# In[61]:


#valid phone number 
import re
def phonenumbervalidate(phone):
    pattern="^[0-1][4][0][-][0-9]{6}$"
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phonenumbervalidate("040-997968"))
print(phonenumbervalidate(5553900396))


# In[64]:


## rollnumbers
import re
def phonenumbervalidate(phone):
    pattern="^[2][2][1][8][1][0-9]{7}$"
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phonenumbervalidate(221810304040))
print(phonenumbervalidate(5553900396))


# In[67]:


# unique words

import re
def phonenumbervalidate(phone):
    pattern="^[1][2][5][U][K][a-z][0-9]$"
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phonenumbervalidate("125UKc8"))
print(phonenumbervalidate(5553900396))


# In[ ]:





# ### validate vehicle number TS
# * TS 10 RR 8444
# 

# In[70]:


import re
def phonenumbervalidate(phone):
    pattern="^[T][S][ ][1][0][ ][B][A][ ][8][4][0-9]{2}$"
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phonenumbervalidate("TS 10 BA 8444"))
print(phonenumbervalidate(5553900396))


# In[79]:


import re
def em(i):
    p='^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$'
    if re.match(p,i):
        return True
    else:
        return False
print(em('charithblue22@gmail.com'))    


# In[90]:


import re
def em(i):
    p="^[a-zA-Z0-9!@#$]{6,15}$"
    if re.match(p,i):
        return True

    return False
print(em('ALPHA%$'))    
print(em("passwo8"))


# In[91]:


# file on the virtual machine


# In[108]:


def createfile(filename):
    f=open(filename,"w")
    for i in range(10):
        f.write(" This is %d line \n" % i)
    print("The file is created and data is stored Successfully")
    f.close()
    return
createfile("chinmay.txt")
    


# In[109]:


# add data


# In[110]:


def appenddata(filename):
    f=open(filename,"a")
    f.write("new line 1\n")
    f.write("newline")
    print("The data is appended")
    return
appenddata("chinmay.txt")
readfile("chinmay.txt")


# In[111]:


# count the lower charecters in the file


# In[112]:


def countsmall(filename):
    countlower=0
    f=open(filename)
    if f.mode=="r": 
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.islower():
            countlower +=1
    return countlower
    
print(countsmall("chinmay.txt"))


# In[113]:


# count of digits


# In[114]:


def countdigits(filename):
    c=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.isnumeric():
            c+=1
    return c
print(countdigits("chinmay.txt"))


# In[115]:


## count of special charecters


# In[116]:


## 
def countspecial(str):
    count=0
    
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=32 and ord(lst[x])<=47:
            count=count+1
    return count

print(countspecial("chinmay.txt"))


# In[ ]:




