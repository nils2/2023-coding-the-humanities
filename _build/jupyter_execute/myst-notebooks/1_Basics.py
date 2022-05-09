#!/usr/bin/env python
# coding: utf-8

# # Python basics 1
# 
# This notebook contains the basics of Python. Use it as a reference whenever needed.

# ### The Zen of Python
# 
# The 20 principles that influences the design of Python. 
# 
# Written in the 1999, they have been included as the 20th entry of the Python Enhancement Proposals (a.k.a. [PEP 20](https://www.python.org/dev/peps/pep-0020/)).

# In[1]:


# easter egg
import this


# > *In December 1989, Van Rossum had been looking for a 'hobby' programming project that would keep him occupied during the week around Christmas" as his office was closed when he decided to write an interpreter for a "new scripting language he had been thinking about lately: a descendant of ABC that would appeal to Unix/C hackers". He attributes choosing the name "Python" to "being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus)".* 
# 
# Taken from: https://en.wikipedia.org/wiki/Guido_van_Rossum

# ## Getting Started
# _See the previous [0. Hello World notebook](0_HelloWorld.ipynb) to check if your Python installation is up and running_
# 
# The simplest way is to type commands directly in the **Interactive** IPython shell:

# In[2]:


print("Are we having fun yet?")


# If you are using **Google Colab**, you can bring up an interactive shell by using !bash and then asking it to run Python 3 (type python3 into the input field once bash loads, and then execute commands):

# In[3]:


# !bash


# This is great for testing purposes, or for exploratory analysis, but it is very inefficient if you want to reuse the same program multiple times. Instead, what you will do in this course is to write your instructions in a Jupyter Notebook, in which you can also explain your code to the reader using text blocks, and which can be loaded by Google Colab or Jupyter Notebook in Anaconda.

# The basic interface of Jupyter notebooks:

# ```{image} images/notebook-ui.png
# :alt: notebookexplained
# ```

# ```{admonition} Tip
# :class: tip
# Save your work periodically! All your unsaved code is lost when your browser with Google Colab or your Python interpretor crashes/stalls!
# ```

# ## Variables
# 
# Variables are reserved **memory locations** used by a computer program.
# 
# Each variable is associated with an **identifier** (i.e. a name). Python restricts the naming possibilities of a variable:
# 
# - identifier characters may be letters, digits or underscores...
# 
# - ... but the first character cannot be a number
# 
# - Python keywords (= words that have a special function/meaning in the Python language) cannot be used as identifiers

# A list of these special keywords can be retrieved by importing the `keywords` module and by printing the `kwlist` attribute.

# In[4]:


# list of Python keywords
import keyword
print(keyword.kwlist)


# We're not going to use all these keywords in the code we're writing for this course. You'll get to know the most imortant ones soon enough. Luckily, Jupyter provides some syntax highlighting to let you know that you're typing a Python keyword, and to make you code easier to grasp.
# 
# If you use one of these keywords as the name for a variable, the Python interpreter, which checks and compiles your code so that the computer can run it, will raise an error.

# In[5]:


# Nope.
None = 10


# In[6]:


# This syntax is NOT valid
pass = True


#  
# ```{warning}
# The Python interpreter does not always return such an error. It is possible to declare variables with names such as `list` or `id`, even though these are built-in functions of Python. This probably gives unwanted results in the rest of your code. Avoid _hijacking_ them!
# ```

# In[7]:


# Valid!
oceans11 = "https://www.imdb.com/title/tt0240772/"


# In[8]:


# Not valid
101dalmatians = "https://www.imdb.com/title/tt0115433/"


# In[9]:


# Valid
hundred_and_one_dalmatians = "https://www.imdb.com/title/tt0115433/"


# Keep in mind that all code you write is case sensitive. Although the following is allowed,
# 
# ```
# # Very bad coding example
# true = False  # the keyword True has a capital letter
# ```
# 
# it is better to stay away from naming your variables this way! What counts is that you give the variable a name that makes sense. But, make sure that they start with a lowercase letter! (= naming convention)

# ### Declaring variables
# 
# Python does not require variables to be declared explicitly, unlike what is common in some other programming languages. In Python, variables are created when you first assign a value to them and you can declare them on the go and where needed.
# 
# The symbol `=` is used to assign values to variables.

# In[10]:


# Let's associate the value 55 to the variable named "lucky_number"
lucky_number = 55


# In[11]:


lucky_number


# This variable is now declared and has been assigned the number 55. When you run the cell in this notebook, the variable is kept in the notebook's memory. This means that we can call it in other cells we run _after_ the cell in which we declared the variable.

# One of the built-in functions of Python is the `type()` function, by which you can inspect the type of value that is assigned to the variable. You can use this function on any Python 'object'.

# In[12]:


# The type of value of the variable can be inspected with the function type()
type(lucky_number)


# ### Changing variables
# You can change the value that is assigned to a variable. In Python, this is NOT restricted to a change within the same datatype.

# In[13]:


# Let's print the initial value of the variable and its type
print(lucky_number, type(lucky_number))

# Now convert our numerical variable into a digit (i.e. into text)
lucky_number = str(lucky_number)

# Do the same printing
print(lucky_number, type(lucky_number))


# In[14]:


lucky_number


# As you saw above, converting any datatype to a text (=string) can be done using the `str()` function. This is for instance usefull if you want to dynamically format the messages that are printed.

# In[15]:


message = "My lucky number is " + lucky_number  # this only works if lucky_number is of type str()
print(message)


# In[16]:


unlucky_number = 13
message = "My unlucky number is " + unlucky_number  # what is the datatype of unlucky_number?
print(message)


# How can the error above be fixed?

# ---

# ## Built-in data types
# 
# Python natively supports the following basic types:
# 
# - **Boolean**: *bool*
# 
# - **None**: *NoneType*
# 
# - **Numerical**: *int*, *float*, *long*, *complex*
# 
# - **Sequence**: *string*, *list*, *tuple*
# 
# - **Set**: *set*, *frozenset*
# 
# - **Dictionaries**

# #### Mutable vs. Immutable objects
# 
# Python data types can be organized by distinguishing those types whose objects can change after their creation (**Mutable**) and those that do not admit such possibility (**Immutable**). If a variable is of a mutable datatype, you can _overwrite_ its value, instead of creating a new object. Assigning a new value to an existing variable is always possible. 
# 
# | Immutables|   Mutables|
# |:---------:|:---------:|
# |  Numerical|          -|
# |     String|          -|
# |      Tuple|       List|
# |  Frozenset|        Set|
# |          -| Dictionary|

# ### NoneType
# 
# It has one sole value: `None`. It is used to represent the absence of a value.

# ### bool
# 
# Boolean logical values, can be `True` or `False`.
# 
# To be used to represent the truth or falsity of some condition.

# #### Boolean Operators
# 
# - **and**: conjunction
# - **or**: inclusive disjunction
# - **not**: negation

# In[17]:


True and False or True


# In[18]:


not True == False


# In[19]:


# Why does this give an error?
True == not False


# In[20]:


True == (not False)


# ### Numerical Types
# 
# - **int**: integers, e.g. `42`
# - **long**: long integers of non-limited length, e.g. `15L`
# - **float**: floating-point numbers, e.g. `8.75638`
# - **complex**: complex numbers, e.g. `1.23+4.56j`
# 
# Most likely, the only two datatypes you'll be using are integer (`int()`) and float (`float()`).

# #### Using Python as a Calculator
# 
# The simplest way to perform calculations with Python is by using the interactive shell as a fancy calculator. 
# 
# Some of the operations supported by all the numeric types are:

# In[21]:


# addition
3 + 5


# In[22]:


# difference
9 - 5


# In[23]:


# product
9 * 50


# In[24]:


# quotient
9 / 2


# In[25]:


# Floor division
9 // 2


# In[26]:


# The remainder of the floored quotient
9 % 2


# You can combine the floor division and the remainder by using the built-in function `divmod()` ([manual](https://docs.python.org/3.8/library/functions.html#divmod))

# In[27]:


divmod(9,2)


# In[28]:


# x to the power of y
3 ** 2


# Alternatively, use the built-in function `pow()` ([manual](https://docs.python.org/3.8/library/functions.html#pow))

# In[29]:


pow(3, 2)


# In[30]:


# Round a number to a given precision in decimal digits (default 0 digits)
round(1.765432, 2)


# ---

# ### Quiz
# 
# Calculate the number of seconds we're going to spend in this classroom together.

# In[31]:


# your code here


# ---

# ## Changing variables
# While the previous operators produce new variables, the following perform the operation **in-place**. 
# 
# That is, the variable itself is changed in the result of the process.

# In[32]:


# Our variable
magic_number = 8
magic_number


# In[33]:


# In place addition
magic_number += 3
magic_number


# In[34]:


# Is the same as
# In place addition
magic_number = magic_number + 3
magic_number


# In[35]:


# In place subtraction
magic_number -= 3
magic_number


# In[36]:


# In place multiplication
magic_number *= 3
magic_number


# In[37]:


# In place division. What's the datatype after this operation?
magic_number /= 3
magic_number


# In[38]:


# In place modulus
magic_number %= 3
magic_number


# ### Relational Operators
# 
# Comparisons are supported by all objects. The main comparison operators are:
# 
# |   Operator|                Semantics|
# |:---------:|:-----------------------:|
# |         ==|                    equal|
# |         !=|                not equal|
# |          <|                less-than|
# |         <=|    less-than or equal to|
# |          >|             greater-then|
# |         >=| greater-then or equal to|
# |         is| object identity|
# |         is not| negated object identity|
# 
# Relational operators are used to **test conditions**, and the output is a boolean value

# In[39]:


# Is 7 bigger than 9?
7 > 9


# In[40]:


# Is 10 smaller than or equal to 10?
10 <= 10


# In[41]:


10 != "10"


# ```{note}
# `is` checks if two things **are the same object, and have the same identity in memory**, not just if they are equal
# ```

# In[42]:


# The value 0 (of any numerical type) is considered to be False, but 0 is not False
print(False == 0)
print(False is 0)


# In[43]:


print(True == 1)
print(True is 1)


# In[44]:


unassigned = None
print(unassigned is None)


# In[45]:


assigned = 0
print(assigned == False)
print(assigned is False)


# ### Quiz
# 
# When to use the `is` statement? And how does it differ from `==`? Can you illustrate this with an example? How is this related to Python's memory management?
# 
# ```{admonition} Tip
# :class: tip
# More info on the `id()` function in this ([thread](https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is))
# ```

# In[46]:


# Test this out. When is the identity of an object changed?
# 


# ---

# ## Iterables / sequences
# 
# We will focus on three types of sequences: **strings**, **lists** and **tuples** (see the [documentation](https://docs.python.org/3.8/library/stdtypes.html#sequence-types-list-tuple-range) for the full list). 
# 
# Most sequence types support the following operations (where `s` and `t` are sequences, `n`, `i` and `j` integers):
# 
# |   Operation|                Result|
# |:----------:|:-----------------------:|
# |      x in s|  True if an item of s is equal to x|
# |  x not in s|  False if an item of s is equal to x|
# |       s + t| Concatenation of s and t|
# |       s * n|   add s to itself n times (negative n are treated as 0)|
# |        s\[i\]|	ith item of s, origin 0|
# |      s\[i:j\]|   slice of s from i to j|
# |    s\[i:j:k\]| slice of s from i to j with step k|
# |      len(s)| length of s|	 
# |      min(s)| smallest item of s|
# |      max(s)| largest item of s|
# |  s.index(x)| index of the first occurrence of x in s |
# |  s.count(x)| total number of occurrences of x in s|

# ### Lists
# 
# 
# Lists are **ordered** **mutable** sequences of **heterogeneous** elements.
# 
# In the Python language, lists are defined by square brackets `[]` and their elements are separated by commas.

# In[47]:


# Lists can contain different types of objects,
# even another list like [1,2,3]

demo_list = ["text", "text", "text", 23, "42", 92, 'another text', [1,2,3]]

print(demo_list)


# In[48]:


# The len() function returns the length of the list
len(demo_list)


# In[49]:


# Membership verification (return a boolean value)
"text" in demo_list


# In[50]:


# Count the number of occurences of an element in the list
demo_list.count("text")


# In[51]:


42 in demo_list  # Why?


# In[ ]:





# #### Strings

# In some ways, string behave the same as lists. For instance, you can check the length of a string, or check if a character sequence is part of a string:

# In[52]:


demo_text = "Coding the Humanities"

print("The length of the text is:", len(demo_text))


# In[53]:


print("The word 'the' is in the string:", "the" in demo_text)


# #### List concatenation

# In[54]:


# Concatenation
new_demo_list = ["Example", "concatenation"]

new_demo_list += demo_list
new_demo_list


# In[55]:


# Repetition
new_demo_list = demo_list * 3
new_demo_list


# #### Lists are ordered

# In[56]:


# Lists are ordered, elements can be recalled by using their index
# Remember that the index of the first element is 0

demo_list[0]


# In[57]:


# The index "-1" is associated with the last element

demo_list[-1]  # As you can see when inspecting the original demo_list, there is a list in a list


# In[58]:


# Check the position of the element "23"

demo_list.index(23)  # Is this the third or the fourth element?


# ### Quiz

# In[59]:


# Make one list out of these two lists:

first_list = [1, 2, 3, 4, 5]
second_list = ["One", "Two", "Three", "Four", "Five"]

# Your code here
# all_elements =

# What is the position of element "Four" in the new list?
#

# How many elements does this new list contain? Hint: use len(all_elements). 


# In[60]:


# This also works for strings (e.g. emojis). Print 200 ants in one paragraph:

text = "🐜"
# paragraph = 
# print(paragraph)  # TODO: Make it print 200 instead of one

# Fill in (and uncomment) by using the .count() method on a string
# antcount = 
# print("There are" + str(antcount) + "printed here")


# ---

# #### Slicing
# 
# 
# Slicing is a **computationally fast** way to extract a portion of a sequence in order to create a new sequence. 
# 
# Slicing Notation works in the following way:
# 
# 
# ```
# sequence[start:stop:step]
# ```

# ##### Slicing rules
# 
# - The slice of the sequence `s` from `start` to `stop` is defined as the sequence of items with index `k` such that `start` <= `k` < `stop`. 
# 
# 
# - If `start` or `stop` is greater than len(`s`), use len(`s`). 
# 
# 
# - If `start` is omitted or `None`, use 0. 
# 
# 
# - If `stop` is omitted or `None`, use len(`s`). 
# 
# 
# - If `start` or `stop` is negative, the index is relative to the end of sequence.

# ```{image} images/list-slicing.png
# :alt: listslicing
# ```

# In[61]:


print(demo_list)


# In[62]:


# Slicing with positive indices 
demo_list[3:5]


# In[63]:


# Slicing works with negative indices as well 
demo_list[-3:-1]


# In[64]:


# Slicing works with a mixture of positive and negative indices
demo_list[1:-2]


# In[65]:


# If an index is omitted, Python reaches the first or the last element of the list
demo_list[2:]


# In[66]:


# The same as above, with the first index omitted
demo_list[:3]


# In[67]:


# Slicing with steps
demo_list[1::2]


# ---

# ### Quiz
# 
# The following code creates a list whose length is a-priori unknown. Extract:
# 
#     1. the last element of the list by using a positive index
#     2. the first element of the list by using a negative index
#     3. a new list of every element on an even index
#     4. this list reversed

# In[68]:


import random  # built-in package

random_number_list = []
for i in range(10):
    random_number = random.randint(1, 99)
    random_number_list.append(random_number)

random_number_list


# In[69]:


# Your code here for 1.


# In[70]:


# Your code here for 2.


# In[71]:


# Your code here for 3.


# In[72]:


# Your code here for 4.


# ---

# #### Lists are mutable
# 
# Lists methods allows you to manipulate the elements stored in the list quickly and effectively. The method `.append()` on the list allows you to add an element at the end of that list. This is a method that you'll be using often!

# In[73]:


empty_list = []
empty_list.append("appended")

print(empty_list)

# Another element
empty_list.append("second addition")
print(empty_list)


# The `.extend()` method allows you to add all the elements of a second list. It works the same as the `+=` operator we saw before.

# In[74]:


groceries = ["Apple", "Crisps", "Soda", "Stroopwafels"]
fruit = ["Apple", "Banana", "Orange"]

groceries.extend(fruit)  # similar to +=
print(groceries)


# The `.remove()` method allows you to remove a given elements from a list. 
# 
# What happens if there are duplicate elements that you want to have removed in a list?

# In[75]:


groceries.remove("Apple")
print(groceries)


# The method `.reverse()` reverses a list IN PLACE (i.e. the original list is modified)

# In[76]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

numbers.reverse()
print(numbers)


# You can replace or delete parts of a list by slicing:

# In[77]:


# Replace elements

numbers[-3:] = [10, 11, 12]
print(numbers)


# In[78]:


# Delete elements

numbers[4:6] = []
print(numbers)


# Sorting a list is as easy as calling `.sort()` on it. This changes the list in place. However, the list elements must be of the same type!

# In[79]:


# This renders a TypeError
["text", 1, 2, 3].sort()


# In[80]:


homogeneous_list = [1, 56, 33, 8, 220, 9]
homogeneous_list.sort()

homogeneous_list


# Lists of strings can be sorted as well. Useful if you want to sort from A-Z. 
# 
# Is the sort operation giving the expected result?

# In[81]:


homogeneous_list = ["canary", "hippo", "kangaroo", "narwhal", "Elephant", "raccoon", "yak", "ant"]
homogeneous_list.sort()
homogeneous_list


# ---

# ---

# #### Lists of numbers
# 
# Lists of numbers can be manipulated by additional functions, among which `max()`, `min()` and `sum()`

# In[82]:


some_numbers = [4, 8, 2, 6, 2, 9]

print(max(some_numbers))
print(min(some_numbers))
print(sum(some_numbers))


# ### Quiz
# 
# Get the minimum and maximum number of the list below _without_ using the `max()` and `min()` functions (e.g. by sorting and slicing).

# In[83]:


numbers = [21, 1, 56, 33, 8, 220, 9]

# Your code here


# Compute the average of `some_numbers`:

# In[84]:


some_numbers = [4, 8, 2, 6, 2, 9]

# Your code here


# Explain the sorting of the following list:

# In[85]:


homogeneous_list = ["21", "1", "56", "33", "8", "220", "9"]
homogeneous_list.sort()
homogeneous_list


# ---

# ### Tuples
# 
# Tuples are the **immutable** counterpart of the lists. 
# 
# They are defined by round brackets `()` and they mainly differ from the list in that they do not accept those methods that tries to manipulate its elements.

# In[86]:


# Tuples can contain different types of objects (even another list like [1,2,3])

demo_tuple = ("text", 23, 92, "another_text", [1,2,3])

print(demo_tuple)


# In[87]:


# Elements can be accessed on the basis of their index...

demo_tuple[1:3]


# In[88]:


# But, they cannot be replaced. This raises a TypeError error!

demo_tuple[1] = 2


# For now, just know that tuples are a datatype in Python. You'll know when you need them further on in this course!

# ### Strings
# 
# Strings are **immutable**, sequences of characters (so, they are **homogeneous**)
# 
# In the Python language, strings are defined by single `'` or double quotes `"`,  and their elements are contiguous.

# In[89]:


demo_string = "Does Cersei have any friends?"
print(demo_string)


# In[90]:


# Using single or double quotes is indifferent
demo_string_single = 'Does Cersei have any friends?'
demo_string == demo_string_single


# In[91]:


# Remember: Digits are not numbers! (frequent source of debugging frustration)

print(type("1979") == type(1979))


# In[92]:


print('"1979" type is: ' + str(type("1979")))


# In[93]:


print('1979 type is: ' + str(type(1979)))


# By being immutable sequences, strings accept all the sequences methods, but they not support item assignment:

# In[94]:


# You can check the length (in characters, whitespaces count!) of a string
len(demo_string)


# In[95]:


# Strings can be looked for in other strings
"Cersei" in demo_string


# In[96]:


# How many 'a's do we have in our string?
demo_string.count("a")


# In[97]:


# Concatenation is possible
demo_string += "\nNoway!"
demo_string


# In[98]:


print(demo_string)


# The escape sequence `\n` indicates the end of the line. 
# 
# Python escape sequences are introduced by the escape character `\`, whose goal is to signal the interpreter that the following character has an "unusual" interpretation. Here is a partial list:
# 
# | Escape Sequence|         Meaning|
# |:--------------:|:---------------:|
# |              \\\\|  backslash|
# |              \\'|  single quote|
# |              \\b|  backspace|
# |              \\n|  new line|
# |              \\t|  horizontal tab|

# In[99]:


# Nicely print our string!
print(demo_string)


# In[100]:


# What does a backspace do?
print(demo_string  +"\b")


# In[101]:


# The escape character may be useful when you need single quotes inside a single quote-marked string...
'Can any of you pronounce \'s-Hertogenbosch?'


# In[102]:


# but this solution is preferred (when possible)
"Can any of you pronounce 's-Hertogenbosch?"


# Strings that span multiple lines can be written in a readable form by using the sequence `"""` as a delimiter

# In[103]:


print("""Unsealed, on a porch a letter sat
Then you said, "I wanna leave it again"
Once I saw her on a beach of weathered sand
And on the sand I wanna leave her again""")


# ### Quiz

# Run the cell below. Where do all the '\n's come from?

# In[104]:


""""On a weekend I wanna wish it all away, yeah
And they called and I said that I'll go
And I said that I'll call out again
And the reason I ought ta leave her calm, I know
I said, "I don't know whether I'm the boxer or the bag"""""


# In[105]:


# String slicing
"Monty Python"[-12:-7]


# In[106]:


# But single characters cannot be replaced. This raises a TypeError. 
demo_string[5:11] = "Melisandre"


# #### String Methods
# 
# Strings have a buch of dedicated methods (see the [documentation](https://docs.python.org/3.8/library/stdtypes.html) for a complete list), that allows them to be both inspected or manipulated (they are not modified, rather a **new object** is returned). 
# 
# The following are commonly used the most:

# In[107]:


# Is the string composed solely of 1. digits 2. alphabetic characters 3. both?
print('100'.isdigit())
print('cat'.isalpha())
print('my cat is 100'.isalnum())  # Why False?


# In[108]:


print(demo_string)


# The `.startswith()` and `.endswith()` methods are useful:

# In[109]:


# Does the string starts or ends with a given sequence of characters?
print(demo_string.startswith("d"))  # it is case sensitive !!!
print(demo_string.endswith("Noway!"))


# If you want to compare strings, or want to have them stored in a normalized way, you can use the `.upper()` and `.lower()` methods:

# In[110]:


# Change case to all the characters of a string
print(demo_string_single.upper())
print(demo_string_single.lower())


# If you want to get rid of unwanted characters at the beginning or at the end of a string, you can use `.strip()`. This is commonly used to remove all whitespace (i.e. spaces, linebreaks, tabs) from the string.

# In[111]:


# Remove a given character (default is any whitespace) from the beginning and the end of a string

text1 = "Twice minus: - before and after -"
text2 = "  \t  Too much space?"

print("Before:")
print(text1)
print(text2)
print()

print("After:")
print(text1.strip("-"))
print(text2.strip())
print()


# You can remove one or multiple elements from a list by using `.replace()`:

# In[112]:


# Replace a given sequence of characters with another 
print(demo_string.replace("Cersei", "Melisandre"))


# In[113]:


# Or if you want to completely remove a character or series of characters,
# simply replace it by an empty string! You can also chain these. 
print(demo_string.replace("?", "").replace("!", ""))


# #### From strings to lists

# A string can be transformed into a list of string by splitting it on a given character. This is done through the `.split()` method.

# In[114]:


# By whitespace
demo_string.split(" ")


# In[115]:


# However, the default character is any white line (that's convenient!)
demo_string.split()


# In[116]:


# the maximun number of splits can be specified
demo_string.split(" ", 2)


# #### From lists to strings

# The inverse operation is possible, a list of strings can be joined by a single character using `join()` on another string. It's argument is the list.

# In[117]:


# A whitespace
" ".join(["One","Two","Three"])


# In[118]:


# An hyphen
"-".join(["One","Two","Three"])


# In[119]:


# Any string basically
predifined_joinchar = "🌞"
predifined_joinchar.join(["Eins","Zwei","Drei"])


# In[120]:


# Or no characters at all
"".join(["Super", "cali", "fragilistic", "expiali", "docious"] )


# Keep in mind that you can only join elements of type string.

# In[121]:


# Raises a TypeError
" ".join(["This", "is", "notebook", "number", 1])


# ---

# In[ ]:





# ### Sets
# 
# Sets are collections of **unordered** and **distinct/unique** objects.
# 
# They are commonly used to test membership, to remove duplicates or to compute mathematical operations such as intersection, union, difference, and symmetric difference. Being unordered collections, they do not support indexing, slicing and any other sequence-like behavior. But, this  makes them extremely efficient.
# 
# In Python, sets can be create beither by using the syntax  `set([])` or by using curly braces `{}`.

# Sets come in handy if you want to count the unique occurences in a list:

# In[122]:


text = """the quick brown fox jumps over the lazy dog"""
words = text.split()  # 'the' is in there twice
print(words)

unique_words = set(words)
unique_words


# You can add elements by calling `.add()` on the set. 
# 
# ```{note}
# The `.append()` is for lists only! Trying to add an element that's already in a set does not change anything.
# ```

# In[123]:


# Elements are added with the function add()
unique_words.add("sheep")
unique_words


# In[124]:


# elements are removed with the function remove()
unique_words.remove("fox")
unique_words


# In[125]:


# length of a set
len(unique_words)


# In[126]:


# membership test
"sheep" in unique_words


# You can use `.union()` to get all the elements from both sets.

# In[127]:


# the union of the two sets
all_words = unique_words.union(set(["pack", "my", "box", "with", "five", "dozen", "liquor", "jugs"]))
all_words


# In[128]:


# Intersection of the two sets
other_set = {"brown", "dog", "purple", "fox"}

intersection = unique_words.intersection(other_set)
intersection


# In[129]:


# Elements that are in the first but not in the second set
unique_words.difference(other_set)


# In[130]:


# Variables flipped
other_set.difference(unique_words)


# In[131]:


# Every elements of smaller_set are in all_elements?

all_elements = {1, 2, 3, 4, 5, 6, 7, 8, 9}
smaller_set = {2, 4, 6, 8}

print(all_elements.issuperset(smaller_set))
print(smaller_set.issubset(all_elements))


# Go over the other methods that can be used on a set. You can find them including examples here: https://www.w3schools.com/python/python_ref_set.asp. For sure, check out the `.update()` and `.isdisjoint()`.

# ### Quiz

# In[ ]:





# ---

# ### Dictionaries
# 
# Dictionaries are **associative arrays** mapping **immutable** types (string, numbers, tuples...) to arbitrary objects of any kind (all datatypes you earlier saw, variables, functions, modules...). Intuitively, they can be thought as collections of objects that we can recall by means of a unique key. 
# 
# To visualize a Python dictionary you can think of a telephone book, in which people names are the unique keys that you use to retrieve difference kinds of information (phone numbers, street address, mail address...). The same telephone number, street address or other information can be present in the entries of more people, but a label cannot be associated with more than one entry. 
# 
# In Python, dictionaries are defined by curly brackets `{}`, in which key-value pairs are separated by commas and joint by colons.

# In[132]:


# An English-Dutch dictionary of colors

color2kleur = {
    "black": "zwart",
    "white": "wit",
    "red": "rood",
    "yellow": "geel"
}

print(color2kleur)


# In[133]:


# Values can be recalled by their keys
color2kleur["white"]


# In[134]:


# We can change a value associated with a key
color2kleur["white"] = "sneeuwwit"

print(color2kleur)


# In[135]:


# If the key is missing a new key: value pair is added
color2kleur["blue"] = "blauw"

print(color2kleur)


# In[136]:


# {Key: value} can be deleted with the command "del()"
del(color2kleur["blue"])
print(color2kleur)


# In[137]:


# Check if a dictionary has a given key
"blue" in color2kleur


# In[138]:


# Count the number of entries in a dictionary
len(color2kleur)


# ### Quiz
# 
# What you're actually doing by calling the dict that way, is calling the `.keys()` method. Try using the following methods below on the `color2kleur` dictionary:
# 
# 1. `.keys()` vs. just calling the dictionary by `color2kleur`
# 2. `.values()`
# 3. `.items()`
#     
# What is the datatype that is returned for each of these methods? And what is de datatype inside these 'iterables'?

# In[139]:


# You code here


# #### Iterating over a Dictionary

# In[140]:


# iterate over dictionary keys:
print(list(color2kleur))
print(list(color2kleur.keys()))


# In[141]:


# iterate over dictionary values:
print(list(color2kleur.values()))


# In[142]:


# iterate over dictionary key-value pairs:
print(list(color2kleur.items()))


# ---

# ###  Type casting
# 
# Sometimes, we may need to change the type of a variable. 
# 
# For instance, we may want to change a list into a set in order to delete all its repeated elements. A quick way to do so is to transform the list in a set.
# 
# Other example may involve the `.join()` method that does not accept numbers. Conversion functions can be used to quickly switch numbers to strings. Sometimes, these conversion functions are built-in into a function, which is the case in the `print()` function. It is basically applying the `str()` function on every object that you give as argument.
# 
# ```{note}
# Not all types of variables can be switched to other types. In what follows we report some common conversion.
# ```

# In[143]:


# From number to string
str(3.123424235454)


# In[144]:


# Sometimes you want to round the number
str(round(3.123424235454, 2))


# In[145]:


# From string to integer
int("3")


# In[146]:


# From string to floating numer
float("3")


# In[147]:


# From list to tuple (list cannot be used as dictionary keys, tuples can)
tuple([demo_list])


# In[148]:


# From list to set
set([1,2,3,1,2,3,3])


# In[149]:


# From string to list
print(list("this is a sentence"))


# ### Quiz
# 
# The list `numbers` contains 21 integers, ranging from -10 to 10, unsorted. 
# 
# Create a new list containing only the positive numbers from the list. Use `.sort()`, `len()` and `round()`

# In[150]:


numbers = [-7, 1, 3, 8, 7, -2, 5, 4, -10, -4, -3, -6, 2, 9, 0, -5, -8, 10, -9, 6, -1]


# In[151]:


# Your code here


# ---

# # Exercises
# 
# ## Reading
# * Check out number 8 of the Python Enhancement Proposals (PEP): https://www.python.org/dev/peps/pep-0008/. Try writing your code with PEP8 in mind. 
# * [Python Cheat Sheet](https://www.cheatography.com/davechild/cheat-sheets/python/), which collects much of the syntax we used today.
# * Have a look at Python's built-in types: https://docs.python.org/3.8/library/stdtypes.html. Be sure to check out the part on [string methods](https://docs.python.org/3.8/library/stdtypes.html#string-methods). You can skip the other sections. 
# 
# ## Tasks

# ### Excercise 1
# 
# Italian nobles tends to have an awful lot of names. For instance, "Vittorio Emanuele di Savoia" (or "Vittorio" for close friends) has the 12 names listed in `full_name`. 
# 
# Can you find a pythonic way to eliminate the less used names from this string?

# In[152]:


full_name = "Vittorio Emanuele Alberto Carlo Teodoro Umberto Bonifacio Amedeo Damiano Bernardino Gennaro Maria di Savoia"


# In[153]:


# Your code here


# ### Exercise 2.
# 
# The code in the next cell creates a variable called `zen_text`, and assigns it a nicely formatted version of the textual elements of the Zen of Python.
# 
# * Count the number of in this manifesto of:
#     1. Characters
#     2. Words
#     3. Unique words
#     3. Non-empty lines

# In[154]:


import this
zen_text = ''.join(this.d.get(el, el) for el in this.s)  # forget this complicated pattern for now


# In[155]:


# Your code here


# ### Exercise 3.
# 
# The dictionary in the following cell reports, for each Scrubs character, a dictionary mapping is given with the name of the actor, the age of the character and its credentials.
# 
# Write code to answer the following questions:
# 
# - What are the **names of the actors** of the cast?
# 
# - What is the **average age** of the characters?
# 
# - How **many M.D.s** are there in the main cast?
# 
# - Which character is not listed in the credentials dictionary?
# 
# ```{admonition} Tip
# :class: tip
# Check the dictionary and set methods.
# ```

# In[156]:


scrubs2age = {
     'Bob Kelso': 70,
     'Carla Espinosa-Turk': 36,
     'Christopher Turk': 31,
     'Elliot Reid': 29,
     'J.D.': 31,
     'Janitor': 40,
     'Perry Cox': 45
  }

scrubs2cred = {
     'Bob Kelso': 'M.D.',
     'Carla Espinosa-Turk': 'RN',
     'Christopher Turk': 'M.D.',
     'Elliot Reid': 'M.D.',
     'J.D.': 'M.D.',
     'Perry Cox': 'M.D.'
  }


# In[157]:


# Your code here


# In[ ]:





# ### Exercise 4 Assignment Week1!
# 
# A string is stored in the `coe_books` variable. 
# 
# * How many different books of Jonathan Coe are listed?
# * Check if the string starts with 'the accidental woman'
# * Print this text titlecased (every word starts with a capital letter, ignore the prepositions for now). And uppercased. And capitalized.
# * Convert the string to a list of words. Two of the book titles contain digits: 58 and 11. Find the index in the list and replace the string object for the number as integer. Print the list.

# In[158]:


coe_books = """the accidental woman
a touch of love
the dwarves of death
what a carve up! or the winshaw legacy viking
the house of sleep
the rotters' club
the closed circle
the rain before it falls
the terrible privacy of maxwell sim
expo 58
number 11
"""


# In[159]:


# Your code here


# ---
