---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"id": "X8NI2UYxmAxm"}

# Python basics 1

This notebook contains the basics of Python. Use it as a reference whenever needed.

+++ {"id": "ptTHd2UqmAxo"}

### The Zen of Python

The 20 principles that influences the design of Python. 

Written in the 1999, they have been included as the 20th entry of the Python Enhancement Proposals (a.k.a. [PEP 20](https://www.python.org/dev/peps/pep-0020/)).

```{code-cell} ipython3
:id: EgKhcsNImAxq

# easter egg
import this
```

+++ {"id": "K7yP9VRcmAxr"}

> *In December 1989, Van Rossum had been looking for a 'hobby' programming project that would keep him occupied during the week around Christmas" as his office was closed when he decided to write an interpreter for a "new scripting language he had been thinking about lately: a descendant of ABC that would appeal to Unix/C hackers". He attributes choosing the name "Python" to "being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus)".* 

Taken from: https://en.wikipedia.org/wiki/Guido_van_Rossum

+++ {"id": "JxsAcPsGmAxs"}

## Getting Started
_See the previous [0. Hello World notebook](0_HelloWorld.ipynb) to check if your Python installation is up and running_

The simplest way is to type commands directly in the **Interactive** IPython shell:

```{code-cell} ipython3
:id: YdFO7KTxmAxt

print("Are we having fun yet?")
```

+++ {"id": "ZuIak2fwmQSP"}

If you are using **Google Colab**, you can bring up an interactive shell by using !bash and then asking it to run Python 3 (type python3 into the input field once bash loads, and then execute commands):

```{code-cell} ipython3
:id: 0VVoKA3YmRda

# !bash
```

+++ {"id": "CIMcx-QHmans"}

This is great for testing purposes, or for exploratory analysis, but it is very inefficient if you want to reuse the same program multiple times. Instead, what you will do in this course is to write your instructions in a Jupyter Notebook, in which you can also explain your code to the reader using text blocks, and which can be loaded by Google Colab or Jupyter Notebook in Anaconda.

+++ {"id": "BZxSNCNtmAxt"}

The basic interface of Jupyter notebooks:

+++ {"id": "wY7z_gBUmAxu"}

```{image} images/notebook-ui.png
:alt: notebookexplained
```

+++ {"id": "dnEQeu_9mAxu"}

```{admonition} Tip
:class: tip
Save your work periodically! All your unsaved code is lost when your browser with Google Colab or your Python interpretor crashes/stalls!
```


+++ {"id": "IVFjzAAimAxw"}

## Variables

Variables are reserved **memory locations** used by a computer program.

Each variable is associated with an **identifier** (i.e. a name). Python restricts the naming possibilities of a variable:

- identifier characters may be letters, digits or underscores...

- ... but the first character cannot be a number

- Python keywords (= words that have a special function/meaning in the Python language) cannot be used as identifiers

+++ {"id": "qcOmr7rvmAxx"}

A list of these special keywords can be retrieved by importing the `keywords` module and by printing the `kwlist` attribute. 

```{code-cell} ipython3
:id: 7zlxy3mHmAxy

# list of Python keywords
import keyword
print(keyword.kwlist)
```

+++ {"id": "KDRLgtr7mAxz"}

We're not going to use all these keywords in the code we're writing for this course. You'll get to know the most imortant ones soon enough. Luckily, Jupyter provides some syntax highlighting to let you know that you're typing a Python keyword, and to make you code easier to grasp.

If you use one of these keywords as the name for a variable, the Python interpreter, which checks and compiles your code so that the computer can run it, will raise an error. 

```{code-cell} ipython3
:id: OOy_sqxKmAxz

# Nope.
None = 10
```

```{code-cell} ipython3
:id: CeYIyT5vmAx0

# This syntax is NOT valid
pass = True
```

+++ {"id": "QiRXsrhQmAx0"}
 
```{warning}
The Python interpreter does not always return such an error. It is possible to declare variables with names such as `list` or `id`, even though these are built-in functions of Python. This probably gives unwanted results in the rest of your code. Avoid _hijacking_ them!
``` 

```{code-cell} ipython3
:id: vUHU0-d9mAx1

# Valid!
oceans11 = "https://www.imdb.com/title/tt0240772/"
```

```{code-cell} ipython3
:id: 5NG9MpHymAx1

# Not valid
101dalmatians = "https://www.imdb.com/title/tt0115433/"
```

```{code-cell} ipython3
:id: KwEkFbSCmAx2

# Valid
hundred_and_one_dalmatians = "https://www.imdb.com/title/tt0115433/"
```

+++ {"id": "2zXmXJjJmAx2"}

Keep in mind that all code you write is case sensitive. Although the following is allowed,

```
# Very bad coding example
true = False  # the keyword True has a capital letter
```

it is better to stay away from naming your variables this way! What counts is that you give the variable a name that makes sense. But, make sure that they start with a lowercase letter! (= naming convention)

+++ {"id": "Pbuw6-3fmAx2"}

### Declaring variables

Python does not require variables to be declared explicitly, unlike what is common in some other programming languages. In Python, variables are created when you first assign a value to them and you can declare them on the go and where needed.

The symbol `=` is used to assign values to variables. 

```{code-cell} ipython3
:id: HstJJsPamAx3

# Let's associate the value 55 to the variable named "lucky_number"
lucky_number = 55
```

```{code-cell} ipython3
:id: _eYFc0G3mAx3

lucky_number
```

+++ {"id": "vriubYbimAx4"}

This variable is now declared and has been assigned the number 55. When you run the cell in this notebook, the variable is kept in the notebook's memory. This means that we can call it in other cells we run _after_ the cell in which we declared the variable. 

+++ {"id": "NcX--6p6mAx4"}

One of the built-in functions of Python is the `type()` function, by which you can inspect the type of value that is assigned to the variable. You can use this function on any Python 'object'. 

```{code-cell} ipython3
:id: Pd3xBsXzmAx4

# The type of value of the variable can be inspected with the function type()
type(lucky_number)
```

+++ {"id": "eo7LK8rimAx4"}

### Changing variables
You can change the value that is assigned to a variable. In Python, this is NOT restricted to a change within the same datatype. 

```{code-cell} ipython3
:id: Xekp7V9GmAx4

# Let's print the initial value of the variable and its type
print(lucky_number, type(lucky_number))

# Now convert our numerical variable into a digit (i.e. into text)
lucky_number = str(lucky_number)

# Do the same printing
print(lucky_number, type(lucky_number))
```

```{code-cell} ipython3
:id: vm4AOh_FmAx5

lucky_number
```

+++ {"id": "Yp9ZHJXamAx5"}

As you saw above, converting any datatype to a text (=string) can be done using the `str()` function. This is for instance usefull if you want to dynamically format the messages that are printed. 

```{code-cell} ipython3
:id: 0nBI5XG6mAx5

message = "My lucky number is " + lucky_number  # this only works if lucky_number is of type str()
print(message)
```

```{code-cell} ipython3
:id: 827G0uZmmAx5

unlucky_number = 13
message = "My unlucky number is " + unlucky_number  # what is the datatype of unlucky_number?
print(message)
```

+++ {"id": "KtfFGIadmAx7"}

How can the error above be fixed?

+++ {"id": "E3AhPD8amAx7"}

---

+++ {"id": "k7nyhryYmAx7"}

## Built-in data types

Python natively supports the following basic types:

- **Boolean**: *bool*

- **None**: *NoneType*

- **Numerical**: *int*, *float*, *long*, *complex*

- **Sequence**: *string*, *list*, *tuple*

- **Set**: *set*, *frozenset*

- **Dictionaries**

+++ {"id": "HkkC6WNsmAx7"}

#### Mutable vs. Immutable objects

Python data types can be organized by distinguishing those types whose objects can change after their creation (**Mutable**) and those that do not admit such possibility (**Immutable**). If a variable is of a mutable datatype, you can _overwrite_ its value, instead of creating a new object. Assigning a new value to an existing variable is always possible. 

| Immutables|   Mutables|
|:---------:|:---------:|
|  Numerical|          -|
|     String|          -|
|      Tuple|       List|
|  Frozenset|        Set|
|          -| Dictionary|

+++ {"id": "MInY1pyomAx7"}

### NoneType

It has one sole value: `None`. It is used to represent the absence of a value.

+++ {"id": "ZhQswr1NmAx8"}

### bool

Boolean logical values, can be `True` or `False`.

To be used to represent the truth or falsity of some condition.

+++ {"id": "KrvKab04mAx8"}

#### Boolean Operators

- **and**: conjunction
- **or**: inclusive disjunction
- **not**: negation

```{code-cell} ipython3
:id: RgvO2P5DmAx8

True and False or True
```

```{code-cell} ipython3
:id: L4HP6n01mAx8

not True == False
```

```{code-cell} ipython3
:id: v3rxqdH4mAx9

# Why does this give an error?
True == not False
```

```{code-cell} ipython3
:id: dQEQea5VmAx9

True == (not False)
```

+++ {"id": "QJfCmr0imAx9"}

### Numerical Types

- **int**: integers, e.g. `42`
- **long**: long integers of non-limited length, e.g. `15L`
- **float**: floating-point numbers, e.g. `8.75638`
- **complex**: complex numbers, e.g. `1.23+4.56j`

Most likely, the only two datatypes you'll be using are integer (`int()`) and float (`float()`).


+++ {"id": "j7SHu6NNmAx9"}

#### Using Python as a Calculator

The simplest way to perform calculations with Python is by using the interactive shell as a fancy calculator. 

Some of the operations supported by all the numeric types are:

```{code-cell} ipython3
:id: gMMNfzMhmAx-

# addition
3 + 5
```

```{code-cell} ipython3
:id: bYJcbGoomAx-

# difference
9 - 5
```

```{code-cell} ipython3
:id: 6I7SRNHHmAx-

# product
9 * 50
```

```{code-cell} ipython3
:id: 8BATUPmTmAx-

# quotient
9 / 2
```

```{code-cell} ipython3
:id: vxUBiLgvmAx_

# Floor division
9 // 2
```

```{code-cell} ipython3
:id: k1FBwTUrmAyA

# The remainder of the floored quotient
9 % 2
```

+++ {"id": "lrfvNMITmAyA"}

You can combine the floor division and the remainder by using the built-in function `divmod()` ([manual](https://docs.python.org/3.8/library/functions.html#divmod))

```{code-cell} ipython3
:id: 1OEsdXnSmAyA

divmod(9,2)
```

```{code-cell} ipython3
:id: tO9O0Xa4mAyB

# x to the power of y
3 ** 2
```

+++ {"id": "Wd9KcfeamAyB"}

Alternatively, use the built-in function `pow()` ([manual](https://docs.python.org/3.8/library/functions.html#pow))

```{code-cell} ipython3
:id: 9zMIXug6mAyC

pow(3, 2)
```

```{code-cell} ipython3
:id: HHYV_MUomAyC

# Round a number to a given precision in decimal digits (default 0 digits)
round(1.765432, 2)
```

+++ {"id": "DhTlM6CUmAyD"}

---

+++ {"id": "GUCH2yFpmAyD"}

### Quiz

Calculate the number of seconds we're going to spend in this classroom together.

```{code-cell} ipython3
:id: YznnllDzmAyD

# your code here
```

+++ {"id": "2SxlzhghmAyD"}

---

+++ {"id": "OdGDe0KbmAyE"}

## Changing variables
While the previous operators produce new variables, the following perform the operation **in-place**. 

That is, the variable itself is changed in the result of the process.

```{code-cell} ipython3
:id: cMPYHxWlmAyE

# Our variable
magic_number = 8
magic_number
```

```{code-cell} ipython3
:id: h94rfMISmAyE

# In place addition
magic_number += 3
magic_number
```

```{code-cell} ipython3
:id: SdRh9HVPmAyF

# Is the same as
# In place addition
magic_number = magic_number + 3
magic_number
```

```{code-cell} ipython3
:id: m_tcBfN-mAyF

# In place subtraction
magic_number -= 3
magic_number
```

```{code-cell} ipython3
:id: xDjozll6mAyF

# In place multiplication
magic_number *= 3
magic_number
```

```{code-cell} ipython3
:id: xoG69qPImAyG

# In place division. What's the datatype after this operation?
magic_number /= 3
magic_number
```

```{code-cell} ipython3
:id: qGhhbpoTmAyG

# In place modulus
magic_number %= 3
magic_number
```

+++ {"id": "eY8vfIm-mAyG"}

### Relational Operators

Comparisons are supported by all objects. The main comparison operators are:

|   Operator|                Semantics|
|:---------:|:-----------------------:|
|         ==|                    equal|
|         !=|                not equal|
|          <|                less-than|
|         <=|    less-than or equal to|
|          >|             greater-then|
|         >=| greater-then or equal to|
|         is| object identity|
|         is not| negated object identity|

Relational operators are used to **test conditions**, and the output is a boolean value

```{code-cell} ipython3
:id: NRWeAtvRmAyG

# Is 7 bigger than 9?
7 > 9
```

```{code-cell} ipython3
:id: P55BfwjOmAyH

# Is 10 smaller than or equal to 10?
10 <= 10
```

```{code-cell} ipython3
:id: 9STDLb1LmAyH

10 != "10"
```

+++ {"id": "y264OyLomAyH"}

```{note}
`is` checks if two things **are the same object, and have the same identity in memory**, not just if they are equal
```

```{code-cell} ipython3
:id: l-Dj5xBRmAyH

# The value 0 (of any numerical type) is considered to be False, but 0 is not False
print(False == 0)
print(False is 0)
```

```{code-cell} ipython3
:id: 0M0LckUPmAyI

print(True == 1)
print(True is 1)
```

```{code-cell} ipython3
:id: PblcQSVjmAyI

unassigned = None
print(unassigned is None)
```

```{code-cell} ipython3
:id: zQRbeEDCmAyI

assigned = 0
print(assigned == False)
print(assigned is False)
```

+++ {"id": "wIFEfhP9mAyJ"}

### Quiz

When to use the `is` statement? And how does it differ from `==`? Can you illustrate this with an example? How is this related to Python's memory management?

```{admonition} Tip
:class: tip
More info on the `id()` function in this ([thread](https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is))
```

```{code-cell} ipython3
:id: 8CSR-W6zmAyJ

# Test this out. When is the identity of an object changed?
# 
```

+++ {"id": "E6osLX-MmAyJ"}

---

+++ {"id": "bbse84_WmAyJ"}

## Iterables / sequences

We will focus on three types of sequences: **strings**, **lists** and **tuples** (see the [documentation](https://docs.python.org/3.8/library/stdtypes.html#sequence-types-list-tuple-range) for the full list). 

Most sequence types support the following operations (where `s` and `t` are sequences, `n`, `i` and `j` integers):

|   Operation|                Result|
|:----------:|:-----------------------:|
|      x in s|  True if an item of s is equal to x|
|  x not in s|  False if an item of s is equal to x|
|       s + t| Concatenation of s and t|
|       s * n|   add s to itself n times (negative n are treated as 0)|
|        s\[i\]|	ith item of s, origin 0|
|      s\[i:j\]|   slice of s from i to j|
|    s\[i:j:k\]| slice of s from i to j with step k|
|      len(s)| length of s|	 
|      min(s)| smallest item of s|
|      max(s)| largest item of s|
|  s.index(x)| index of the first occurrence of x in s |
|  s.count(x)| total number of occurrences of x in s|

+++ {"id": "WzTk_X4rmAyK"}

### Lists


Lists are **ordered** **mutable** sequences of **heterogeneous** elements.

In the Python language, lists are defined by square brackets `[]` and their elements are separated by commas.

```{code-cell} ipython3
:id: OPHL6EKnmAyK

# Lists can contain different types of objects,
# even another list like [1,2,3]

demo_list = ["text", "text", "text", 23, "42", 92, 'another text', [1,2,3]]

print(demo_list)
```

```{code-cell} ipython3
:id: hl692GQRmAyK

# The len() function returns the length of the list
len(demo_list)
```

```{code-cell} ipython3
:id: Vy9eKYEvmAyK

# Membership verification (return a boolean value)
"text" in demo_list
```

```{code-cell} ipython3
:id: 6uHL_NC0mAyL

# Count the number of occurences of an element in the list
demo_list.count("text")
```

```{code-cell} ipython3
:id: Jh8SxO7FmAyL

42 in demo_list  # Why?
```

```{code-cell} ipython3
:id: 61GQp85AmAyL


```

+++ {"id": "ZyCfKFIFmAyM"}

#### Strings

+++ {"id": "2FlXMgW_mAyM"}

In some ways, string behave the same as lists. For instance, you can check the length of a string, or check if a character sequence is part of a string:

```{code-cell} ipython3
:id: 4nqfjwbvmAyM

demo_text = "Coding the Humanities"

print("The length of the text is:", len(demo_text))
```

```{code-cell} ipython3
:id: __LMq0LTmAyM

print("The word 'the' is in the string:", "the" in demo_text)
```

+++ {"id": "IhgK3tGHmAyM"}

#### List concatenation

```{code-cell} ipython3
:id: coeup2rxmAyM

# Concatenation
new_demo_list = ["Example", "concatenation"]

new_demo_list += demo_list
new_demo_list
```

```{code-cell} ipython3
:id: JHIqHmhAmAyN

# Repetition
new_demo_list = demo_list * 3
new_demo_list
```

+++ {"id": "Jz9IMwYXmAyN"}

#### Lists are ordered

```{code-cell} ipython3
:id: -7xaQAElmAyO

# Lists are ordered, elements can be recalled by using their index
# Remember that the index of the first element is 0

demo_list[0]
```

```{code-cell} ipython3
:id: BanYs00ZmAyP

# The index "-1" is associated with the last element

demo_list[-1]  # As you can see when inspecting the original demo_list, there is a list in a list
```

```{code-cell} ipython3
:id: NcD0AMSRmAyP

# Check the position of the element "23"

demo_list.index(23)  # Is this the third or the fourth element?
```

+++ {"id": "0r9LpggwmAyQ"}

### Quiz

```{code-cell} ipython3
:id: YeKmFSfemAyR

# Make one list out of these two lists:

first_list = [1, 2, 3, 4, 5]
second_list = ["One", "Two", "Three", "Four", "Five"]

# Your code here
# all_elements =

# What is the position of element "Four" in the new list?
#

# How many elements does this new list contain? Hint: use len(all_elements). 
```

```{code-cell} ipython3
:id: GvIANk4WmAyR

# This also works for strings (e.g. emojis). Print 200 ants in one paragraph:

text = "🐜"
# paragraph = 
# print(paragraph)  # TODO: Make it print 200 instead of one

# Fill in (and uncomment) by using the .count() method on a string
# antcount = 
# print("There are" + str(antcount) + "printed here")
```

+++ {"id": "WTTCR9IBmAyR"}

---

+++ {"id": "b3jv3Jp5mAyS"}

#### Slicing


Slicing is a **computationally fast** way to extract a portion of a sequence in order to create a new sequence. 

Slicing Notation works in the following way:


```
sequence[start:stop:step]
```

+++ {"id": "M7h--pdemAyS"}

##### Slicing rules

- The slice of the sequence `s` from `start` to `stop` is defined as the sequence of items with index `k` such that `start` <= `k` < `stop`. 


- If `start` or `stop` is greater than len(`s`), use len(`s`). 


- If `start` is omitted or `None`, use 0. 


- If `stop` is omitted or `None`, use len(`s`). 


- If `start` or `stop` is negative, the index is relative to the end of sequence.

+++ {"id": "ELFBXE9BmAyS"}


```{image} images/list-slicing.png
:alt: listslicing
```

```{code-cell} ipython3
:id: 04u2-bChmAyT

print(demo_list)
```

```{code-cell} ipython3
:id: EGqXF1smmAyT

# Slicing with positive indices 
demo_list[3:5]
```

```{code-cell} ipython3
:id: u35EMz_tmAyT

# Slicing works with negative indices as well 
demo_list[-3:-1]
```

```{code-cell} ipython3
:id: CxGDcU82mAyU

# Slicing works with a mixture of positive and negative indices
demo_list[1:-2]
```

```{code-cell} ipython3
:id: 0-1j3oUymAyU

# If an index is omitted, Python reaches the first or the last element of the list
demo_list[2:]
```

```{code-cell} ipython3
:id: mAUWpnIDmAyU

# The same as above, with the first index omitted
demo_list[:3]
```

```{code-cell} ipython3
:id: VFNFjCRGmAyV

# Slicing with steps
demo_list[1::2]
```

+++ {"id": "_sC6jmgFmAyV"}

---

+++ {"id": "ur-eM7jbmAyV"}

### Quiz

The following code creates a list whose length is a-priori unknown. Extract:

    1. the last element of the list by using a positive index
    2. the first element of the list by using a negative index
    3. a new list of every element on an even index
    4. this list reversed

```{code-cell} ipython3
:id: 278eQ4xamAyV

import random  # built-in package

random_number_list = []
for i in range(10):
    random_number = random.randint(1, 99)
    random_number_list.append(random_number)

random_number_list
```

```{code-cell} ipython3
:id: EaL9dMz7mAyW

# Your code here for 1.
```

```{code-cell} ipython3
:id: nxw_YyPNmAyW

# Your code here for 2.
```

```{code-cell} ipython3
:id: R2GFp-n6mAyX

# Your code here for 3.
```

```{code-cell} ipython3
:id: 2fmnB5JlmAyX

# Your code here for 4.
```

+++ {"id": "ekwyqy5YmAyX"}

---

+++ {"id": "40fTej_mmAyX"}

#### Lists are mutable

Lists methods allows you to manipulate the elements stored in the list quickly and effectively. The method `.append()` on the list allows you to add an element at the end of that list. This is a method that you'll be using often!

```{code-cell} ipython3
:id: RdCV6F-RmAyY

empty_list = []
empty_list.append("appended")

print(empty_list)

# Another element
empty_list.append("second addition")
print(empty_list)
```

+++ {"id": "LsgOruXgmAyY"}

The `.extend()` method allows you to add all the elements of a second list. It works the same as the `+=` operator we saw before. 

```{code-cell} ipython3
:id: TXR82VeamAyY

groceries = ["Apple", "Crisps", "Soda", "Stroopwafels"]
fruit = ["Apple", "Banana", "Orange"]

groceries.extend(fruit)  # similar to +=
print(groceries)
```

+++ {"id": "TQoDTzkgmAyZ"}

The `.remove()` method allows you to remove a given elements from a list. 

What happens if there are duplicate elements that you want to have removed in a list?

```{code-cell} ipython3
:id: _UUQs6fSmAyZ

groceries.remove("Apple")
print(groceries)
```

+++ {"id": "EgOxZU0HmAyZ"}

The method `.reverse()` reverses a list IN PLACE (i.e. the original list is modified)

```{code-cell} ipython3
:id: DA6I1wqgmAyZ

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

numbers.reverse()
print(numbers)
```

+++ {"id": "Nq_6AEYRmAyZ"}

You can replace or delete parts of a list by slicing:

```{code-cell} ipython3
:id: p_HecsA0mAyZ

# Replace elements

numbers[-3:] = [10, 11, 12]
print(numbers)
```

```{code-cell} ipython3
:id: NXZb-M-XmAya

# Delete elements

numbers[4:6] = []
print(numbers)
```

+++ {"id": "bFwtA9DomAya"}

Sorting a list is as easy as calling `.sort()` on it. This changes the list in place. However, the list elements must be of the same type!

```{code-cell} ipython3
:id: lRu7GpAhmAya

# This renders a TypeError
["text", 1, 2, 3].sort()
```

```{code-cell} ipython3
:id: crrO66-8mAya

homogeneous_list = [1, 56, 33, 8, 220, 9]
homogeneous_list.sort()

homogeneous_list
```

+++ {"id": "eo0V8ekxmAya"}

Lists of strings can be sorted as well. Useful if you want to sort from A-Z. 

Is the sort operation giving the expected result?

```{code-cell} ipython3
:id: MrgBYr0bmAyb

homogeneous_list = ["canary", "hippo", "kangaroo", "narwhal", "Elephant", "raccoon", "yak", "ant"]
homogeneous_list.sort()
homogeneous_list
```

+++ {"id": "U1AT9-XnmAyb"}

---

+++ {"id": "tLSqYWKrmAyb"}

---

+++ {"id": "Ec2GKpW_mAyb"}

#### Lists of numbers

Lists of numbers can be manipulated by additional functions, among which `max()`, `min()` and `sum()`

```{code-cell} ipython3
:id: M8yPjikimAyb

some_numbers = [4, 8, 2, 6, 2, 9]

print(max(some_numbers))
print(min(some_numbers))
print(sum(some_numbers))
```

+++ {"id": "p2coAh49mAyb"}

### Quiz

Get the minimum and maximum number of the list below _without_ using the `max()` and `min()` functions (e.g. by sorting and slicing). 

```{code-cell} ipython3
:id: uwmA95uZmAyc

numbers = [21, 1, 56, 33, 8, 220, 9]

# Your code here
```

+++ {"id": "0dQqbtoimAyc"}

Compute the average of `some_numbers`:

```{code-cell} ipython3
:id: BqSV9TG5mAyc

some_numbers = [4, 8, 2, 6, 2, 9]

# Your code here
```

+++ {"id": "JkLOTBNjmAyc"}

Explain the sorting of the following list:

```{code-cell} ipython3
:id: a_NF8eSOmAyc

homogeneous_list = ["21", "1", "56", "33", "8", "220", "9"]
homogeneous_list.sort()
homogeneous_list
```

+++ {"id": "rsPMBTatmAyc"}

---

+++ {"id": "RgAWy8FemAyc"}

### Tuples

Tuples are the **immutable** counterpart of the lists. 

They are defined by round brackets `()` and they mainly differ from the list in that they do not accept those methods that tries to manipulate its elements.

```{code-cell} ipython3
:id: cWZ2BjyWmAyc

# Tuples can contain different types of objects (even another list like [1,2,3])

demo_tuple = ("text", 23, 92, "another_text", [1,2,3])

print(demo_tuple)
```

```{code-cell} ipython3
:id: 7mc_49sSmAyd

# Elements can be accessed on the basis of their index...

demo_tuple[1:3]
```

```{code-cell} ipython3
:id: RezsQC2vmAyd

# But, they cannot be replaced. This raises a TypeError error!

demo_tuple[1] = 2
```

+++ {"id": "TqeRPC2hmAyd"}

For now, just know that tuples are a datatype in Python. You'll know when you need them further on in this course!

+++ {"id": "aBD18s9ZmAye"}

### Strings

Strings are **immutable**, sequences of characters (so, they are **homogeneous**)

In the Python language, strings are defined by single `'` or double quotes `"`,  and their elements are contiguous.

```{code-cell} ipython3
:id: 6OnqjW8KmAye

demo_string = "Does Cersei have any friends?"
print(demo_string)
```

```{code-cell} ipython3
:id: qbbbfVKamAye

# Using single or double quotes is indifferent
demo_string_single = 'Does Cersei have any friends?'
demo_string == demo_string_single
```

```{code-cell} ipython3
:id: VSGs9ZMfmAyf

# Remember: Digits are not numbers! (frequent source of debugging frustration)

print(type("1979") == type(1979))
```

```{code-cell} ipython3
:id: 1UgPCLTYmAyf

print('"1979" type is: ' + str(type("1979")))
```

```{code-cell} ipython3
:id: LmLCmwQTmAyf

print('1979 type is: ' + str(type(1979)))
```

+++ {"id": "Dx3AMRYBmAyf"}

By being immutable sequences, strings accept all the sequences methods, but they not support item assignment:

```{code-cell} ipython3
:id: ECO7gPhqmAyf

# You can check the length (in characters, whitespaces count!) of a string
len(demo_string)
```

```{code-cell} ipython3
:id: FS-6kKHHmAyg

# Strings can be looked for in other strings
"Cersei" in demo_string
```

```{code-cell} ipython3
:id: Yeoqca6FmAyg

# How many 'a's do we have in our string?
demo_string.count("a")
```

```{code-cell} ipython3
:id: J-CqwSOdmAyh

# Concatenation is possible
demo_string += "\nNoway!"
demo_string
```

```{code-cell} ipython3
:id: l3jC4e6LmAyh

print(demo_string)
```

+++ {"id": "aijPKDOPmAyh"}

The escape sequence `\n` indicates the end of the line. 

Python escape sequences are introduced by the escape character `\`, whose goal is to signal the interpreter that the following character has an "unusual" interpretation. Here is a partial list:

| Escape Sequence|         Meaning|
|:--------------:|:---------------:|
|              \\\\|  backslash|
|              \\'|  single quote|
|              \\b|  backspace|
|              \\n|  new line|
|              \\t|  horizontal tab|

```{code-cell} ipython3
:id: AZIW3j81mAyi

# Nicely print our string!
print(demo_string)
```

```{code-cell} ipython3
:id: Gf5Fpn9fmAyi

# What does a backspace do?
print(demo_string  +"\b")
```

```{code-cell} ipython3
:id: -9EFZSEWmAyj

# The escape character may be useful when you need single quotes inside a single quote-marked string...
'Can any of you pronounce \'s-Hertogenbosch?'
```

```{code-cell} ipython3
:id: a-vwBersmAyk

# but this solution is preferred (when possible)
"Can any of you pronounce 's-Hertogenbosch?"
```

+++ {"id": "QDWZTabamAyk"}

Strings that span multiple lines can be written in a readable form by using the sequence `"""` as a delimiter

```{code-cell} ipython3
:id: Kem3RR91mAyk

print("""Unsealed, on a porch a letter sat
Then you said, "I wanna leave it again"
Once I saw her on a beach of weathered sand
And on the sand I wanna leave her again""")
```

+++ {"id": "9U8FswPhmAyl"}

### Quiz

+++ {"id": "i82TbsndmAyl"}

Run the cell below. Where do all the '\n's come from?

```{code-cell} ipython3
:id: OOj9TxtFmAyl

""""On a weekend I wanna wish it all away, yeah
And they called and I said that I'll go
And I said that I'll call out again
And the reason I ought ta leave her calm, I know
I said, "I don't know whether I'm the boxer or the bag"""""
```

```{code-cell} ipython3
:id: RdC7o9_fmAyl

# String slicing
"Monty Python"[-12:-7]
```

```{code-cell} ipython3
:id: j0IXxGmamAyl

# But single characters cannot be replaced. This raises a TypeError. 
demo_string[5:11] = "Melisandre"
```

+++ {"id": "xhimsX8-mAym"}

#### String Methods

Strings have a buch of dedicated methods (see the [documentation](https://docs.python.org/3.8/library/stdtypes.html) for a complete list), that allows them to be both inspected or manipulated (they are not modified, rather a **new object** is returned). 

The following are commonly used the most:

```{code-cell} ipython3
:id: TWF4n7lbmAym

# Is the string composed solely of 1. digits 2. alphabetic characters 3. both?
print('100'.isdigit())
print('cat'.isalpha())
print('my cat is 100'.isalnum())  # Why False?
```

```{code-cell} ipython3
:id: SreTtIeYmAym

print(demo_string)
```

+++ {"id": "2RmcIDdcmAym"}

The `.startswith()` and `.endswith()` methods are useful:

```{code-cell} ipython3
:id: DcphuqOtmAym

# Does the string starts or ends with a given sequence of characters?
print(demo_string.startswith("d"))  # it is case sensitive !!!
print(demo_string.endswith("Noway!"))
```

+++ {"id": "0431Dh5tmAyn"}

If you want to compare strings, or want to have them stored in a normalized way, you can use the `.upper()` and `.lower()` methods:

```{code-cell} ipython3
:id: mBGyjgofmAyn

# Change case to all the characters of a string
print(demo_string_single.upper())
print(demo_string_single.lower())
```

+++ {"id": "6OcrVbU8mAyn"}

If you want to get rid of unwanted characters at the beginning or at the end of a string, you can use `.strip()`. This is commonly used to remove all whitespace (i.e. spaces, linebreaks, tabs) from the string.

```{code-cell} ipython3
:id: pXt1IRAtmAyo

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
```

+++ {"id": "hmvBna4zmAyo"}

You can remove one or multiple elements from a list by using `.replace()`:

```{code-cell} ipython3
:id: CEOid6T3mAyo

# Replace a given sequence of characters with another 
print(demo_string.replace("Cersei", "Melisandre"))
```

```{code-cell} ipython3
:id: M0RZKf25mAyo

# Or if you want to completely remove a character or series of characters,
# simply replace it by an empty string! You can also chain these. 
print(demo_string.replace("?", "").replace("!", ""))
```

+++ {"id": "sC2DXTe-mAyp"}

#### From strings to lists

+++ {"id": "WA3OU9Q9mAyp"}

A string can be transformed into a list of string by splitting it on a given character. This is done through the `.split()` method. 

```{code-cell} ipython3
:id: 6uE3td6imAyp

# By whitespace
demo_string.split(" ")
```

```{code-cell} ipython3
:id: krUm1CBimAyp

# However, the default character is any white line (that's convenient!)
demo_string.split()
```

```{code-cell} ipython3
:id: za1Lkg0HmAyq

# the maximun number of splits can be specified
demo_string.split(" ", 2)
```

+++ {"id": "IXtJoYcAmAyq"}

#### From lists to strings

+++ {"id": "rkT8Rn8jmAyq"}

The inverse operation is possible, a list of strings can be joined by a single character using `join()` on another string. It's argument is the list.

```{code-cell} ipython3
:id: jGoHyN0CmAyq

# A whitespace
" ".join(["One","Two","Three"])
```

```{code-cell} ipython3
:id: 74BhY6eUmAyq

# An hyphen
"-".join(["One","Two","Three"])
```

```{code-cell} ipython3
:id: TxLEf1TYmAyq

# Any string basically
predifined_joinchar = "🌞"
predifined_joinchar.join(["Eins","Zwei","Drei"])
```

```{code-cell} ipython3
:id: ysKaOB6amAyr

# Or no characters at all
"".join(["Super", "cali", "fragilistic", "expiali", "docious"] )
```

+++ {"id": "7CR5wvyimAyr"}

Keep in mind that you can only join elements of type string. 

```{code-cell} ipython3
:id: prXkMsUjmAyr

# Raises a TypeError
" ".join(["This", "is", "notebook", "number", 1])
```

+++ {"id": "hG0TQMzOmAyr"}

---

```{code-cell} ipython3
:id: pCEdB6H7mAys


```

+++ {"id": "JZs8oKTMmAys"}

### Sets

Sets are collections of **unordered** and **distinct/unique** objects.

They are commonly used to test membership, to remove duplicates or to compute mathematical operations such as intersection, union, difference, and symmetric difference. Being unordered collections, they do not support indexing, slicing and any other sequence-like behavior. But, this  makes them extremely efficient.

In Python, sets can be create beither by using the syntax  `set([])` or by using curly braces `{}`.

+++ {"id": "95RR_DssmAys"}

Sets come in handy if you want to count the unique occurences in a list:

```{code-cell} ipython3
:id: 6YtsxauLmAys

text = """the quick brown fox jumps over the lazy dog"""
words = text.split()  # 'the' is in there twice
print(words)

unique_words = set(words)
unique_words
```

+++ {"id": "Y6k8yc-TmAys"}

You can add elements by calling `.add()` on the set. 

```{note}
The `.append()` is for lists only! Trying to add an element that's already in a set does not change anything.
``` 

```{code-cell} ipython3
:id: T8vP7NCamAys

# Elements are added with the function add()
unique_words.add("sheep")
unique_words
```

```{code-cell} ipython3
:id: Vjsiqc03mAys

# elements are removed with the function remove()
unique_words.remove("fox")
unique_words
```

```{code-cell} ipython3
:id: eBy0YgnSmAyt

# length of a set
len(unique_words)
```

```{code-cell} ipython3
:id: 2fRbYGu8mAyt

# membership test
"sheep" in unique_words
```

+++ {"id": "w0DYyLEdmAyt"}

You can use `.union()` to get all the elements from both sets.

```{code-cell} ipython3
:id: Ii8aw5WPmAyt

# the union of the two sets
all_words = unique_words.union(set(["pack", "my", "box", "with", "five", "dozen", "liquor", "jugs"]))
all_words
```

```{code-cell} ipython3
:id: xbLPSXQjmAyt

# Intersection of the two sets
other_set = {"brown", "dog", "purple", "fox"}

intersection = unique_words.intersection(other_set)
intersection
```

```{code-cell} ipython3
:id: kLniT592mAyt

# Elements that are in the first but not in the second set
unique_words.difference(other_set)
```

```{code-cell} ipython3
:id: WmmZOVVrmAyt

# Variables flipped
other_set.difference(unique_words)
```

```{code-cell} ipython3
:id: 9jLMMSl2mAyu

# Every elements of smaller_set are in all_elements?

all_elements = {1, 2, 3, 4, 5, 6, 7, 8, 9}
smaller_set = {2, 4, 6, 8}

print(all_elements.issuperset(smaller_set))
print(smaller_set.issubset(all_elements))
```

+++ {"id": "t-h6XDdXmAyu"}

Go over the other methods that can be used on a set. You can find them including examples here: https://www.w3schools.com/python/python_ref_set.asp. For sure, check out the `.update()` and `.isdisjoint()`. 

+++ {"id": "76r_UM2omAyu"}

### Quiz

```{code-cell} ipython3
:id: drW9OQ7smAyu


```

+++ {"id": "-eGcr4ERmAyu"}

---

+++ {"id": "hBr4KQzpmAyu"}

### Dictionaries

Dictionaries are **associative arrays** mapping **immutable** types (string, numbers, tuples...) to arbitrary objects of any kind (all datatypes you earlier saw, variables, functions, modules...). Intuitively, they can be thought as collections of objects that we can recall by means of a unique key. 

To visualize a Python dictionary you can think of a telephone book, in which people names are the unique keys that you use to retrieve difference kinds of information (phone numbers, street address, mail address...). The same telephone number, street address or other information can be present in the entries of more people, but a label cannot be associated with more than one entry. 

In Python, dictionaries are defined by curly brackets `{}`, in which key-value pairs are separated by commas and joint by colons.

```{code-cell} ipython3
:id: lDM2PLycmAyv

# An English-Dutch dictionary of colors

color2kleur = {
    "black": "zwart",
    "white": "wit",
    "red": "rood",
    "yellow": "geel"
}

print(color2kleur)
```

```{code-cell} ipython3
:id: GrrV1A-gmAyv

# Values can be recalled by their keys
color2kleur["white"]
```

```{code-cell} ipython3
:id: NvGQFsrdmAyv

# We can change a value associated with a key
color2kleur["white"] = "sneeuwwit"

print(color2kleur)
```

```{code-cell} ipython3
:id: AdxpH3yImAyv

# If the key is missing a new key: value pair is added
color2kleur["blue"] = "blauw"

print(color2kleur)
```

```{code-cell} ipython3
:id: F9eB0loGmAyv

# {Key: value} can be deleted with the command "del()"
del(color2kleur["blue"])
print(color2kleur)
```

```{code-cell} ipython3
:id: hXyIkdUSmAyw

# Check if a dictionary has a given key
"blue" in color2kleur
```

```{code-cell} ipython3
:id: bWVydw5VmAyw

# Count the number of entries in a dictionary
len(color2kleur)
```

+++ {"id": "YRKzzvjQmAyw"}

### Quiz

What you're actually doing by calling the dict that way, is calling the `.keys()` method. Try using the following methods below on the `color2kleur` dictionary:

1. `.keys()` vs. just calling the dictionary by `color2kleur`
2. `.values()`
3. `.items()`
    
What is the datatype that is returned for each of these methods? And what is de datatype inside these 'iterables'?

```{code-cell} ipython3
:id: icDTmUP-mAyw

# You code here
```

+++ {"id": "FXY9PzofmAyw"}

#### Iterating over a Dictionary

```{code-cell} ipython3
:id: 5rL_YIXgmAyw

# iterate over dictionary keys:
print(list(color2kleur))
print(list(color2kleur.keys()))
```

```{code-cell} ipython3
:id: qQGYGuRvmAyx

# iterate over dictionary values:
print(list(color2kleur.values()))
```

```{code-cell} ipython3
:id: -Vn_EOnnmAyx

# iterate over dictionary key-value pairs:
print(list(color2kleur.items()))
```

+++ {"id": "B-zxqXotmAyx"}

---

+++ {"id": "5suk_BdYmAyx"}

###  Type casting

Sometimes, we may need to change the type of a variable. 

For instance, we may want to change a list into a set in order to delete all its repeated elements. A quick way to do so is to transform the list in a set.

Other example may involve the `.join()` method that does not accept numbers. Conversion functions can be used to quickly switch numbers to strings. Sometimes, these conversion functions are built-in into a function, which is the case in the `print()` function. It is basically applying the `str()` function on every object that you give as argument.

```{note}
Not all types of variables can be switched to other types. In what follows we report some common conversion.
```

```{code-cell} ipython3
:id: edqdGgg4mAyx

# From number to string
str(3.123424235454)
```

```{code-cell} ipython3
:id: mwUDKmWkmAyx

# Sometimes you want to round the number
str(round(3.123424235454, 2))
```

```{code-cell} ipython3
:id: 5c8LaAY2mAyy

# From string to integer
int("3")
```

```{code-cell} ipython3
:id: q9_tgwTmmAyy

# From string to floating numer
float("3")
```

```{code-cell} ipython3
:id: ClFTmeO_mAyz

# From list to tuple (list cannot be used as dictionary keys, tuples can)
tuple([demo_list])
```

```{code-cell} ipython3
:id: VQv6E-53mAy0

# From list to set
set([1,2,3,1,2,3,3])
```

```{code-cell} ipython3
:id: kocD8ybAmAy1

# From string to list
print(list("this is a sentence"))
```

+++ {"id": "kvsp2sqqmAy1"}

### Quiz

The list `numbers` contains 21 integers, ranging from -10 to 10, unsorted. 

Create a new list containing only the positive numbers from the list. Use `.sort()`, `len()` and `round()`

```{code-cell} ipython3
:id: d4TvUuy2mAy1

numbers = [-7, 1, 3, 8, 7, -2, 5, 4, -10, -4, -3, -6, 2, 9, 0, -5, -8, 10, -9, 6, -1]
```

```{code-cell} ipython3
:id: WiGveyLpmAy2

# Your code here
```

+++ {"id": "J89IuYlymAy2"}

---

+++ {"id": "yXuBnZe-mAy2"}

# Exercises

## Reading
* Check out number 8 of the Python Enhancement Proposals (PEP): https://www.python.org/dev/peps/pep-0008/. Try writing your code with PEP8 in mind. 
* [Python Cheat Sheet](https://www.cheatography.com/davechild/cheat-sheets/python/), which collects much of the syntax we used today.
* Have a look at Python's built-in types: https://docs.python.org/3.8/library/stdtypes.html. Be sure to check out the part on [string methods](https://docs.python.org/3.8/library/stdtypes.html#string-methods). You can skip the other sections. 

## Tasks

+++ {"id": "E5tEL618mAy3"}

### Excercise 1

Italian nobles tends to have an awful lot of names. For instance, "Vittorio Emanuele di Savoia" (or "Vittorio" for close friends) has the 12 names listed in `full_name`. 

Can you find a pythonic way to eliminate the less used names from this string?

```{code-cell} ipython3
:id: nwffyJv2mAy3

full_name = "Vittorio Emanuele Alberto Carlo Teodoro Umberto Bonifacio Amedeo Damiano Bernardino Gennaro Maria di Savoia"
```

```{code-cell} ipython3
:id: TyqHvGIcmAy3

# Your code here
```

+++ {"id": "9DLqwF1NmAy4"}

### Exercise 2.

The code in the next cell creates a variable called `zen_text`, and assigns it a nicely formatted version of the textual elements of the Zen of Python.

* Count the number of in this manifesto of:
    1. Characters
    2. Words
    3. Unique words
    3. Non-empty lines
    

```{code-cell} ipython3
:id: b1x3rx_LmAy4

import this
zen_text = ''.join(this.d.get(el, el) for el in this.s)  # forget this complicated pattern for now
```

```{code-cell} ipython3
:id: ZaykSfG_mAy4

# Your code here

```

+++ {"id": "pX5hC93-mAy4"}

### Exercise 3.

The dictionary in the following cell reports, for each Scrubs character, a dictionary mapping is given with the name of the actor, the age of the character and its credentials.

Write code to answer the following questions:

- What are the **names of the actors** of the cast?

- What is the **average age** of the characters?

- How **many M.D.s** are there in the main cast?

- Which character is not listed in the credentials dictionary?

```{admonition} Tip
:class: tip
Check the dictionary and set methods.
```

```{code-cell} ipython3
:id: ePZx4vLXmAy5

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
```

```{code-cell} ipython3
:id: XHHCJsVXmAy5

# Your code here
```

```{code-cell} ipython3
:id: l6hmP2HxmAy5


```

+++ {"id": "aYXVFYyPmAy5"}

### Exercise 4 Assignment Week1!

A string is stored in the `coe_books` variable. 

* How many different books of Jonathan Coe are listed?
* Check if the string starts with 'the accidental woman'
* Print this text titlecased (every word starts with a capital letter, ignore the prepositions for now). And uppercased. And capitalized.
* Convert the string to a list of words. Two of the book titles contain digits: 58 and 11. Find the index in the list and replace the string object for the number as integer. Print the list. 

```{code-cell} ipython3
:id: S5b1g7tjmAy5

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
```

```{code-cell} ipython3
:id: dey43Pi0mAy6

# Your code here

```

+++ {"id": "oJxlYRSOmAy6"}

---
