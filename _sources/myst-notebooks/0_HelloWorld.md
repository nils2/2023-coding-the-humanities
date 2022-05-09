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

+++ {"id": "MsV62m480HY8"}

# Getting started

+++ {"id": "q1ii-I_S0Ozf"}

## Running a Jupyter Notebook in Google Colaboratory

+++ {"id": "BXnmGHop5mvQ"}

If you are reading this, you have probably already managed to do this. Nevertheless, here is the basic idea: Using Google Colab, you can open our class materials from Github directly and keep the whole process in the cloud. View the list of class notebooks that are available for running and editing by going to your Google Colab: https://colab.research.google.com/ and loading them using the GitHub option. Enter the GitHub link of our course materials: https://github.com/bloemj/2022-coding-the-humanities and you will see the notebooks. For example, to open this notebook that you are currently reading, choose 0_HelloWorld.ipynb.

To start working, save a copy to your own Google Drive, and you will be able to edit the notebook while keeping your changes. If you quit and continue later, open your own copy from Google Drive, not the class copy from Github which will not have your changes,

```{note}
Google Colaboratory only work while you have an active internet connection. If you expect to be working offline, consider installing Python on your own machine.
```

+++ {"id": "dy7M2q7K0HZC"}

## Installing Python for offline use

+++ {"id": "GYn-ouV40HZD"}

If you wish to have the ability to work on these course materials without an active internet connection, we recommended that you install the full Anaconda Python 3.8 on your own machine, as it sets up your Python environment, together with a bunch of often used packages that you'll use during this course. A guide on installing Anaconda can be found here: https://docs.anaconda.com/anaconda/install/. NB: You don't have to install the optional stuff, such as the PyCharm editor. 

For more instructions, take a look at: https://github.com/bloemj/2022-coding-the-humanities/blob/master/setup.md. 

+++ {"id": "kIFcGKLv0HZE"}

If you completed all the steps and you have Python and Jupyter notebooks installed, open this file again as a notebook and continue with the content below. Good luck and have fun! 🎉

+++ {"id": "lDDbmY6g0HZF"}

# Hello World

This notebook contains some code to allow you to check if everything runs as intended.

[Jupyter notebooks](https://jupyter.org) contain cells of Python code, or text written in [markdown](https://www.markdownguide.org/getting-started/). This cell for instance contains text written in markdown syntax. You can edit it by double clicking on it. You can create new cells using the "+" (top right bar), and you can run cells to 'execute' the markdown syntax they contain and see what happens.

+++ {"id": "2CADL1_M0HZF"}

The other type of cells contain Python code and need to be executed. You can either do this by clicking on the cell and then on the play button in the top of the window. Or by pressing `shift + ENTER`. Try this with the next cell, and you'll see the result of this first line of Python. 

+++ {"id": "UwVH2wcA0HZG"}

**For a more extended revision of these materials, see http://www.karsdorp.io/python-course (Chapter 1).**

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: U-FJWcoA0HZH
outputId: 6156319d-326a-424f-9a9f-914e6d1bc91d
---
# It is customary for your first program to print Hello World! This is how you do it in Python.

print("Hello World!")
```

```{code-cell} ipython3
:id: umHZLgio0HZI

# You can comment your code using '#'. What you write afterwards won't be interpreted as code.
# This comes in handy if you want to comment on smaller bits of your code. Or if you want to
# add a TODO for yourself to remind you that some code needs to be added or revised.
```

+++ {"id": "uHf1nTo00HZJ"}

The code you write is executed from a certain *working directory* (we will see more when doing input/output). 

You can access your working directory by using a *package* (bundle of Python code which does something for you) part of the so-called Python standard library: `os` (a package to interact with the operating system).

```{code-cell} ipython3
:id: XpKvRwOq0HZK

import os # we first import the package
```

```{code-cell} ipython3
:id: NqnJ9Cct0HZL

os.getcwd() # we then can use some of its functionalities. In this case, we get the current working directory (cwd)
```

+++ {"id": "fWQ4fLEW0HZL"}

## Python versions

```{image} https://www.python.org/static/img/python-logo@2x.png
:alt: pythonlogo
```

It is important that you at least run a version of Python that is being supported with security updates. Currently (Spring 2022), this means Python 3.7 or higher. You can see all current versions and their support dates on the [Python website](https://www.python.org/downloads/). Furthermore, every Python version adds, but sometimes also changes functionality, so if you use a different version, you may not always get the same results.

If you are using Google Colab, your code will be running using version 3.7.

If you recently installed Python on your machine through [Anaconda](https://www.anaconda.com/products/individual#), you're most likely running version 3.8!

This course was mainly designed for version 3.8, but as the differences are minor, both 3.7 and 3.8 can be used.

+++ {"id": "jMLEpE3g0HZL"}

Let's check the Python version you are using by importing the `sys` package. Try running the next cell and see it's output.

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: st3VJcog0HZM
outputId: fdeff1aa-6506-4f99-f462-10ac953f5aac
---
import sys

print(sys.executable)  # the path where the Python executable is located
print(sys.version)  # its version
print(sys.version_info)
```

+++ {"id": "4NHmMiT40HZM"}

You now printed the version of Python that your Google Colab instance is using or that you have installed.

You can also check the version of a package via its property `__version__`. A common package for working with tabular data is `pandas` (more on this package later). You can import the package and make it referencable by another name (a shorthand) by doing:

```{code-cell} ipython3
:id: UOqK823Y0HZN

import pandas as pd  # now 'pd' is the shorthand for the 'pandas' package
```

+++ {"id": "NP-mXqRb0HZN"}

```{note}
Is this raising an error? Look further down for a (possible) explanation!
``` 

Now the `pandas` package can be called by typing `pd`. The version number of packages is usually stored in a _magic attribute_ or a _dunder_ (=double underscore) called `__version__`. 

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
id: 2NUb8EJQ0HZN
outputId: 4ae719b1-9016-4c24-e2e4-d5c5268e70cb
---
pd.__version__
```

+++ {"id": "xawPsMHM0HZN"}

The code above printed something without using the `print()` statement. Let's do the same, but this time by using a `print()` statement. 

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: MOZdUviV0HZO
outputId: 4672adb8-535b-48af-e1fd-419645905f0f
---
print(pd.__version__)
```

+++ {"id": "LYffpbGo0HZO"}

Can you spot the difference? Why do you think this is? What kind of datatype do you think the version number is? And what kind of datatype can be printed on your screen? We'll go over these differences and the involved datatypes during the first lecture and seminar. 

If you want to know more about a (built-in) function of Python, you can check its manual online. The information on the `print()` function can be found in the manual for [built-in functions](https://docs.python.org/3.8/library/functions.html#print)

More on datatypes later on. 

+++ {"id": "iAKTDhLM0HZO"}

### Exercise
Try printing your own name using the `print()` function. 

```{code-cell} ipython3
:id: QEFNDPiB0HZP

# TODO: print your own name
```

```{code-cell} ipython3
:id: TxuQsg0i0HZP

# TODO: print your own name and your age on one line
```

+++ {"id": "hQLjrEm10HZP"}

If all of the above cells were executed without any errors, you're clear to go! 

However, if you did get an error, you should start debugging. Most of the times, the errors returned by Python are quite meaningful. Perhaps you got this message when trying to import the `pandas` package:

```python
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-26-981caee58ba7> in <module>
----> 1 import pandas as pd

ModuleNotFoundError: No module named 'pandas'
``` 

If you go over this error message, you can see:

1. The type of error, in this example `ModuleNotFoundError` with some extra explanation
2. The location in your code where the error occurred or was _raised_, indicated with the ----> arrow

In this case, you do not have this (external) package installed in your Python installation. Have you installed the full Anaconda package? You can resolve this error by installing the package from Python's package index ([PyPI](https://pypi.org/)), which is like a store for Python packages you can use in your code. 

To install the `pandas` package (if missing) in Google Colab, run in a cell:

```
!pip install pandas
```
The exclamation mark tells the notebook cell that this is not a Python command, but a command for the operating system (a command line script).

If you are working on your own machine with Anaconda, this should work in most cases (it will make sure that it installs into the correct Python kernel if you have multiple):

```
!{sys.executable} -m pip install pandas
```

Or to update the `pandas` package you already have installed:

```
!{sys.executable} -m pip install pandas -U
```

Try this in the cell below!


```{code-cell} ipython3
:id: CW8QbBf10HZP

# Try either installing or updating (if there is an update) your pandas package
# your code here
```

+++ {"id": "bA2k1IlX4pJ4"}

Do note that in Anaconda, it is usually better to install packages directly through Anaconda and not use pip. This is done on the command line (outside of Python):

```
conda install pandas
```

+++ {"id": "BexxAPkt0HZP"}

If you face other errors, then Google (or DuckDuckGo etc.) is your friend. You'll see tons of questions on Python related problems on websites such as Stack Overflow. It's tempting to simply copy paste a coding pattern from there into your own code. But if you do, make sure you fully understand what is going on. Also, in assignments in this course, we ask you to:
1. Specify a URL or source of the website/book you got your copied code from
2. Explain in a _short_ text or through comments by line what the copied code is doing

This will be repeated during the lectures.

However, if you're still stuck, you can open a discussion in our [Canvas course](https://canvas.uva.nl/courses/22381/discussion_topics). You're also very much invited to engage in threads on the discussion board of others and help them out. Debugging, solving, and explaining these coding puzzles for sure makes you a better programmer!

+++ {"id": "k5Cztcsp0HZQ"}

# Basic stuff
The code below does some basic things using Python. Please check if you know what it does and, if not, you can still figure it out. Just traverse through the rest of this notebook by executing each cell if this is all new to you and try to understand what happens.

```{image} https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Don%27t_Panic.svg/200px-Don%27t_Panic.svg.png
:alt: donotpanic
```

The [first notebook](https://github.com/uvacreate/2021-coding-the-humanities/blob/master/notebooks/1_Basics.ipynb) that we're discussing in class is paced more slowly. You can already take a look at it if you want to work ahead. We'll be repeating the concepts below, and more.

If you think you already master these 'Python basics' and the material from the first notebook, then get into contact with us for some more challenging exercises!

+++ {"id": "Ou2CfT8-0HZQ"}

## Variables and operations

```{code-cell} ipython3
:id: pZZHBXZo0HZQ

a = 2
b = a
```

```{code-cell} ipython3
:id: QjNmtNS10HZQ

# Or, assign two variables at the same time
c, d = 10, 20
```

```{code-cell} ipython3
:id: 2bnkcTnh0HZQ

c
```

```{code-cell} ipython3
:id: JZkzYatf0HZQ

b += c
```

```{code-cell} ipython3
:id: S_2I7XWp0HZR

# Just typing a variable name in the Python interpreter (= terminal/shell/cell) also returns/prints its value
a
```

```{code-cell} ipython3
:id: icJb2iJU0HZR

# Now, what's the value of b?
b
```

```{code-cell} ipython3
:id: 9BUbqPH50HZR

# Why the double equals sign? How is this different from the above a = b ? 
a == b
```

```{code-cell} ipython3
:id: z0yXvh6z0HZR

# Because the ≠ sign is hard to find on your keyboard
a != b
```

```{code-cell} ipython3
:id: kQstdK5g0HZS

s = "Hello World!"

print(s)
```

```{code-cell} ipython3
:id: YJVvpeHw0HZS

s[-1]
```

```{code-cell} ipython3
:id: OreSbELN0HZS

s[:5]
```

```{code-cell} ipython3
:id: EWGHfzBw0HZS

s[6:]
```

```{code-cell} ipython3
:id: vkgR6_f10HZS

s[6:-1]
```

```{code-cell} ipython3
:id: b6ewJYao0HZT

s
```

```{code-cell} ipython3
:id: BznPTGX80HZT

words = ["A", "list", "of", "strings"]
words
```

```{code-cell} ipython3
:id: UyxXotbR0HZT

letters = list(s) # Names in green are reserved by Python: avoid using them as variable names
letters
```

+++ {"id": "D8rvmj690HZT"}

If you do have bound a value to a built-in function of Python by accident, you can undo this by restarting your 'kernel' in Jupyter Notebook. Click `Kernel` and then `Restart` in the bar in the top of the screen. You'll make Python loose it's memory of previously declared variables. This also means that you must re-run all cells again if you need the executions and their outcomes.

```{code-cell} ipython3
:id: G-dUE8IT0HZT

# Sets are unordered collections of unique elements
unique_letters = set(letters)
unique_letters
```

```{code-cell} ipython3
:id: ArgkBRkM0HZT

# Variables have a certain data type. 
# Python is very flexible with allowing you to assign variables to data as you like
# If you need a certain data type, you need to check it explicitly

type(s)
```

```{code-cell} ipython3
:id: YF6iKbiO0HZT

print("If you forgot the value of variable 'a':", a)
type(a)
```

```{code-cell} ipython3
:id: rhhBm4gi0HZU

type(2.3)
```

```{code-cell} ipython3
:id: u2hm9uYE0HZU

type("Hello")
```

```{code-cell} ipython3
:id: -f_Vt7av0HZU

type(letters)
```

```{code-cell} ipython3
:id: 8lAggS9D0HZU

type(unique_letters)
```

+++ {"id": "LuvIbH1E0HZU"}

#### Exercise

1. Create variables of each type: integer, float, text, list, and set. 
2. Try using mathematical operators such as `+ - * / **` on the numerical datatypes (integer and float)
3. Print their value as a string

```{code-cell} ipython3
:id: VzXgFLnq0HZU

# Your code here
```

+++ {"id": "X1RpU6jO0HZU"}


```{admonition} Tip
:class: tip
You can insert more cells by going to `Insert` and then `Insert Cell Above/Below` in this Jupyter Notebook.
```
