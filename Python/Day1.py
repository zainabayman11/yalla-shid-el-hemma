
# import sys
# import keyword
# import operator
# from datetime import datetime
# import os

# Keywords ---------
# print(keyword.kwlist) 
# print("Total number of keywords:", len(keyword.kwlist))

# Identifiers -----------

# val2_name = 10
# print("val2_name is an identifier:", val2_name)


#  Comments in Python -----------

"""
 Multiple 
line 
comment

"""

'''
Single line comment
'''

# Statements -------  Instructions that a Python interpreter can execute.


# Statements -------

# p1 = 10 + 20 # 


# Multiple line statement
# 1

# p1 = 20 + 30 \
#     + 40 + 50 \
#     + 60 + 70
# print("p1:", p1)

# 2
# p2 = [
#     'a',
#     'b',
#     'c',
# ]
# print("p2:", p2)



# def square(num):
#     '''Square Function :- This function will return the square of a number'''
#     return num**2

# print(square.__doc__)


# Variables ----------------

# 1-  id() function returns the “identity” of the object.
# d = 40
# a = 30
# id(d)
# id(a)

# 2-  Memory address of the variabl

# hex(id(a))

# p = 30
# q=20
# r = q
# p , type(p), hex(id(p))
# q , type(q), hex(id(q))
# r , type(r), hex(id(r))


# Variable Overwriting  -----

# a = 10
# a = 10 +20
# a


 # Variable Assigment --------


 #  Multiple Assignments

# intt,floatt,strr = 1,2.2,'python'
# print(intt,floatt,strr)



# a1 = a1 =a3= a4 = 20



# Data Types ---------

# 1- type(var)
# 2- sys.getsizeof(var)
# 3- isinstance(obj, class_or_tuple) ??? اسال هو ايه صح ولا غلط

# size int = float = 24 bytes  & complex=32


# Boolean --------True & False---------



#  Strings  ----------- ' ' or " " or ''' ''' or """ """
# ممكن تكتب الاسترينج بالشكل دا بدون اي فواصل ولا حاجه 

# mystr=('hello '
#        'mr '
#        'ahmed')

# # or.
# # mystr=('hello ' 'mr ' 'ahmed')

# print(mystr * 2)


#  String Indexing -------------
# المهم فيها لو بدأت من الاول ابدا 0 - لو بدأت من الاخر ابدا من -1

 # str1[len(str1)-1] = tr1[-1] 



 # String Slicing --------------- 

# str1[-4:] # Retreive last four characters of the strin

#  str1[:4] # Retreive first four characters of the string


# Update & Delete String -----------------------

#Strings are immutable which means elements of a string cannot be changed once th

# str1[0:5] = 'HOLAA'  -----> TypeError : 'str' object does not support item assignment 


# del str1 # Delete a string1
#  print(srt1) ---> NameError: name 'srt1' is not defined 


# String concatenation ------------

# s3 = s1 + s2 or s3 = s1 +" " + s2

# Iterating through a String --------------------------

# mystr = 'hello'

# # for i in mystr:
# #     print(i)

# #  Enumerate method adds a counter to an iterable 
# # for i in enumerate(mystr):
# #     print(i)

# list(enumerate(mystr))

#  String Membership ----------------------

# mystr1 = "Hello Everyone"
# print('hello' in mystr1)


# String *******Partitioning  --------------- (before, arg, after)

# str5 = "Natural language processing with Python and R and Java"

# print(str5.partition('and'))


# String ***rPartitioning (the last occurence of the specified) --------------- (before, arg, after)

str5 = "Natural language processing with Python and R and Java"

print(str5.rpartition('and'))

