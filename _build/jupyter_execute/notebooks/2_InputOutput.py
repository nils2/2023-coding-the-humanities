#!/usr/bin/env python
# coding: utf-8

# # Python basics 2 + Input / Output
# 
# This notebook contains more basics of Python. Use it as a reference whenever needed.

# ## Python Syntax

# ### The Significant Whitespace
# 
# Most program languages use characters (e.g. `{...}`) or keywords (e.g. `begin ... end`) to delimitate blocks of codes. But, when writing Python code, you rely on **indentation** to structure your programs. 
# 
# All programming languages allow you to indent (and you should!), but in Python you **have to.** Otherwise, you'll receive an IndentationError and your code won't work!

# #### How Indentation Works
# 
# - All statements with the same distance from the left border belong of the same block of code. This is related to the _scope_ of your code. 
# - Sub-blocks are more indented, while the block ends at the line less indented.
# - It is recommended to use **4 spaces** per indentation level. However, a tab character (`\t`) can also be used. Often, you have a setting in your favorite editor that automatically translates tabs to 4 spaces. 
# - When a statement is too long, it's good practice to avoid lines of code longer than 79 characters, it can be split with `"\"` at the end of the line.
# - **Never mix** spaces and tabs in a single source file. This will raise an error when you try to execute the code, but is also very hard to spot by hand. To help you, you can set your text editor to display whitespace characters.
# 

# #### Recommended Reading on Python syntax and style
# [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

# ##### The code is way more readable:
# 
# 
# ```python
# # input() reads from standard input (e.g. keyboard)
# n_string = input('Enter a number, please:')
# 
# if not n_string.isdigit():
#     print("This isn't a number...")
# else:
#     n = int(n_string)
#     if n == 0:
#         print("Zero? Why zero?")
#     elif n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# ```

# ## Conditional statements, loops and functions
# 
# Up till now, you've used the Python language and syntax as a fancy calculator. Most likely you felt that you needed additional elements to prevent replication in your code, or saw that you needed a conditional statement that only executed your code when a particular variable/statement was True/False. 
# 
# Below are the building blocks for writing such code blocks introduced. Let's take a look at conditional statements first.

# ## Conditional Statements
# 
# A lot of programming has to do with executing a block of code only if a certain condition is verified. 
# 
# In Python, the `if-then-else` construct has the form:
# 
# ```python
# if condition1:
#     # statements
# elif condition2:
#     # statements
# elif condition3:
#     # statements
# else:
#     # statements
# ```
# 
# Note that the `elif` and `else` clauses are optional. A conditional statement can contain a single `if` block, and nothing else.
# 
# All methods from the previous notebook that return a boolean (True/False) can be used after an `if` statement. You can of course combine these with the `and` and `or` operators. 

# If you inspect the function below, do you think you can change the `elif` statement into an `if` statement? Would this alter the code? What is the difference? Try playing with the code by adding some `Pear` to the grocerylist. 
# 
# Can you describe what the code is doing?

# In[1]:


fruit = ["Apple", "Pear", "Banana", "Orange"]

item = "Pear"

# To remind you that you can check for elements in a list
if item in fruit:
    print("Already on the list!")
    
    if fruit.count(item) >= 3:
        print("It's on the list three times or more!")
    elif fruit.count(item) > 1:
        print("It's on there twice!")
    # You don't have to finish with an 'else'
    
else:
    print("Not on the list yet, adding it!")
    fruit.append(item)


# ### Quiz

# Finish the following code block. The `intput()` function askes the user in the Python interpreter to input some text. Implement the following:
# 
#     * Print a line with a friendly message, telling the user what their input is
#     * Check if the input is a digit
#     * Check if the input meets the > 0 condition 
#     * If the input is a digit and meets the condition, tell the user if it is even or odd
#     * Otherwise, print another informative message 
# 
# 
# 

# In[2]:


user_digit = input("A number > 0 please: ")
# Your code here


# ## Flow control / Looping
# 
# ### For Loops
# 
# Programming is of little use if we cannot repeat an instruction for an intended number of times. In the previous examples, you had to change the code and re-run in if you wanted to play with, for instance, the value of the `item` variable. 
# 
# The `for` statement allows us to define **iterations** (i.e.taking items from an iterable) by following this template:
# 
# ```python
# for variable in sequence:
# 	# statements
#     print(variable)
# ```
# 
# Little known fact is that the for-loop also has an `else` clause. It's also rarely used:
# 
# ```python
# for number in [0, 1, 2, 3, 4, 5]:
# 	# statement
#     print(number)
#     
#     if number > 4:
#         break
#         
# else:
# 	# statement
#     print("All done!")
# ```
# 
# The code in the optional `else` clause is executed if and only if the loop terminates successfully (i.e. without a **`break`**). 

# In[3]:


# Let's iterate over our list of fruit

for item in fruit:
    print(item)


# In[4]:


# Or from another function we recall

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
words = text.split()

for word in words:
    print(word.title())


# In[5]:


# You can also nest for loops:
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
words = text.split()

for word in words:
    for character in word:
        print(character, end='-')  # What is the 'end' argument doing?


# #### The enumerate function
# 
# The `enumerate()` is problably the most used among the functions that supports the iteration of an iterable. This function return the current item plus **its index** in the iteration process.
# 
# You can see that we assign two variable names, `i` and `word` to the outcome of `enumerate()`. 
# What is the datatype that this function is returning? 
# And what are the datatypes of its elements?

# In[6]:


# Use enumerate in the iteration over a list of words
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
words = text.split()

for i, word in enumerate(words):
    print (i, "-->", word)


# In[7]:


# What is the datatype of the returning value of enumerate(words)?
index_words = enumerate(words)
index_words = list(index_words)
index_words


# Optionally, you can make the `enumerate()` function start at another number:

# In[8]:


for i, word in enumerate(words, 98):
    
    if i > 100:
        break
    # No else here?
    
    print(i, word)


# #### The range construct
# 
# The  `range()` construct can be used to control the iteration. It generate lists of numbers on the basis of the following three arguments:
# 
# - `start` : the first integer of the list
# (default is 0)
# - `stop` : one larger the last integer of the list (list stop at n - 1)
# - `step`: the increment of the list (default is 1)

# In[9]:


# Let's play with range
print(range(0,10))
print(range(10))
print(range(1,10,2))


# This each prints the function name with its arguments. Not very informative at this point...
# 
# Similar to the call with the `list()` function above, we first have to transform the outcome of this function to a list to make it printable. This happens for some efficient functions that don't put everything in memory at once, but only during each iteration (when you run the code). So basically, the `range()` function produces a list of numbers.

# In[10]:


print(list(range(100, 1, -10)))  # You can make it reverse with a negative step!


# In[11]:


# Let's use range in a for loop

for i in range(1, 10, 2):
    print(i)


# ### While Loops
# 
# The `while` statement allows us to control a loop on the basis of a condition. 
# 
# A `while` loop runs as long as a condition is verified. 
# 
# It has the following general form:
# 
# ```python
# while condition:
# 	# statement
# else:
# 	# statement
# ```
# 
# the code in the optional `else` clause is execute if and only if the loops terminates successfully (i.e., without a **`break`**)

# ### Quiz
# 
# _Think before doing._ What do you think happens when you execute?
# 
# ```python
# 
# n = 1
# 
# while n:
#     print(n)
#     n += 1
# ```
# 
# If you dare, you can execute this code. **Do this in a terminal window  instead of this notebook!**

# More safe is the code below, this does not let you end up in an _infinite loop_. Try executing the code a couple of t imes and see what it does. What is your longest streak of odd numbers?

# In[12]:


import random

n = 1
while n % 2 != 0:
    n = random.randrange(99)
    print(n)


# ---

# ### Break and Continue
# 
# The clauses `break` and `continue` are two statements that allow for a more flexible control of a loop. Intuitively:
# 
# - `continue` is used to pass to the next iteration of the loop
# - `break` is used to interrupt the loop abruptly

# In[13]:


# When we encounter 7 we skip to the next step
for el in range(1, 10, 2):
    if el == 7:
        continue
    print(el)


# In[14]:


# When we encounter 7 we stop our loop 
for el in range(1, 10, 2):
    if el == 7:
        break
    print(el)


# The `break` influences the execution of the loop in yet another way: when a loop terminates due to a `break` statement, the code embedded in the option `else` clause is skipped.

# In[15]:


# The continue statement does not influence the execution of the else block
for el in range(1, 10, 2):
    if el == 7:
        print ("(let's ignore the " + str(el) + ")")
        continue
    print(el)
else:
    print (">>> the iteration ended with the number " + str(el))


# In[16]:


# What if we replace continue with break
for el in range(1, 10, 2):
    if el == 7:
        print ("(we encountered the number " + str(el) + ", let's break the loop)")
        break
    print(el)
else:
    print (">>> the iteration ended with the number " + str(el))


# ### The Pass Statement
# 
# Given the importance of indentation for Python, sometimes we may need a placeholder that allows us to write down a condition for an `if-then-else` construct or for a `while` loop without writing any statement (maybe just a comment). This is the case in which the `pass` statement comes in handy. 
# 
# In what follows, **nothing happens**:
# 
# ```python
# if condition1:
#     pass
# else:
#     pass
# ```
# 

# In[17]:


numbers = range(10)

# Handy if you're quickly typing a loop
# or function (see further on in this notebook)

for n in numbers:
    if n % 2 == 0:
        pass  # TODO
    else:
        print("Odd!")


# ---

# ### List Comprehensions (advanced)
# 
# A list comprehension is a syntactic construct that allows us to create lists by applying a function on another list, in just **one line** of code. 
# 
# Even if the reverse isn't always true, list comprehensions can always be (inefficiently) expressed as loops. We will exploit this family resemblance for introducing this construct.

# In what follows, we start with a list of numbers and we want to square all of its elements and save our final values in a new list.

# In[18]:


# Our source list
source_list = [1,2,3,4,5,6,7,8,9]


# In[19]:


# We can solve this problem with a for loop...
final_list = []

for el in source_list:
    final_list.append(el ** 2)

print(final_list)


# In[20]:


# But this can also be done in one line
final_list = [el ** 2 for el in source_list]

print(final_list)


# These list comprehensions cary the form of:
#     
# ```python
# [i.method() for i in items]
# ```

# **Conditional statements may be implemented**
# 
# In what follows we want to ignore all the odd numbers

# In[21]:


# We can solve this problem with a for loop...
final_list = []

for el in source_list:
    if el % 2 == 0:
        final_list.append(el ** 2)

print(final_list)


# In[22]:


# ... or by using list comprehension
final_list = [el ** 2 for el in source_list if el % 2 == 0]

print(final_list)


# **If you want to implement an else clause the syntax changes slightly**
# 
# In what follows we want to leave the odd numbers unchanged

# In[23]:


# we can solve this problem with a for loop...
final_list = []

for el in source_list:
    if el % 2 == 0:
        final_list.append(el ** 2)
    else:
        final_list.append(el)

print(final_list)


# In[24]:


# ... or by using list comprehension
final_list = [el ** 2 if el % 2 == 0 else el for el in source_list]

print(final_list)


# ### Quiz
# 
# The following list contains 100 random extractions (with replacement) of numbers between 1 and 15. 
# 
# Find the number that has never been extracted

# In[25]:


random_numbers = [1, 2, 1, 1, 9, 13, 15, 5, 9, 8, 12, 14, 3, 2, 8, 10, 3, 12, 15, 13, 5, 3, 7, 5, 2, 13, 12, 8, 10, 5, 15, 8, 2, 8, 5, 12, 9, 2, 3, 5, 1, 4, 5, 9, 13, 2, 12, 5, 10, 8, 1, 15, 15, 6, 12, 3, 1, 3, 7, 14, 15, 10, 15, 7, 10, 12, 1, 2, 13, 7, 9, 6, 6, 7, 4, 12, 10, 8, 8, 3, 8, 4, 6, 14, 10, 5, 2, 3, 15, 4, 9, 3, 7, 7, 2, 4, 4, 1, 7, 15]


# In[26]:


# Your code here


# ---

# # Input / Output
# 
# We now discussed the art of looping, to automate bits of your code and prevent repetition. If you know that you're going to use parts of your code more than once, you can make a function out of it. Functions are constructs that allows us to organize portions of code more than once in a program. The alternative way to obtain the same results without functions would be to copy the same portion of code every time it is needed. Organizing your code with functions makes it easier to split your problem into smaller subproblems.
# 
# We have seen plenty of built-in functions so far. If you used them, you could have recognized them by their parenthesesis after their name. The `print()` functions is such an example. 
# 
# A function **takes optional parameters** (inside the parenthesis) and **optionally returns a value** after it has done something. 

# ## Functions
# 
# Functions in Python are defined by a `def` statement, following this template:
# 
# ```python
# 
# def function_name(parameters):
#     """
#     Documentation on what the function is doing
#     """
#     
#     # your statements
#     result = True
#     
#     return result
# ```

# > The list of the parameters required by the function is reported between round brackets right after the name of the function. Each function may have **zero or more** parameters. When a function is called, its parameters are called **arguments**.
# >
# > The (optional) documentation string should be placed immediately after the function definition. There are many way to format your **docstring**, [PEP 287](https://www.python.org/dev/peps/pep-0257/) recommends reStructuredText, but more formats are available. See [this tutorial](http://daouzli.com/blog/docstring.html) for an introduction to the topic.
# >
# > The **indented** function body contains all the statements that are executed every time the function is called. When a `return` statement is executed, the function exits and its output is the argument of the `return` statement. 
# >
# > When there is no return statement in the body function, or when a return statement with no arguments is executed, the function  returns `None`

# For instance, the following function calculates the number of characters in a string:

# In[27]:


def chars(s):
    """
    Calculate the number of characters in a string
    """
    
    if type(s) != str:
        return "This is not a string!"
    
    r = len(s)
    
    return r


# The docstring is saved into a  `__doc__` variable and can be accessed by using the `help()` function or the IPython `?`

# In[28]:


# Don't use this, it is just to make the point
print(chars.__doc__)


# In[29]:


# Use one of this two
help(chars)
get_ipython().run_line_magic('pinfo', 'chars')


# Or keep using the `shift + tab` ipython magic!

# In[30]:


chars('test')


# In order to execute the code included in a function, you have to **call the function**, either in your script or in the interactive shell. For instance:

# In[31]:


chars("voodoo")


# In[32]:


chars(1979)


# The `return` is also optional. What happens when you assign a variable to a function call that does not have a return statement? 

# In[33]:


def tokenize(text):
    words = text.split()
    
    print(words)
    
    # Forgot something?
    
words = tokenize("What happens when there is no return keyword?")

print(type(words))


# Sometimes, you don't need a return statement, as you're for instance writing a function as some kind of wrapper function, that ties several methods together. Or write the output to a file, instead of to the console. It's best to make clear in the docstring/documentation of the function (using the `""" """` docstring style) what the function takes in, processes, and spits out again. 

# ### Parameters
# 
# A function can receive any number of parameters:

# In[34]:


def higher(n1, n2, n3):
    """
    Find the higher of three numbers
    """
    
    if n1 > n2 and n2 >= n3:
        return n1
    
    if n2 >= n3:
        return n2
    
    else:
        return n3


# In[35]:


# A parameter can be passed either by position
higher(4, 2, 8)


# In[36]:


# Or by name/keyword
higher(n3=8, n1=4, n2=2)


# #### Optional Parameters
# 
# In some situation it may be useful to have a default parameter value, that is used when a call leaves an arguments **unspecified**.

# In[37]:


def higher(n1, n2=0, n3=0):
    """
    Find the higher of three numbers
    """
    
    if n1 > n2 and n2 >= n3:
        return n1
    if n2 >= n3:
        return n2
    else:
        return n3


# In[38]:


higher(9,4)


# But what happens now:

# In[39]:


higher(-6, -3)  # How to fix this? 


# #### Arbitrary Number of Parameters
# 
# A different situation is when we want our function to have an unspecified number of parameters. Python functions admit the so-called "tuple references", marked by an asterisk `*` in front of the last parameter  (that becomes a `tuple`).

# In[40]:


def print_params(*params):
    print ("your input:")
    print (params)


# In[41]:


print_params("Down from my ceiling", "Drips great noise", "It drips on my head through a hole in the roof") 


# ---

# #### Quiz
# 
# Remember the grocery list. Can you write a function that:
# * Takes *one or multiple* items as arguments
# * Takes in an existing dictionary of groceries (keys) and counts (values)
# * Adds the single (or multiple items) to this dictionary if it is not yet in there and update the count if it is
# * Returns this (updated) dictionary

# In[42]:


groceries = {
    'kiwi': 8,
    'bread': 2,
    'banana': 3,
    'soy sauce': 1,
    'red wine': 1,
    'soup': 1
}

# Your code here



# ---

# ## Modules and Packages
# 
# Python modules are groupings of related code that are structures as to facilitate its re-use. 
# 
# Physically, modules are `.py` files implementing a set of **functions, classes or variables**, as well as **executable statements**, that can be accessed from other modules by using the `import` command.

# The `import` command can be used both to import **the whole code** of a module, using the following syntax:
# 
# ```python
# import module
# ```
# 
# or just **specific attributes** (one or more functions, variables, classes or a combination of these) with the following syntax:
# 
# ```python
# from module import name1, name2, name3
# ```

# For example, if order to know what is our current working directory, we can use the function `getcwd()` available `os` module (see below) in two different ways:

# In[43]:


import os
os.getcwd()


# In[44]:


from os import getcwd
getcwd()


# You can think of a **package** as a structured collection of Python modules.

# There are some modules/libraries available in Python as built-in. Take a closer look at three of them:
#     
# - Math ([manual](https://docs.python.org/3/library/math.html))
# - Collections ([manual](https://docs.python.org/3/library/collections.html))
# - Itertools ([manual](https://docs.python.org/3/library/itertools.html))

# Can you figure out when to use the `defaultdict` and `Counter` from the Collections library? Can you use them in any of the functions/code you wrote above?

# In[45]:


# Example

from collections import Counter

# Your code here


# ---

# ## File Input/Output
# 
# A huge portion of our input data will come from files on disk, and a lot of our work will be saved in memory. So, mastering the art of reading and writing is crucial even in programming.

# ### Files in Colab
# 
# In these examples, we will work with a file referred to as "data/adams-hhgttg.txt". This means there should be a directory called "Data" and inside of that there should be the file "adams-hhgttg.txt". You will find this in the course repository in the Notebooks directory. Obtain this file either by downloading the course repository and finding it there, or opening it on Github and saving the raw file.
# 
# ![github-download.png](data:image/png;base64,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)
# 
# In Colab, you can view and edit the file system by clicking on the "Files" icon on the left side. You will see the file system of your Colab session there with a directory called "sample_data". You can make directories and upload files here.
# 

# Normally, you cannot upload a directory full of files, but there is a trick, which we will use here: you can upload zip files (containing multiple files and directories) and then unzip them.
# 
# Find the "data" directory in the repository that you downloaded, and compress (zip) it. 
# 
# On Windows, this is unintuitively done by sending it to a compressed folder:
# 
# ![compressfile-s.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAkEAAAEsCAIAAABL5PDjAAAACXBIWXMAABYlAAAWJQFJUiTwAAAgAElEQVR4nOydd3wU1fbAz5TtJbvZzW563TRCSEhCCkmQLl0QCwqWp6LCQ/BZnj67TxEfog/LE3k/nw1BEJDeS0JCTQgkpFfSe7Zk+87O3N8fG0KAgIi0wHw/fMLMnXvv3NndmTPn3HPPwRBCwMLCwsLCMgDBb/UAWFhYWFhYrhGSQUCzmhgLCwsLywCErNTDmQ7gsPoYCwsLC8tAgwQAlQDE3Fs9EBYWFhYWlj8Iq3+xsLCwsAxUyEuLCKCEVA2ibYDhGAYYhmMYDhjG4EIj5n/zh8jCwsLCwtIv/cgwDlhCiBNWQxnQVpwgCJJDkByM4FCkspgz7+YPkYWFhYWFpV/6sSViGEZwhSJVAinyBcQgxCBEAzA4ctz88bGwsLCwsFyOfufDEDA0htE8txCEGMTQiGEQYgAxV9MjZTn96QtvtOhZgcdyd8HY9BYbfW4P2Q1tnc11ug4t3acOoh3GjnYnAkTbDa11nc313SZLT3N7t7alrrO53mi09l3tghymbq2OAbDqmjqb6zpb2yiaOddbTydGk7W3k66Wus7mepPJ5uoEOa2G9vrO5jq9trv/RTSM02I09IY6oO2Grua6zuYmi+2CWxgxrnPVdTbX6XV6BgEA2A0tnc11na2tDid9Sb8DCsZp0ja7rq6zuc5sdTiMHd3dFqdVf3L7Gp3FfoWmyGmtO7oha/v2jnPfQl8szfnH9mdc+DS0NxxdX1TZdX2v4K6lPxmGAAABQwGiGdqlhzEuhexqekSMtb2hiXL2c780n96cmV325wbMwnI7YtfX5u/4X2WT2bVrbi/KOZDR1dpYcWhTZV1r783g0J/NyzxEIXNd7t6SMyUdZ4tO7d2qtwOizNXZO2oaajuby/L27NCZbOdaoO7aYwWnK2wdJaezsltbG2rz9hbml9EAAJbaE3tKC0s6as7k7d+mdwDjMFVlba9trOtoKj25Z4febAOAllN7S0tLulqrCw9ubWjTXzJwR/OpndmZhx1OBgDA0nomc1NleU1LeW7ewYOWPvUo89lTe3e3NjV2tTYadN0MAkpbmX8os6W1ob7gQEHOGecN+VxvFg5D8d41FTV1Xa2NXa2NFput/fS2vFPVTkSbDTr6isGMLK1F5U1E8pQpHmLBpUcZymo2mi5sjxxmnc0+sD+w24d+5sMAAIABoAE5ETCAUM+/P0197pZcJB6ZHvHnu2JhuW1A2uIdJ/IbMIvR61xRc36ONGp8eLifyYd7+NAJje9UksABQFtfKg6JQa1l1fVU8oNTROB0P7HuzKmK4cOCvBMnhEjlOKIFth8rypqTE4IBANGOhtpm38EJJJeJm/IgnyDA7pv92/724HCZpbimiUl5YKIQKNmxtUWnK5PjA32SJwkkMhxRfOtPleVtiXEBstDhKpmSxDCVZNfJk4V+k9Ix7Ny4GVvO2k+6MZmd9AMAAKa1LLtbEDsiPRYDc/munyvLO4aEe7iqM5SVkAWFDk3lnXtmUKRyyKQHBCQHHEHHNm1r6Yz2U17ueTIg4HpHpQTKOa4dlPaEN+CMTfu7zZyUle+uZlcn3Sou85tDDDA0gBMxDGIYhBBirmhLRFRb9YlN3/63zSbWpIT2KM7O9nX/equsg3K4aZ55/gVR8+Y1Ww43My3vm2oWPftQ/YFvN2WWMBzesOkvTRoeimOX7fvaMGvbDA1lOMEuHmC50SBHty0kOJjrdKe68lqtJAAQfLG4u6K1qJahzH7ujo6SwxiGAYCl2+YubNQ2Gj09CGPxYSMAjYuUlor2sjYcwAgAgACXyqwVrUVNAIAYmiR5nPYzWrL3l+xQeYjtZw93OnVeHnh3cXY3AEOI3G3l7WWtPZ0gpG23Ym44AAjlHq5mDM1gBAF9bjQMI8PHPE2SprzDJQAACFmNep5EjmEAIHJXu5W0NpvVxuKjZTETJiKrxYmBzaynCY5ALMIAONKe5z1iGAZw7Lrfw7cUU82hGktQhEbas884Gs8cqKvvogn54HvGuIv5PeXdNQW5pzr0cIRwxiUnc8BRdey3TjMBTn5Q+mgvd3lvhzTV3VRwuKFVRwokhJlCAADIaaovPHzc4qSEXvGDh0Y4mvPKqg08opv0SAwL92EfXldDvzIMAaIBaAAMuSyLgAAQhpx81GHDPC5tYKo98NlHv9z/9udJQdz8H9/d5Co1tIc+8snDweKSX9/44efdb776+KP3HcxCc/7+3FiwddWETHl3+ivGpsMf/GNxXPRKbynv+l6Y02EN9Ver1err2y0Ly9Ux+A+WX4GYP9qAoqjyKm2Yv/v5Imt7dVmj1+CEC+QMRsrU3nZ95bldXKb2Ly/KNQ4KEKGupvpGxi0U5whlKhWOAfCUcqm+Jj+zq77NL3lySKhvz7MDMe2luVZxmIc78ccv7bbCXndyf7cAB457SGwsZWzVdnsgcMkwWl+ZUd4iHH7vWGfdwRNHctPHpvNclysNjhkWV3CWkzoyhbZ2nNr5m3TofcODPanO4mP7f8PGzT4nA6Hu2IZ6NGTklEkOY82xdScFGmCc3QUH94gHTRuqkedv+b7aXeHl6GqqqU+cMcdT1o9ZkqVfLqeH0YBoQAgYBvUYEhGBbHK6pIW859LaZ08cEIRPGRYkB4BBM+4L3PQtANiAb8r/8ZOv8jqbSzq9fPrOajqBkDgr//PKh20mW1mzzeR0AlxnGcbCcjcTHOqtlgkBAMBpbD5bcmwHGTI5PEh1xUaYLHRkPJN1es9qrkTpJlHgOMEVeYYneAIAKMOH3hMOgChzVdbGAx6ej7hLuE6brv7EzlqrfGhq0sC/gbmqsDhfNxIwDp9DXuDFQXXXFpdKAiZ1t9UB4jg7q03WdJ744vYWXZWW9okLUuMAPOWgAOXJlpZWaU+1jpYGSjNuEABwxV4+/j56ANpQ1aYjFGBsqzeRXGdnm85LDiIPjTsrwP4Il7clIhoQwyBEIIQQAgQADAb9ex85nXaC5PZovjhBAABtzP7+7yflTz73wXxr7mef7r2gfnPO6pWrC57/57c+RMM/X/nb9bscFhYWAAAcaMZJAUGaWvJOHigNHj3Lz8eT+D1rH0bwPAaN8xgEAFRt5io3T+9LdCuMI1ThmMnpoACsxXs3W8Wa5LHpwgE9EdYDJpC6S2Sc/g4xDE1TFoNRDwCiiMQUcX8SGyEnwkmsx1yLEQROM70PTJphMBzHAQAwzGVYRgxNOx3mbq2TBL7PMI2nJ+hqAWctiH+My/jWIycgxmZsd+30FF4WzCcspiF/W2GLEZymkg1rCwAAKGOnyT0wRsZzFBzLdPkPc3hCymYDAIdNbxMM0qj5LSU7q+uv8yWxsLDodV3NDXU2S2fxwSN+o6cG+v6+AAMA2mIwWe0AYKo9UdftExahoq3ahvJyCiGHod3qBACnvjLHJvAXiDjtp/bq+JFxo+8MAXZFOG7+IYF2hhMQlaQZEu0m8eD0J+mE0hCRs6a+pYsBoAzV9Z3I16fXy0culzpqqqoAgNI11NXVMwCkm0YhYcRekZohSb6BwVIRv59OWX6Pfn59LtshhmgrBRSpApJEBEnjHBzj0NC/kquKfXDug7rVbzwnUHkPTgxL8qonubLRT81b+q/XPtwn81ZrvL1kOEBk+gO7ln///qfNzz04KXrfF++/+JSbf1hYpDeH9bxgYbmu1FUU6YoaRz+YRjuxppO72vNdEkwZM3m8GLtwUgznCEQiVxltaio8eYphMK7Ac9DIdCGA1dJelX9GERrmaD59uqKTS9AMzztl3BgxHwwU5tCW5m6vBgAArmpQqibYe6D6dWA4Tywj+8h5nCcR8HkYRggkbgTGkUWNUx3edmxHKYE7lBHTZH2a4qRAICABgBSr4saNLzq0qZErYGhuYPJ4tbvQbuULRCIMeKEj7i04cvzI9gKu1FPpG4xxCZwji01JOJmztZHAcKEiYtgYkisUiHgD9TO8RWBlWtRquiBuPQGUisnzcp6oISfrcc2tG9ufwtBa682zsT4dLHchFEWt+nUTEqsGD01SqDxx1jzFcufSjx5GA6cVT7QTMgpEN39ALCws1wE2sS3L3UH/lmwEuJZgVyKzsLCwsNzWsEYGFhYWFpaBCgkAdhqIOy52l+OmxCClabqxsdFisWAYplar5XL577dhYbnx0AicNNidYHWy3tosdzKkSgB3ZPBJ5sb7+1oslpUrV3733XdNTU04jqempr7//vuxsbE3/MQsLL8HiQOHBDEPpFxWhrHcyZByPsjvxGUJtWaw2X6/2jXDMMwXX3yxYsWK55577tlnn21tbX3iiScWLlz4/fffh4SE3MATs7BcBSIOqKQQ6Q6eHqwMY7mTueNXJ94ouru7V61aFRAQ8OyzzyqVSnd390cfffSzzz7btWvXiBEjVqxYkZSUVFZW1tjYOGfOnPHjxwNATk7OypUrKYqaMmXKzJkza2pqPv/884SEBK1Wm5+fP2HChFmzZpEk+42wsLCwXC39PTEZu9NQwFBmDMcwDMdwHMMJDMMxUgLCQTd9hLcpXV1dOp0uISFBJpMBAI7jQ4cO5fF4tbW1ERERe/fuPXLkyLhx4+rr6xctWvT999+TJDl37tzY2FilUvnBBx84HI6QkJD9+/dnZWWNHTv27Nmz//znP0NCQlJSUm71lbGwsLAMGPqXYbij2qGrZBw6nCAIkiRIDkZwcK4CY2XYOUiSxDCMoqjeEpvNBgAeHh4YhuE4Pn369LfffnvXrl1PPfVUQUFBU1NTe3t7YWEhj8fTarUHDx708/PDMGzSpEnvv//+ypUrly1bptPpbt0FsbCwsAw8+pNhGOAEKVBGO0yNTlMNYnCGYQicAYbqp/LdilKp9PHxqaysbGpqCggIoGk6JyeHYZjIyEhXWASBQIDjuEQiQQjZ7fa2tjY3N7eHH35YpVIBgL+/v8tsyOfzSZLk8/kYxoaYYWFhYfljXC5/GIOBgyv2d3ZXI5wBxCBAV1j6b2gqOV2PhqdE3T3JTIVC4csvv/zWW2+99NJLjzzySE1NzTfffDNz5sxRo0adPHmSYZhdu3Z5enpu3LjRw8MjJSVFqVTu3r27sbExIiKiu7tbKBSyQovlxsGcu11pa3dVbZ3JTgvlvqFBqktzfCGno6VTp1KpSBwDAFt3a0VVsxO4XiEhXm7n46PSlLmmrNxIAQAIZV7BgV5cHLoayuo6LECKQsKC3fj9RnwfINCOhrNVHd09bmDqoEixraULKbyl9PrV6+959Al/yWU932ib8diOjeU25ZipYwKlF0eU1VWd2Hi869E5k4Tny2x5W9c0+06ZGnflVDgsV0V/HksIzoWudzIMgxCDEAOuv/2DWor2fb1qr/UGjvO2A8Ow+++//+uvv9bpdG+//faqVateeeWVf/7znxKJBABwHFcqlStWrKiurl6yZElsbOz999+/aNGiQ4cOvfHGG6tXr/b19eVyuR4eHhKJBMMwoVCoUql4vIGfg4nl9qClvbvT7ACA0qMHK7RWgQAvOrQ7p7Ltomo2c+eJnevW7M5xOBEA0LqzW3bsbrUQYGnbt3lXu/P8a6vdXJ+dVQQcgUAg4PFIDANrS2nm8Uok4FtbS3buOWG+fJr3AYDDeHz/7mYHVyAQCAQCkmBaS08cL2mhATkpJ7pi4C59U3GBQTFn9pRLBRgAIMRQTvqiDhink764jOUauZwXHAPAAHIiYHri2F/pa8Qi7l306703ZHy3MxwOZ9y4cePGjev36LBhw9avX08Q5198X3nllVdeeaV3NyAg4PDhw67txx9//PHHH7+ho2W5q8C626sb5QAQmDAqSi4nAGTQ/tuJ0mSNulf/R4xl8/f/dbh5Y07atV955oRdMWx8WhSAzdG2KqegbVK8p+s9l7FbCJl3eESk6Jy6hcS+k2aGC3AcNPKm7zZXtiXFeg1kVQxIH014pLLnEtSjHwkHcJi6freZ0+kQK5Ts6+et4vI5MBkagEIMgxgGIYQYBi6rh0HLyXXv/tax7KMF+xbPP8KNFJaerqYcCePn+JsKDuSUNjLi115/Jz1SVXrox69/zjDTDm7IlCV/e1jOs+dlrvv6q31ILgmKDqzK6Xr3q4+C3WybVny8+ViTlRA9/OKrM+N9T2774fvtmVYKuSU+9+/nL80izcLCcjFOIHh8EgDEbm4uIeQwWbkiGfQxYGM4f/LjCxh762+7SwAAAFktZq7QZTTje6okxc0tWl/9ls1nHpj7IGa2mKzG+roaHlcU4K8mALgSiasfxmZzII6Af0ctC2k9tS3bED5pmMK1i5ymY/t3VbXbHDQvffLEcFXPtYOuZnfmqVodrCaoqWOSMLM2+8AOrVPgNKOIUffEhfj1dmgztuYcOtJgsJF8PtNp4fsBADK2FO/Yl08TDEcePnFsguPs0e0nO5RuSOKXnBrjc6nhl+VSLjcfRgOiAQAhxAAiEAOAgHEgRwvG9bq0gdNqaG7X0gDdHZUFhsiN339nL9zxxEPzh7+7afl3L+f/+Nq/f96bsHiO1H/Yu8tnK0WWxU/O2piXNlNR8NHKYy9/uXK4L6dw/aezf2tzOKmKPV//fNb365Xvk6W/PPHlqqQVs//35c5Hvlk1IhhVVt7IRcvXj4iIiCVLloSGhrI5L1huFYzYI9CjzxSMselwQXN4euqFc7C4RCo1d50zMGK4j39Q1pHjLfEhSqY1r6QWeYbyJKqklBg+BpgsMH4wx9DZUHmqpDJ+3MgkTY/mgZjyk0dNisgA+UCf37Ue3raulIcDXzX23hFOm9FgsZ+zPjkbTu0vsQU8Oiueqjm0+kCu1wOjpS6FTR48YWTc7jLO7CkpDmPrpk3bQsfPnBCgsGurN2zYIxE/2vu4zD+4rVGcMnvKYLux4bdvSxgA2qHfvftoaPr98Rq3/Wu+y6n0j6Ytbe3d90x9JFDK6nVXy+X0MBrACchlSOwpAsYOllLoT4b1QZk2OVUGYPcM81TFjZkUzsfI8Og48+aqToD2qiObl3/WZGRKilpnmkwllQfdIu8d7isBgPDJY8O/KAOHfs9ve0XqB3b/tgYsdc6a7OqOv0WFwP999cnZUWPuHzf8+l78DcLLy+uBBx641aNguasJ9BQrha6nrKO+qHjfoUPBI2ePCFdesRGmihr9GO/Eri2rOW5egX6+RozDE7oPHuIOAODul5zsBwBJiWH/Xb6tTePnr+BZDM1Ht22udYuZNTl54Ef7EaROeWiokgMAGIY19j3iMBQUVAr9vYry88Bmsnd06Cwgdbu4vaGzsg3zf9BfgQMI3ENifI6WN7R49YRQba2sRcMe1gAAT+KhCVA3ATi6Kms7aY+2mhwtmCiLocUQrQI3ryA1K8D+CFfQwxjE0AxCBEIIIUCAAP2pFy39qU+X/Tbr4x8+GOqxfMG9FACOE06KYlyOJQ67DQAwnMslhXLPgAB3gIC3l02OUktSlq5MOXN69/r/e/l067K3HpKyug0Ly1VTX5i197hhzINPBXrIfr82gLsmabYmCRjr8a1r/SP9+pngQlyMcDppmna07Fq/WxiR9mjKEOEdYfbCMKx/b2EMJwmCJ3RzdycB3GcEidT9pVbEcBJDTgYQDhgAopw0eT5DPYZhiGYYAACEnAyNADCcIEium0wu4WHuqVNFCm9oqLtR13bnchmBgGhgGKuxrcdH0fWvZ/ta4VD6boGnQqKt2LvnpBYA0wyOqzu9ZX+lFij9wZU/nQQAjtuEqaNq6moiho0cOTKGZxMKeO0l1Ux86r3zHhnVVF3RzS5RY2H5AxiPZJTETRgbopIRV/EGShk6WrqtANBadLjEFpgYLrcbW49k51kRMrXWax0A4KjPO2qXaeRSsuZYllEVOyrtDhFgV4IjjR0c1Nqh9Q7QaDSeyIr1GxLOzT1IydQeL2+jAcytpUXtnKjgXquV3M/DeSS/FADMrdV5ZfU0AEce4icxU3wPjUajcBPcUdOJN5F+PzcMMBzAAaSMdJMTJIETJEZyMIIE0r3fXngyn9hIAQfAO2wwrpYAAM4VRiUMcSNxAOBIPGNjGJ4o7u/zEv/75nxRRNLEKSM8FSKPoTNXvoV9+s6La929xk9LG777EI5zAsa/+LeWf70y/yku4Ux75O04sGxf9t4XXNwp8Hv7vb96s0o2C8tV0N7eXt9iik7SiISi4qwd5bhLgiknPDpecaGqQXCE3l4eOI4BAGPXHzu0z+pAbh6h06YPFQOYHZaWpjYnAqv27K792SSGSGXoXx6KE/Ghk+eGOos2ri4FAABucFxqUqT3QLWS4By1r7+Ec374PDdPH0JMEBxvP18+yVHHTUg27dq4bjWO0eEpMwL7NOUKZV4qEgA4YtWMOQ8d2rbrlzwSEW4jpk8NkPPNFjdfL4wA7vCpM+mMw6tXl4lUQcNSkpxuXILrNnXq+G2Hdlcep3ly73vuuYcrVvh6cu/4V4LrC4YudZpHTjCXgP4QKCaCQHMDT44YmgGCwAEhU+naRz+oWvm/t72Ev9/uaqitrbXZbGq1+vp0x8IycKAoatOmTSqVKikpydPTk/UtYrmD6TfWFAniIUC6A3FjtR5rffabXx0I1/iAqetIad0L7y+7XgKMhYWFheVu4PI2WL7vjT63wDfxr4+7dZhtAOS42aHBnpLfb8PCwsLCwnKOWzqPSAhComPZfJEsLCwsLNcGayhnuUYYhikqKmLzxbCwsNxCWH/Oawch1NLSsnLlyq6uLoIgZs6cmZqa2jdA4jV3u2vXLoqipk2bdkti2zMM88svv/j5+aWnp19hAE6n85tvvpk9ezabt5OFheVWwcqwayc3N/fzzz+fN29eamqq1Wp9++23CwoK5s+f/+fFmFgsdjqd12WQ14abm5tQyDrYsLCw3O6wMuwaoShqzZo1Tz/9dFpaGgAIhcK33nrr9ddfLy0tDQ0NbWlpkUgkLS0tDMOEhYXx+XwA0Ov1DQ0NJEkGBgYKBIKmpiYej9fa2koQhKvE1TOGYdHR0RRF0TTd1NQkFApbW1sFAkFAQACHcz5sQltbG47jHR0dDMMEBQWJRCIA6OzsbGlp4XA4wcHBZrOZoiiVSuV0OhsaGry9vblcrmtgrgQxJpPJYDB4e3szDNPY2KhUKkUiUUdHB0EQiYmJJEm6Unfy+fz29naJROLv74/jOEKooaFBr9fz+XyGOR8GuqamxmQy4TgeGhrK4/Hq6+s9PDwEAoFOp7NYLD4+Pna7vbW11c/Pj3X1ZmFhuV4Q77333sVltNXRmUnpTtOmMsZcgSxVYK1CthpwajGezy0Y4zWh1+udTqdYLL5B/RuNxrVr186ePVtyLnq3QCAoKyuzWCxisXj+/PldXV1dXV0ZGRmFhYVxcXE2m23JkiV1dXW5ubkdHR0xMTEvv/zyoUOHaJres2dPS0vL0KFDew13mzdvPnz4cGRk5Ny5cxsbGw0Gw9q1a6VSaXBwcO8Ali5d+uuvvyKEjhw5UlhYmJCQYDab33333fb29qysLIqidDrdqlWrRowYUV1dPXfu3CFDhqhUqvfeey8wMNDT0xMAysrKPvvss5EjR3Z1dc2bN08ul2s0ms8++4zL5e7bt6+5uVkoFM6bN89qtTY2Nq5atSoqKkqhUOzdu3fVqlV2u/3UqVNHjhwZN26cj4/Ptm3b1q1bZ7PZMjIySktLY2JiFi9eLBKJgoKCVqxY8b///e/+++8vLy//6quvxowZQ/Yb5IDl+sEwTFlZmUgk8vX1FYvFbLZVljuYfp8mFAcz2K01lK0Nx4EgOUByMIKDceQgSbzZA7xd0Wq1OI73Kk8ueDye1WoFAC6XO2vWrKCgIJqmn3/++cLCwtOnT4eEhDz99NMtLS1vvvnm+PHjMQxLTU2dM2dORUXF4sWLZ8+efan5DsOw++67Ly4uzt/ff9++faNHj+77PIqNjZ07d65er1+0aFFLS8uvv/6anp7+4IMP1tXVvf/++x988MG3337b3t5+5syZpKSk8vJylUrFMEx4eLireXh4OIfDqaystFqtcXFxhYWFycnJjY2NiYmJBQUFrjoEQcyePVulUonF4j179vj4+KxZs+att94KDQ01GAxlZWUAUFlZuWnTpi+//FIsFjscjjfeeOPEiROpqam5ubkjRozQ6XQ8Hk+n05WWlg4ZMoTLvXtyfbOwsNxw+n8jxjDEk4fhFhnVXYoYhmEYAmdc2ViuC4imDHodcKVuEj5jN+m67QKpm4g3kF7PxWKxTqczGo1yeU9gaoSQwWDw9fXFMEwqlbp0HYIgBAKBwWCoq6urqKgoKCigKEqr1TocDqFQ6O/vDwBCodDpdPY7ASaXy12hRqRSqdVqpWm6V4nhcrkBAQE4jvN4PBzHTSZTbW3t6dOns7KyHA6H2WwmSTI4OLiysrKmpiYtLa24uLi8vNxl6HP1wOPx4uLiioqKKIqKi4vLzc2tqalRKBR9RamHh4e7uzuGYXK5vKGhwWQy2e121yULBAKXmtvV1SUQCFytuFxucHBwc3NzcnJyVlZWZWUln8+Pj48vLi6urKwcM2YMqxOwDCAQYmw2O5fPJ674u3U6rFY7wxcJOfjF1RiaslMMn8/rcwA57TYa5/E4rFH9OnC5uPUMBnaOyJPSlyCcAcSgnsi/14fTW775dGvumKkvPjQ5dMuSV/YbvR558pnxQ274qurriEKhGDRo0KFDhx577DFXSU1NTXV19VNPPWW1Wp1Op91uFwgEDMNYrVapVKpQKB544IFHHnnkBo2HJEmFQjFt2rQJEyb0FoaGhh48eFAgEAwbNiwjI+P48ePjxo3rK0XCw8M3bNhAkuTChQtLS0sPHjwYFRV1BZ8UkiSdTqdL17TZbN3d3QAgFovtdrvT6eRyuQzDNDU1BQYGenl5AcAPP/xw7733qlSqlStXkiQZFRV1gy6f5SLoc7er09R1pqhIb6El6tD46IBLb3iGsp5tbPP3D+AQGABYOs/m5ldTwOXiXpEAACAASURBVA+JjQlSng874HQYzhzP1ToAAKSq4CFRwXwCmstyShq7geMWkzDEQzSQg5k6rWVFpxs7La69gOhkubmmCXmFqfG1P6wd/fjTAdLL5pZxmrUZWzZ1iINHjE7xFV9cTV9zct2RzsefnNon0r399I5VTX73TR/GRsK7DvT3IuCKT4+cwDgYhkGIQYgB19+rhK7//IUXjjdd7rBh9+4DY+cufmpmHNNVurGEev+d1weWAAMAgiBeeumlwsLCH374ITc3Nzs7e/ny5Y899pi3tzcAdHV1/fTTTzk5OStWrAgPD4+Jibnvvvuys7P3799/7NixDRs29PWGuC5wOJxHHnlk8+bNGRkZR48e3bJlC8MwiYmJNTU1kZGRCoXCx8enoKCg74waAGg0GqPR6OPjo1KpNBrNoUOH4uLirnAWqVSakJCwYsWK3NzczZs3V1RUAEBISIhGo1m+fHlOTs6aNWu4XG56erpQKExMTKyoqBg0aJCfn19xcbG/v/+Nm55kuYimZm2zwQYAJccPW8Te0dFhuqKMjPz6C2uhruby3Wu+XXvgDEUjALC3lqzbmS30Dtd487J/21JvPW96cVgaC0p1IRHR0dHRGn8VBwdLY9HJamtI9GAfgW7ntkz9rXSk/dNQlsLjOaRvZHR0dHR0tKcbaWyrr28zXs1ru665rJL2eWjaqEsFGMtNoD+fDsYO1gpADCDMbqzDMAzDcQzDcYKPuV1dFkrj2R+/+y3s3keD+s9YZDm2a0fIyFmhHjxrd232ybpJE8cLuddZrb7RPh0AIJVKU1NTm5ubGxoajEbjk08+GR0djWGYVqs9ceLEtGnTqqqqxGLxU089xePxFApFYGBgeXl5V1dXQkKCUqmUSqUhISESiYQgCJVKFRIS0qsAucyMXl5eSqUyJCSEy+VyuVxvb29/f/9eLUoikQQFBcnlchzHFQqFRqPx9fX19vaurKzUarUpKSkymUwqlSqVysTERIlE4ufnFxwcHBER0VfN4vP5SqUyKSnJ3d1drVYHBATExMRwuVyRSBQYGKhWq728vIKCgjAM4/P5fn5+vr6+iYmJDoejvr5+0KBBY8aM0Wg0crk8NTVVq9U2NDSIRKLHH3/c9bGrVCrXGXk8XmBgYHx8vEKhuHFfB0svDMPkHTrQRUuSY8O8gyOC/X0kYjcxtzP7lG7YkKBePRwx5q0/rwaVn9WGxQ8J5+BMee6+DknihKRgmYcH1ZBXbvUK85G6qtt19WXNRGJStFwqFvC5OAbAkWgigpUSiYdaXHnsKO4T4yUdsCHXndaSgiLvhJEalVQsFvNIUu4XFu4nRw5rYX5RUEyc7PIzHabOs/VGYVyEX79HrdrG4gZLTGx4n3lgZ3NpgdEtIsKHfaW7Dlzui6EBOQEw1JvKGV3JlqhvLFqx7MPibqEF5z/77N/bd76XWXCm9u9PlT67UJH5YUH84iUzwgE6np75xOz3vjEdX7k+4+T+tr+2/uWp+oP/zc48s/BN8aIX/5YYeEli1NseoVB43333XVqO43hCQkJ6enrfwqioqL7GtOHDe14IRCLR6NGj+9YMCemJwDVq1CjXhlqtvigG/9ChQ10bJEmOHDnStR0XF9dXkeJyub09+/n5+fldfJsRBJGamuraViqVvXbIIUOGXDSAwMDAwMBAAODxeFOnTr30eqdNm3ZRoaenp2tSEAB6R8hyc3AARyzhAYBALHa9Hpq79EJFMPSZlsFw8cPPv2zRVf+6s9hVQlEO6BFDXKVClN/a2tnctfrn3Cde/gthNml1LfmnTnL58pghIRwAzjmHJtpktCC+VHpHees0Hlu7Vzf4oRE9CcCQXbt785ZWK2G30MMm3xcfcC4Lla5md+apWh2sJqipYxId7fUHDu53cN0cOovf8LT0mMjeDk2d1Qf3HTUyOE7i1la9zA8AMV01JzYdKBOIMDvhM/2+kc6qzF+yGvx8JMqg4akxPgP2jeCmcoU8zjQAIIQYQARiABAwdmSrwfjBl9Yvz1hVK7nvv589wlh0CIkk4e8dy3vrwaXfjQ40rTlAMz2yD9FOmiFF0+a+XHa6PPqF/0yMlOhjOQ2WTf9a/JZCNJAcOq6Ma2qKdV5guYWQMg8/xTmnWcSYm4oPlXXHjA656EeJ9V2rh+EBmqiczGPF9SoV3pVTXA9eYSJF8MyHlRIcxzwHTx7nDWCvzM3e2macOCZGiGMA4LR2nzx8GPxi/Ad8yG7r4a1rS3g48NXjJowAxDDn81I5Ko7t7XJPenRUBF1/7PtDJ4JmTXR3iWx58ISRcbvLOLOnpFh19Zt3H06Z8ViISuI0NW9et6NM6R3Q0wN9MmM/BI2ZnaxxWtu2//A9A+C0dezKKBk+6YFBvqLs9d+dKIuMJxgaCZPvne4t6CeBNku/XEZyIAaABoR6lDAAAASMA2y10I8Mw4ISJwu3vv+3Nyvumfr4o8PlYLiBI779CQwM/OKLL271KFjuanyVQhnfdXfbKk7kZBaUDh33cPzvmDoweUjSLJ7o8JljzRJlSKB3EXA5PLF/gBgAQKwMC1MCQGio6v+Wb+6IiwhQ8I2d1Qd+22ELGzEzZcjAf+gK0qbNGqrsuY7GvkccxorKBqubLGN/PTi6LDqr0Qrul6idJn2dnvAO8ZDgAFyxd6S3sLK1M6DHbbmjoRkblu4LAKTAzUft3gRA6esa24zi/GP1RdDRqWXkJlCBSOklZwXYH+EKehiDaCeDEIEQQggQIECX0yxU4SM+/O/PHU1Fb732d8NLH85L6D1CcLk45XAgAAwoh/VGXAILC8tlKTu660iVYPqcv3iIrsrjQOo7eJLvYHCasjaVhCUG9WMfdAKNMQyDHMbqzWszg0ZNT4r0v8O9xHGSz+N4a2ISA3kAkDyS0+88O0HwMFrrRIiLYQC0yWLnefZKIwLHGIdr/QzD2CkKAWAkT+imGDI0QSbAITGRK5BYKutu1iXdOVzmp4doYBirsbXHR9H1r2e7n9rl5QVGu9gvcnRaBKUz2UEgkmCYwWhkED8mJrzwSEaXxVa046fDDQPadYmFZSCBEALQ5+U0JYwerhRwEcP0tY71i6Orua7LyDBM3amDlXhobIDYomvYtf2QmUHdDZWtVoZhrBVHskA9SOFG1OSeQMHDEiJ9CbiKrgc0pGToEE1VZSkhlMlkWPNZPervwSlVBHrh9Zmn6x0Mo6/LL9OJojWe5w7Kg70h48QZhmEMjWU5JfU0AFcWHCDSNhpBJpM5rXqjyX4TL+nOoV+/RAdYygDZadyDEAWT4gBC6E/w/TCBDyYIwjgel/aiK8n8Yvk3G7dvl6YtfPGBeJJQRAQR336zolk8aNzYyeK67St/2Kj1HjEhyiMqLtFDQhp1Rt9B8WoJydAOk42Ijo7iktd59ugm+CWysNyeMAyTlZXV2GaJig+ldab6+sriHlp8BgcLLpypRchppwg/Xy8Cx2ib9nh25qn8Qqs4asqEOAGA025saNL7awIcHVUHDh4uLi7rlkfPmTyMRyBLt7G1saqkp+cKC0fmrZQM1ElgxFitDg//ILdzDtK03cII1f4qsd1m9w4MUvpEKK1Vh47mFhdXqaMSPCXnLViM006TEj9Pd5wrGhQf05q3//jpoqoOcuL9E7xEXMbpcGCCAH/vwLAIXmf5oeN5rbRH8pAAidLPWyGN0PgXn8zOyz/TbiE1oSEcZKc50gAfJevNcfVg6NLXJ0SDrRZ0B0E+CgSaWzGq60Btba3NZrvIl4+F5W6AoqhNmzapVKqkpCRPT082yDLLHUx/82EYAYIQICSA31HOsiwsLCwsdxiX92jnqm7iMFhYWFhYWP4wrJGBhYWFhWWgwsowFhYWFpaByp0THePm09LSotVqAYDH4/n7+3O53KamJolEIpVKr9cpjEZjY2MjwzACgcDf3/9y2SMNBoPFYnGFiu/Lf/7zn3HjxoWFhV2v8bCwsLDcVrAy7BphGGb58uVWqzUyMrKqqkqj0cydO/fjjz8eO3ZsvxEUe8nJySFJ8srh4V3U19d/+umn/v7+QqGwtLR08ODBzzzzzKU+ZgihvXv3Hj9+fOnSpRelTWlubrZYLNdwdSwsLCwDgn5kWHt7u91uh541kuAK0wGASJLj5eV5heRSdxsEQUycOHHixIl1dXV///vfp02btnTp0supSi4QQtnZ2Wq1+ndlWFNT05tvvjl37tz09HQMw0wm00cffbRx48YHHnjgokiMGIZNnz59ypQp7FfDwsJyt9HPA7e8vDwgIABc0gsAECCEOjs7rVaLXq+PiIwg2WflhYhEIgzDLBZLVlZWcHCwUqncunWrWq0+evRoWFjY/PnzewXb4cOHt23bJhAImpubFy5caLPZvvrqq9bWVhzHX3/9dS8vr175dPLkSaFQmJqa6ioRi8X333//999/P3ny5F27dqnV6rS0NJqmv/7662nTpun1+vz8/Mcee8xms61bty4vL08kEj399NOurhwOxzfffCOXy3vTddI0vXHjxqysLB6PN3v27Li4OKfTmZGRsWPHDoqiHnzwwdTU1AMHDuzatYum6YcffjghIWHNmjWnT59WqVSvvvoql8vNysratGkThmGzZ8+Oj4/PyMjYsmULSZJz5syJj4+/6d8ACwvLXUo/MowkSR8fH6ZX/0IAABgGTqfT7nCUlZUNZrPxXkheXp4r+dbq1auFQiFJkhs2bPjoo4+WLl36j3/849ChQ2PGjHHVTEtLmzJlilqtfuyxx9ra2t55550nnngiJSWloKDgjTfeWLx4sY+Pj6tmQ0NDfHx8X9XKw8PDaDQ6HI6qqiqa7skqkJ+fP3LkyM7OztLSUoTQJ598olAovvrqq7a2Nlcdh8OxfPlygiAefPDB3q6sVmtYWNhDDz1UXFz86aeffv311/v379+zZ89HH33E4/Gqqqq2bduWlZW1ZMkSHMdramp+/fXXzs7Ozz77bP369d98882oUaN+/vnnL7/8kmGYlpaW/Pz8devW/ec//7HZbB0dHTfvc2dhYbnr6ccvsSf0mSt8x7mg9RwOp6Ki4mxNTXVV9Y0bDe2wVlZUWmnG2FZ99uqSqN5CaJpeuXLlggULcnJyXNpJ76Hw8PDk5GShUBgfH19UVNRv1uaCggKpVJqSkoJhWExMjJeXV0lJSe9RkiQvmsqiaRrDsCukdDGZTLW1tTNnzgQAtVrt7e1NUdSPP/7Y1dX17LPP8vnnQ74SBOF0Ol999dVly5bV19ebzeaDBw8+88wzEomEy+WGhIRkZWU988wzQqGQz+f7+PgcOHAgNDS0qKiIz+cXFhYSBGGxWDIzM9vb20NDQ6VSqdFozMzM7Orq6s18xsLCcjUwTnt7W7vzNn/Y3cb0o4e5wtQjOJd1BSHAQKn0GD1mLI5hGZmZ/XZk0VZ9u+yzMr0wbdazj4642BHu7OFNB43Bf5kY45KZDXlb99apnr4/+eJOOqpee/WdJT+vbf317Z9g3ooX0i+NFLJx+fuKyfNGhqoAgNYV/fu7nNlzH/OScgCMGd/90BXz4APxnpc0uiEQBPHcc89NnDjx0kNcLtelQhEE4dKHLoWiKIIgXDLJlSiZoqjeo6Ghod9//73D4egVjQ0NDUqlsq+kvIju7u6+9QHA6XTqdDqFQnFRq4yMjO3bt7/zzjsURb3++us2m02n0wmFQtdRq9VqMBgE5zIcMgxjtVqrq6v1ej0APProo+Hh4R9++OG+fftWr17917/+NSUl5cMPP9y7d+9PP/30wgsvJCYmsrnTbjn0ufdPqrv16LHjHUan3C92ZErYpVk9GIe5uLohPDTcFbPU2FJyMLvIDsLBaamDvOW91Sib9uje/W02AAC576DUpMFCAs6e2p9bpQWuIm10qrf0quLi36bQttLcI4RmZJicKT2ZUVinBwCu3GdEajKpLc2ttiQMT3TjAICz/syJRjJkmIdh09Gm9NHDvSR8AKDsrUePNiSkxosstRv25TEIAfDixozX9KZwAwCb/tjRww2dPS+mQ0ZO4TfldQjDIxXWjev2PjT/aQXJrnS6Fvr51PpGUEQAgGHnxJnrTz8vDJS+8PUn31HM/MfHbzx28suX1xR3X1ShrfTY3rza3qad1Sf2HS2/thEjQ8Gqrfmu7bMHf/zg89VHajsAwKlt+G3Db6Tsdg+QyOVyXS4zkZGRbW1t5eXlCKHa2tqmpqa+WZ6Tk5MDAwN/+uknh8MBAEVFRT/++OOcOXMEAkFISEhZWZnD4aioqKitre1tolKpZDJZdnY2AHR3d+v1eoFAsHDhQj6f/+mnnxqNxt6aBoNBqVR6enoWFhZ2dnaKxeJhw4Zt3rzZZrM5nU6j0RgbG7tlyxaHw0FRlNlsTkxMVKlUTz755Jw5czQajcPhkMlkzz///AMPPHDgwAGXmJw/f/7UqVMzMjIuJ7NZbib1dW21XVYAKMnJkUWlzZgxid98ZPuRygvuXoTqy46tWfHZ+kNlTgYBgKX+5E87Tw0aMXnCiNC8jesrjOcTTThszbWdgnGTZ8yYMWNU0iAhAaa6/DKD4t4Z0++J5O3YsLNjQEddZxwN5QXN3TQgZ0N5pSJm5IwZM6KlnT/9shNX+5gqC8oadADg6O7IPlrh7S+n9U0nj+zbe7jcddG0Q1d0pspGMWBqa7V5jJsxY0yCav+6DXXdfe4FylxZWjdo7AwXYR4cJ+VwONmb5c/Srwzr+dtHEXP9DwigvxQL6Ozx/Wf9ku+P95P6Dn5yWsTmtZnmq1SNEWPWdzY3NTW36/oxtwEAQHdXc1NTU1NTu9XJAEBc+lhtaa6OAWD0xzMrRyV45Bc2AoCusfosVxPnhzE01dXe5Fq5dUORSqV9DXSuEoFAwOVyZTKZq0QoFPaNnY9h2OjRo11+8Gq1et68ecuWLXvhhRc++eSTefPm+fv799YUiUQvvviixWJ56aWXFixY8Prrrzc1NQmFQpPJNGbMmM7OzoULF27dujUwMJDD4fB4PKlUSpLkokWLMjMzFyxY8PHHHxuNRqlUKpFI/vrXv5rN5k8++aRXuqSlpWm12gULFpw6dcrHx4ckyYcffpiiqBdffPGFF17o6Oh49NFHzWbzokWLFi1apNVqZ82aVVhYuGDBgpdeekmr1dbX17/22msLFiw4fPjwk08+2dDQ8Oqrry5YsCAvL2/OnDlX9sxkuTnwKGNbhxkAItPGx/irOBxx6GC/puqGvtmTELKczin2jU1Su37FiK4qL1ZokkM9RVLPkCHB5JkzjRRNmYwWBoAxW0Ao4fE4HA6HJHAAEHhGjhsZ68bhqkNC5VR7Y6fjllzpjQAnORwOJygyxt1RV2eQxyb4FZ4sogFpa0vwoBgfIQ8A9x+cwNTm5J+9+DmDYQSHw1EEBUkYq8lMXXSQ5PSAY5zAmJQ4jUefRzBy2MwGg8HQbWEti1dP/7bEc6nCMOgVZOf2+9PDUF1ZcUDwwwIAACIoJLhtf43FASLe75++u/7oG298I/Lzbqxpvv/d5eNlFx23F+/a/PmGbe7eQaaqGnHKtJefe9gnLFbc+HFBKyQ5KzafVc1/IfzzHcdssxPrSo+7hY7w5xq2fb5iW0VNsH/I9Cuu0/qTuDwJLyp86aWXXBsff/yxa2PGjBkX1Rk8ePC3337r2k5MTExMTLzcKZRK5cKFC13bDMPs3Llzw4YNI0eOTE1NvTRPdFpaGgCEhYUtX768t/C1115zbSxevLhvZT8/v6+++qpviUgkeuONN/qWvP322313ly1b1ne39xJcvfXdZbkdsANX4sYHAC6f73pKGtu0ElU49LHyYrjovsefMXdVnq0v7ilCyG5ziSJSKubrO7u0bd0//3TiL68+TZhNLU1VB/fZOSLPkSNieAAEr+cOpwx6IxLKZXdaiHDGZrPSXD4ffMPiFMd/K28Pqyhoi5uSzsGBBuCI/NKGiPdkHonym3zJYxTpaqpt7r5esivZV6uzf83Dh08Z0vMxOvR1v23O4MncDW2dgyc9mOB33UIl3NlcRoadMxuivmUAAKgfPQyB1WwSeFw5U5ctd9OXz9Rscd1BXWdPOePDgO5a/cWXvg+/9+rUcP2RFY9+tmroG2P7ttGdPfnhtzvf+HrFYLXEaWlavHDR5hPJc9MGp0WgQ8fLfD1KJVFD7hkcu2rlj8VaKvdoVfSoB6v2/bCmkrNs6VdUR7PNZvvDn8ftCo7jU6ZMmTJlyq0eCMvAQOihDjg3GYMYuqPs8MFq5z0TNFeaqMSI4KiEM/uPZefz1BxDXkkjeIdL1BFPPx8oJXAITH7miSEA9soT2es2GKdPT5WSGADYdC2ZBw5JIkf4iW7Gdd0U6K6mumrQNhad8IofEygGApTpI4J/+mmDT/wIjfy8qPYelBJVvvpoSVdq0PnG7bUnN66uB7NZGZXKwZx9n7EM3X1w4+o8DoDAZ+rU9AvOyZhzMw5Kou+dGOftrDv89YGjmkcn3HFvBTeEy/l09FG3zssvhBCG0OVsfleGP2zGC9++eR+BAQCc/vXNf+UAmFtP51bU1n9SsRloU73BGmGxXyDDDJ3lJjw4TCHGADhCn9RI/51VjTAiIGGIZnFOfoQkVx0+i+cTMdS9Pb8i/0yFdcbzvnV7SuSBD/iIuLWsjzfLXYzajSfmuhZmWM4czDhWq02fOCPC63fkjNhn8P2TRIU17d24W2SQZyHO5xBcoetRyhUqlUIAUEwaU7R8o1YfL1UKdM1FO9ftdUufNjkm+A5aNMqYDdpOnt09ckyyxpcAAMDdw2P4vxVHRwT0vUycK00anfLzrwdCPM7PZKsCE2bOThc7jTtX/3SAFExPCj5fn5COnjk7QtKz29L3nI7uhqaO9q7MX8oAKL3NJLNTAKwMuwr6kWEMw7jWNfctdO1icHE5AACGD0pMXnegwAopAnCcKTgzfPIi96swJAJP5h/snTTvk6eTFK4CY1Nh3+MCkSc4TxoZhgcEgLW8vtEzTA4Amntnkfs/zrTT0z+KBRCPGZ+4dPHiVv/xMRr3lgKV/kzLnaN/sbD8OY5vWl3FG/rUM1Ov8nko9AhK8ggCW+eOAmzo5NBL/RjBbrEgDMMwY/PJdetLRz/+XJjizlHBAACA4z9oaFKI/KJCjpQnvGSuV+gRmxZVsXPXYQounAghJX4ekiLqovmwy0MK5G4Sr+T77gllU8//MfrTwwAuElMXeCr2N9sYdM+Dw/d++M+lPyb5OQ+e8V74edhVvZTxvOc8NvVv//uXrG0kF2s0OkZMvNDZ3iMkaXbKvldfW3rfuBh95dEq0di/TwgHAJFbQDBVud8y+e9+YgDwiomtn/d+yJI3VBxcOWF26KFl7/zLmhymGhQZeTWjYGG587BYLK3tBgraispMgaM4VT1LDwVBg4IEl29lbSo73mhSS4Sd1WdQ+PBB7tzu1pLV6089Mn+2vTirlPZQ8exni0rCh4/xcsdKdhVhnv5UW11JGwAQMrWPl0J8Fy6qiEgeXV31v+PnZJjZ0FpeUiLobjimlYwZFnC1vZBuySmxa4/tkVgj+aRWZwxKTvK5g1TbGwjx3nvvXVRUXVMdEBCAzvkk9pVZGIZVVVVGhIdf1AQnpENSYomuNgvfY8bjD2mkF2thAnd1WFion4fE9RMXSNWa8DBftVwWED1YTXZojTQjThmXrhTzA4JDNYEBcg+/0NAwX5UyOnWUL67tMtq56pgnn5yq5pEAgJO8kLCY5NFjB/vLcACe2DMqMebekfcoRSTOVw6/J5Fv6ei2Up6enn19AllY7hIYhikoKMAIXlhEhJ+PN5eD0T0QCrWCc6GcwUmeQqFwl0txDMNJwmEx2ymne8CQYVF+BABOcOUKDw8PGYfEzUYTTWOKkJjhg/0JDOeJ5VJ+b8+IJ3FzE/EGqgzDcLG7Sq1SiniEWK5Qe3iIuBdKEIxwV3ioVUoOiQMAxhMqPJQKqQAHwEiht7e3X2CQt1JG8IRiEYnRNE2KhyalBvS1RxEcmYdKrXDnneuYJ5Kp1Cq5VOyhUnso5SK5j5+cMFvtNM0NjgoT96MCs/QDdqltcOu27T4+3qjHnIjOx5xCCCGoq6ub9fBDv9etMXvtpvwOg2tH7Bf1wISREv5NXcFXW1trs9nU6tt9uRgLy3WHoqhNmzapVKqkpCRPT89Lcx2wsNwx9GNLTE9LdQWM6In423cDICxUcxXd8oJi40WWnkWPXImSRw7U9zMWFhYWltuWfmSYXC6/tPAPwvWNiPL9072wsLAAANh0WScqUtMTCZx9F2RhuQDWyMDCcttDYKbCDc989GuH8c6JhcHCcl1gZRgLy20PRzbp2ddT0eE3/7PJ4mAj7LGwnIeVYSwsAwGu4pnX3h3HzXluyTqD1fn79VlY7g7Y8KzXSHt7+5IlS1zOLzqdztvb++OPP+5NWYkQ2rdv3/bt2xmGQQg1NjbGx8dPnjz5p59++vTTT9mouCzXAld5/7zXHF99/I8vyHf+Ot1TzEZxYGHpT4aVlJS48nSgCwA+nz9kSPQV8lfdVahUqn//+9+u7aVLl4aFhfXNuYxh2Pjx48ePHw8Ara2tr7766rhx4/z9/SdPnsw6OrNcM4RANXvRPxzLPpi3jF713iPs4kcWln5kmMFgSEhIQL3rmxEAQHNzk8FgOHkyLyZmiEh0h4WW+VM0NzdXV1fPnTv3chW+/vrrqKio5ORko9EokUgAoLq6mqKo1tbWzs5Ob2/vYcOGcTjsgkaWq4Pr8eTL7yr+/dbsJdxvX5zuIWCDObDc1fSfAxPDcQxcie8xwHo2ORyOTOZ2prDw0iZ3LTRNr1+/Pi0tzc3Nrd8KJSUlhYWFDz30EIZhLS0tX3/9NU3T+/fvnz9/fnd3t0wm+/HHH/ft23eTh80yoHHaLVqzU+YmJVlXe5a7nivkD3Pt9PwnFkuamptpJ6036G/W2AYAer2+oqLigw8+wHGcYZjt+f1WBAAAIABJREFU27dXVFSQJDl16tSQkJDu7u5PPvnk2WefDQoK6tsKw7D09PRJkyaRJCmRSFatWjV27FjWSMtyVdhaVn6y5Khk8v/NH8faQ+4AKIvhTFHNoIRYAftGck1cLvfKhWmcMZBIJPHxCTiGZWRmXqYr1N1cuXrt6qEzX0sOEF50LH/dBwt/yNd4udkMzofeXjo1xpO44vdlN1Uv+ss7T3z2nxS/i9NiXoq+8fiCv33/7ndfhEquJlr+9aSwsFAmk7kshDiOJycnDxkyBMMwlUoFADt37sRxfOzYsRh2wdXiOK5UKl3zZwKBwGq1Msy1ZbRhubugjA0rly6p85624qnfEWAmu1NKMwDQUZF3KL+MogFxvcdNTFOLL7pHGG1deXZFx/iRaQIODpSlJD/7RGE7DpjnoLhRyYN6X6xsprrfftrqlLoTGCj8o0cMH8Jz6I8d2FVtYGgKH5w8Ij5iIMeodZqyt67jJjye5E1nb/v5jJYj45MUxolNHhNEnt2a2TBm5n3eIhzR1txdW3R+6SPd6j5emz/9sdkxPm4AYDdXrV9fOuWhSbLuM8vWHld5SBmz1T9pbFp0ILfX1GVu27B+ow53ExIAAEPH3Eflb6t1Sx4diuccPxkYF8PKsGvj8npYjwhDfZI5IwSXzR+Wu+GD9z5bc9LotXbaq5cetXXTsdMXLX9uRFXmZ698tCL1+3c8RFf6wZM85UN/eSxQdoUQ2+cRyAIf+8tDHrxb4OxXVlYWHx/fO5vlEl0uOjo6du7cuXDhwkvnuhBCZrOZYRiCINra2pRKJTsfxvL72NvWLP9XvmT88qfGiXm/Iy86m1tspPQeAF23PXnCTH8Z98z+9fuOlM++d0jvkxIhJnfPz1nHS/Tq5HH3AADqqs49WGaf9fAjUtS2bdXWosDgOM+eTMQ01U0JQmY+NKnXHdLU2SbUpD4S4U+1nFm37aCnz2P+kksHMkBAjNVooJ0IAFmN9kEjZ44KkbeXZP6yZ4/3UzO88fyyunbvQZ52Y3tZGzNxrBo1VFCm9iPZp0JmjRIDIIYyGEw0QuC0CZSD75+dTmpLV6856Of7WKji3K3NOC1mSH+8N38Y3RkZJ+EqcNDdsqu+I7iMDMN6YyRi59OtIDhXfilWK618a82+vYv/duXzKbz9CftxBgEga+bGX2q6AZShsyYMF3IJU0vp7oxj3TYISJo0KlzO4/ecqru5ZP/B43oHqGPHTI4LyNn1XVELgFLz8IRUV2xpHOdzuAgAumtP5baJ5Oai/FoDhmEpKSnX/LlcDSaTKScn5//ZO++wKK6ugZ8p2ysLLEvvXUQEQUUQLNhbLLGXRFOM8f3eFDVGjYmpxjSTmPLGxBiNJfYYNYpSFBVFqiCdpbddyvY68/2xuAIuaoqJZX5PHjPl3jt3Ljtz5px77jmvvmpDZhuNxk8++aS9vf3GjRslJSUA4OzsbJVwBEGcPn3awcEBx/G0tLQNGzZ092mkoLCBrmnLurVSj5nfrRx3L8XpZr2iUwcAAVFDLa6wYnfHjkxZ1zN9s1GS7TNnafTplGIAANJcVV7s4jfBgYMDuA4I4V/MrwjkO1eVt/qHBZgVKuDyuv9Oue6BAy3XcnTikWq5wuDBe6Ts4WIPHxHkNXawIuL67zt1OSZkYl3OVWFYrD0TNwDiHhHvrCo5l+k9Kcbr9rpMPp+OmM13Wo+O0Wgo2T3PFWluqS6tauok6aKBAwMeqaG8n9j06eiWQIwkeyZhIfvQw1jxTy4f4tXbhNgNU0drfUX59cM7j4c9OUvExsi6y9fUEn9/j7bU77b9dsNoqHtn1VttDCd/f25lUYtZr97x5YfFrSpDQ/ryVz7tZDn7+wtqiqsvf7/uu0yDl7+nSt5i0HWt9NR3Nmz7/PMGraE5a/+ChSsuyVj+/v6ctmt/elDuESaTuXr16l5zXRYwDFu4cOHatWv9/Px8fHx8fHycnZ29vLzWrVuH4ziGYRMnTgwPDw8MDNy4caOXl9f97irFw42h7cAXm+u8Zr69bPQ91tBjXEdxt+fRbKgtb5D4unUTYIAg7Jj4YUKrZyOC8gTC1oYagxlIs0Gl0uq1Oq2yJfNSno4ExGRqa7h+YM+u7T8db1Lqur96O+uqOzBHF/Gj9tZVylq0mJNYBHYugcHc1tyC0uw6PKq/+82XJjdy+KCGaxeatT0klVGvkrc2F13KIj37e4l62ldIU4e8tbW1tVXeaSbJpqKMzBvNNyuTHTXZv6YXcQRCg/Ty6Wt1hG1tgaI3NvUwopvsgu45xEgSyD85tPryrHP7kEqzUaRolKp0EXbuiQsGp/20/0xFbUXl+eynx0bWlzYN8Y+O6+8YB2BUtwEAgO78j9+4T3x9/vQQGkAcKA+/ugV3HRU1OGFEnM2roAFDxz05dbwDHaTu7jrd/c3njON44G2p1Lr6gaJBQUG3H7eWp9FoUVFRvebJKChsQ2Je8QunRYXfe8xfe2dHd0GXKZ4w6vPO/nxF4TIj3ueO9VGf/vG1yb/9fLDNkYtqmtTgADynoKefDQIA8I3773/iAIw1BemHfv591qKJDkwMANoqrx1OvhYQ+4TTo2MO1xddPKu+wVR1tIWPmuRMAwBB9MjwrVuPhs6Y7dIth5TIo98Q77y0ixVjo29VVrXVFuRgdIOZTmpkCq2b6NaECEnoKwpyFAwAhkNs7IAe1zR1XE676j90UT8/DjioPzmY2Rbq5sC833f6KGBThvXM49xNlgGCkL2TPN8jnKhxk9Y+G2/uqHtpweJjcTGeV97+rNx/3bPLYlwVHxYDzgza8OGyTz9/8TOV/ca1awf5sAAADIr8olrvkd43nw7u+Dd21L/93DOLvnAb8vSGZ5P4vfLUAWYndGM88J+Drq6uxntPUk5BwRBERQ+4e7Fu8JkYHUMAQKuoPnsozewVOm9qpPBui8loAufESfNUWgOCodLzLaV8+9teEDT3fgPp535WKPQOTOz6heTMgrZhMxf529/BBvPQQfcJHzTUU4jRGGx2lxhhOvqKHK6EuIl7FEQZ/UaOK/rueLFLf+sxO+fghKQ4Lmm+evT7lDzJgsRb2eQRjBOZkBRkc9bQpOtQKEtTj9RmApAmJxd3anbhHrEhwwiCALJXAueuXaR3Yuc/DILiDJzPobddTL0+Zf03kUFE5kWCIABBEO/Y2V8Mm15yZMvyLXu//2QJAADO8vYWp1RUEoNCUATMZgJnCVa8v//phpyli95ISYqZ6MM1I91vgVAqZDoDyaMjpFkO8ID6Ho8bd09TGhQUfxnyyonfdF7xT4zof08uTySJ0pgCOotQNVa00PsPc8NIwmQmMRwDkgBAEQQIlUxJMHEca6+6ej5PPW7BTC/+I6YvIEwO/7YVnwiCo9hthhOM7jxooPi3tMtG6CneAMVxGoN5z45mNK7YXugYPm5kiAiAJAig4vncI7b0MOitanWXW39WhGkK0o58Zb6urrzQGDV7dJCfy+i4TR9vUEaKrp9L1XtHG3Q57y0/6holaS6Xjpn8jL3FARjlTX1+9f4176wtGuDhrDPZxQmrr6j4PINWxQobOMAFOfnO7J85K7bOl9y8ClF58eTWzwzOHHpLVtrsVW/+ub5SUDzsdHZ2KjUwIKapuFztLGq7fOECAADwwmPDeX3bEzW115NvNIk4rM7GGsGghAAe3tmQ/93OzCWvPq3LOZ3ZyXVk6OsqG2OSxruKIO9iqZnnWJefVQcAgDt5B/q52j2GxnG/qBGhpd+e68r4C52tlZkXEIayrlDjPCnO615bwXhD4mJ2JR8nW3yYeLuJFhUX40ypYvcCcrtedSY5eXh8PEHYkFYoipw8dWrq5Ml9tGZqkEp5Eh8es/cnhKq1+oa0BQBQnO4bHC5kAhg783NLjThD4ijQklwvV2bZtSIVADDswkJ9GAhRXVlu7+7HY+DqtrryikYDgItfCKOjvkrWCSgu8Qxwc2B11le2YWIPe5pUWufm41t7+I1V6b4blkWYdAaFgnR15Ts5Of31MaKgeLgwGo179+7l8kSjxsTRjaQBsT6PdCcPSe8FYiZdW6dWJLJDESAM6ubWNqOZpLOFjg58DMBs1LTKNA4SB7Na3tymBgCMLXR14AOQmg65XKG5+ZZAOXb2Ih7rYZVhpLlTLkN5Yh6dVMhlCE/E67VWhzTJWtp49g4MHAUAQqeQazF7O45lZLWdrXIdJnG0w03q2qY2y5jwHVyE7G6NmA1yeQfHXsy8KZp0CpkauEI2Kpd3isSOOBCd8uZOjREARBIPKqTzPWJDhh05clQgFHYF+r0V+BdIkiBJkLfJ582Zc7dm24998nV6vdyyw/eLeXHhE3bs+/5VUXZg/aqMsJ2fzOIBSKVSnU5HyTCKxxCj0Xj48GGxWBwTEyORSKgw0xSPMDZsiePHj+sVNuLmWjEAgHt7HgSjnnp+mLmrEZTG4P8jkUk5LkHR/VyovCYUFBQUjwk2Xvh/R+A+lC0Q/vOOSi5D57029B+/KgXF/YYk9AYjg/FPh1KjoHjwoYwMFBQPPJrGb9/ZcCq/+d/uBwXFAwclwygoHnjYTnPnjdz90dtHMiv/7a5QUDxYUDKMguKBB8HtA5Pe/0/igc83nyps/bd7Q0HxAEE5QPwlDAZDZmamTCYDAC8vr+Dg4JycnKamJgBgs9nDhg2z5rxua2u7ePGi0WhEUXTQoEEuLi7WRpRKZUZGhlarxXF86NChfD4/Ozu7X79+lromkyknJycgIMCy6JIgiNzcXBqN1q9fPypU1WOF68Bpn28UvLB+rf6/66ZEe/7b3aGgeCCwoYdlZ2dfunTp4sWLGRkZFy5cOH/+Qnp6+rlzKRkZGUql6p/v4gOLQqF47733MjMzeTwei8XKzs5WKpXbtm1TqVR8Pr+goOCjjz7S6/UkSZaUlKxatUqr1fL5fJlMVlNTY22kvr7+nXfe6ejo4PP5crlcKpWq1eovvvjCIhcBQK/Xf/PNN3V1dZbd9vb2b7/99ssvv1Qqlf/CPVP8myB2vgkfrZl4+OtPfr5WS2Wco6AAm3qYXq+Pjo4GuJUCEwAa6usUCkVefl5YWJiAz/8nu/hgQhDE1q1b3d3dn3rqKetBhUKBYdjQoUN9fX3Dw8NXrlxZX1/P5XLfe++9VatWhYSE9GqEJMmUlBQmkzl79mzrwY6OO2XKzsrK8vX1lUqlN27ciImJ+XtviuJBB8Gcw6d88BK28q03sI2bp4c4UIYUisccm7lXSBKAIEiiGyRJ6vV6Dpudk539z/fyAUShUBQVFSUmJto8S5JkZWUlj8cTiURXr151cnIKDg6+vRiCIL6+voWFhRkZGXfONWSBIIisrKzo6OikpKTMzEwq+/PjiVPwyA3TvT7/Ykd9BxU5muJxp+88zjfTOFuOCYRChUJJEGalSv0Pdu/BRS6XkyQpFAp7HTcajZs2beLz+WKx+NlnnxUKhRUVFe7u7n3NXUVHR8+ePXv9+vWRkZHPPfecr6+vpZE333yTy+XCzfkwS+GmpqbS0tKlS5daAjHIZLLumaMpHhPqc4+/9kvd2s2b3YSPTr6TxxaDSp6RWTgoMY57z4l1KLpjW4aR3UNzkCQgwGaxAwIDUQRpbrHhFmXsqN3+/jtnWwyIWuM5bM7bL07ptRqz8Njbb50V7/7kGfzPO0Iqc1KyXWOGi9kAhLHsauoXWza38NxZYOjA3VY89+zwCG/sH/wN0Ol0m8mXaTTa66+/zuPxVq5c+cQTTwAAg8EwmUx9tYNh2PTp06dNm7Zr165ly5Z9+OGHvr6+NBpt/fr1np6eAKBWq//v//4PAEiSTE5ONhgMZ8+eJUmys7MzJSVl1qxZlGfHYwRpqrr486vf5K/44IMkn97fT91pVxs4RjMA1GanpN6oxVFEreclTR3rJeoVe8BUX5iVXNIxc2ISm46CvvPyhd/zKnR0MHE9QyeOibEmv9J2lv/09SG6iysNBXuPsPih/WnqpuTfTjQRDKNK5xM5PCHK7yE2bBoVZ/Zspw97YbiH+cyer/LVdhIeXaPTBQwaM0BY//OvxeMXzPfkY6RJlbr/Z3Xw+FG80tXfZjz57AtDfUUAoFPd+P77vCefnmHffvWNHZd9vMWmdrlowIgxQ/rdCrGnrP/xh11qvpuABgAQMXKyKmNPuShhYhijuLCk//BhlAz7c/Sth5E3FTHk1jYJiM08znqlNnjqC4sHh0Fr3ppla85OmDjep9f7nbQVQ/iPoCz/5qOtC74eLmaDrOrc6rd/Wb72q/ghfnQwVVw6+eb6NfTt3w2T2MzMc19wdHRkMBi1tbV2dna9TqEoKhaLZ82a9f3337/11lv9+vU7cOCAVqtlsVg2m7JUWbBggVqtPnfunCUxNIqilrBeKIpapJTFffHJJ590dHQEgKSkpJSUlKlTp1LhGx4XSGNN9q9rvsl+cfXq4b69f3W9UDY3VuD8EQAky2H89GGObLwk43BKxo3FkyKtb0qSNKUe/F9eeWun0JL+imwszsyT289dlMAi237/+WCONHSoF9dSmDCrGZKw6U+Os8ai1Wj0fvGTRrs6mttK9h04L/X19XuYw9Z3S1nPGDh6aqKvXUdF5u7fz/ountNfcuN6Wa1npJemraHW5DA5xBlqyuz59JwLlwI8xjrQsO7JqsReUdPnxTFUFbt3pNQGBgQ63gp7hGC8EdPn3cwfRijjJ3nRhJip5Z++1UcLG2oRQVh0MGvy5h7OHTbzOHPdA4YPDmMCMIUOLgxDQ5v+9jIWSi/sP3Hh8g8fvf/Gxo3nK9UAoK3N2rU/Levs7jfeeOP9T7ZVdACA4Xry3t8LLY556qN7fiquaT78/bbM0qLtH71xOKfmwt49nlOXJQzxowMA4L5Dxiwbw/9x71WtQb735z1NCsvV76/Nk8FgzJgx48svvywsLAQAo9GYm5tr1bdQFB0/fnxHR8fFixcjIyOdnZ3fffddiydhfX19bW2ttZ28vDyLL75arS4uLnZ1de1Lr5JKpQiCJCUlxcbGxsbGTp06tbOzs6WFegAeF6ou7X3l07QXN7wxPNT5roVxwqjRGAHAIzjMkc0AwPgivqZT2TOvksnRd8jshbM8LAtASHN9bZWjeyCPgeFMxxA/QVlxlVLZlHH+mpYkzUoNsLndTQ9siae/qyMOwOAJmKRepe3T2PCQIhRLuEiHXEnvF9O/NvOqAoxVeTkOYTF8BgaAOAXH+NDq0q5U2cxsT6PTUYS84wJcVK9sampXd8trZaopunLqxIkT57L7fIFS3MYdhrhL/7o5I2YVZHdSpxpyL2aoghLC+4yVWJ72/fLXv/cfO+PpJO/1a1aXykya2msbX//v6Wb3pUuXDmBXvbT+w3a9vjBl35kbFhmmObZ/l1QBw8dN8Xf3mjRn6XBfY0FuS0R4UDcVkh4Y3q/+WpHM0LZ/7/5mhQEA7rcMs4iTF1988YcfflixYsV///vfoqIiGo0WGhpq0bfYbPa8efNSU1NxHH/xxRcjIiLWrl27YsWK9957T6FQWBohSbKuru7NN99csWLFmjVrRo4cOWPGDDqdHhoaymR25RXEMCw4OJjL5ZaWlo4cOdJ6XCwWJyUl3bhx477eJsUDAWGovbpv1Tf5L7z22jC/u2hgFvQ0oYukWw5Yg6qksM4jyKv7BxKCMPtFDOAxbsolBBU5ODVWFauNQBg0Ta3tRr3BYNA01jebSEAB13eWHdy7c9vXe8qaOrs5IJEtpTc6GG6ekkdtck5WX21kebs5At8lcKCT8uKF7JwWfkyYy82XJjtyRHx7Tmqtqofw1iiay0tuXPg9nRY0xLdnHmySMNSVl5SUlJRU1BkIUl6Zd72q7aZdi2gqvvB7bltYZJSHueRQWpnxr9mtHh9s2hKJboo1dE+BSZK29TBLrbrLe1d9sifhuXf97vBjxtgJE5+ICvZjIC5BW7aXt8jtATxCRs+eFu/OAodpy3YfXFOmXdKrEoJiIkcnDpMldnEXITdatXo/vIetEkUx0tRHz+4bGIb169dvy5Yt3Q+++uqr1u3ExESL4yKO40888YRleqw7CIJMmDBhwoQJ3Q/S6fQ1a9ZYd5lM5ssvvwwAlumx7ldfsqT3QFE8mmhbj/1e/N91a4b6299jDbGzyIVrMTKTJp368vEdpVj4zBD3O1ZCPcPiB8qP7/xptx2fw9YiiAC49j4zZvsAAHgOembpIABTS9XVAwfPzFg8VczBSZJsLkw7lFERPeoJu0cn5o8u+8zhhssMksRjksbbowDA6Z8w8LMPT4TPW2CP3/oK4In9hgVnpacXTYy/9cozm/QqpZopEpvrpdJWbz+n7tnkCY1KqTQD0NDecyvG9muZhcFxiyQOLEl4wJmDuR3R/o59Tj5Q3MKGDCN6qVrdZBkgSB96mCp5+5bP9tSv37kvxvWOAesxjGcnxFAAksnCjTqTGQCYTCfLVBGGYnQjorvzzBnP2d+Rnp1XMmtA5E05Ziy7fl0S+cSd5rgpKB5eOK4vrHvjj9WgoziGAIBSVvzrvguOQ5IWDwyg303MYBzRkAkLhwAAmPNP/kjY365b4Y5eIQxztkqtF3MMmSeOFTTgTyxaKmH+od494DAHjp6W2HPGkS70ELkIgyQ9vyFQWtDIyde/2p1XEW49xhN5DIiK4gLQT2w/X1Dl59TPegpBmQEDooJsztqbDUqVSpr+W30WAIB/sDfj0fkmuL/YWh9GEJYpypvJLwF6THjaEDB1Vw7/73Drm/s+jb6zAOuDzraKxlYdALTUXW+VuPszeC4ugpaaWh1BquVl1ZaIBBiGAUkQBIBwyovziw/tyKtoJQAAiMaiyzt+bZo9YxAbEzkxOms7NABmtbz8T/SEguLRwnTx+FlhzMhRUXcXYABAGA06oxkA9K0Vxa2Cgf0lYNK1yTvMACa91kAAAKFtqlKiQiYDby68mNfEmzR/yqMlwP4ogsHDAvPPX+wdwcisV2gRkZBjs44NGHwPFweP/sNmznryySenJ0aF8yhXrXujL9/6bju9ztqw2JFVuVfrOxv3f/jWfgAALCT2ydmTw+/9T6Btrd6x5c19QDTeqJuz/h0nNlMwbukXr2x6ufYUn21WMEkAAL7P0ADWZ2++1Lh89ayIGW+voH/77kq6gwcd9FoDZ8zqd0d62uGkad74qPfe23DejS4UOU2bMvCeu0BB8Ughl8ub5fr+MR5V1QoOO/94YyEAANgNnxwn7Hsxhq6x+NjVEhZON2kNnnGJHkyss6Hwh52ZS159Wpt3NrnGLKQZ2zrMI8ePcRJA3vkalYGeefoEAADQPPpFhvs6PYbKg1vwkAEF+adurjmS1RWcOtpG07TKOUGTg+5svO0GwomMjd138uTBakc6phS6jx02kPFPJA5++EFu16vOJCcPj4/vMtf2NB2iKHLy1Kmpkyf3qmLUqRRKrdXpns7i87mM7g+K2aBRG1A+l2nQKAwoi8ukAYBK0UFj81VX/rfgU8XW/y0VGEwYzhLYcTEAIEm1sl2jN9NYHMxsZHB4dBw1apUdKh2TZ8dj4gCgVchVegIAGBwBn93lwEqa9O2dSjNByjqViMng5OT094wTBcXDg9FoPHDggMjeMS5usJArIG/lXkdZXPZtq17MeoOJwWAgCJBmk1anI0jAcDqTSUcASMKk1ZmYbCZp1Gn1JgBAcDqHSQcgTQa9zmB1Z0BwBoNJe3hXiJEGnQ6hsWiYZYNJ673alNBp9TQGE0MRACDNRp0JmAyapZDJoNObERaTgZJGlabLqZDO5NC7TZ4BSeh0ehqTZW3YbNCZEBodA53eyGAxUSANOq3BRAAAg82lPYafA38KG785rVZ3LiWFJIEkiZv/ktZdnV53exUak2vP5HY7IN+z8Y0zNV1u33bBw19bPs+BiwMAnc23Lpfg8oUAoAIABOMI7By7t4ggHL6olx5OY/EcWbdsySy+/e1TngjOENkzAECtVuv68PU1k/DU0TvFJLwDThx082gqXCTFgw6GYQw6jgDG4nJR9E6vQwTFmMwuuYZgOJvD7XkWZ7NxAAAak9tjcgzB6UzuX0/5/qCA0Jmsnhu9QJnd1nciGI3V7VsApzO73qQIjcvtw6UN6dECAGD0rnFndbWF0JnsR2dE/ylsyLDJkyb+5Wbt52x8f869FWU595syznDPZuO/AZKEX0t7L8DAEAhwZES7M9OrNCIW5udAv1qrrWzrHY/O247S7ykoKCgeFP593Z/tHfus97/ZAQaOuPLxmWH8Z6KFrnx85s/1QY70jaMcazuN76bIUys1jUqT0Uwt1qCgoKB44Pj3Zdi/hR0LWxDBZ9PQYDE9zpvtIexhAGfTkEAH+nfTJaWtxsu12hsteqOZ3Hqx/d/rLwUFBQVFbx5fGebIwT6eIEYQQPt206KhSKgTPdSJbiZIkgRKhlFQUFA8UDy+MgxBALvnQNEYivzFkMUUFBQUFH87lP/mw0d+fn5OTo7Nxeb/Io2Njdu3b8/MzPyLHdNqtT///PPx48fvJSmoFZIkr1y5Yom/TEFB8fhgQw+7dOmS5TXU5VlPkJYkzjiOhYeHi0QiKmEVAJAkKZVK9+7dW19fbzQaw8PDly9f/rdfxWw2b9y4cezYsUOGDKmurnZ2dmYymVeuXDEYDOHh4bf/IVpbW1evXp2QkDBv3jxLejOSJH/99ddjx4699957169fv3Dhwtq1a21mPvsrkCT5xRdfRERE+Pn5KRQKpVLp5ubW/ez333+flpbG5/NJknRzc5s5c6a3t/ft3SBJ8tChQw0NDcOHD7+zR/jtFdPT0yUSSWho6N9zSxQUFA8Dtm2JMTExpDVGBwkA0NBQr1Kpbty4ERIaKrotY9ZjiF6vf/fdd+fNm5eQkKDVahsaGu7HVVAUHT16tKenp1qtfvfdd9euXWvJLtYXZrO5vr7+5MmTkydPtuSY1mg0Z86cqaurM5vNPj6KiPpFAAAgAElEQVQ+NBrtD8mGe8RkMrW2tkZGRtrb2x8/fjwnJ2f9+vXWsyRJKhSK+fPnJyUlEQRx9uzZV199ddOmTf369evVDkEQZWVlo0aNcnV1/ds7SUFB8ejRZ6wpy/pmsKYNI8m2tjYajXblypWxY8b8w728H5S2GujrSm4/bibI34rh04y7uG8YDIba2lqRSAQALBbL19cXAEiSLC0tzc/PR1E0JiaGw+FcuHBBq9V6eXlFR0crFIqCggKhUFhUVOTs7DxkyBCrIlJTU6NUKkNCQgwGw5UrV/r378/n8/Pz8x0cHHg8HoqiaWlpVVVVJ06cGDFihOXqycnJHR0dAwYMCAgI6N4xoVDI4XCuXLmSlJQEAMXFxSaTSSwWW/ppyQtDkmRBQUFxcTGDwRgyZIhUKmWz2VKpNDExkcPhpKamtrS00Gi0UaNG8Xg8AMjPzy8uLmaz2bGxsXZ2dhqNJj09XaFQcLncMWPGEASRkZHR0NBw9uzZ8PDwjIwMqVR68uTJuLg4LrfHglkAQFF01KhRjY2NO3bs2Lx5s9lsvnjxYnNzs7e3d1RUVF5eXmlpKYvFEolEISEhRUVFhYWFHA5n5MiROI5nZmba29sXFBTw+fzY2FgOh0OSZElJSX5+PpvN1ul01j/N+fPn5XJ5QEBAeHh4S0uLVCo1GAwCgSAsLIyyIlBQPErYivl7U3jBzX8ASJG9vaubm6NYTJht5HEGMHU0N9bU1NQ0NGkMNqYx9Kq2Ggu1de0q/R+dMFHLr25c/ZlMZdQpZDKF7m+ZCHLh478ucju5xL3XfzHurBlh/NuPH13o1r06l8udMGHC22+/feTIkY6OrqgfGRkZW7dudXBwYLFYVVVVpaWlJpPJwcHhp59+KiwsbGxsXLt2bUZGhkAg+PHHH69du2Ztra2tbdu2bWq1uqys7K233rp69aper9+xY0dnZ+fevXuvX78uFAqZTKaDg4PlxX369GmDwUCS5Ntvv93Y2Ni9YzQaLSkp6cyZM3q93mQynT17dsSIEZZczyUlJbt37zabzcePH9+xY4dEIiFJsr6+/rPPPvvxxx/FYrHJZPrqq68uX77s5OTU2Ni4efNmSxrPXbt2icVirVbb2tqqUqk++OCD6upqiUSSnZ29bds2g8Fg7R6fzxcIBBwOx8HBoS+LJYIgwcHBcrlcr9cfOnQoOTlZLBbv27cvNzeXx+NxOByRSMThcCorKz///HMWi5Wfn3/o0CGL4rtz505HR8fU1NQDBw4AQFpa2hdffOHk5EQQRHJyMkEQJEnu2bPn4sWLjo6OP/74Y1FRUXFx8fr165uamizy+DHhVrYJs1Gp6Ghvb1eo+3juSEKru5UrwmzUdbS3t7d3WoL/ditlUnW2W1CotJawqXqNsr29vb1DabT9Wnh4IAmdWqk3kQCkTq2w3GaHQmUmSLNBq1Sqby4QJQ1atVpnIk269g6lddkoSRpVSg1BApj1XWPU3qE39RwT0qxW3hzB9nadiTBoVGqdSdfZfOzwb4qHfQD/PfrSw0irFAOSBAQYdIaLiyuKIOXlFbdX0bdkf/PpcS0Dra0qwMOXfPNS70gfOXveenpP84z4QKOuvbpesO7zNcHCPxDh3qhvy88p0Zm0Odue/4Zc9tPrSX89sY7BTAoY2GCP3jG3P+NgnkJ8pG/v7h0p6hGZGkXRF198MSYm5scff/zhhx82btwYFhZ29OjRRYsWRUdHW8qQJJmZmZment7Y2JibmxsZGSkQCGbNmiUQCGQy2fnz5wcNGmRRC0JDQw0GQ0NDQ1FRUWxs7I0bN/z8/Mxms0W9sxRwcHCIjo728PAAgJiYmDFjxmAYdu7cufr6emfnW4l9EQQZNGhQWlpaUVERj8eTyWRPPfXU6dOnbw2m0XjixIkXX3wxJCTEcoTBYEyYMCE6OjovLy8rK+ubb77BcTwuLm7t2rWZmZmdnZ0AEB0dzWazAeDgwYM0Gm3ZsmUoig4YMGDlypXjx48PDQ2VSCRRUVFubm7+/v56vX7QoEF3GHwajUYQRFtb2/Hjx9955x0PD4/GxsZTp06tWrXK3d09IiJCIpFs2LBh1qxZiYmJYWFhGzZsiI+PZ7FYU6dOHTRoEJ1O371795w5cw4dOjR37tyhQ4eaTKa8vDwURdva2k6fPr1lyxZnZ+eKiopz587179/f29t7ypQpdPpjFMdH1qljC80AUJGZfLVJa8emNTdqh0wcH+TUK1KaqeJqanKlYcETY9l0FDSy1LOn6lU8Hmi0TMnkaYlWPVqnrNzz3UnHAH86BgKJf2S4P9pZffJkGmnnoJe3cj0jx8T3e4iTYJpU6Qe+o8etSPAwpx/cXo55eNmx2uWNQv+E4V6Knw/kjZ4/30eIEwZV6v6fkUFT4miFb3yT9sSylQmBDgCgV5X/+H3u7KUz7duzv/g5L6yfh7G51uwaMWFENM/6ilU1HfhhN+LRz4EOABAUEy9L3V1ulzixP6O+toHKePmnsS3DgLRG+yVv5nMGizQjSRvfCzRhv+UbBvBYdEVZyvxndxa9ODGk98+Z3m/E7A2vT0GM7dtWzD6cVh88xf+P95Y57IVtA0ju35LqQa4x78rpHOjKoPcO7mmDDh3xQ5aNEIvR0dHh4eHHjh3bsmXLxx9/3NraahUnRqNx48aNfD5/zpw5anVXUmmLjoIgCJvN1mq1BEFYlBUajRYcHJybm1tZWZmYmJiamlpQUBAQEGDztYsgiKOjI4ZhKIrSaDS9vnfcLA6HM3bs2HPnztFotIiICA6nRySvjo4OlUrl4OBgPcJgMCw2RoVCwWQyLV1CUdTNza29vX3KlCnt7e0rV6709/d/5plnZDKZnZ2dZVKNwWAIhULr3d0jJElWV1d7eHhYTK+bNm1iMBgajSY2NtZaxmg0Njc3f//99wcPHjSbzRKJBEVRNpttmeRjMplGo1Gv1ysUCssRFEUtt6BWq4uLi9944w06na5Wq0eNGgUAPB7vb3djecDRyRrLcP4oAL57yOQYDx4Nrbp2/Mz5wsDpQ6zGVJIw/PbjVmkndLL9AACAkF6/WEX4Lpg5mAaKlL17rhQPSAyysxQnjBq6Y9DosWM4Nx9tLckcPPEJsYBLqKT7dieXhwQHOzwag0wPHjwi0ddOXZ+3+0hKa+iSKO/CnOsVPsMC1a3VTXT3J/zFIL3hLHG4npbi5z7Vjd3jZSdyCR01Po5lqN3z7ana8PAQp1sJPBCMGz1y/M38YaTruLmhKBNR3Zep9McHWzkwCYsORgIgAFYBZkmBaTuPM0pnW/4uDAaH5cSl960WoySiI5g4AwEgs3/96rvDWVq7sI0bn/fkMWqyjm7dfqxNTw6YtfrFsUEIQEddzrYtn5cruNHjAkkAAERecOxwW8ySRKefvt8ZGOh4ZH8q4jPo1RVL3YQ0kuw8/fkX+3Ir7FxCo93Reodh40PvZDsiSNiVq1gUKRjkdneZeKpEdbZC0+sgSZIIgjAYjNDQ0N27d+M4zuVyW1pa3N3dAaCjo6Ompub999+XSCT3Mgfj7+9//vx5NpsdHBz866+/ZmVljRgx4k9P3kREROzbt4/H402c2FsnZrPZNBqtvb3dMknWHctcl9FopNPpJpOpuro6JCSExWI9++yzCxcufP3110+fPu3i4nLt2jWz2YxhmEaj6ejo4PP/WBBkpVJ57NixJUuWCIXCwMDA1157zcfHBwBI0pIfDgCATqe7u7vHxsaOHTvWcso63WUFwzA6nd7S0hISEmI0GhsbG8ViMZ/PDw4O3rBhg5ubm8UpKT093VrFcgRBEIIgUBS17v6h/j8UoKTZaCQAQOzu2fXBwaQZDT3jfyIQOmxqDNd8PPkGAABJyFoa7cQRDBwBEPh6CVOrajudVJcyKuPHx5vVWpLJAiAIErGEBWDZO1nMISidjoPJaHrUVAkOT0BDVEotFhARnnUouy3Wuzov37nfSA4N1QMi8o7wI0ouXCmfNTz49roYQZhRBMfusAAXaavKkyJ+YdankDCWZadnlTQRLPdp0+LYj+LP8n5wpyG2iC+rxffm/2z/UiuvHjuX1yKrrR3zzAo/G6nDjFVZZ7Z/12qSN5d7TXp7mGtd2ufrD6u/+XibLv2jlZv27nx7voywe+WDbyV82X8mPXXcdWcCM3PRK/tf2PzJ2kDs8PoXi4ELAO2VF9Nq3ecOZZ/fuTFr4eEvt//v5AfzX/ve66eXxh18/4Xd6nGHv3+9rercsjHzmMvD7yzDAKBTZ37+SNOeOS7+9n1amUiAa/W6V060qA09JHNbW9tLL72UmJiIomhBQcHMmTPt7e3nzp378ccfjx492mg0hoSEuLm5bd++3d7e/sqVK/7+d9E7Bw4cuGfPntmzZzs4OAwYMGDXrl3PP/+89SyPx/Pz89u9e/eUKVPu3I4FZ2fnQYMGqdVqT09Pg8HQ/RSHw5k5c+Y777wzevRorVbbXfsJCAhISEh46aWXoqOjpVKpj49PfHz8b7/9VlVVJRAIMAwLDw93d3fPzc194403AgMDr1+/Pn36dA8Pj+5rufz9/U+cOHH06NHExESreCMIIjU1tbm5Wa/Xl5aWLlq0KDY2FkGQiRMnWpzyFQrF0KFD+/fvbylPp9OXLl361ltv1dTUYBjG5/MnTJjQ6x7pdPq8efM+//zzmpoavV6fl5cXHh4uEAiSkpK2bt0aFhbW2dmZmJhoLW82m9955x0XF5fBgwe//vrru3bt2rx5s7+//4IFCx49MWZgOHi4dNO/te05OTX+4RO73yiC0L39/dTyspv7mJOL+8W87I4Idx7ZWVHdZOL6kwiCYQgA4DiHYS48dmB3c6M2bsqUcF+nrncHSdbkZ7dz/Hwkj1rAhIbKErMg1EsMPAiI9ck+dyJdqXSaEeZ0cwgZA0ePPvrT8bL+fp7dNDGFrCrrEqoov84eMDqgp2JKEtqirEvtTAC63YABAYrG8ipUHCq2vC7NNTm/p1Ty58+c1X7t6O4T+QvHhVOpnO8Fm7ZEomcizFubJGlbDwMAvtgrONi+ldZ5aM8vowa/5sHqZVVAeWK34GDnE5/+7v30m3a44ovtByImbNW01ICDpzn/VGX7Ijdn4YkvVqWXd+TWt/TraMstPC0ePGNkoAgAEpbO9Ms82aM9p8jF06OZCDYgOva7XwqUEJqW3vnsR+MBQOQ5cMqogcn3dv+5jfrnDzfvmu0i4dowg5AAhc36Zw41NSh753Hh8/krVqywvLujo6P9/PwAYMiQIa6urk1NTTiOh4aGBgcHl5eXczicCRMmcDgcLpe7fv16HMcBID4+PjIysrubu0QiefPNNy1Gs8mTJ0dFRVnMfc8//7xQKMRxfPny5WVlZfb29pMmTbKoEQDw0ksvdbcKikSi9evX29nZYRi2ePFig8GAYRiDwVi9erVIJAoPD3dzc8MwbOzYsf7+/nK5nMlk+vn5vfLKKxadjE6nL1y4MCIiQqvV9u/fPyQkBMfxQYMGOTo6kiQZHx/v4eGBIMgrr7xSXFxsMBgiIyODg4MRBEEQ5KWXXrI0EhIS8sorrxgMBqshFEXRJ598sqGhwaK5Tp482aoCTps2LSQkRK1Ws1isoKAgFEWXLFliZ2cHAJ6enuvXr29ubgaA4OBgJpO5bt06y7KzgICAVatWYRgWFxfn5uYmk8kEAsG4ceMYDAaCILNnzy4uLtZqtRwOJyAgwN3d3dOzSxdZsmQJnU7n8Xjvv/8+m81etmwZk8l89AQYALg4C8RdeTzMytam878fUDjHTw6U3LES4hoaP1Kd/Mu+3Xy+0I7GQVCULXRLGucGAODaf86c/gBmRUvh7r1nXRbPdObTTAZ1+eXk1Gp94sjhvT1QH2J02WcON1xm0NiikWOH8wEAGAFxMb+/dyRy0aLu38VMgVtCtHPKuat2o4XWg3Qmz9HJ2UPIuHTtSp6LXbjXrZVICILZOTo5sQEwNt7rV2doy8mt9I6crupop9mLlTnFnbpw8R/wGXh8sW1L7J7+srsoQxCE6CMKg4NnfwdPgGiv0t8WHLry7P8Nd+x5HnPwCB4aOyFUgMx75c3RIZuUan3ppZMHKwEAxj05yV6b/9Ky5xLX7vp+re+mp4cDkDq1hs7kdOXVodFvm1/jcOgoAGA4jpgMZtDotTjLUgpF6fg9zHEBAICZIM9Vqpf80rhtqpO3Xe+LZNfrnjvclNNgI2UajuNRUVG9DiII4unp6enpadllMplW/w4LVj94kUhk8cu/NUAYZtXV+Hy+VYPx8vKyVomJiel1RYsVzgqdTrdeQiAQWDZQFLWIWDqdbm3Wz8/PchAArJ4jlluwKkMWxGJxL6sji8WKiIjodePWnuA4Hhzc27ri5ubWfdWzFRqN1muVmMUSa8HLy8t6+wBgHR8Oh2PpM4Igvr6+3ftvuc3ut0Cj0ax3bW3c0kOLg8wjCQNHLKHU2hvyjx7KDRo1dXSQx13TKqIMbmjc1NA4ADDl/bbTIHG+zU0D4zl60uG8VmcAvu780cN1ZqeZT07p25DxMMIcOHpaom+PVbA4W8yX8L1Egh4FEcwrZrQob2du2a3fMJPr4OnjwwUfTXXB1fL67jIMELqzp4+PTfMQYdLp9B1VRdAKABAd04/zEHvI/KP06Vt/07Gj28Gbm7dXaWtp7FDpAUDZXFulYgZ72vd1Pbvg4UtikG/3FQ4bGY65R/znlddee23lpPhEe3qjnAiJ7++parqaW2YAwLyCAoqzzpa0acGsvn78VO5dbkTi6qo+fikPANS1xb9eK+wj/6UNSBJOl6mm7qw7Vaq2OsuqDcTB68pJP9ZdsyXAKCgeEvRpx9J9Ro0dEnJ3AQYAZq1KoTMCgKI6P79NHB3uROgVVZW1RhL0ynaNCQDM7RUFSrqEy6bVXk0pN3pMmjH60RJgfxRe7IjIkvQLvT2+DMqGDpPEUWizjg2YogBvJ5ajd+LI0aNHxwV7eLIoGXZv9LnG+dZOr7O2bImtRcmf/HjSgDCNCBk1d12CV+/HBcPpFv8/BOeMXzh/19JdbW+96L3nk8VL9nPpyohxbz07beCIgB/XL18i9PKmCxg0DPNPWLig+P1XFi5x9HAL9mX4MwFBAMXpDBqGICiDybQE7EUxGpNOBxAue3XFK299/FTKdp67vwNf1PFHDEQECflN+oX7G1YOFXXqiGaV+dUTLT/nKTp11KINioeSlpaWmkZVWIynTKaRXT5Xn2N5JB3Gzk2y7/loIAiC412GdIOs8lh6LgIYjvMHjo4X40hna82xw1kL/2+hpjjjeFEnFzdpSeGUKaMcuJAv6+iUtfy2rx4AAOg+A2Njgl0e1hkcBDCchiEIgGXDRgkajXZr5FCMhneFDHfwHhDtnX2yEUcQBFC0rTb74O4aXN+BesSOD3Du3gKO490bRjAcQxEEQXAajgCj3+Dh5SfO7K7KxFGt54CZQ3tZsij6ALk9QuuZ5OTh8cPJ208AIAhy8tTJqZMn/zOd+5MYWj955mnVtPdnBqJOTk63nzcRIN7S/Ofa9rbDri1zuHs5Cop/D6PRePjwYbFYHBMTY5lh/bd7REFxv7DtSnQuJQVIkrDEnCLIWwB5b8+DfM/GD8/UtFh27IKHv7Z8ngPn/rotnT/8eStvsJ+Y0XDlSLogfq0/E8BgsySGQspCkc1Td4VxrxNtFBQUFBT3HRt62ENKw/XUo2dydAA8+4ApT05QN0p1Op1NPYyC4tGG0sMoHh8enSUdLv0Snu+XYN39Y6EjKCgoKCgeQh4dGfaHuD0+EwXFQ8d9yqRDQfEQ8TjKMJIkr1+//m/3goLirxIYGHh7dhsKiseKx1GGIQgSGRn5b/eCgoKCguKvQhkiKCgoKCgeVmzoYampqZZIdwRBdCV0JkmNRg2A9O8f5uLi8kjGl6OgoKCgeOiwIcMYDEZ0dDR5M2a9xfe+saFeo9HU1tVhGCaR3DlyKAUFBQUFxT+B7XiJpOXfntTW1qpVqmvXsv/5XlJQUFBQUNxO33mce0StJ8ViMZvDRQCuXbt2h+YUTRXFciw61Kv38cay3LJGAEBxul+/SAn/j8WzVLacX70qecPn6yW8OzqhkERrdXFpjcwMoFarvb29/9BVKCgeUMz6+qZ2FxfJvVvxrQG7CYOmsaVVZyQYXHsXJ+HtH62k2diuUAmFQktmS6Omvb6xzQy4yFlix76VCZAw65pq67VmAAAGx07iJMIRUMjqWjv1gDElLhIO/WFO4kya21uaUIGLgEG2t9a3KQ0AgDI4LhInRNfeqjA5SsR0FAAIlbxFhfLFTENVs9rZVcKmYQBAmDVNTSpHiSPNpKysayUBADAHVzcBs9v7yqxvbmpS6bqikdu7eGLqVi0u5JFth45dmDB/phCjvBP+DDZGjSAI0mJBvJUAE1AM5/N5AoHgzpNhhzbPn7Dmh9uPFx3f9sqnB8rKK3JTdz2z9muZynYUqL4wmzRNDa0m891CipDGlO+2bD92qaKiwpJ3ioLiUUDfdvCzN384L733Gs1t6k6dCQCKL/yeUVguk9Wn/vprQW37bQUNN9KP7/otQ2ckAQBUjSeOH7lWUl9bkvfrkbPdY7HrVNITx87VNclkMlmHUkOQoG8uOXUqo0bWWpqddjIl74890g8aJvXVU/tyGoxg1l89dfBCUbVMJsvP+O1IepHZ0Hjy4PGaDiMAEHpl2pEjJe0aQ921z7Zuu1Ait9Q2aKoPHzir0JmhtXDf8Ut1MlllTtrR3y90dM+brZGdOnSgoFZmQWPU30g7lpxdazSbFJ2Ku77bKPrCpi2x69+bIoy0SjISoK/8YQBmacrnBwrYItt522jeA0cuXrJk+UubYhVHdl++fwKGNWjM9CVLliQkJNy3S1BQ/LOwnVe+ubZ2/8Y13527xxpEW2NxdQcAeEaNnD5udExM/MhhkvOped0fX5LQ7P3y4/xWjVlvsuwXZaUo7WKmj49PGD8miFmfntVgTdxAaFU0e5+omJiYmJh+/m50FBCO6+S5MxNjBo+bNIKUXilqMN7Wi4cUmkdIRExMzISkBF1xmhQJjR8oyLiUDwAdtUVy+9DBnvYAmHdQYHnK8cJWTa/KfHvPyJiY0TPG0mpL61p7ZG5CUFZQZIwFFz4nevqzc0cEPI7Lm/5W7mxLRLrpYl370IcMU9XmfvBl3tzlU786KrvD9RCS1BpNdKL96FffHr1aryf0AcOffW1h3PXdL2y66hxGa62rK+MOX/n2snF8VJFybO++IykGnO/izuq01FfeWPXSOzIz1mzgvb7hzSF+nHM7P9lz/jpBmhxiX9q8ZMBfGAoKigcYlvtrb6/7avPHq/5HvrkogXU3w50RcBabDgAcPt/yoarrVLEE7tDNjIKgrKlP/ceorj1wsggAAEi9TosyLNnAGGJHXkFDk7yp48Av2XOWz0PVmk6VvKy4iM7gB/i74QD0m8urzRqNlqRz2I/a2xghCD0BCAJe/aKzdv1epfQpu1YRFjeNgSE6ALZ9wGBxQ0bKVZ8Z8bfZpkhNU6OWKxLxGLYa7qI8fV8+GjU6qGvcTJrWsydPt6gJjQ4bNfMJXzvmfbqvR4w+ZFjXZJhVXlm3SJt6GGlWnNj9rWjC4kGOZV+BTRlGmgxatUrVnvtbNha9JdyVCHh22yJhW132Cy9/JZ0WbVS3l5Zz3t+9OZAmnbPw1cxRQ8IURz87XPH2x9v7OaJXd7174pIMAIBgL37zKy8Bce2n17/cl95/tf+uXTkv7NgR5WaWSu897eXfhlwu/+GHH6RSKQCEhIQsXrz4/PnzWq12ypQpD9oKBJIkDQYDnU5/0DpGcY/QhX7PvfrfDza8u/kX1trZQ2wmubKC8B3dHFg390iTvPL89daQ4cN71kGYLJZZc/MYgrp7BWScv1TV311MtmQVSklnf5bAdeRoFhsFxME/PoYPJmXh5YzKpmGjhgUzEQAAwqQvuHLB4BTqIXx0flcmg0Gv11cUZDE9B3kLgQ7OQwcITh84wbT3G+7CuVkK9YmMrfx5f2F9dGi3VJct0qyDu6v1Mplz3BNOPYOoEGbFuYO7r9EAWK6TJsWZDVodaia7XsKGG5fOtgnCZ08N1haf2Xkma/ETw7iP2lfBfcHmIN1yqbfsdhNltvQwkszY+eGJpvAta4YpL5b1cSFD/pldr3dcZPP9t37zocRYf+r0zi/TK02kobBRqTWbAcUHjhrvJWICBIWIFNKWZrhywXXgnH6ObADwHxHrtfMoAMgbyw/vPdHcqu2ozmr2iSQw1whf/Wdb3omOHbF0aiLAP2rNyMvL++yzz5YsWfLyyy8TBHHp0iWDwcBmsx/MEHZNTU2vv/76J598IhAI7l6a4oGEYee/YfNbH6x76/kO5ecvjGH1XdJDzLHvygSsr8rJTb50JXjk3CF+d045hDgExc1ncpJTfqXxnTw93dRAp7MEAUECAACB84ABzgAQHu71v0+ONod4e9oz1e016UeOtbhEzxoXeSeN4yFDX3gxubOQIXQJmzG+HwMAAPcYHKs/tTs6aUL328TZTiNGD9xz4pTjE/7Wg2KvqOnz4rgG2f4de84gU8dGuFtPoRh/xPR5Qbyu3cbu19TJi0rqSA+XSxkZoOvUtsjVekqG3RM2BsncpWqRPTwTAUiSRBDkdj2MJMypyeebdc6rnspStZSVlajWfx7436VzRT2eMMbACcs+fX2K5dux8Nddu9JNX378NUdTtvjpV233jIbr1VozAAZA6jQaANC37t3yNjLluw/Gekl/Xb/mIiCY3XMfbR9VduPEzm/+U6rYsnr8XxiKP4bBYPjf//43b968uLg4AMAwbNiwYQAQFhZmNBrlcjmGYXZ2dgCgUqk6Ojrc3Nw6Ojrq6+txHPf09GQybxkK9Hq9VCo1Go18Pt/DwwMASJKsqKjQ6XRMJtPb2xtF0fLycr1ez2KxvLy8TCZTRUUFALi6uk6zYQUAACAASURBVAoEAoIgqqqqtFotm8329vYmCEIqlWq1Wg6HY/XM1Ov1N27caG9vLy0tDQ4O5nK5MpmsqakJQRBnZ2eR6E9mU6P4F2C5r3zt5a/e/eC1nwWbZsbwaHfRfiqzz53LNY6b87Sr8J4iKwq9Bs7wGghmzcWj5d79PWw4EBMoiZkIgjBpa4/vT3YYOPrJyEDmg/jZ9qdhhCeMT/S163mQyXTkCOn0XkUFntEhdj9cvAa9M77THUI9BVkdynu9JorTaTSmk7u3BAfw9o/giO7whULRDdu2RJLsoW6RNpWymyAYvm53qmW76uIPC7+Vbnpx7l0ui5EtSroTD7964serVbY7Fjpo0PVN+9JmDh3hbjq27adCkABOIjpSi7FwQ9uvx06ouP8hiPqCEiwyMs6h8+rivXU6813v92+jpaWlsbExLCys1/HTp09LpVJPT8/r16+vX7+eTqcfPny4urp65cqVH3zwAZfLVSqVoaGhCxYssFbJz89PSUnhcDh5eXlr1651dXU9ePBgVlaWr6+vXC5ftmxZcnJybm6uj4+PTCZbvnz5/v37a2pqBAKBXq9fs2ZNcnJyamqql5eXXC5fs2bNiRMnLl265OHhIZfLN2zYYLmEWq0uLCyUyWRXr16VSCTV1dVff/11UFCQSqWqqqratGmToyOV+fyhgSVwifAWnCoqUxsG8Wh3nhhTXD5fHjVjsbvdPQkwQ3tzK8JzFbLr89NumHxm+wl0nQ2Xs2piEmOIJqnO3tuBYajKvGC0DxTx8YqLF/SuA4cNCnyENLA/AS0qMb545z45HtDjsLIhr1bjEy++12bodv0Dnc81yUZEDGLgHaVFOjH1RN4btpTVvsSX7QM94Nh7Do+08f0g8uoXY+ds/WIMTlzyXMFnTz31lPeQccvn8gV0nOU9KErnaPmYC4qMt3PgigMX7lzH+eyt/+4Sej4x86nn+Y0sptPSjz5c9cprL5y0jxuxbDTpiZu1v3266UsaZhYEbX33WUc65hrqdeqnt6/uQR0dHZcsWfIHRuIPotfruVyuRZ06derU0aNHpVLpl19+aTmbkJBw4sSJlpYWiUSSnZ29ePHiPXv2eHt7L126tLGxcd26dUlJSdb8nBEREXZ2diUlJYWFhampqTExMSkpKR999BGXyzWZTEVFRRcuXPj4449ZLJbJZDp//nxZWdmHH36o1WpffvnloqKitLS0hISEsWPHEgQBAOnp6UlJSUlJSWbzLZEuEokmTJiQlZU1b948Lpf7/vvvz507NzY21mw279y5c8+ePStWrHgwTaAUvTF2HPj6g521obvemSem9fkna2lpqWlUhcUE2ImEhWnHb3Q9ew5j5ybZ95wQxelcT3dnDEUAgDSps9LPpeoIkXPojGlhHACN2aDsVBIAWkX9qXMXUQQYziHPzA6n44ScJ0Zqrx/YXQgAAHSfgbExwS4P628IxcWefjgHBQScPH0wTm/9E0HoXr4+bEbXFwPGdfB27dphOwaOSRh8oYlDx1FgibjmzCO7axCS8EuYFeXbzcKBMz18vLubB7liT3eES6PTfHy96AjNZ/CEjovJv+zbjQA5cPTch3m13T+KTVuiWa/X9dS9epy9Q3PiwBFvBwKAWd2h0Jq6SqI0pt+ohS91e3BQltPc1e/2UNaSVlo/Y2Yu32TZCBj65JdDn7RsT4wDAADOoE9/+rF7vQ09d2PnvBo7BwBAKpXqdD0cW/9eeDyewWDQ6XR8Pn/s2LHx8fHPP/+8RYoAgEAgcHV1LSws1Gq1JpPJ09Nz7969paWl+fn5RqNRJpNZE5iRJLlz586ysrK4uDgajUYQRHV1tVgs5nA4AIDjuFQqdXFxYbFYlt2Ghobc3Nz//Oc/BEGUlpYajcYFCxZ89NFHZ86cmTdvXmRk5Pz587du3Xr69On58+dHRETc7sGh1+vb2tqcnZ0BAMOwAQMG7Ny502w2UzLswYcwKH7f8eGxJp/P1i64gwADALFYLBaL2WA3bsGCO/9lGTznEQnOXduOPlOm+3Q/yxZ5TX7CCwC4QcMWBA3rdgb1iRrpE/Unb+SBA2MPSJhs2QwfPu728wjKHT1hrHWX5twvyfnWSc/IMZ6WTUbgokWBti/Bsk8Y16Nl1/6JrgAAMGbCaAAAjBOZMIVKqPFHsSHDnMROubm5QAJBkrdCTnVtgZur2z00qzi349vzDV0LAPl+0S/Mn2bHfqQ+LEQikYuLS1ZW1vjxNibh6HT6tGnTfvjhB4lEMmPGDB6PZ29vP2PGjDlz5vQq2dbWlpaWtmnTJnd396KiIgBgsVgKhcIy+wgAbDa7s7PTWl4oFA4ePPjdd9/t3siOHTssdsgdO3YMHDhwx44dWVlZ69at27Nnz+0eHDQajc1mq1QqACBJUiqV2tvbUwLsIcDYfvL7LTsqvb95Y5HoNkWBguLxxIYMGzAg/C83azfp/1ZP+sutPMjgOP7cc89t27ZNpVL5+vqqVCqL57q1gGWqrKio6NVXX8UwbPLkyZ9++qlYLOZyuXV1ddOmTbOIDQ6HY2dnl5qaKhaL09LSpk2bFhYWdurUqa+++iomJqaxsbF///6nT5/++uuvIyMjGxsbBwwYcPr06ePHjzs5OZWXl48fP/706dM+Pj5yudzX1xfH8f379/v6+ra2tvr5+XX3HLGzsyNJMicnZ+DAgePGjfv6668XL16sVCrPnDnz2muvYdgj9YXxCGJSHPx686/NPl9tWEgJMAoKK8id57ceXiy2ROuc031CoVCcOnVKrVYDQGBgYExMjFQqVSqV4eHhCILk5OQYDIaYmBhL4cLCwitXrgDA0KFDAwNvGRzq6urOnTsnEAicnJyEQmFQUJDJZPrll190Op2Pj8+wYcMIgti/f7/BYPDz8xs6dKhcLv/tt98sV4yOjs7IyKisrKTRaHFxcW5ubmlpadXV1XQ6PT4+3t39ll8vSZKZmZkVFRUJCQkuLi7Xrl0rKCig0WjDhg3z8vK6r6NE8VcxKVN2vPdlqfdnaxe4Cu++9NVoNB4+fFgsFsfExEgkEkrJpniEoWQYBcUDj1b+e0ru8NEJzLt4IXZByTCKxwdqER0FxQMPy37M+JH/dicoKB5EqA80CgoKCoqHFRt6WHt7u8HQlUjBYmm0/IPjuEgkoib/KSgoKCgeEGzIsIKCAhcXF7iZZoUkSABoa2vTarUuLs4BAQGUeZ2CgoKC4kHAhgyj0Wje3t6EZTnYzQXODAbdZDJptNqSkpLg4OB/uJcUFBQUFBS300ceZ2sm85spVzAMv1FcXC2Vlpb1FZn+fkEYNU0tbf9gKEQKCgqKfwjSbOrs7KTyOP9p+oj52yuNMwJisXj06CQUQVJSU221o7t0YPtvuY0A8P/snXdgU1X7x597b3bSJE3SpEmT7pXulm5ayt6gUAEFEVQU5KeWqb6vKKKyHAiKCAiKyFBANlQ2ZVNaCm3p3ns3TZNm3/v7I6WLAvVVQfB+GL2545xzb3rPc55znnO+FJp0xsL/c2F3HmsquHj4sm7CjOE8AMANNxN/rRIPGhumAABt451te3NemvmMDeO+EZJtxVfe/PLapk1LhO07DMlHfm1wGDwyRE72aZKQ9IrlbvvT3FqfcjOtSWvmyXwiQ1zvnR2NG9vyy6pdXVytgmSauvwryblGYHqFhXpIOhd5MRtUKRcuNRgAAHhSz7AgTwYG5ZmXbpeogGYbFhUqeaDe4z8d3FBwOwVzinTh4wW3r+ZUqgGAyrOPDA3GVAW3S/UBoYE2FAAwV2XfqqY4BQrUv6fWhEeHijl0ADAb6lNvVvv382PpK49dTCcIAoDu1z/WuauOpUF9M+VGVbPO+kkZOYRem9HIdHXjanftOjl57qtCClmf/S/08tS6rZQIAAjSTYal9/lkjRf3nvAZO3fu3LmzX5vs0H3VXx7DfHDXt7dKzQBg0qp+/X7Z6u8SVQAAUJ2a+Pv1Qhz5Q3Eiloay/PJGLdlwIfm3oK3eunZtelnLw8+8S0VFfUWzHgDuXL+KypSxseHGgguneohEEERNSfrBbRt+OZtpshAAoK9M333smr1PRKiP6Or+A8Vtnd0fRl1FTqkxJDI2NjY2WOlEw0Bbnn67EusXG+MrNhw/eKrJ+Nfc6+PBYihKv16qsgBuLspIxxz9Y2NjHYjSHb+dAVvbmvQbeZUtAGDSNF64kG5jxzY3lZ4/dfTU9ULrTZuNDSnJd3QmHNQVBXW0kNjYQGfKyX2HKjRdJFmMrZlpWdLgWCtyPqZprm9U68l67E/Sqw1r/7+LI2b9CcTdQI+etGlacDtnF5lMJpNK7WjdU8XkYXHOltt5pQRAmzq/zSJjlt0oaSQAiJy0VId+oUwagluMOp1Op9MbzdZvnTAaDWaTUac3dhEwww0GndnCHDH7g1cGe6AEbjAaLWajTqfTG00dOp0mg16n0xmNj0HWmYTkb4FpGxvIXvLhF7f7bMao+pbKWg0AeEUPDfdy4vHEvoHyouzi7qIUbRdPnmc4egmo1nfeUpBzi+0cEeBqZ+/q4+dguZVeaSFws9lCAFjadAibz+fzeDweh0VHAeh2nsOHRUh5fBc/X5u2itL6J9qIdQVhsLk8Hk8ZGGKjzi/TioODJbdvZhEALWU5JrmvM5cJgDr6BGpzLt+pUPe4mEJlcHk8hZ8Px9Ciau3+TBCMzeVZoVNontEj4wIcurbfcYvFZDKZzGTP4h/gPn4YAQAEANKhhAmdQ2O927DSxurDP2/YsPWXzMp7XzNOcJDz5fPJOAHF545oByyKdK24llkCxuJrV1uGxEVqym99lvDq/y1alPDG/82a+2GeymTSNv/f+IC5Hy5dtHJ7U7tVgxt7V0+eMul0XuvRz1945+eU2pwzY4bGffLZqvcS5o6dMuN6SRsQloLru2ZOnLlo0aKff/75r3g+JCT/AFCG56DXvpihWPbBp6llPSvNXjECjcNlAACDxbK+5Jr6ZradLXSRMUBQ9qTX344L8+4QBLFYLJb2140q4LMaa+sbqjPXffFDswXHtZr6urLrVy5dupFjrZgpDAYNRQHArG5pJRh8Xk99yCcdwmjU4RiVBk4+Ydzq23mN9VdvVoRGBtNQBADoXNe4SNmVs5e1vVgcQl1aouPbS3gPWhgs/+zPv57P72hrm9Tl+3f+tGfvvq2btmXUaP6GG3o6uV9fYrsvRhBdtgAAiN79MK7n++tWxMeFSbGij6b9J0PbMwLDI2pgQ85VrUl1O700Mjoy1t/9Vlq+Kv9ODuIZ5IntWvepJeqNzd9++93mtc85l6755boZANrQgFEvf7tslpCCEril8PyP3xyvX/TVjpFKbme6ak3wpHlfbdywsD+2OfGmUd+0Ye2OsR+u/Pbbb1999fm+3D+Hw+HQCZa5lmWsYBmsf6ttbGz6OH+gqqoqOzs7Ozu7pqYGAL7//vsLFy705cKHcvLkyR9//LHrHrVanX2X8vLyDp2XrmRnZ69ataqrchiO49u3bz958mTfs9ZoNHl5ednZ2YWFhR0zBftOeXn5hx9+aDb/KT9Yp9OVl5f/oYXQWlpaamtr/0ym/3A84176dKbvymWrbxY3PvRkmkDsKGzv0ycIXFV043yeLsTP/UGqzwjq7BlgLr+amlddUZh1PasMAGzs3KfNmMBFUY5D8OQJg92cJYbSG/uP3uiouI2axssXLtJc+yn6pLL5RICrG+uqq6tTbySL/OKcbQBj28VEyU/sOtgq9nEXdppquV+0B1p8I1/Vtb6rK0n5beeufcdT7dy9OZRuNSFuUZ/9befOnTt37j+vNnWvJAld2oVzFI9Bzz8/ZcZI13Onr7WY/tZ7fHq4X0xHF3eroyIhCIJACKKXqhNoNkr/IAAIC/PQpk3fc67cf6xz1+Mie29J7earOZlJd4TzPpZwsZCqrTcLJK2osp8HvfSrNHP87AAKANBsho0csnHN7cbpPmAn9ZG3h3G05p965UNs+dd7Y134XZPFnEOjPbgogIuLtDm1XG2Esmr7uW4yAABgAjxcPww1tRizdxFtDUBlAcYCC2LIPGI76+S9slv3PqXDhw/fuHFDKpVqNBoGg5GQkFBZWSkW91m59YE0NTVVV1d33XP+/PktW7YMGzYMRVFnZ2eJREK7Rxm9ra2ttLS0R9VfVVVFpfZ1pfOampp169aJRCIGg1FbW/viiy96eno+/LIu6PX6wsLCP7kOZ2Zm5urVq3fv3v3gkuM4npiYGBwcLJVKjxw5kp2d/fHHHz+10/BRhk/ctE8sW5d8+tW8pe/EOnIfcK5MwOC2azTqsi9duZRdEjZiUqDC5oEZIDznfpNGcZKzs7VsgYezLBOhU6kseykLAIDFd3TkA4BCwduy9kBDpD9bxGipyzu19zgSPOzZUOVTtGydua40P1vDslH0H+NrjYLBxAGh2JGd/n7dgmJQum30kPCdB047TvTu2Cl2Do2fFssxtRza8fMpbOz4MOfO8zHu4Php3ne/hG6vt0FVVFKjbrl9pPY2GBr0KqbeCDxSn6AP9PKLd9fT6hrI0b6B3C+kowMLYURws7mnH0aXOE+Ksdn2wyE0OMiXAWaXfsLCVd/TIGzMVAAOi2Nu1ekBOAB4bXUVhS/vEeHEcYx4zaNx76HESLdpEpv7vywIncDb2kxmgL6GSJkbcxCLGWcpGw+tMhI811c/MZdk9OVCjUazc+fOFStWuLu74zj+J92OvoAgSHBw8BtvvEGh/F3VhcVi2blzp5ub2yuvvIKiqMlkelzz2YODg7dt2/bQOzUYDEeOHJHL5TKZbPLkyRaL5ak1YFZQqnLIa8sp2xf/9yNi9bIYB5uHfj2Z5w9fqxRNnvkyj9anXxuO1Guw1AtM6nP7b3v37yWOEcwWM4ITQBhacvfvvuQ79oV+rhLsIU2+Jwuae0j/QW62PXbS+Eybe1pUHGlIiCLj7OV0c48+LSrPXca7qdX1NU+Mxmaz7PvFhTvSAWAERqE/bV2zfxf38cMI6D72S/S63UFb2Z0UNc3fQVR5++DhbPuPlih6noFwwgcFvTbz59mrtmMAmEgW5dj6wU3slwR7AOGwUS7frN0SsmY2VVWx8afkKR/O5He/GmXavrjgHdOS2W9+jvz436n3M6M0hnuwR/OXu0+vfXmAtu4WxvW+z4ldbs3UhjD4lKYsKtTb+kciljYw98mBoFAoBoOhqKjI0dGRRqNZXSKCIGpraxcvXqzX66dMmdK/f3+TybRixYqGhgY7O7uEhAQul/v1119LpdLs7OyFCxfW1dWtXbuWQqFMnDgxJibGYrFcuHDh8OHDACCXyx/qyuj1+o0bNxYUFKAo+sYbb3h7d96vwWA4duzY2bNnbW1t9Xq9k5MTADQ2Nm7YsKG2tjYqKmry5Mk5OTlJSUk4jru6uo4ZMwZBEBRFeTxeVlaWSqUSCARUKjUpKam5uXn8+PEoimZlZZ04cWLw4MGXL19mMBipqalhYWHTp09HUVSj0Xz55ZcNDQ0SiWTMmDEWi+XIkSPnzp0TCAQLFixgs9nr16+3t7fPzc1dtGiRyWRav359TU0NhmHvv/++nZ3drVu3rKo06enpMTExU6ZMqa2t3bt37yuvvLJp06bS0lKz2Yzj+OLFixkMxoYNG1pbWz09PefOnbt3797k5OTW1tbhw4f7+fnl5eVNmTLFbDbv27fvypUrCILEx8cPGDCgubl527Zt7u7uZ86ckclks2fPtrW1ve9j/YeDYN6xU1bVls9evmnnigQnfu9tdRzHjSYLAU1paXXBzw6mmY06sxEAZbAYDzB7hvryUhNDzmdX3jpbzlJOlrPamkpOnc8f8uxQc2mWiu8iphsKLl+kOQaJeFhh0g3UNchLamPQtQEgFBqNRnmqGxC9gwbExGVt39UIbtbPFotJ19aGqstvVBh9B0sffHEnVH6wr+JoVkaALJRBac7PBt8gh7+ryE8X2EcffdRjV1FRkZOTE3E3PLFrPYogSEFBgbdXT7FtS1v9oV+2HztxLrfF5p1PP/AR9eIGce1lYLIdO3GolMcAlCWVIWxp4MjYMBYV3MOGBtDzN27bf+VW0aA5SyYGOgAQRqPRKyBUyKIRuMWEcgKDAqKjBhjyTmXp5d5ylq3C38ueY0HZIcF+NADcrEf5LiHeroOGD1ZfTdybeKpI7+rrIuRwHtJJT22rRAABM+AWatm503bB0aaqEnrQeIPB8GATQqVSXV1d169fn5SUJBAI5HI5giDHjx/PzMxct26do6PjF198MXToUI1G4+Xl9eKLLxYWFt68eTMkJGTlypVyuXzx4sVVVVUrV6585513YmNjv/zyy/79+1+6dOnQoUMrVqwYNWrU+vXrhULhwIEDO3LMzc09fvx4c3NzamoqjUZjsVjvv/9+v3795s2b5+bmtmrVKj8/P4PBcPPmzdGjR2/dujU/P/+LL75QKpUbN24MCgry8vL6+OOPIyIiEhISdu/ejaKoXq/funXr22+/HRUVZe07RRDEz8/v7Nmz3377LUEQbm5uDAZjzZo1cXFxHA7nt99+4/P5NBrtm2++mT59+pQpU3788Uc7Ozsmk7lw4cJJkya9/vrr9vb2BEH8/PPPQ4cOnT179oULF6qrq/39/VesWOHi4rJw4cKmpqb//ve/EyZMeP311yUSySeffBIZGVlUVLRhw4bXXntt4sSJmzdvttrvPXv2xMfHx8bGjh49WqVStba2Tpo0qaGhITY29rnnnktMTNTr9WPGjMnIyJg3b96IESNu3bp169atAQMGrF69GsfxpUuXhoSErFmzRqFQMJnMTz/9NDg4eP78+VevXi0pKQkJCXnwL8Y/mYb880s3nJuQsCjWhderQcJx/PLly3VNBp9gT0xvrq0pL2ynUertxOzZT47jQJPJJBiK4EZ1euqNrNx8M89vxOAABoDZ2NbQpJe7yM0t5deu3SwsLNHbBUweGkTDCIPeoKqvKGpPudRI50sEnCfWHyPMZpwvdRYwEbPFzLdXCFg9GgeEyUTIFAomDQMAwM0WGk8u4WEAFKatlE/FePYejlIqgtfUlJYWFBRW1AcMfDbI0aZbChZUonDsiKDBzSYaT2ovYBKAyZ0cRVJXm7bilNtZhYWVTsHhgofrxJEA9OqHmUym+vo66BJTT3QJSTSZehlqZEh9F7y/ossOY3lWbm2bwfqBZmPn7eZI43i8szSh4wxZ+Avvhnd8ovmNmvXlqM7rMRpr0sy51m26nceMSR4AADzZjIRlAADgFQQAAK+/0j5UIw4Y93IAAIHXq5HnF34wg4KUZKc+fDTMek84aJs01SVNVCd/hM7tox8GABERERs3brx8+fKqVasmTJgwc+ZMFov17LPP0mg0JycnBoOh1WrZbHZGRsa3335bUlKiVCoJghAIBDExMQCQnJzMZDJbWloMBoNery8oKDh9+vSkSZNsbGwAYNy4caWlpV2zQxDE0dExLi4OwzB7e/uSkhKNRjNs2DAEQby8vIKCgq5fv251xQwGQ0pKyrx58wBALBbHxcUhCFJTU5Ofnz927Nj09HQmk5mZmRkUFOTr6+vq6to1FxqNtnz58vz8/M2bN1++fHnp0qUODg55eXksFistLe3dd98tKysLCgoKDAyk0Wi+vr65ubkEQVilqqwlyc/Pd3R0HDhwIJ1ODw4OvnPnDo7jAoEgOjoaANLS0gQCgdVqBgcHi8Xi7OxsAAgPD/fx8aFSqR4eHvn5+YGBnWLihYWFZ8+efffdd1EUpdPpiYmJaWlpeXl5zs7O97YztFptRkbGmjVrUBSVSqXPPvvsiRMnpk+fLpPJhg4dSqFQgoODk5KSntReRwJvKjj/wReHwucseSnY/gGdgyKRSCwWM4EbM278gzuEaSy78FC79m1bxdBR3TpRmDzZwCEyAGC59Jvg0q/LEYrcJ0Lu8z/fyT8MjOEVFmfd8gqNufc4grIiY/t3fKTYuUfZdR6VeEeNtnaC0Jyfeda59yzovNCY/l13iD3DrIPn0bGR1ou9woZ4hf2vt/BvpZe3wN3DvaGhAYi7f4i7QR4EEED4+vRlsURDacbt2w3tQfYcuY+Ls4JG+dubaITFcHzLRxeKMCYTE+D41Lfffvg1OOhStlNtXBx93cFEaJNPmUvT+56jUCgcP368TCZbtWrVCy+8gCAIjUazdsoBgMFg2Lp1q0QiWb58+fnz563dZSiKdhxtbGxMTU0FgKFDh8rlcoPBQKe3u7AUCuXeuBKhUKhUKq2jRCUlJSiKdpzDYrEMhvZGA47jJpPJGg2BIIi1sjabzWq1OiMjg8lkyuXykJAQlUpFpVLvzYVOp/v5+a1Zs2b+/PnJyclDhgy5ePGixWJxcnJycnIqKyuj0WjWNDEMs1gsjY2NPUpLpVKthaRQKNYgSQzDrJeYTKaOkxEEYTKZ1lYRjUazPhZrmh1JabXaDRs2PPvss56enlqtdvny5UOGDFm3bt2GDRt6/z5xvKt94nA4er2eIAgqlWp9ICiKdk3/yUJbeX3Bhz8Ne+ODaQPcH3dZSEj+EfRiwzzc//zrYRMz5cVeGjN/MwiF+eI730wyWQCgoqISxx9eVdHch9JdBwB0iV2BPtlao9FYWFjo7e2NIEhTU1OvxsBisdTV1Q0ePJhCoaSkpPRwYQMDA5OSkqyOV2lpqUQiUSqViYmJQUFBAJCYmOji4vKAAigUCovFkp6eHhoaWlNTk56ePmfOHKsZo9FoMpns9OnT3t7eNTU1Fy9eVCgUUqnUxcUlMjIyNDS0oaEBRVGVStUjTYIgsrOzPT09KRSKXq/XaDRMJjMkJGTPnj3p6enLli3r1Xfx9vbes2dPcXGxq6trbW1tr556B0ql8sCBA/n5+e7u7qWlpdXV1Uql0uqK3QtBEEePHrW3tx81ahSCIGazWavV+vn5qVSq9PT0yMhIFEWpVGqH8QYADofj4OBw6dKlWjpxRgAAIABJREFU+Pj4lpaW33//ffz48X9fFMyjpC4r8f3VB8YuWB4fKn/cZSEh+afwNLzbXcGodGs/No1G1esfbsPadL31OBo1vc6+6opWq12yZIm9vT2CICwW691336XT6RwOh8FgAACCIHw+n8VizZgx46uvvjpw4ACLxeLxeADA5/OtDoFSqRw1alRCQgKLxXJ1dX3rrbemTJmyZs2aefPm2dnZeXp6stnsrjkyGIyuw3tCoXDBggXr16/ftm0bQRDx8fE+Pj4ZGRlcLhfDsNdee+2rr7568803ZTKZt7c3i8ViMBizZs3asmXLtm3beDzenDlzaDSatd+yA4vFcvjw4ZKSEgqFYjQaR48eHRMTw2Kx/P39r127JpfLAYBGo3G57VHdLBaLTqc7Ozu/+eabH330EZfLdXFxGTlyJJ/Pt1p0Op1uzYLH41kNiYuLy+uvv7569WoGg4Hj+JtvvqlQKIqKijpKwmazmUwmhULh8XgFBQW//vornU6fP38+lUqdM2fOqFGjrAOKLBbLmnt8fPzatWtHjBghl8utE/sSEhI2btx47tw5AIiOjo6Ojq6rq+PxeD2K9CRB4Nqq5P+u2h8zY/5zYaQBIyHpBPmT83j+sZSUlOj1eolE8rgL8sSD4/iaNWtkMpm1s/RxF+dfibbq6+WfO0xYFB/Wp1g1k8l04MAB6yClvb09KfhH8hTztPlhJH8tzc3NSUlJKpXqtddeIw3YY4Mpfumdj6x+PAkJSVdIG0byINra2vR6/VtvvUVWoI8TlMLnk8+fhKQXerFhVVVV1lAuuBtWb/2fQqEqFPKnY3icpI84ODg8/3yfVp4kISEhefT0YpAKCwvd3d2hY6FfAgiCaGio12q1anWLUqm8d5k+EhISEhKSR08vNgzDMDuxmMDvSrAQAABms4ljY2MymXJycgICAh5xKUlISEhISO7lAfph1g/tP+h0en5eflFhYVFxyd9dJotOdTs1q+3vzoaEhITkcWMx6SvKK01PaXz4I+B+2ivdZZwREAiEgwYPRhHk3PnzvSZE4Mbs0zu+2XvJhNInL/hsuFfnFJz6jGNbE9WzFr8gQgAs+vO7vi6RTZg5xAMA1DXJn313a9F7r/CZnSXRV6V/tGD7yqQt3t0zqC9O/m7d5pJWoLB4L87/dIBbt+lTJCQkHZgJsM5wNDRXXLh8taHVzFcEDYn1YdwTXGrWqdPzy3x9fOkUBIBQlaefupBpJJh+cQMCFKKOs026hvNHE+uMKAAIHf0HRAcwUbwg+ffkgmagCWKHDHAUPMnvo0WXceUcxWu4UohnXD15u7QFAaDyZYMGxNCas67kaqLi+vNpAGAqSrlcwfCMEjXvTiodPHKQnMcEAJO+MimpLHJgBEdbuPP4dUAQIGghw0Z5S7osIKlrvpB0rqxRZ90TPGQCvexaLUcZIDYeOXBy8txXhX//SkZPJb3bsM5tAECQu7sIAOQ+4ivGi9s/2JSr/P7bLSxaT9/OTiq8eWZDWnz8MDeaUdt8dM/6ixzmuCEeQoCq5JOZtTYY9tA4EaLuyg+Tvk1f/+UGfylDVXA56wlc646E5JFRXlqtQzlRADlptx3CRoyQMq8e3HXkIuW5AV6dNSVBFGYknT9xtpgT4u3tA4BoipO3nyl4ZuIkMVT8tmMfbcaryrsaVkZ9dZVGGD9tNOfuaLimNKPY5Dhx2ihd0fV9vx17ZvpkyZO7TC1uqi7KoTkMVQos1UWlDv2nDnKzLUs9sn330ddeGWI5/WtWmTLaXWBQ119OLR30Un9LRc6dm5dMLMm0cf0YABaTOjenJDgmjNPWoAKnGdNiiYobO/fuY0yf7sK7W1WZ20oKa8JfmntXP8xcXEWlYOTUvT/L/XScezhi1p9AdKqLdcNUkbrtlGXhey/ca8AAAETBA73QlMx8AkDbkK6lBYqbkvOrzACmzJvpruERDIqpvrw4Ozu7sKKhY2kNvbouPzc7O7ug1UQAmLNv3uTIQz0lDADgu/ePdmYDABCmyoLs7Ozs7JJqg661rLyqvrqkqLLRAhZtY3UvJSEh+XdAN2vrG9sAwKf/UF8pH4DuolTUllR2WVMNCKItJ7vCJ3awg1XwmbAU5mdJPKOcBDSmwCnIg5GRXm4065saVRYAXNsGTFbX2dJMmc/g/r5MQASOLgK8qarxD0t+/8ORe/jbWSrLVNygMOc7N26bAW8oyKS5B0sYVADU0T+cVpWaklffa6PeRia3AWOb7gGyghQHrwBvhW2XJ0roWpvramtr61UPWSWIpAu92rCuwpd3vbJOLZZeHm/JnWs1HG7p0Y3vvvvuuv1X7zlODwhwS7uahhNQkJRo6v9GqEv9zZxSMJSm3mqNiQiqvrF3wTsrjxzZ+/H7S87mNwOAQXdn27qtBw8f+WXtR+9+vbNWSw0cM4Z+ZvPcFbs1HamaVCd++uL9L7ccOfLbiu/2lKadmvH82M93HDifWmSuS95z9PyffDQkJE8uBqBzbRkAQKXTrY6XuqaBay/quhoogrLHTHkxwMOBcddVQBBU1y7biLGYVHVTc3Nd3o/f722x4HibpqLsTuLRQ4dP3rAuT4lRqRQEAQCTqklNsASCpy1cGdfrdRY6iwVSjyA7dW5ude31zMaQUCUVAQCgMGVR0a63Ll7RmO+tEonGwgK90MmB/yAx3uKrB45eK+mwcobmot/2HUpJSzt96LcbJT3XMiW5H/frSyQAOh2xrurNvblhRG15qTqvTjfjo0VR2nWrl64gPn8n3qtr0h5Rw+r371cZht+8VTdoZrQTL2lbclY9vy2LGvx/rvVfzdo7fuF3k0Ilt3/5aMWPx0NmKjCqZeCUeeM9mGDWffDKuMT0mJlRI7fsdfhm/dejBnw/8uV3/u/FkbqspK2nG9ZuWS1jYAaDSZVzgko4zXj7bV86BhbD81P58KSuTk5C8mfhiO2dbFnWbcJirkw/c7oYGT7G40FDLgjm4R+RffLiqWtgT9NkZFeCzJtr7/PG254MDEVcYxPmRgAY8q+d27FL89ykOB4VBYC2htJTJ5JsA4YpmI/ivh4J5privDt6TlVOsmPUCGcWoCCKG+y55cdfnWNHuPE6dcVk3pFBuTsv3q4b4Nl5cV1Jym87y1C9TuQZDrgJoPN83KI++9vOVCoA02HcuNhueeKaa6fP2oU8MzzAzlJ59ZsTlzxfHGvbVzn6fzX3i+noZrU6dcQIpFc/jM3jMbxdn4v2pAHMmzLo+V3nZo/3EnbRkBOI3Vx0lZduZ1wqFP7Xl882+1euT82T6TjKYHlbeVZabv4X/01kgbYuv81VjBMKCiXA25OJAgCVKaHZNKjbADCBa9DSNT88f+OXlYvWbJW6xmlS2Yp+MgYFAOh0GoIA6mAvoWMARMml7T8ez3zl5Tf+2ofVFRzHd+zYceXKFQqFwmQyp02bFhgY+NDVmPR6fYfIyGOBIIgzZ840NzfHx8c/rmJoNJr169fPnDnT3t7+sRTg34Adl8qmoQCAW9Rpp86lNxqHjhrrbvcQO8O09x4/lpNX3ogwRD4ukkwKi4JSqCwKAACFxuHQADhBQwamrNvb3BLJE9HrSm6dOHTJftCzsUrF0zSwg1vMZrPZqd9IZ0cpCgCA8Fz9OJDu5+HQ9TYRKqff4Jidu89WSnw7doqdQ+OnxXIs2pO//HSGwo6Pcus4hGLcwfHT7o6HQbfRDmNrdW1TXcuphkwAsxq3CE1kE7xv9GLD7o54tXthXcPskd79MMTF0593vkwHQAOwEDiTb9MjxIZq5zRlEG/9ln3C8GglDUyuoc6VRzdcRKJemAVMs9zL6/lPvhni0R7XpC28QBAanQ6ACQC6eoPZjdP57nmFPf/SMye33cgf2M+mobWhl3sy1B/Y+jM66rs/+Cj+MDk5Oc8888yoUaNycnLee++9TZs2PXiJYb1ev2jRorlz5/r4PE7pQDab/XgFtFAUFYlE5IIvj4abv/+WYfB6cXpMH9v0TIE8UCAHY9OJFMR/mCv13jOMej2BAiBt9Rn799+OnTbTV8L9a8v8uKHI3H0C3Wx77KRwaMx7os+YAt8Iz1tnzqcYgdXtAMZ2EHJuPVCHqHvydB7XRt5/Qowb6+Enk3ThPn4Y0c1WdYtU7M2I8ZUDh/M+/Or7A+O86L/sS31pzmbuPd91cFzE1fjv3vx2FgBQbe2jPdvmp2Jz/yMGFvu5oYrtO3YJng1tbSk1YcHhMjBos39av8c41KPh2t4a+TNv9JNc2rqlUu7pKbaB5tLdGbqRr4f4uTl7HftkyXeu8ZGi7GJttMPdepnG9PBwP596BYJj4ZEglUp5PF51dbWdnV1VVVVTUxOHw3FxcUEQpLm5uby8HEVRR0fH6upqq5gyj8dzcHDQ6/UlJSVGo5HNZru6uiII0tDQYDKZWltbJRIJh8MpLS3VaDRCoVAmk3V4eEajsaqqisfjVVZW4jju5ubGZrNbW1tVKpXZbGaxWGKxuKampr6+nk6ne3p61tfXU6lUW1tbAGhpaVGr1UqlUq/XWxOsrKxsbGy0Fo/L5ep0uvr6ekdHRwBoamqyWCx2dnZarba0tNRsNkulUju7dvFalUplMBjEYjGCIDqdrrq62tnZWa/XFxUVIQiiUCi4XG5dXR2O4yqVysHBAUGQsrIys9ksk8kEAsGwYcOsAihtbW2lpaUmk8nGxsbZ2RlBkLq6OmvuJpPJxcXFKjdTWlra0tLCYDBcXFysyjUkD8ZgMKha2izQkHGnxX2kpL6iAgAAaGK5+AHDVvqawowmi5TLqs2+1urQb7CYrqnP238085kZE0x5N8qoMjHdUHQzWeofLbFFC07fpjh5ckzqigo1AMrmC/gcxr8wPFwZNSjn55/Swdn60dCmqqqoYKnLr9ZSo4b1WSiHwg8N8dp/47w9FsCgNFXXCENCHcjg676AffTRRz12FRYVOjk6Eb0ZKwRBCgryvb287kmG5R8e1Jp9LbNM23/y/40NEN37q8yWyGX2HiOGR4o4dEAYDi4iN9+I2BAlg4K6+4cz1IVpmXkqHSVyUCyfRRHKAiN8sdRrtxtxz7ffnSqlYbilOfNWZnFZWVmdceyr80cHSihs8dCRA5qvXbxTVslVePl7OYskDj4eLhSE7hnej1qVL3Zy6iq49ddCEMTZs2ednJw8PDyuXbt28+bNmTNn5ubmfvHFF0aj8dChQwqFwmw2f/bZZ62trXl5eTiONzQ0nDp1yiokJpPJVq9efefOHZVKtWfPHiqV6u7uvnXr1i1btlAoFKlUevPmzR9//NFgMBw8eNDHx4fP51vzraysnDNnTm1tbVNT04ULF1JSUvr165ecnPz+++/jOM7j8YxG4/LlyzUazbFjx+zs7K5fv37q1Kno6GgURXfs2JGamqpSqU6ePNm/f/8rV65s3rxZr9ffuHHj7NmzkZGRhYWFK1euHD9+PAD89ttv165dCw0N/eyzzwoLC6urqysqKgIDA63FSE1N/frrr+Pi4uh0+tWrVzdt2jRw4MCNGzfevHkzPz8/NTU1JiZm7dq1u3fvptFoIpFo48aNxcXFVVVVlZWVHh4eixYtCg4O5nA4n3zySUFBQXNz8+7duzkcjqur6zfffPPTTz8RBJGcnHzjxo2wsLCUlJStW7fqdLrU1FQvL68nT/3rkYPjeEpKis6IePt5Ctg2Bn1rczsGsZOU3v3lRFCMybYRiwQoigBhrikvrWtoYkj8Y8PdaQAEEAjKkMrsEJO2tKS8uVlNVwQMj/CkooBiNDBp7qasRlh8IZf5pNowBKEy2CKJjMtAqQyWSGLPZVB6nMBgsO1l9nQqCgAIRmFyBRIBBwVAaTZSMd9WonCSCilUqsmkaW1qbm6zBPcf6inp4lQhKJ1tI7GXMO+aJoxK54ns7Xhsto2Nvb2EZ+doR2ktr6ptbta7BPhzn7YQmb+LXvwwg8FYVFwEXRb87br8r8HQewQt3cZhwitv3/3Udvt0Ur5Ka/3AFLsMigxmMRUvvjql43yRz7DpHT1qTOGo+BmjOhNzGPOcAwBERHfucg4bNidsWI9MUUz83NsdmcIzo+8KHzPlocOG6/W96Vv+dVgslk2bNh0+fLitrW3VqlUoim7duvXll1+OjIxMSkravn37uHHjWlpaZs6cyWQycRzX6/X79u177rnnlErlrl27OBzOW2+9RaVSBw0a9Omnn8bGxiIIEhwcPHPmTL1ev3Tp0g8++MDd3f2HH344ePDgvHnzOu8aRadMmeLu7m6xWBYsWJCamgoAUql01qxZKIouW7Zs0qRJgwcPzs7OXrNmzeLFi0+fPq1SqWxsbNLT09988807d+4AQGtr65YtW95//30PDw+z2bx27dojR474+vr2uEe9Xp+RkbFixQprdh37w8PDf/7555ycnJCQkMuXL8fHx587d06j0SxdulStVr/99tulpaUoikZERLz00kstLS1ZWVkrV650dXW1WCxGoxHuDijKZLLZs2dTKJSoqKjPP/88Li4OAPz8/GbNmmU0Gl9//fWKiorLly/7+/tPnz4dRVFSCquP8Hg8sVhMB3ZATOyDHxqVwffxbm8hUWzEYVHirkfpbFFIqAgAGDKvOFnXxitm5+Jr9yCl8ScKlOaoDLZuOXr3spYegjB8gzr3Y3y5H7/zqMDJP9oJAACo0gEDpL1nQeN4d1+lz1ahtPZX+gf6AQAAxUkZ6qT8n+/hX0ovNiwkONhg0PdctZ5o/xMVFdmHZBEqncFktkd/MGi0p1J5CsOw2bNnDx8+/OOPPz527NjEiRNzc3M3bdq0Y8cOtVotFAq9vb09PT3feuutoKCg1157rcOzxXG8uLhYqVRau8Xs7OxQFG1ra0NR1LptrfRXr15Np9NramrCw8O75stms2UymbUAbDZbrVazWCyRSESj0TQaTUFBQWVl5YEDBwwGA0EQfD5fIpFkZWUJBAIqlapQKKw2TKvVGgwGgUAAABQKxc/P7+bNm/cO1LHZ7HHjxlmlkxMSEoRCoXU/lUoNCAhITU21t7evqKiYM2fOrl27rl69mpCQYLFYysrK9Ho9hmFCoRBBEC6XO3r06OXLlysUinnz5lnXjMZxvLCwMCYmxjowJpVKLRaLXq+nUqn29vYYhtFoNKuc9JQpU1auXJmcnBwfHz948GAMI7tYSEhI2unFhslk92lH/AGYPrGDHmfcwiMEw7BXXnll0aJFUVFRTk5Ob775pp+fX8fRxYsX63S6zz//fPPmzTNnzrTuRBBEJBI1NDQQBIEgSGtrq9Fo7KoGwGKxPD09ly5dKpf30p9uNpsNBgOLxcJxXKvV8ng8092hYxqNJpVKp06dGhER0XH+hAkTdu/eLRQK4+Pjmcz26Bg6nY5hmNVVJQiiuLjYagUtFguO4yiKajQa68ZLL700derU3bt3f/LJJ6tWrWIw2hdjGD58+KeffkoQRP/+/W1tbQUCwaBBg957771eH9HMmTNffPHFnTt3fvrpp++//z4AWA12fX299SGoVCocx3sd61IoFBs2bKitrZ07d65AIOjXr1/fvx0SEpKnGzI27C9AoVAMHz589+7dMTExu3bteuaZZ9ra2qhUqp2dXVZWllwup9Fozs7O1pCEq1evsliscePGLVu27Ndff3Vzcztx4sTYsWO53M7gLh6PFx4e/uuvvw4YMKCurs7JyamrXdRoND/88ENMTMzt27clEkloaOjVq+3zyplM5oQJE3755Rez2UwQhFarHT58eEhIyA8//FBcXNy19udyubGxsd98882ECROqq6vz8/OXLFmCYRiPxzt06JCtre2JEyeio6M1Gs2+fft8fX31er2Hh0fXYEInJyc3N7dz586tXr0aAOLi4latWnXs2DGhUJifnz916tSOM9Vq9YEDB3x8fAwGQ0ciKIrGx8d/+OGHbDbb0dHx6NGjzz33HJ3eM3oOx/Fjx47x+XxrqIg1OIWEhITESi8xHU8H1ji9vy+mAwC4XK6bmxuPx0MQxNXV1Wg0DhkyhMViFRUV6fX6/v37oyiam5tbV1fn7e09cuRICoXi4+NTWFhIp9N9fHzCw8NLS0urq6uDgoLGjBmDoiibzXZ2dhaJRAiCBAQEqNXqsrIyOp3er1+/DgelpaUlKSlp0qRJ+fn5DAZj5syZLBaLTqc7ODjI5XJrRW9jY1NYWNjc3Dx48GAmk0mhUGQyWVRUlEKhAAAmk6lQKBwcHKzJFhYWIggyffp0kUjEYDCCgoJyc3MNBsOECRO8vb0lEklubm5tbS2fz58yZUpXZxHDMIVC4enp6e/vj6KojY2Nv7//nTt3GhsblUqlXC63BmcKBAKCIPLy8mpra21tbSdPnkyn04VCobu7u1gsDg8PLy4utvaXDh8+HEEQ61XWTktbW1sPDw+LxZKbm9vU1DR+/HgPD4+HTsIjwXE8JyeHzWZbvwXyiZE8xSC9xso/BZSUlOj1+gdP2HoSKSsrW7Ro0bZt21gsch4JSe+YTKYDBw6IxeKIiAh7e3syEIbkKYb85X7CwDDM6qg97oKQkJCQPH56GQ8rKChoa2uD9qh663xnwiqD6enpSc4wfbw4ODhs2LDhcZeChISE5B9BLzastrbW398frKtM3Z3qXFNT3dqquXXrtp+/H5Px5MoEkZCQkJA8PfRiwxAEYbHZBE4Q7VYMAIDBYFAoFIIgsrKy+oWEPOJSkpCQkJCQ3Mt9NDC7LvQLAEAwmaySkpKCgsLy8opHVbZ2TC1VZy7dMjziXElISEj+fsx6TfadXMNTGlv3CLif9kp3GWcE+Hx+TOwAFEHOnT9/7xVpRzd9vz9ZDwBgaalriJmz5q2xnfph9Wm/Ld9Rvnj1PAcKEGbtwbX/yXF8+d3JwShAU+mZ9z67uerz+QLWfWeqGWqzvvv5WlBM0N2pQ22HvvywVPnK/432IRdsICHpFZ3ZYsIJAFCXZ52/ka414DS+27ChYXx6jxeN0NRXJOdVR4eHMqgoWIylOdcvpZTiBMW5X0SUv0vH2QZt1fE9RzVUNoqA0NF/QHQAA9fdunD8To0eB2ZobJyPo/AJDjQya5NPHaEGPhcssdw49dvtGguTigKDGx49UGzKP3mjLm70CDETAdyQkXSiVthvgKBmw5Hs0fHPeoo5AGBsKz16LH/ouEHc1uzv9l/ncBiEAfcaMLyfm6RTwaOt/vixY7V6qlXrPnjIs5BzupIbHOlInD9zQezlQac8wc/vMXIfDUyii/QK0rlNQK/6YUjw2Dkbxs4BAG3Nzf/M/zw2spsApp2Lc+OdHzOL5zh4MEzalisXDl5guM2aHGwHUHnjQi2IqdQ/NNWa4uQfzpbakl84Ccn9qCmv0WPcGICK8lrfgeM8RIzU478kXuI+P8S388Uh8IxLh5IupNQIwiLDAIBQFd04cqMufuIUAVF9cMfxLOkrAaL2GYFmY6Ma5PGTR3PuThHUVBbrhIGTh7gbylP3/n6CP3WqA/uR3+dfBWFR1VXR9DgQeHNds1vs1EFutlXpp349lDjjlTFcTWp2Wb3YS6xvrbtVoB4WKcYrcuvKc89dSJc/F80CwC1t1VX1JgsBhlac7TlhWixSl75rzzHR1JfcBHcrN4uxoa4t6qW5d/XDLFUqR4LJQaD1sd31U8F9+hKRDu0wBDo7FK1HH5Rc+umDSOCUEFH3vfygQf7YhdQ7BIC66rqKHafQXs4s1gPob6dkBMTFsKigKruVmJiYmHg6s7iBACAspsy060V5txKT0nR4e5amtuYbFxILG0Dq5u4gYJo0DTdS08sL0k4lJp5PzTW3n6bLupSUmJh461ben3kuJCT/ILTVW9asuVXW0vcr6BZdc7MOALwjBriLbACoDm7Sxspa6PL+EoSuUUMfGj/R2Wp7CLw4P9veI0zKpdJ5iiAvVmZ6sc6gLi4qNxGAt2qBzem6ViVb7h0d5E4H4ErlPFxdp+p9NfAnF6mLl4ioqVCxg6OVOVdS9WCpzkxjKyPsGFQAVBHYX6DOuHS7stcakS0UMcFiNPWiGHwXjGdnZ8uhd21SqGpKs7OysvIrzH/5zTy99GrDugpf3p0D3f6T6FXHuR284vD+nJhhkfckivkFeOelpOMEkZN0Aus/o59La3p+GdFWejtbHxagLE89sPidb6taW+vLclYvevNiudasb1238Nn3fjrXqtVb8yNw87Fv3/1y7yWDBb+2Z/nmU3nN5WnvzY5fdzCtqaF8y6oFB9NbADdd2v3Zh1tOtra26nSFf/LRkJD8U2AK4vpxl374RVqpqo9XGBCmrYgJACiGIQBA4A1ldQKFBLp0XyAoe+Co0Qo7LmbdiQCNwVA1NuJ3ddzbWjWtTWWHD5zR4Diub6soTtu7e+fP+86qzTgAIChqvU5XX9sCPLHoaRMLMWjUOoLH54HIyceJKM0qKr9RYAgJdrE+LpQiCO/vm3f1ssrYTVEWxy1Go74iM9Mo9VTY9ngmhMloNBqNRpOZAKhIO33+duXdi4m2uqwDxy83t2qKkk9dyK4nx8f6yH36Eu92JhId++CerXtovn4kz+WZ//TrRWDeJXxow7Yf6nTDb6Zrhr8dpRCEb7iaWW3Tms2OfNe7bd0Lm+Lmb30xwgHAHMItX7rpROB/BgLqOG361Ge8JZq807hJf+q7hKO1oWs/f92eAfl3k8VoiulzXgnkWNzM6Z8lXh7lofx+R+ri736OcORZ1+n43x8MCck/B5TuETfrc/z79z749L+ffBDqxHvoFXypvTO/fSUX3GzMv7z/XA174jjPB/bAYx7BA4p+/33f760ShrGqoB6kwJP6JSz0AwDwHPz+u4MBDIU3Tu348fjzL40W0FEAUFfcOXTioiLiWYc+CkU/AZiKbl/HKlmNFYVeg8c60gFAEDs84OtNv3iPn+TM7qwzxR6hUfk7zl4vHxbUeXFjRcaJww1Uk4Fn56bVGTi0zueCWzTXThzHWRT3AAAgAElEQVTOpQEwpCNGRnXL06K+dOqiS8y0aE8uuKBfHrgU4DJBRE5i6gP3i+noZrWIzgO9jocBAICp5cDes/3HfNmrLLlA7OpLU525nHalSrzCnc3Q+1cdvp4hNYh9B4qgrrGWIbW1vpYUd6Wv7lhNKwDw2Da09uK15p9cVmj7+boP7Lt/qYjYScYBAIzDZZny1TpzlVYrFLIe0TdvlUjuUKd8ADt27BAKhSNHjnzA+homk+mrr74aNWqUdXJerzQ3NxuNxgcvoLV7924bG5shQ4bU1tY6OTkdO3aspaVl6tSp5NIeTzqecS+tQH9Zsmz1f5Ys7OcqfPDJtizMGiNg1NVcPppUxxTFjx8g4z1kgQKarePI8ZNqmjQolcbXV+SwePeETdFdQ6OoV/a0qPUCO1rRrUsXLuX7jns+SC74E3f2TwMT2CtcFFwvn0CRsL25wJR62HJTfB27v3ooI2DQkDs/nS+Sdi7JbecYNO65WA5uuPjbj+fSbZ+P7RRdQzGb2HHPefeq4Wpqa1Kp6y4cqbwBgOu4XClCOmJ9o5e+RBzHgehYpKOzK7Fbn+I9GFubrjTyR4bY9XoUs5XHDxL8tP03bli4KwXEToHezWVbrtZGxPoD2AnFhlqVta/fXJiTxXC07/Et87xGfjU74ttvv82qeZBrhaA2hKWxSfco4vBxHP/xxx+PHz/el5OtsssPPocgiLKyMo1G84ATDh48uGHDhq5alPdSV1fX2NiYk5OTkJBgNpsbGxvr6uqe1lUx/12gdO/YqZ9Oc1rx6ZoLZeo+XpSaeLia4/7c+GEyXp8cJSrbVqFQOPCx8nrML8Cpl0auvrXNgqEoqq5IO5lU0X/q1DAnIRV7mlpIKF8iUygUEhGvy21hGJ1Cu2flSSrbJdyPfTEpuWelg9L5bCbR96dCZQn43MAB46dNmzZt+qzXXhgjZP7vN/Cvojc/DKBHhde1BrxfZdhYcbVRJ5Yx7vee0IMHDkhb/vmg+PkAQLG1H+DXNusCtthZAsB5YdazH6xYap4xhtracO5E65JvRrKgu63CaOHPv7tY+5/ZCQu/+Hjp/apwOstrerx8yYefvzE+xGRoDAiKuc+JTyQIgkybNg3H8b6IQPr7++/atYtcGOxpA6V6D561grpj0X+WEquXxcq591vwVKvVVtU0m6A2M1fjNADJTk8HAACWu7876/4Vq64i61KpWmLDaiy6g/rEKG2p6prM7b+kTntruiEjKdMkFNMNJXdyfWKHyQToneOZIFG0VRSmVwAAZitzlItsniZT1ke8IoYUFWy5DO2qQBpVVVZ6OkNdfrWZPzzCua+pYNyo6ODdlxKZGm8GpalF5xEd4UDOHeoLvWivFBYVOjk59ep2IQhSUJDv7eUF90ChcLwCA50chOh9fosZIuew8P6D+/tzGVQAulzpHRs7MNjTkYaBnWtwXJC0sbmNxhaNmT7DX2KDYBRnN28PVxcWFUPpNm7ubo5SsatvZKCcjXBkSl8/paeHg1jsrVQ6O0gpAAy+g9LLSyEW+PSLUfIxrRnH2S5iPuPv014hCOLKlStcLtff33/Tpk3V1dXffffd2bNnnZychEKh2Ww+c+bMN998c+TIETabXV1dzeFwmEzm7t27w8PDCYI4ffp0bm6uh4eHVqvdvHnz9u3b8/Pzy8rKQkND5XJ5VVXVkiVLfv/9dwzDXFxcOroBU1NTr1696unpuW7durq6uo0bN16+fNnT07Or9tj169cZDIa9vf22bdvCw8PT09MbGhpSU1N37dpVWlqqVCppNNqmTZuKiop++eUXpVJ5+fLldevWnThxgsPhODo6Xrhw4eTJkydPnszIyMjOzvb19UVRtLq6ev369UFBQffqe5E8ahBUJPcMtKTN35E+tH8Yn9FLRYfjeHp6OoXG9PTycnZ0ZDGpSDtUgVhA7f6GYhSGSCy25XFQBEGpVMJowAnEzjkwROmAAaAUhlgitRPyaXSqSW9AEKrYMzBc6YAhCJMnsuV0pIyxOFwbFv1JtWEoZiOU2osFLBrGFYnt7UQsWrcHiyAUO7G9nVhAxVAAQBkcsdjO1oaBAiAUptRB7uzqYi/kYQyOLY9BRRCEwQ8Jj+oW04HRhPb2YqEt7W67g2EjtLeX2HI5EnupSMBn2cochUyj2YIgLDelO5tsf/aNXvwwnU5/+/btjqV+OzoUrT/bdL335jGFLmGdXfTqc9v3pNa1x1BxHAOmjh/CZYgGDY/tOIPrGDzYseMTZu8dMd67MzUEowaGRbcXkWMXFmgHAMDghsaOAAAAOwcAAIgMb++65Mh8wmRAWEy3MrLco4aEMrGSlON6ePhI1V/CxYsXhULhV199debMmXXr1q1bt+73338/ceLEypUraTRaQUGB9TSVSnX79m3rdllZmcFgMJlMS5cuDQ4OXr9+fWpq6qFDhwCgurp66dKlixYtEovF77zzjpubm5ubm/WqmpqavLw8i8Vy6tQpk8m0Zs2anTt3fv/998uWLetRJK1Wm5qaShAEjuMnT57csWOHQqH46quvNm7cuGDBgitXrri6un7yySd6vV4sFlst4uLFiz09PSsrK48fP75p0yYURRcsWBAZGenp6ZmamkqhUDo0oEkeLw35l1bvz3/1P1848O9bz7HZbLGYTwWGwtf5wdorGI3tKG+f2IUx+R7e3d4aKoPr5sEFAKpA7ifoqiqO8iSOvKdG2gihiBWu1k07uUtvJ1AdXZ07PqFskVOXyXAcsZPSuoXZ+vreR6aVwpA7d0uZY6ewNrGdXa1VIWancLdT/E/l/xfTiw2LGzDAbDZB+5q/Xf8RAODr69OHZJnK/nFifft8ESrblkl9FCIvCELU3vz9m3WbCQyxs3F4+Q3XR5ApAPB4vPHjx6Mo6uHh0dLSolarz549O2vWLKsX6OPjk5iY2OuFLS0tlZWVixcvBgA/Pz9fX18AyMjIwHFcq9Xm5+fjOF5UVNRhwzoQCoWjRo1CUdTPz+/ixYtms7mrwnJXUBQdM2aMXC5HUXTYsGFff/21yWSysbGJi4uzHqVSqUuWLGlsbKyoqLBGckZFRYlEIhRFg4KCUlNT5XL56dOnX3755ftlQfLoIPDG/HNLvjwS9cYH04Mk5PdBQtLLW8Dj9Rpa+Ieg2rt59BJi/3eD0kbMWjZiFsBdDcxHlC2KWjvZUBQlCEKv1zc3N/dFo9JisRAEYR3fQhDE2l42Go0tLS23bt1CECQmJsar955bilVSGUVRHH/APEpAEIROp1t7IzEMs+aIoqg101u3bq1fv37ZsmVCofDNN9/sSNzaPTRo0KBt27Z5e3szGAw/P78H5ELyaNBUXpv/4fYRcz+YNsD9cZeFhOQfAamB+dfD4XBCQ0MPHjxoMBjMZnNlZaV1v0gk0mq1zc3Nra2tycnJZrOZw+FgGJaSkgIAd+7cyczMBAAfHx8WizVhwoSXX3556NChdna9h3r2ERzHU1NTNRoNjuNnzpwJDw9ndJHO0Wq1HA5HoVDk5uZWVVX1uNbDw8NsNq9bt27EiBF9CSQh+VupvXM84b/bnlm8YmosacBISNoheyP+RxAEsbGxsQ4R8fl8q1eEYZhAIMAw7Pnnn9+4cWNCQgKCIK+//rqNjQ2LxXJwcBg9evSCBQsEAgGXy+VyuSwWa8GCBRs2bDh69KiXl5eHhweNRnNycpo6derChQtZLJZCoehwjwCAwWDY2NggCGJra2vt2aNSqba23frfORwOi8WiUCgCgQBBEDabLRAIli1bptfrBQLB/PnzrQW2Oo7+/v7Hjh1LSEiQyWROTk4YhrFYLBsbm46khgwZ8t1333l6ej6q50rSGwSuqbz239UHB8ycH9/P4XGXhoTkHwTytM4csvYlPng6MMmDIQhi586ddXV18+bNe3BcAMnfi7bq6+VfyCcunBjaJwNmMpkOHDggFosjIiLs7e3J747kKaabH2YNY+uxxzpgQ74G/zZaW1uvXr2akpLywQcfkN/+Y4YpnvHuR11nUJCQkFjpZsMsFotKpTKbzQwGw2q6DAZDS0sLi8USiUTW7jKSfwkGg0Gj0SQkJAiFD1nWiORvB6X8FZFWJCRPIT39MLPZbDKZOBwOjuMWi0Wn07W1teE4zmQyKRQK2R7/9yASiSZOnPi4S0FCQkLyIHrGdFCpVAzDMAyjUCgYhnE4HD6f39DQ0NjYaDKZhEIhGZ9GQkJCQvIPoadfZZ14RKVSrTYMwzAqlcpkMlEUVavVKpXqccWAEBaj3mB6OuNPSEhInihwi8lsedC8zP8dAjeZyIruD9DTDzOZTGazGUEQo9GIYRiCIBiGEQRBoVAqKyuNRiOXy30sK8kWnfh8wUnBz2vfIIcFSEgeiuXuyt1mbVN2Tm6LzsKxcw1Qyu+dTIOb9GXV9XIHOQVDAKCtqex2ZokJ6E5+vk6CzuVGLcbWOzfTrFrNHJGTr7cTHYWagrS8qlag2vgG+gpZT/J4uVlfkJNR1aQDACpPGuLrblWuuR+FSbuu4REvDPX+3ycnGVvv3MlqbG1f794tKAqtzdWwFfZYw0+/nH8p4VWyousjPf0wHMfNZrPBYMAwjEajUSgUvV6P0lgWOp8rdQE614yTTQQSkn86VdXNNWoDAGRdu9iI8VxcZFU3z1zMrOx+FqGqLz6zb9vu02lGCwEAxrrcfcfO4VwHe64laf+RSkOnq2FoK0u9VSWRu7i4uDhIbCkItFXeuZ7VJHFx5lmqjx+7qDY/0hv8izFp0y5dNtoqXJwVhtJrv525ZbrXy8JVFw7tL2z+i3LUNSdfTkYlLla4DEttUXZRtZqsXv8oPZsR1hWPrApVKIoiCIIj2M0KTWpB7enkbD7V+OH0of28HXtLioSE5J8Cpm0srRYCgHv4YCaPhwFQ+5Xsu5E30NehQwyVwNt+37MHs3di6nDr54I7KZgson+QG4CipfhOSnqNNExmbefiOj3KtVM4Klh36wyqrcvIsUo6ioKUnrf1QGFdbLDsSXbFABVK5QoR1Z6p/XHfjUpNsHMPV8igqaipEfx1phpBaWKZQnFXLDFoxCQA0NYW/mUZ/DvoacOsw10mkwnHcb3BQGWyDRa0qlHT2toqZOAtjY0tLSqw8AFlAdLlWpP69M9rNh0pQJmIcsyr78ZyFi5ZNnjhz2OdqpfPW+n11mdx6NXV3+xvA3MD6vn1Z+/b63Nee+n9/2/vvsOjqLrHgZ87s32zu6mkkoT0SkkgdAhFpYoCL1JFQAXpqMj7ExQQRWwUGwYB4StIjS8aAYUgNYEQCCEJMQmB9LabupttszNzf38MxAhSBCkh9/P4+GQns7Nnht2cvWXODR7eq+JCVrZeNGvskD/OJhVUlWjtunzz4RsO9anTXvksemTXwgs59RWXff+zatHYnk0vVZnx0/IP91jlYFFFLl82L9Dhz8pJPGNcOW2MNrCnuDBfpMJTXlv0YC8eQTyubCBSKCUAoFCphCRkqmuQ2/tCsx4yRClGvbLAqi/ac/ASAABgxmpF19Yckbg4qzIqKqoranfvPD9h7iTa1FjfoLuUeVEisw8P9REBiK9XBOWMBhOWqJQtOoH9iWJtVqDqLx3YUOkwYXh3pQi0+Unxx2rC3auulFXU/ry9umt/T8B1Zdm/7M0wNmiNLl0mDOqilNiunE87m32Jp+RWA9dp+ND2Hk4VZ3b/dFnc1o411GuxV4+R/Topbj0O88eRbTnyHgOu1/e2Gcp/3Z9YbwOjSTTwP88HOJJVI/7ejX2Jwk3NwrQOqVz57anKD3++lJZb2qivR4yRYs3AFEPFSqg/BripsY0LknfEnafXbvnuuw+nZ+/57rK684yJ/U7s/Sl53z5L+5Fjot3svTotWrXu448/GW53/tvDuSzPmRrLXaMmrN28+cOhdp98dbDXzGWbN383SJL8fyfyeY7V6zPF7cas+Wbzd1u2aPe/93uu9tpL8TWrP9vUY/rSzZs3P+uY9+1PaTdEbzFqkWPX9zdvfm3WrAd86Qji8UWpXdo6Xa86jbG1Kvdkdl1EuN9fB3mQWCJpapYBorz9gxuunL5caWyoKky9VIgxKBy8Bw/vZ0dRcpeQAb0j5GL2akri/mNZ5ut9XhxjSj+dxHtEemse0qk9MNhiMhn1defSLnpG9Azv2JEvy6isMwPwpVcKvTu079N/sL+ne+yzE2Ij3AFjo4XuOXTkhAmjoPh8UbWpruDCsUxdnxETJ0yYMOKZsNMHjjSYWZ5l6gxcl6efmzBhNF+QcqXK2Pz1OKbuyI/bt2/fvv3H44085myMjeWbYsk4dZRx7zZuwoQxPRwOHUkztuiu2gfpb/oSaZqWyWQcx/G0+FB6EWIaHUU2KTZLEetqr1SIDNCQBlYx2MdeS4EYZ5462lDl/MOGtcDUNhSl/FEOL/Sd2il98Zcp6o8+GCIByEk/tP1gJhbJr2aVukcYeZAiCOzW20sMEBga4eRmDPGzB4BQn7a78su4cIlU1mfQIF8JADj5R9op8surI4X4qtOSzlQgv32fpEJJ7tVSSyFAj7+egXuX3sFyAJA4w8OqW08Qj5u2bZQOcuHTbblyLu33c+kRA8d19bvF0lbXIMfAnuOldsdSEi+r2rTz8bqEJBKZ2j9ADQCgdo2IcAWA8HCvDWv2aSMDfJxkjTWFx/6XUO/bY3Rsp5bfCrNmJf+uldPOvn2GR/qJKYj2luSVVPsrmIxCUb/uXgCVf+6LKC//YAe5CMDdQ2FpMDfyBfkK766eahkAOHoEe+G0EovFASEPv1BnOzGAq5vCWttoAPhz2TFa4jBg5IQg1c2RAFhqcvLLsXfJ8aMlvKnaWG0wM6Ak1W3/zt/0JbIsK8zsQEgMjNFLxS8dLbYXVwBrBcZij7PApAfKfH3eEwCAVC53Duw0dGh3ABg2arJnO2AatYV5ZoUUahrZQNHlb7/e13Px/73Q2eHnD64k3lVgNhsrRGczcbxaIgIzAACIFWoX1x79nwl0EsHQoXbOj6z+Kca4pKREp9MBgFwu9/f3l0gkRUVFGo3mhiK894xhmLy8PKvVCgCBgYGk1BBxDy6fPXwimxo2foqrWnnnvQE03h1GeHcAznhqX65/J5+/6friEKZ4nudtpqKE3Uc8ug95ur2/5EkofiDrPHBYJ+c/zzgwPOziqbRsm1gaGOmlvv4n6BbEYjFnYXgACoDnWTOLJeg+LgolksmkGp+gcDcxQHjHXopmYybEX9x4lW02m81m4ziOYRieY9soQCW2BbtVucrSXUWprpAsNeeAxQQi5z+fi6gu/QbXFZ6GNmFhYW3rChooKZw8sAF1fXFmd8+vtu0DKcU0AiWi9YVn4o9k301YFmPaj7vSrAAVqdvOWkL6dbw+i8QhqmewJacWhYWFOSj4hppH1tLCGH/99dc7duzIyMjYunVrXFwcx3GfffbZiRMnbv/E5OTks2fP3vH4DQ0NwnrQGRkZv/766/nz58vLy+Pj41n2Dn0K1dXVu3fvZhjmH5wM8cRqSD1d1PmpPu4aJXW7ueLXMLWVJXVGAChNP5bL+0f5qS31pYd/O2XksaH0is4KANYrp09xLiGOatHVlGSbd+fuHZ+MBPY37L0C2tgK4o+XdmzvSwOAWCxFyGr9208W7R0cor98NrO0DgDKss/onfy97e4j7Uid2we6FJZrHV3c2rSR1FYYyTJZt3JjrSmMsc1mq66uFolENhv732cjRDQH3CFgrCCKBLUTuASByBWU7QD9WbDDsePouDncuwunUghHDnkt6I/ElKK2k+f39aWDC77e9Hvx8Lc/mPbZ2tdP+XZ4dtIUo6+TWCHu/UxPYc1zqXNAbE+rMF7pFtI5BrlRUCuTd/QSnZw39Usr1+7DzSuCFBKtR0SfaKUY5P9v1Rcfro2b+pPevm3orHlvNo8f0eIOvft6ONx58cl/BUVRAwYMGDx4cFlZ2euvvz5y5Mg1a9bcvhwXxjg5OdnV1TUmJub2B09KSqqoqPj000+FdTUxxqdPnz516tSwYcNuv55ycXHxsWPHhg0bRupbtmZarba4ojGya7BzG8dLx3/JvpbAnAeNf9oJ/SWbiaQqv3ZetJDisPnCsWMnzJyTV/sXRkUoAEyYZ6w2DGA1Vf229wwCkHu1nzEugqa4Oo27qDRrz/YsAACQ+EX17Brq0VL/0tIS74BgB+lfw5c6RQQ6Zxe4eGtkAAAi1/4Dovcf22Po2D/E1a8d1gjX0cMvRGUnk7u2f3Gs5uTv+7NsSOYUNOE/0QqKMrv4+NnZCwd18w0Wq5vNy5Ao/AIDVM3auRp3P2+pSiyDoGB/MdABPUcYko/s2ZmDKKrL02NJeaRb+cvaKzabrbKyUuhLBACe53meV8iotnb7ofYwMBhUg0HVGRy6P9CYjFdOTJz6fx8e3xhyx10xoyvTWq8/Ets5uNpf6zB50Guv8Dy/ZMmS3r17Dx48WKfTzZ49e+XKlcnJyQEBAc7OzvHx8R4eHikpKe3atZs7d25TOjl58uQ777wjl8v79es3d+5cvV6/fv16nU6HMV64cKGPjw+6/vclOTl59erVq1atateuHU3T+fn5K1euzMrKGjhw4PTp00tLS/fu3cswTGxs7PPPP5+ZmXnkyBFhOemMjIzz58/3799/+vTp/v7+tz4D4olF1l75V2DOlPzTbr3fU4M6et5FI5Z4NP7yjV4sFrdp08ZoNFqtVo7jhCpTMpkEuIHAKoGxgMQXlIGPKtab8Zzu5w0biq4/9OgyfMbwLg8/jNTUVA8PD29v7++//16tVkskkoSEhFWrVo0ePXrx4sXHjx9/6qmnhD179eo1bNgwV1fXSZMmVVZWLl26dOrUqTExMZmZmcuWLXv//fe9vLyEPbt27fr888+/+uqrAwcOHDt2bEBAwNSpU+Pj45cuXSoWiw0Gw/vvvy+RSKZPnx4SElJbW5uYmPjVV1/5+/unpaVt3Lhx2bJlCsVDao8SxJPHqstPPH7BrAwmCewxd2OvlFQqlUqlQuMM/dnnEA6ysGs/3s9A5d2Re8d8syPsbuZFUCLPae+996DjuRWO4+Li4vbv3+/p6blo0aLmJbhCQkJiYmKkUmmnTp2ys7MHDBhw83fhixcvajSamJgYhFBkZKSHh0d2dnZTDqNpety4cQMHDty9e/eMGTPWrFnTvMXMsuyaNWsqKyuvXr2q1+sBICIiwsfH58GfNEG0CmKNR7d+Tkq1msyleMz9/cgKQjd880Bw45YHiBLLXD1awDuHpunp06cPHjz45l8J5f+FfYSiJzdjWVaohAIACCGJRHLDfA2KolxdXWfNmqVSqfbs2dOvXz9he1VV1YcffvjWW29FR0fPnj1b2CgSiW76VyMI4h5REoWTE+nJaAFIR/nDJpVKLRYLAISHh1dWVl66dAljfOXKlbKyssjIyKbdioqKqqqqAMBms5WUlDg6OkqlUoZhhEk3GGMfH58rV67k5+ffcHyJRCLs8DBPiiAI4pEgd83dOycnpxvGnBwdHZVKpUwmc3FxEbaoVCrhBi8BQmjgwIHr1q2rq6ubNWvW/Pnzv/zyS5qmKYqaP39+U0ciAFy6dGnPnj1KpZLn+dDQ0BdffJHneZVK9d57702ZMiU6Onrx4sU+Pj6BgYEymQwh1LTaso+PT5s2bZYvX07mdBAE8cRDT+oX9gc9L5EgHltkXiLRepA3N0EQBNFSkRxGEARBtFQkhxEEQRAtFclhBEEQREtFchhBEATRUpEcRhAEQbRUJIcRBEEQLVVrvMcZY5yTk/OooyCI++Xj40MqOxOtXGvMYQghd3f3Rx0FQdwvskQcQbTGHAYA9vb2jzoEgviXWSyWy5cvAwDP8yKRyGKx5OTkFBcXk2LQxBOsleYwgnjy2Gw2mUzm5+cHABEREY86HIJ4GJ7wHCaRSEh/C9FKcBxHUZSw6A9BtBJPeA6jKKr50pQE8QQTiZ7wjzNB3IzMrScIgiBaKpLDCOKxZ67+7cBRlnsyl0kiiPtBOh8I4rEnEnOX40cczvt26Use9tL7P57Rhi5qqdJGiseAAJzkOMqVc5SRHEm0PCSHEcRjT6wZMnOF7qPFCz7c+s3SKQ6K+xriLTOgd5Jkp8pEDQzCGDgeVBIc5cq93dXa2Y37t0ImiIeD9CU+MhzH/fTTTwUFBY86EKIlEDtMfmvFf1wuvbh4c63Rds+H0TNocZJ8X7642oza2aNJ7SkRDXoGHSsRzToi15rInWREC0Ny2D3CGGdnZ7/99ttTp06dOHHixx9//E+PwHHcL7/8UlhY2HxjUVGRVqv916IkniQSp5Gzl77omT1zxXeF9dZ7O0Zioehw4bXJ91Ia1j6NXotGEhoA4Eo9tTlTwpMORaJFITnsHlkslvfee++pp57avHnzxo0bR48eff/H5Dhu8+bNJ06cuP9DEU8kSub4n7nvDrZLn7psS+09ZZvkctrMIoRAqN1RZYSXO1GT2iMRBTyGc1W0nrldU4zjOIZhGIax2a61BY8fP56YmIjxA099lZWV69ev57g79HZyHLdr166MjIy7OSbLsg8hcuKBIjnsHtlstpKSEpVKBQBNxRFYlj127FhcXFxCQgLP8w0NDb/99ltaWtq333574MAB4WPP8/zRo0fj4uIOHDjAMEzzY6anp6ekpBw+fHjfvn0YY6vVGh8fHxcXt2XLlqY/GURrJ3GavGjlQteU4f/dWmn8x8NXqVU0AMT6oCkdkZSG3Bq87Dj/2VNUe1cEAJfrqDrL7XLY5s2bR40a9d///nf8+PHHjh3jeT4/Pz8vL+9uMgHHcUlJSXq9/h8FnJ+fL1To1uv1SUlJPM/ffn+McXp6enl5+R2PzLLs5MmTk5KS/lE8xOOG5LB7ZGdnN3bs2CVLlnz33XdNvX+HDh3as2dPeHj4yZMnDxw4UFVVtWjRouTk5KCgoN27dx87dgxjHBcX9+uvv3bo0EGv1y+Qn6oAABzASURBVJ87d675MV1cXFxcXHx9fQMDAw0Gw7JlyyoqKtq3b6/T6ZYtW9bY2PgoTpR47Fj02j/KTf7+3jLxPx6+KtFTAFDRCJMiqVeikJsdvBJFbUrH+bUYAKrNlIW93dNFItHYsWNXr149b968nTt3Wq3/oEvTaDRu3ry5urr6HwV8+PDhkydP/qOn3CWappcvX96hQ4cHcXDioSHzEu8RRVFz5szp1q3bpk2bvvvuu48++igiImLHjh1vvPFGx44dAWDLli1z587VaDTjx493cHAoKys7efJkt27dDh48uGbNGn9//w4dOiQmJjY/poeHh4eHR2BgYHh4eEJCgslkmjlzJkVRXbp0mThxYk5OTufOnR/R6RKPDXPJ6mXvpXm+sHV6f+U/f7aBQQCQU43fOMRvfpaKcIEvU/E7R3mTDQDAzIKNv6u8KJfLKYpqqiZcU1Pz+++/jxw5UiwWZ2Zm6nS6/v37WyyWXbt2FRQUREVFDRs2bPv27ZmZmZ9//vlzzz0XGxtbWFi4e/duk8kUHh4+cuRIoURWRkaG0AnRu3fv2NjYjIyMX3/9laIojuO6desGACdOnEhKSnJzc5s8ebJU+udtBhjjw4cPJycnu7q6ms1mYaPRaNy0aVNtbe3AgQM7duz4yy+/DBs2zM7Ojuf5AwcO+Pj4XL16VSQSqVQqrVa7bds2vV4fFhY2ZsyYS5cu/fjjj3K5fPz48R4eHv/8MhMPD2mH3ZcuXbp88cUX8+fP/+CDD/R6fUFBwcqVK6dOnbphw4agoCCEkEajUSqVCCG5XG6xWKxWq81mE9Z8omm6+YfwBnV1dWq1mqIoYU9XV1eDwfDwTox4LDF1+ctfX1QT8dL/vTHiHhJYc3oG9AxgAK0JuDv0z/2J5/lLly4dPHhwy5YtY8eObXoD19XVCb3lGOPc3NwzZ85gjNevX280GmfOnJmamnrkyJGhQ4cGBARMmjQpJiYmNzd36dKlgwcPnj17dlZWVlxcHAAcOnTom2++mTZt2rRp0/bu3fvrr7+Ghob26NGjT58+Y8eOlclkV69erampmTp1anZ29r59+5oHtn79+tOnT8+ePTs6OjolJQUATCbThx9+6OXl9dprr/3www/Z2dnnzp07duwYAGi12v379zs4OCQmJpaWlhYWFi5ZsqR79+4zZsxo06ZNbm7uN99889xzz3Xo0GHdunU3dPgTjxuSw+6RMF4FAGKxuF27dlarVSaThYSEzJ07d/PmzVu3bl2wYIFMJrvhWWKxmOM4nU4HAA0NDTf32iOEhKEFT09PnU5nsVgAwGQyVVRUuLi4PIwTIx5XrL7g65Xvl/qPfe+lfgrxPX5ypTQGABcl+vQpZGbwlVoYFYqmdUISCgBATAGN7jCyxbIsy7IRERGJiYkmk+lWu9XW1p49e3bgwIFyuTwwMDAlJUWtVkskEgcHB6lUumPHjlGjRkVERDg7O48bNy4lJaWxsTEhIWHSpEmenp5eXl7jxo1LTEykKEqpVNrZ2dnb21MU5ebmNmTIEC8vr549exYUFDSNjVmt1jNnzowZM8bZ2bljx449e/YEgIKCgvLy8u7duysUCnd397y8vMGDB588eZJhmKSkpICAAE9PTwDAGJ84cSImJqZbt25ubm69e/dOSEjo1KmTr69vUFBQWVlZZWXlvV1q4uEgfYn3qLa2dtq0aX379qUoKjc3d/LkyU5OTi+++GJcXFxqairDMNHR0d7e3jc8S6lUTp48eenSpbGxsWazuaKiovlvaZqOiYlJSEjAGA8dOvTChQvz5s0LDQ29fPny6NGjQ0NDH+L5EY8Zc8nyN96qCZ/y7fwh93MYP3ucVY1iPOBsGSQW4Hd6w3fpePOz1JkyPq0Cuyrx7e+fpiiqQ4cOw4cPNxgMs2fPzsvLu9WeDMMUFRWtX79e+CYn5BWBMN1Jo9EIXZFqtRpjzDCM0Wi0s7MT9nFxcTGbzTfM4FAoFELLTyKRMAzTNJGE4zir1SqXy6FZmW+LxZKXl7d69WqhFLK/v39kZOSuXbtyc3NTUlImTZokvDrP88XFxaGhocJDjLFerz9//rywEltoaChZKfsxR3LYPdJoNCtWrBBm+g4fPtzHxwcAevbs6eXlpdfraZoOCgoCgLVr1wqfqP79+3ft2pWm6RdeeKFLly4mk8nZ2XnChAkODg5Nx0QIDR06NDg4WCKRKBSKefPmXb58mWGYQYMGBQcHk5UMWy+LbuuqFY1Rr340pd99HinUicuqpg5dxYkFOMgReajgtc7U+nM4rwYDQFsVr5Lc1Vxzg8GAMXZ0dBQeKpVKnucNBoNYLBbetA4ODuHh4ZMmTYqKijKbzRzH8TxPURTLsiKRKCoq6syZM126dFEoFBkZGa6urhqNJjAw8Pz582FhYQCQnJwcEhIikUhommbZ284zAZBIJEql8o8//vD19a2urs7Jyenbt6+7u3tgYOC8efO8vLyEwGQyWXR09I4dOyiKateunfBciqLCw8PT09OfeeYZpVJpMBgiIiLkcvmbb74pEolqa2ubzpF4PJEcdo9EIlFkZOQNG2maFibZN2l6qNFoNBqN8EQhvf0tqVQaHh4u/CwWi4XPM9HaIWnk8DkToyJoCgHHYaMJOA453Mta5L082P9dFtuuz8lv3watTcErTvImGyCADi6cvfR2OYzjuPj4+MzMzJqamqefflrojgMAZ2fnnj17Ll682MnJSafT+fj4yGSysWPHfv31187OzjRNT5gwITg4OCoqatWqVRMmTBgxYsTHH3+8aNEipVLJMMzMmTNpmh4/fvzq1auzsrIQQhKJZMGCBQihzp07f/755zabrU+fPreKSiQSTZs27Ysvvjh+/Li9vb2Q81xdXYcMGbJ8+XInJyepVPrqq696enr27dt33rx5b775plJ5bTwRITRw4MDCwsJ58+Y5OTmFhISMHj36k08+WbBggdAL+sorr9zDdSYeGvSk3uJXWFhosVh8fHyEHgaCeBLwPF9Syp6/wGb/ARjToSHibjGUhztQFADU19fn5+f7+/vf5gA6E5p+WH6sRAQAIc5odChac4YXald52vE/P29qp7ndBA+bzSYMAwvTlCiKEu5cFAZ6zWYzQkgsFmOMpVIpxljoD6QoSiaTCY0wi8UirEzLsqzVasUYi8XiprkhTceXSqVCB4ZwEGGLsFA1ALAsy/N88+VthfFpoZGHEBKJRDRN8zxvNpsxxjRNy2QyYbDZYrFIpVJhtpTFYhGLxTRNC8HD9VVzbw6DeGyRHEYQLQfHsZmX2DMpttQ0vrISicV0SLB03BhRZDhQ1N3kMABI19Lzjsrz6igKAcZgYUFMg6cd/25363MB5FZ6ooUhfYkE0XJYrVBfj3U1uKYGcRzwmEvPsDQ0yKa8KIq523sHO7bhfnrOeLhIlFtDcRgQgKcKD2rHetrd9RR7gnhsPOE5jOf5Ow4IE0SLQVGcnR2vkGOlAhsageeRVMIVFFni98m8PDmavsvD2Evxf4JIk4t4EjzhfYmurq6POhCC+FexLOh0UF2L9/4Il/4AlgWpFDAGXx9j56jasGDviIhHHSJBPDxPeDuMIJ40IhG4u4O7O3Jzxd9shLQLYGWQRIKvFkqLip0u+lNzXETebR91lATxwGGMbTZbK81hRqPxUYdAEPdHIZeNfo4yGiEvH1utIBZRLCvKzkE7dslenkqTNEY86ViWbaU5DGOcn5//qKMgiPsV4O+vnDcL7/0fZGRBdQ3mOQzAn02zGIzSaZNFIcEgao0fcKJVIeNhBNHCWSw4Lx927uXz8jiLVapQIJqm/dtJx4wSd+sKUknzfbnGLAwYADCGBpOiqLReuEcqIlAqkchFylvefU8QjxuWZQ0GA/maRhAtnEyGIsOBpvGuPdyFDMxxiKK4/KvWbTtxfYNk2GBoNl/RUrpWovDFgDmW09aG5l3mnZ2diwqv+ilKOKpOFfbVIzwPgrgHpG49QbR8CEF4qO3F8fWxvUGlAoYBhuGuFlh37bUlnYZmt5dQtFIkVktUHeQq39oarbe3t4eHB88ZFXZupCAn0RKRdhhB/KswBrMZjEYwmbHRiEQi0GiApsFiBYsZLBZssSKOB8wDzwOPMeYBY5BKkUYDTk5gpwAAaOrgR9ePyXHA8cDxwLPA8cBxwLLAccBywHEgokGjYe3tzf16AwZ85Cg2mkAkApa1HTlKhwZTfy7cgwF4wDwAB5y+vLz8woULDnYYIQ6exFEFk8lkMBge/phCbW0tTdNCidSbGQyGqqoqNze3pjr9TRiGqa6udnd3b/6Vor6+nud5Un34b5EcRhD/Kp4HQyOu0iKtFlVU4uJSsJiRWo0ZBpnM2GQGqwULiYfHgDngMcIYxGIsk4GLM3JxxggB5hEgQAgQwggAA2JZzDBgY8FmA5sNbCzYGGRjMWsDGwtiMbg4U37tpPZq0OoAIWRnhxsNfG0tm53DXyn4M4dhAHwtjTlpwMEnzN/f31h9nqaMHL7bOh07duzIzMwEAH9//wkTJty8Tt7jIzk5eceOHZs2bWq+MSsrq6SkZPDgwU1bMMZJSUkWi2XAgAH33x7lef7rr792c3Pr0KGDyWTq06dP82MajcYPPvhAJpONGzcuODj4hucWFBQsXLhw7969TdUgMcY//PCDwWBYtGjRfQb2RCI5jCD+VRQFDvZIqYC2XmC1QnUNupwPpWWAAWQ8YAw0DRwHmL+WTjCPMUZmK9TWgVYLGBAARoARAkQBQkAhQOjaNIy/whg3rXoFWq00K9uJZcHQiJwcRB07sGkXuNJyvkprO3NW1C2m6SlCHgPAMilVVldXXlbo7YKpOy19KdBqtStWrAgODp41axZN06dPnxaWH2pBbDbbli1bRo0adcN2rVZrMpmaLum/Ijg4eNmyZUFBQe7u7k0by8rKiouLv/3226ba+cT9IDmMIP5VCIFEAte/RKM2LuDfDixWxLLAskjo/eOv9yViDDwPHA8GA5SWoaJi3GhEHAssD/jab4WFGrGwM8aAMeKxkAIx5rGQCK1WZGWQxULV1GKrhTOZ+CotWKyURIwUCqRq9rcSCx2J1/6fnZX2R3am1/BOgLm7maK8c+fONm3azJ49W3j4/PPPCz8wDCMUsJdKpSKRSKgiT9M0wzBC0XqGYYSi8kI9e6vVKhKJhHUsZTKZUDmeZVmhxrxYLBYOSFGUULOb4zhhTXPh+ELN++YvJ9SnFx7C9VUxMcY3p9iKigqMcfv27ZtiBgCJRPLss89ijCmKaoocYyyRSIQy/DcH3BQVQkioyg8ANptN2Ee4mCqVysfHJzMzsymHYYxNJpNarWYYRij8L5TbB4CmwzZpOs2mfxohEo7jhCvJ83zTKTTV/m9tSA4jiAeJokAuhzsunsDzKKojMAxiOeB5xHPAY+B5jDFgAJ5DGGOeR0LO4zHmOcTxiOOA48DGYm0VZGShzEsI85jHwDHAskgqRQ4OtJ+v5KmBTa+Dhf9hDICVCpFcbOrbtx/PXEaUEgAD5gDdsuhiY2PjqVOn3nrrrRu2Z2ZmfvnllyKRqKGhwcfHZ/HixXq9fuLEiT169KirqysoKBg0aFBxcXF9fb1er1+3bp3FYnnxxRefeeYZnU5XVFTUtWvXOXPmnDp16pNPPunSpUv37t07d+78zjvvUBSl0+mWLl0aEBCwevXqsrIyhFCfPn2GDh26evXqqqoqABgwYMDIkSMTEhK2b9/u6Ojo4OCwZMkShNDHH39cXl4uk8kaGhpuaFclJye3b99eLBbHx8efPn3abDYfPHhw7dq1ZrP56tWrCxYsmDx5cmBgIM/zFRUVjo6OK1as0Ov1kyZNEgIuLi6OiYmZM2cORVHr1q0T+lRjY2Nffvnl/Pz8NWvWIIRoms7Ozh4zZgxCqH379mfPnn366aeFV6+rq9u6dWtycvKnn346Y8aMmpqar776SiKR1NfXBwUFLVy4sCnO8vLyTz75REioRUVF3bp1A4C0tLTPPvvMwcHBZDItX768qqrqrbfe6tWrV0hIyLhx44Q82tqQHEYQjwGKat56a4Lu4mfAGFksYGcHVTq+uIRGgCgKqVS0pwcdFiIZMojycG++9/X/eGd7GW3Lri2vCgxnES/ibCZzxf9kbs8i6sYwBEajkWEYlz+nhwAAWK3WTz/9dMqUKX379jUaje+9997Bgwd79uyJMR40aFC3bt3i4+M3btwYFxfXtm3b5cuXHzp0qHfv3gzD9OrVq1evXiaTafbs2efPnwcAqVT6xhtvqNXqjz76qFevXhMnTkxNTf3yyy/nzp2bmZn51VdfOTk5GQyGsrKynJyc9evXq9Vqo9F4+fLlvXv3fvHFFxqNZv78+efOnSsvL2dZdt26dTKZ7KuvvkpNTW2Kluf5wsLC7t27SySScePGvfDCC7t371YoFM8888y+ffuEfViWDQ4OfumllxiGWbFixYEDB3r27Nk84Dlz5qSmptbU1NTV1W3YsEGr1S5cuHDYsGGbNm3q3LnzSy+9ZDQa58yZIxzN1dVVp9NxHCe0sRwdHadPn26z2d59912GYRYvXjxjxozu3bs3NjYuXbo0MTFRGCHDGH///fft2rWbOXMmxvjNN98EAIvF8s0337zyyiuxsbEbNmzYsWNHbGwsAMyaNcvNze32768nGMlh98VkMv3www8FBQUA0Llz5+HDh4tIZQTi4auvx+kZuKICeIykUtrLSzJiqDiqE+XrQ7m5QvOGCMbXuhMxD4BpxCuVdjTVwLEmsUzN1R/j7LuIFD5/+yJCj1lT55VAr9frdLrQ0FCEkJ2dXb9+/U6cONGtWzepVBoUFERRlLe3d5s2bdzd3Wmabtu2bUlJCcbY3t4+Ojqaoig7OztnZ+fKykqNRuPj46PRaIxGY0pKSn5+fkZGhsFgKC0tVavVvr6+CxcujImJmTVrFkLIw8Pj9ddf79Gjx6uvvpqcnJyTk7Nq1SoAuHDhQu/evc+dOzdgwACFQgEAoaGh6enpzQNmWdbJyUn4OScnZ9euXWvXrlWpVE07KBSKmJgYmqblcrmfn19BQUGPHj00Gk3zgMvLy7OzszMyMpYsWWK1WvPy8ioqKvLz88ePH48QUigU/v7+QvtPpVLRNP23/bT19fUNDQ3BwcEIIZVK1bt377S0tMDAQABgGCYrK2v27NlCT2lwcLDBYKirqzt37hxFUQkJCVevXvXy8uJ53tPTs+l0WifyB/fe5efnf/rpp0OHDh09ejTLshcvXvzbd+q2bdsAYOLEiQ89QKIV4HmoqMCHjsCZs1BdQwGgwADZ2NGS50eg200XxAA8AM9YjRp7FUA9AFAUjXkO8C3XKtJoNBEREUePHg0ICGjaKKyD3DRsU1ZWptFo7jgtguM4hmGUSqWw1LKQbwQikcjJyWnixImdO3cWHiqVypUrV9bW1n7++ecrVqz473//+/HHH9fU1KxevXrVqlUxMTFhYWFvv/22MJFPKpVeunSpvr5emJ2h1+tvGBKTSCRarRYALBbLl19+OXHiRG9v779eUZ5hGOF0DAaDWq1u2tgUsJ2dnVqtHjBgwLRp0wBAWL2apunGxkZh56YJ/Q0NDbeaJyIWixFCTa9VXl6uVquFPYUDGgwGYU+DwSCsW+3t7T1z5kwfHx/hRLKysm5/nVuD1th/+q9gWXbjxo1DhgwZPny4vb29s7PzgAEDKIoS3sQAYLVazWaz1WotKyurra3V6/VPalkv4pGx2SD/Cuz/DZLOYL0BWBa3cRaNGC55dji6xQg/FiZ0QFNT7Nrm640zfPu7xCZMmHD06NHt27dXV1fX1NQkJCTQNN2hQ4eNGzdqtdr09PSjR4++8MILdxyYMRgM27dv1+l0v/32G8uywmCPQKFQDB069JdffjGZTCaTKTk5WafTnT17ViQSCU2Wqqqqc+fOicXioKAghFBoaCjHcZcvX2ZZNi0tzWAwDBo0aOfOnZmZmUVFRVu3bhWShICiKD8/P2Hn+Ph4mUzWvXv32tpaYcKIwGq1fv/991VVVSkpKWlpaSNGjKAoymAwbNu2TQjYZrN179796aefvnDhQlVVldVqPXHihFgsjomJ2bBhg06nS09PT0hIED7vZWVlLi4u9N8t7ebo6BgSErJp0yadTnfu3LkzZ86MGjVKyGFisbhv374bN24sLi7Oy8vbuXMnx3EODg4dO3Y8ceIEx3GlpaW5ubm3v8itBL1s2bJHHcMDUV9fz7LszbcQ/luqq6u3b98+ZcoU4WuaIDc3d/HixUOGDKEoas+ePYcPH1apVFu3bi0uLjaZTBEREWKx+AHFQ7Q6egM+m4p+3o/TLkKDHkwmTiG3duuqmDhW6uQIt2gJMdpfJDINojXAGzHmc682sLzUzcHsqJZwnA2ApzQ9aMkt76V1dnYeMWLEoUOHDh06dOrUKZVKFR0d3b9//8rKyvj4+KtXr86fP9/Pz0+YmNepUyeJRMLzvEwmi4iIoCiKZdk2bdo4OjomJib2799/9+7dZWVlS5cudXR05DjOzs4uNDSUoiih6+zHH388c+aM0D+/bdu248ePUxS1cOFCs9ksPJTL5fPnz1er1b169dq2bduJEyfkcnl0dLS/v3/btm3j4+Pz8vJeeuklNze38PDwplOQSqUHDx7s1KlTcnKyyWQ6c+bMqVOnlEql0CnXtm3bgwcP9uvX7+eff87Ly5s3b56fn19DQ8Phw4cHDhy4a9eusrKyd99918nJyc3Nzdvb+/vvv09OTg4LCwsICIiOjmYYZu/evVarddy4cb6+vh4eHnv27AkLC2t+HxjP8yKRKCQkRCwW9+/fv7Cw8H//+19RUdGCBQt8fX2FuZFRUVHt27eXSCTx8fGVlZXTpk3z8vLy8/Pr0qXLxYsX9+/fX1ZWNmDAAKlUKpVKIyMjW+dsDqFxTGr+3qMrV64sW7bsiy++sLe3b9r4xx9/fPTRRxs2bBCLxTt37iwpKXnrrbc+//xzhULx8ssvP6BIiNZIb4DE3/HJJFyphcZGsFjAXmNuH9nwVH+f3j1v89VNn/GSXO2DEI0xy/P457O+SpWzAzrT0c/A2syAQeb3ttjO/4HGXlRUNGPGjL179z6SG6RsNtvy5csHDRrUq1evm39rNBqnTp26ZMmSyMjIpo3FxcWvvvpqfHz8Pw24vLz8gw8+WLJkSfP7w4h/C6n5e18UCgXHcS3uBk/iSWBj4VI2HDkGtXVgNALLofAw6NqF7xhpltyhoS9xHcMCvj7FHoVF+vA8r5bYYbWZBgCgaKnL7Y/Q0onF4ilTpghDYg9aQ0PDyy+/3JonDT4EJIfdI2dnZ2dn54sXL/bv379po0gk4nme53kAEG6xfHQBEk+uyko4kYTr64HnQa0Gn7bo5ZfAxxuMRrjTn2aZ65DmD8MfxV9Xb2/vn3766RH2q/v7+/v7/31bU6lUbtu27Ybhq7Zt2/7888/3EHBoaOg9hkjcNZLD7pFYLJ48eXJcXJzFYunUqZPNZsvOzo6KipJIJKmpqa6urr/88kvHjh0BwMXFpaCgoLq62tHRsXV2WxP/Jozhj1y+sAgYG5JKUKcOEB4K7m7Qct5aCCHJTXfCPT5uzlWPecCtHBkPuy+1tbXbt2/X6/UIoW7dusXGxhYXF+/cuVMsFkdHR4tEol69ehkMhp07d1IUNX78ePkd6zUQxO0ZGuHocf7secjPB0dHNOQZ1LsnqFWAkMFg0Gq1ISEhD24qE0E8PoTxMJLDCKJFMZlxdjZcLcSlZVRkBHSOAodrs4qEHBYQEEBWAiNaCZ7nSV8iQbQoMhkKCACVGgUGQIA/qG5scjUVnCWI1uD/A5XyNynBqc/WAAAAAElFTkSuQmCC)
# 
# 
# On Apple, it is done by right-clicking on "folder name" and choosing the option 'Compress "folder name"'
# 
# Then, in Colab's Files window, click "Upload to session storage" and upload your new zip file. 
# 
# Next, you can unzip it by running this code:

# In[46]:


get_ipython().system('unzip data.zip')


# (This assumes your file is named data.zip, change the command if not)
# 
# Now, you will have the directory with the data files of the course in your Colab session, but Colab doesn't always show the change immediately. **If you do not see it yet, click the "Refresh" button** (next to the Upload to session storage button) to show the change you just made. You should now have a directory called "Data" in your session and inside of that there should be the file "adams-hhgttg.txt", among other files.
# 
# **Important note**: Colab sessions are temporary - the next time you load Colab to work on this notebook, you will have to upload your Data zip file and unzip it again.
# 
# #### Manually creating folders and files
# 
# Besides the "sample_data" and "data" that you now have, you can make another directory by right-clicking somewhere in this file system window and choosing "New folder". For example, create a folder called Stuff for your code's output.
# 
# #### Permanently saving your files: Google Drive
# 
# There is also a more permanent solution, which is to link your Google Drive to your Colab session. You can do it by clicking the "Mount Drive" button in the Files window, or with this code:

# In[47]:


from google.colab import drive
drive.mount('/content/drive')


# In the Files window, you will now see an additional directory called Drive. In this directory will be the contents of your Google Drive. If you put your data there, for example in a directory called "data", you will be able to access this from Colab. It will be located on the path `drive/data/file.txt`. Anything you put on Google Drive will still be there next time you open Colab, as long as you link your session to Google Drive again.

# ### Opening a file
# 
# The following code opens a file in our filesystem, prints the first 10 lines and closes the file. Please note that this file must exist in your Colab session (when running on Colab) on your computer (when running locally).
# 
# If you are working locally and you have only have downloaded this notebook, go back to the repository and download the file to the appropriate path (or change the path below). 
# 
# **Please note:** The code below shows you how the `open()` function works. It's better to use a `with` block (see below), which does this opening and closing for you.

# In[48]:


infile = open('data/adams-hhgttg.txt', 'r', encoding='utf-8')
#If you have put the file somewhere else, such as on your Drive, you should modify the path to open.
#For example to '/drive/data/adams-hhgttg.txt'. Otherwise, you will get a FileNotFound error when running this code.

for i, line in enumerate(infile):
    if i == 10:
        break
    print(line)

infile.close()


# The key passage here is the one in which the `open()` function opens a file and return a **file object**, and it is commonly used with the following two parameters: the **name of the file** that we want to open, the **mode** and the **encoding**. 
# 
# - **filename**: the name of the file to open
# 
# - the **mode** in which we want to open a file: the most commonly used values are `r` for **reading** (default), `w` for **writing** (overwriting existing files), and `a` for **appending**. (Note that [the documentation](https://docs.python.org/3/library/functions.html#open) report mode values that may be necessary in some exceptional case)
# 
# - **encoding**: which mapping of string to code points (conversion to bytes) to use, more on this later. 

# >**IMPORTANT**: every opened file should be **closed** by using the function `close()` before the end of the program, or the file could be unavailable to successive manipulations or for other programs.

# There are other ways to read a text file, among which the use of the methods `read()` and `readlines()`, that would simplify the above function in:
# 
# ```python
# infile = open('data/adams-hhgttg.txt', 'r', encoding='utf-8')
# text = infile.readlines()
# print(text[:10])
# infile.close()
# ```
# 
# However, these methods **read the whole file at once**, thus creating huge problems when working with big corpora.
# 
# In the solution we adopt here the input file is read line by line, so that at any given moment **only one line of text** is loaded into memory. 

# ### The with statement 
# 
# A `with` statement is used to wrap the execution of a block of code.
# 
# Using this construction to open files has three major advantages:
# 
# - there is no need to explicitly  close the file (the file is automatically closed as soon as the nested code exits)
# - the file is closed automatically even when unhandled errors cause the program to crash
# - the code is way clearer (it is trivial to identify where in the code a file is opened) 
# 
# Thus, you can  make it yourself a bit easier. Forget about the explicit `.close()` method. The code above can be rewritten as follows:

# In[49]:


with open('data/adams-hhgttg.txt', encoding='utf-8') as infile:
    
    lines = infile.readlines()
    
print(lines[:10])


# The code in the indented with block is executed while the file is opened. It is automatically closed as the block is closed. 

# ### Quiz
# 
# * Write one function that takes a file path as argument and prints statistics about the file, giving:
#     * The number of tokens
#     * The number of unique tokens
#     * The type:token ratio
#     * The 10 most frequent words
# * Write a normalization or cleaning function that pre-processes the text, by removing:
#     * Uppercase
#     * Punctuation
# * Call the normalization function inside the main function. 

# In[50]:


file_path = 'data/adams-hhgttg.txt'

# Your code here


# ---

# ### Writing to files
# 
# Writing an output file in Python has a structure that is close to that we're ued in our reading examples above. The main difference are 
# 
# - the specification of the **mode** `w`
# 
# 
# - the use of the function `write()` for each line of text

# In[51]:


with open('stuff/output-test-1.txt', 'w', encoding='utf-8') as outfile:
    
    outfile.write("My name is:")
    outfile.write("John")


# Note that this code tries to write a file called "output-test-1.txt" to a directory called "stuff". If you do not have a directory called "stuff", it will give an error. Make a directory (folder) called "stuff" in your Colab file system or local file system in the same directory as the notebook, and try again.

# > When writing line by line, it's up to you to take care of the **newlines** by appending `\n` to each line

# In[52]:


with open('stuff/output-test-2.txt', 'w', encoding='utf-8') as outfile:
    
    outfile.write("My name is:\n")
    outfile.write("Alexander")


# We can inspect the file we just created with the command line. The following is not Python, but a basic command line tool to print the contents of a file. At least on Mac, Linux and Google Colab, this works. Otherwise, just navigate to the file and open it.

# In[53]:


get_ipython().system('cat stuff/output-test-2.txt')


# ### Looping through folders and files
# 
# We can use the `os` module to loop through a folder and load multiple files in memory.

# In[54]:


gutenberg_books = dict()

for root, dirs, files in os.walk("data/gutenberg-extension"):
    for file in files:
        
        with open(os.path.join(root,file), encoding='utf-8') as infile:
            gutenberg_books[file] = infile.read()


# In[55]:


gutenberg_books.keys()


# In[56]:


print(gutenberg_books['doyle-sherlock.txt'][:300])


# Again, this requires you to have the folder 'data/gutenberg-extension' from the repository in your file system. Have a look at the "Files in Colab" section if you are trying to do this on Colab.

# ---

# # Exercises
# 
# ## Reading
# TBD
# 
# ## Tasks

# ### Exercise 1.
# 
# Find all words starting with a capital letter from the text in `text` below.
# 
# Make a list of the most frequent words in this text, but without the words 'the' and 'a'. 

# In[57]:


text = "Right, okay, so right around 9:00 she's gonna get very angry with me. Silence Earthling. my name is Darth Vader. I'm am an extra-terrestrial from the planet Vulcan. That's for messing up my hair. Um, well it's a delorean, right? You're George McFly."

# Your code here


# ### Exercise 2 
# 
# Write a function that:
# * Takes a string as input
# * Calculates the frequency of every token/word (separated by white space) in the string
# * Returns a dictionary of tokens as keys and their frequency in the text as values.
# * Implement an optional function parameter to make the function ignore capital letters
# 
# You can use everything you think you need and that you've learnt so far. Test it on the `text` variable value from the previous cell.

# In[58]:


# Your code here


# ### Exercise 3
# 
# Adapt the function in the previous exercise so that it also ignores punctuation. 
# 
# Hint: you can find all punctuation characters by calling:
#         
# ```python
# import string
# print(string.punctuation)
# ```

# In[59]:


# Your code here


# ### Exercise 4
# Remember the quiz from the previous notebook with the following code:
#     
# ```python
# homogeneous_list = ["1", "56", "33", "8", "220", "9"]
# homogeneous_list.sort()
# homogeneous_list
# ```
# 
# Try to fix this so that it sorts the list as if its elements were integers!
# 
# Can you then do the same for this list, so that Elephant is after canary?
# 
# ```python
# homogeneous_list = ["canary", "hippo", "kangaroo", "narwhal", "Elephant", "raccoon", "yak", "ant"]
# homogeneous_list.sort()
# homogeneous_list
# ```

# In[60]:


# Your code here


# ### Exercise 5
# 
# The [factorial](https://en.wikipedia.org/wiki/Factorial) of an integer $n$, defined as:
# 
# $$
# n! = \begin{cases}
#                1               & n = 1\\
#                n * (n-1)! & \text{n > 1}
#            \end{cases}
# $$
# 
# is the product of all positive integers less than or equal to $n$. For example:
# 
# $$4! = 4 * 3 * 2 * 1$$
# 
# $$3! = 3 * 2 * 1$$
# 
# The factorial operation can be implemented in Python both as a recursive function and as an iterative functions. 
# 
# Write one factorial function picking the approach you prefer.

# In[61]:


# Your code here


# ### Exercise 6
# 
# Read the file `data/adams-hhgttg.txt` and:
# 
# - Count the number of lines in the file
# 
# - Count the number of non-empty lines
# 
# - Read each line of the input file, remove its newline character and write it to file `stuff/adams-output.txt`
# 
# - Compute the average number of alphanumeric characters per line
# 
# - Identify all the unique words used in the text (no duplicates!) and write them in a text file called `stuff/lexicon.txt` (one word per line)

# In[62]:


# your code here

with open("stuff/lexicon.txt", "w") as infile:
    infile.write("something")


# In[63]:


# Your code here


# ---
