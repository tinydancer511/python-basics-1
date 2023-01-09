#!/usr/bin/env python
# coding: utf-8

# # Week 2 - Monday Lesson (variable assignment, loops, lists)

# ## Tasks Today:
# 
# 1) Int & Float assignments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Assigning int <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Assigning float <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Performing Calculations on ints and floats <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Addition <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Subtraction <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Multiplication <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Floor Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Modulo <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Exponential <br>
# 2) String Input-Output <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) String Assignment <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) print() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) String Concatenation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Type Conversion <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) input() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) format() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Old Way (python 2) <br>
# 3) <b>In-Class Exercise #1</b> <br>
# 4) If Statements <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) 'is' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) 'not in' keyword <br>
# 5) <b>In-Class Exercise #2</b> <br>
# 6) Elif Statements <br>
# 7) Else Statements <br>
# 8) <b>In-Class Exercise #3</b> <br>
# 9) For Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Using 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Continue Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Break Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Pass Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Double For Loops <br>
# 10) While Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Looping 'While True' <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) While and For Loops Used Together <br>
# 11) Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) range() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) len() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) help() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) isinstance() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) abs() <br>
# 12) Try and Except <br>
# 13) Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Indexing a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) .append() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) .insert() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) .pop() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) .remove() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) del() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Concatenating Two Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Lists Within Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Looping Through Lists <br>

# ### Int & Float Assignments

# ##### Assigning int

# In[4]:


number = 6
print(number)


# ##### Assinging float

# In[8]:


numberFloat = 2.3
print(numberFloat)
print(numberFloat)
numberFloat = 7.7
print(numberFloat)


# #### Performing Calculations on ints and floats

# ##### Addition

# In[10]:


num1 = 2
num2 = 5.4

result = num1 + num2
print(result)

result += 2
print(result)


# ##### Subtraction

# In[15]:


result_diff = num2 -num1 
print(result_diff)

result_diff -= 1
print(result_diff - 1)


# ##### Multiplication

# In[17]:


result_mul = num1 * num2
print(result_mul)

result_mul *= 2
print(result_mul)


# ##### Division

# In[19]:


result_div = num2/num1
print(result_div)

result_div /= 2
print(result_div)


# ##### Floor Division

# In[21]:


result_floor = num2 // num1
print(result_floor)

result_floor //= 2
print(result_floor)


# ##### Modulo

# In[25]:


result_mod = 13 % 2
print(result_mod)


# ##### Exponential

# In[28]:


square = 5 ** 2
print(square)

square **= 2
print(square)


# ### String Input-Output

# ##### String Assignment

# In[39]:


name = "Jane"
print(name)


# ##### print() <br>
# <p>Don't forget about end=' '</p>

# In[40]:


print("this is my first name", name)

print("Full Name:", name, end=" Kress")


# ##### String Concatenation

# In[43]:


first_name = "Jane"
last_name = "Kress"

full_name = first_name + " " + last_name 
print(full_name)

full_name += ", Fairy"
print(full_name)


# ##### Type Conversion

# In[44]:


number = "32"

change_type_num = int(number)
print(number)
print(change_type_num)


# ##### input()

# In[ ]:





# In[50]:


#input always returns a string

name = input("what is your name? ")
print("nice to meet you," + name)

age = int(input("what is your age? "))
add_age = (age) + 5
print(add_age)


# ##### format()

# In[58]:


age = input("what is your age? ")

result_string ="you are {}, {}! and you are getting wiser!".format(age, name)
print(result_string)

result_again = f" {age} is a great time in life"
print(result_again)


# ##### Old Way (python 2)

# In[ ]:


result_string2 = "you are" #couldn't see the character


# # In-Class Exercise 1 <br>
# <p>Create a format statement that asks for color, year, make, model and prints out the results</p>

# In[ ]:


color = input("what is the color of your car? ")
year = input("what year is your car? ")
make = input("what is the make of your car? ")
model = input("what is the model of your car? ")


# In[ ]:


### If Statements


# In[ ]:


# Available operators: Greater(>), Less(<),Equal(==)
# Greater or Equal(>=), Less or Equal (<=)

# Truth Tree:
# T && F = F
# T && T = T
# T || F = T
# F || T = T
# F || F = F

num1= 5
num2=10

num1 =6
if num1 ==6
    print("this is true")
else:
    print("that thing was not true! it is false!")    
    
if num2 >= num1:
    print("num2 is greater")
elif num1 > num2=
    print("num1 is greater")
else: 
    print("equal value")


# In[ ]:


##### 'is' keyword


# In[ ]:


# the is keyword is for checking for the same object but npt the same value 

num3 = 55
if num3 is 55:
    print("this is the exact number/object")


# ##### 'in' keyword

# In[ ]:


#check if a character is in a string

char_name ="Frodo Baggins"

if"Frodo" in char_name:
    print("the ring bearer")


# ##### 'not in' keyword'

# In[ ]:


sega_char ="sonic"

if 'a' not in sega_char:
    print("a is NOT here...")


# # In-Class Exercise 2 <br>
# <p>Ask user for input, check to see if the letter 'p' is in the input</p>

# In[ ]:


user_input1 = input("favorite 'weeds' character? ")

if "p" in user_input1:
    print(user_input1 + "contains the letter p")
if "p" not in user_input1:
    print(user_input1 + " does NOT contain the letter p")


# ## Using 'and'/'or' with If Statements

# In[ ]:


num_11 = 15
num_12 = 3
num_13 = 10 
num_14 = 3

#if with 'and' statements
if num_11 / 5 == num_12 and num_13 - 7 == num_14:
    print("true and true")
    
# if with 'or' statements
if num_11 > num_12 or num_13 == num_14:
    print("true and false")


# ### Elif Statements

# In[ ]:


first_name = input("what is your name? ")

if first_name == "Smith":
    print("the name is Smith")
elif first_name == "Brandon":
    print("the name is Brandon")
elif first_name != "Jane":
    print("the name is NOT Jane")
else:
    print("the name is Max")


# ### Else Statements

# In[ ]:


# see above


# ### For Loops

# In[ ]:


# syntax:
#for counter in condition

name = "Jane Kress"

for letter in name:
    print(letter)


# ##### Using 'in' keyword

# In[ ]:


# see above


# ##### Continue Statement

# In[ ]:


# will continue to next iteration


# In[ ]:


for i in range(20):
    if i == 5:
        continue
    print(i)


# ##### Break Statement

# In[ ]:


# will break out of current loop


# In[ ]:


for i in range(20):
    if i ==5:
        break 
    print(i)


# ##### Pass Statement

# In[ ]:


# mostly used as a placeholder, and will continue on same iteration


# In[ ]:


for i in name:
    pass


# ##### Double For Loops

# In[ ]:


for i in range(5):
    for j in range(5):
        print("i = ", "j = ", j)


# ### While Loops

# In[ ]:


#syntax:
#while keyword, condition statement

num = 0

while num < 10:
    print(num)
    num+= 1


# ##### Looping 'While True'

# In[ ]:


#bad practice

game_over = True

while game_over:
    print("infinite loop")
    user_input = input("would you like to continue the game? ")
    if game_over == "No":
        game_over = False
        


# ##### While & For Loops Used Together

# In[ ]:


num = 0

while num < 5:
    print("\n while loop iteration: " + str(num))
    
    for i in range(2):
        print("for loop iterations ", str(i))
        
    num += 1     


# ### Built-In Functions

# ##### range()

# In[ ]:


#range (start,stop, step)

for i in range(1, 2, 20):
    print(i)


# ##### len()

# In[ ]:


#checks the lenth of a variable

name = input("give me the name of your favorite book: ")
length = len(name)
print(length)


# ##### help()

# In[ ]:


# use this function to get more information on a certain function 
#ie 
help(range)
help(len)


# ##### isinstance()

# In[ ]:


#check a variable to find out what object family or data type it belongs to
print(isinstance(4.5, int))

if isinstance(4.5, float):
    print("this number is a float type")


# ##### abs()

# In[ ]:


# |-5| = 5

print(abs(-5))


# ### Try and Except

# In[ ]:


#use this to log out useful error messages 
#does not stop the program 

try:
    input_num = int(input("guess a number "))
        print("your number is: " + str(input_num))
except:
    print("that didnt work: change your input to a number!")


# ### Lists

# ##### Declaring Lists

# In[ ]:


list_1 = []

name = ["max", "cindy", "kathy", "bob"]
print(list_1)


# ##### Indexing a List

# In[ ]:


# [start:, stop:, step]

#single index 
print(names(0))

#print starting at index 1 going to the end 
print(name(1))

#print starting at the beginning of a list up until a number
print(names(2))

#print starting at indect 1 and going up by 2 in each ineration
print(names[1::2])

#print starting at back and display in reverse order
print(names[::-1])


# ##### .append()

# In[ ]:


names.append("jane")
print(names)


# ##### .insert()

# In[ ]:


names.insert(3,"devon")
print(names)


# ##### .pop()

# In[ ]:


#defaults to last value if no parameter is given
#pop returns the elements that was removed in case tou want to assign it to a variable 

my_name= names.pop(2)
print(my_name)
print(names)


# 
# ##### .remove()

# In[ ]:


#value to be removed rather than index
names.remove("bob")
print(names)

#remove multiple brandons from list
while "Brandon"in names:
    names.remove("Brandon")
print(names)


# ##### del()

# In[ ]:


#goes by index rather than value 
#be careful with del, it can cause indectinf errors if not used carefully

del(names[1])
print(names)


# ##### Concatenating Two Lists

# In[ ]:


#will append two lists together
#it will not add the values 

list_2 = [0,1,3]
list_3 = [3,4,5]

large_list = list_2 + list_3 
print(large_list)


# ##### Lists Within Lists

# In[ ]:


#lists can hold any type of other data types, including more lists
#they can go as deep as you want, this is called nesting lits

names = ["max", "sam", "josh", "sally", "sue", "tamika"]
print(names)
print(names[3][1])


# ##### Looping Through Lists

# In[ ]:


#two ways to loop through a list: one is by index: the other is bt using the "in" keyword

#by index
for i in range(len(names))
    print(names(i))
    
#loop with in
for i in names 
    print(i)


# ## Exercise #1 <br>
# <p>Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.</p>

# In[ ]:


find_cube= [i*i*i for i in range(1,1001) if (i*i*i) <1001 ==1001]
print(find_cube)


# ## Exercise #2 <br>
# <p>Get first prime numbers up to 100</p>

# In[ ]:


start = 1
end = 100

for num in range(start,end):
    if num > 1:
        for i in range(2,num):
            if (num % i) ==0:
                break
        else: 
            print(num)


# # Exercise 3 <br>
# <p>Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors</p>

# In[ ]:


age = input("what is your age? ")

if age < str(18):
    print("kid!")
elif age > str(18) and age < str(65):
    print("adults")
else:
    print("seniors")

