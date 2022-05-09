#!/usr/bin/env python
# coding: utf-8

# # Data Wrangling

# ## Contents:
# 
# * String formatting (f-strings)
# * Regular expressions (regex)
# * Pandas (Reading/writing CSV)

# ## String formatting

# Instead of writing a series of `print()` statements with multiple arguments, or concatenating (by `+`) strings, you can also use a Python string formatting method, called `f-strings`. More information can be read in PEP 498: https://www.python.org/dev/peps/pep-0498/

# You can define a string as a template by inserting `{ }` characters with a variable name or expression in between. For this to work, you have to type an `f` in front of the `'`, `"` or `"""` start of the string definition. When defined, the string will read with the string value of the variable or the expression filled in. 
# 
# ```python
# name = "Joe"
# text = f"My name is {name}."
# ```
# 
# Again, if you need a `'` or `"` in your expression, use the other variant in the Python source code to declare the string. Writing:
# 
# ```python
# f'This is my {example}.'
# ```
# 
# is equivalent to:
# 
# ```python
# f"This is my {example}."
# ```

# In[1]:


name = "Joe"
text = f"My name is {name}."

print(text)


# In[2]:


day = "Monday"
weather = "Sunny"
n_messages = 8

test_dict = {'test': 'test_value'}

text = f"""
Today is {day}. 
The weather is {weather.lower()} and you have {n_messages} unread messages. 
The first three letters of the weekday: {day[:3]}
An example expression is: {15 ** 2 = }



"""

text = f'Test by selecting key: {test_dict["test"]}'


print(text)


# ---

# ## Regular expressions

# Using regular expressions can be very useful when working with texts. It is a powerful search mechanism by which you can search on patterns, instead of 'exact matches'. But, they can be difficult to grasp, at first sight.
# 
# A **regular expression**, for instance, allows you to substitute all digits in a text, following another text sequence, or to find all urls, phone numbers, or email addresses. Or any text, that meets a particular condition.
# 
# See the Python manual for the `re` module for more info: https://docs.python.org/3/library/re.html
# 
# You can/should use a cheatsheet when writing a regular expression. A nice website to write and test them is: https://regex101.com/. 
# 
# Some examples of commonly used expressions:
# 
# * `\d` for all digits 0-9
# * `\w` for any word character
# * `[abc]` for a set of characters (here: a, b, c)
# * `.` any character
# * `?` the preceding character/pattern 0 or 1 times
# * `*` the preceding character/pattern 0 or multiple times
# * `+` the preceding character/pattern 1 or multiple times
# * `{1,2}` 1 or 2 times
# * `^` the start of the string
# * `$` the end of the string
# * `|` or
# * `()` capture group (only return this part)
# 
# In many text editors (e.g. VSCode) there is also an option to search (and replace) with the help of regular expressions.

# Python has a regex module built in. When working with a regular expression, you have to import it first:

# In[3]:


import re


# You can use a regular expression for **finding** occurences in a text. Let's say we want to filter out all web urls in a text:

# In[4]:


text = """
There are various search engines on the web. 
There is https://www.google.com/, but also https://www.bing.com/. 
A more privacy friendly alternative is https://duckduckgo.com/. 
And who remembers http://www.altavista.com/?
"""

re.findall(r'https?://.+?/', text)


# In[5]:


# Copied from https://www.imdb.com/search/title/?groups=top_250&sort=user_rating

text = """
1. The Shawshank Redemption (1994)
12 | 142 min | Drama

 9,3  Rate this 80 Metascore
Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.

Director: Frank Darabont | Stars: Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler

Votes: 2.355.643 | Gross: $28.34M

2. The Godfather (1972)
16 | 175 min | Crime, Drama

 9,2  Rate this 100 Metascore
An organized crime dynasty's aging patriarch transfers control of his clandestine empire to his reluctant son.

Director: Francis Ford Coppola | Stars: Marlon Brando, Al Pacino, James Caan, Diane Keaton

Votes: 1.630.157 | Gross: $134.97M

3. The Dark Knight (2008)
16 | 152 min | Action, Crime, Drama

 9,0  Rate this 84 Metascore
When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.

Director: Christopher Nolan | Stars: Christian Bale, Heath Ledger, Aaron Eckhart, Michael Caine

Votes: 2.315.134 | Gross: $534.86M
"""

titles = re.findall(r'\d{1,2}\. (.+)', text)
titles


# ### Quiz
# Try to get a list of all directors. And the gross income.

# In[6]:


# All directors


# In[7]:


# Gross income


# Or, you can use a regular expression to **replace** a character sequence. This is an equivalent to the `.replace()` function, but allows more variance in the string matching.

# In[8]:


text = """
Tim Robbins
Morgan Freeman
Bob Gunton
William Sadler
Marlon Brando
Al Pacino
James Caan
Diane Keaton
Christian Bale
Heath Ledger
Aaron Eckhart
Michael Caine
"""

# Hint: test this with https://regex101.com/
new_text = re.sub(r"(?:(\w)\w+) (\w+)", r"\1. \2", text)

print(new_text)


# ---

# # Data wrangling with Pandas

# ## CSV (in Pandas)
# 
# The other often used file type is CSV (Comma Separated Values), or variants, such as TSV (Tab Separated Values). Python includes another built-in module to deal with these files: the `csv` module. But, we will be using the `Pandas` module, the go-to package for data analysis, that you already imported and updated in Notebook 0. 
# 
# A CSV file is similar to an Excel or Google Docs spreadsheet, but more limited in markup and functionality (e.g. you cannot store Excel functions). It is just a text file in which individual entries correspond to lines, and columns are separated by a comma. You can always open a CSV file with a text editor, and this also makes it so easy to store and share data with.
# 
# For the rest of the notebook we will see how to work with the two main data types in `pandas`: the `DataFrame` and a `Series`.
# 
# Information on functions and modules of Pandas cannot be found in the Python manual online, as it is an external package. Instead, you can refer to https://pandas.pydata.org/pandas-docs/stable/index.html .

# ### `DataFrame`
# 
# 
# What is a `pandas.DataFrame`? 
# 
# A `DataFrame` is a collection of `Series` having the same length and whose indexes are in sync. A *collection* means that each column of a dataframe is a series. You can also see it as a spreadheet in memory, that also allows for inclusion of Python objects.

# We first have to import the package. It's a convention to do this like so with Pandas, which makes the elements from this package (classes, functions, methods) available under its abbreviation `pd`:

# In[9]:


import pandas as pd


# Next is loading the data. The following data comes from Wikipedia and was [automatically](https://query.wikidata.org/#%0ASELECT%20DISTINCT%20%3FmovieLabel%20%3Fimdb%20%28MIN%28%3FpublicationYear%29%20as%20%3Fyear%29%20%28year%28%3Fdate%29%20as%20%3Faward_year%29%20%28group_concat%28DISTINCT%20%3FdirectorLabel%3Bseparator%3D%22%2C%20%22%29%20as%20%3Fdirectors%20%29%20%28group_concat%28DISTINCT%20%3FcompanyLabel%3Bseparator%3D%22%2C%20%22%29%20as%20%3Fcompanies%29%20%3Fmale_cast%20%3Ffemale_cast%20WHERE%20%7B%0A%20%20%0A%20%20%7B%0A%20%20%3Fmovie%20p%3AP166%20%3Fawardstatement%20%3B%0A%20%20%20%20%20%20%20%20%20wdt%3AP345%20%3Fimdb%20%3B%0A%20%20%20%20%20%20%20%20%20wdt%3AP577%20%3Fpublication%20%3B%0A%20%20%20%20%20%20%20%20%20wdt%3AP57%20%3Fdirector%20%3B%0A%20%20%20%20%20%20%20%20%20wdt%3AP272%20%3Fcompany%20%3B%0A%20%20%20%20%20%20%20%20%20wdt%3AP31%20wd%3AQ11424%20.%0A%20%20%0A%20%20%3Fawardstatement%20ps%3AP166%20wd%3AQ102427%20%3B%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20pq%3AP585%20%3Fdate%20.%0A%20%20%7D%0A%20%20%0A%20%20BIND%28year%28%3Fpublication%29%20as%20%3FpublicationYear%29%0A%20%20%0A%20%20%7B%0A%20%20%20%20%20SELECT%20%3Fmovie%20%28COUNT%28%3Fcast_member%29%20AS%20%3Fmale_cast%29%20WHERE%20%7B%0A%20%20%20%20%20%20%3Fmovie%20wdt%3AP161%20%3Fcast_member%20.%0A%20%20%20%20%20%20%3Fcast_member%20wdt%3AP21%20wd%3AQ6581097%20.%0A%20%20%20%20%7D%20GROUP%20BY%20%3Fmovie%0A%7D%20%7B%0A%20%20%20%20SELECT%20%3Fmovie%20%28COUNT%28%3Fcast_member%29%20AS%20%3Ffemale_cast%29%20WHERE%20%7B%0A%20%20%20%20%20%20%3Fmovie%20wdt%3AP161%20%3Fcast_member%20.%0A%20%20%20%20%20%20%3Fcast_member%20wdt%3AP21%20wd%3AQ6581072%20.%0A%20%20%20%20%7D%20GROUP%20BY%20%3Fmovie%0A%20%20%7D%0A%20%20%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20%0A%20%20%20%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22%20.%0A%20%20%20%20%3Fmovie%20rdfs%3Alabel%20%3FmovieLabel%20.%0A%20%20%20%20%3Fdirector%20rdfs%3Alabel%20%3FdirectorLabel%20.%0A%20%20%20%20%3Fcompany%20rdfs%3Alabel%20%3FcompanyLabel%20.%20%0A%20%20%7D%0A%7D%20%0A%0AGROUP%20BY%20%3FmovieLabel%20%3Fimdb%20%3Fdate%20%3Fmale_cast%20%3Ffemale_cast%0AORDER%20BY%20%3Fyear%20) retreived. It is an overview of all movies that have won an Academy Award for Best Picture, including some extra data for the movie: a link to the IMDB, the publication and award year, the director(s), production company and the number of male and female actors in the cast. It can be that this data is incorrect, because this information is not entered in Wikipedia. 
# 
# You can find this file in `data/academyawards.csv`. Download it from the repository and save it in the data folder if you don't have it.

# Reading in a csv with pandas is easy. We call the `pd.read_csv()` function with the file path as argument. Pandas takes care of opening and closing the file, so a `with` statement is not needed. The contents of the csv file are then read in a Pandas DataFrame object. We can store this in the variable `df`. 
# 
# Calling this variable in a Jypyter Notebook gives back a nicely formatted table with the first and last 5 rows of the file.

# In[10]:


df = pd.read_csv('data/academyawards.csv', encoding='utf-8')
df


# Think of a `DataFrame` as an in-memory spreadsheet that you can analyse and manipulate programmatically. Or, think of it as a table in which every line is a data entry, and every column holds specific information on this data.
# 
# These columns can also be seen as lists of values. They are ordered and the index of an element corresponds with the index of the data entry. The collection of all such columns is what makes the DataFrame. One column in a table is represented by a Pandas `Series`, which collects observations about a given variable. Multiple columns are a `DataFrame`. A DataFrame therefore is a collection of lists (=columns), or `Series`.
# 
# If you look for other methods on `pd` you can call, you'll also see that there is an `pd.read_excel()` option to read spreadsheets in `.xls` or `.xlsx`. You can also  use this, if you have these kind of files.

# ### Statistics
# Now that we loaded our DataFrame, we can make pandas print some statistics on the file.

# In[11]:


df.head(1)  # First 5 rows


# In[12]:


df.tail()  # Last 5 rows


# In[13]:


df.describe()  # Descriptive statistics


# As you can see by what they return, these methods return another DataFrame with some descriptive statistics on the file, such as the number of entries (count), the mean of the numerical values, the standard deviation, minimum and maximum values, and the 25th, 50th, and 75th percentiles.

# The `.info()` method can also be informative. It gives you information about a dataframe:
# - how much space does it take in memory?
# - what is the datatype of each column?
# - how many records are there?
# - how many `null` values does each column contain (!)?

# In[14]:


df.info()


# Pandas automatically interprets which datatypes are used in the file, but this is not always correct. Especially if you have empty fields in the DataFrame, any other integers get interpreted as float. Every column has one datatype. You can check them separately by requesting the `.dtypes` argument on the `df`. 
# 
# The 'object' type is a string in this file, 'int64' is an integer.

# In[15]:


df.dtypes


# We expect different datatypes for the description-dataframe:

# In[16]:


description_df = df.describe()
description_df.dtypes


# ### Slicing and selecting

# #### `df['column1']`
# You can select a single column by calling this column name as if the DataFrame was a dictionary. A single column from a DataFrame returns a `Series` object.

# In[17]:


df


# In[18]:


print(type(df['movie']))

df['movie']


# The `Series` object is very similar to a `list`:

# In[19]:


movies = df['movie']

print("Length:", len(movies))
print()

for n, movie in enumerate(movies[:10], 1):
    print(n, movie, sep='\t')


# #### `df[['column1', 'column2']]`
# We can also slice a DataFrame by calling multiple column names as one list:

# In[20]:


df[['movie', 'imdb']]


# ### Looping over DataFrames

# You might expect that if you loop through a DataFrame, you get all the rows. Sadly, it is not that simple, because we now have data in two dimensions. We instead get all the column names (or the first row of the dataframe):

# In[21]:


for r in df:
    print(r)


# #### `zip(df['column1', df['column2')`
# Going over these items in a `for` loop needs a different approach. The built-in `zip()` function ([manual](https://docs.python.org/3/library/functions.html#zip)) takes two iterables of even length and creates a new iterable of tuples. The number of arguments/iterables that you give to `zip()` determines the length of the tuples.

# In[22]:


list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list(zip(list1, list2))


# In[23]:


n = 0
for movie, imdb in zip(df['movie'], df['imdb']):
    
    if n > 9:
        break  # stop flooding the Notebook
    
    print(movie, "http://www.imdb.com/title/" + imdb, sep='\t')
    n += 1


# #### `.to_dict(orient='record')`
# Or, accessing all entries in a convenient way, as a python dictionary for instance, can be done with the `.to_dict(orient='records')` method:

# In[24]:


df.head(1)


# In[25]:


for r in df.to_dict(orient='records'):
    
    print(r)
    print()
    
    name = r['movie']
    year = r['year']
    won = r['award_year']
    
    print("The movie " + name + " was produced in " + str(year) + " and won in " + str(won) + ".")
    
    print()
    
    break  # To not flood the notebook, only print the first


# #### `.iterrows()`
# Or you can use the `.iterrows()` method, which gives you tuples of the index of the row, and the row itself as `Series` object:

# In[26]:


for n, r in df.iterrows():
    
    name = r.movie  # You can use a dot notation here
    year = r.year
    won = r.award_year
    
    print(f"The movie {name} was produced in {year} and won in {won}.")
    
    print()
    
    break  # To not flood the notebook, only print the first


# In[ ]:





# ---

# ### Analysis

# In[27]:


df


# In[28]:


df.mean()


# You already saw above that you could get statistics by calling `.describe()` on a DataFrame. You can also get these metrics for individual columns. Let's ask the maximum number of male and female actors in the cast of a movie:

# In[29]:


df['female_cast'].max()


# In[30]:


df['male_cast'].max()


# You can also apply these operations to multiple columns at once. You get a `Series` object back.

# In[31]:


df.max()


# In[32]:


df[['male_cast', 'female_cast']]


# In[33]:


slice_df = df[['male_cast', 'female_cast']]

slice_df.max()


# To find the corresponding movie title, we can ask Pandas to give us the record in which these maxima occur. This is done through `df.loc`. This works by asking: "Give me all the locations (=rows) for which a value in a specified column is equal to this value".

# In[34]:


df


# In[35]:


df[['male_cast', 'female_cast']].max()


# In[36]:


df[df['female_cast'] > 10]


# In[37]:


for column_name, value in df[['male_cast', 'female_cast']].max().items():
    
    print("Movie with maximum for", column_name, value)
    
    row = df.loc[df[column_name] == value]
    
    print(row.movie)
    
    print()


# Other functions that can be used are for instance `.mean()`, `.median()`, `.std()` and `.sum()`.

# In[38]:


df['female_cast'].mean()


# In[39]:


df['male_cast'].mean()


# In[40]:


df['female_cast'].sum()


# In[41]:


df['male_cast'].sum()


# In[42]:


df


# Pandas also understands dates, but you have to tell it to interpret a column as such. We can change the `year` column in-place so that it is not interpreted as integer, but as a date object. 
# 
# In this case, since we only have the year available, and not a full date such as `2021-02-22` (YYYY-mm-dd), we have to specify the format. Typing `%Y` as string is shorthand for `YYYY`. It returns a full date, so every month and day are set to January first.

# In[43]:


df['year'] = pd.to_datetime(df['year'], format='%Y')

df['award_year'] = pd.to_datetime(df['award_year'], format='%Y')

df['year']


# In[44]:


df


# ### Plotting
# 
# Let's try to make some graphs from our data, for instance the number of male/female actors over time. 
# 
# We now have a year column that is interpreted as time by Pandas. These values can figure as values on a x-axis in a graph. The y-axis would then give info on the number of male and female actors in the movie.

# First, we set an **index** for the DataFrame. This determines how the data can be accessed. Normally, this is a range of 0 untill the number of rows. But, you can change this, so that we can analyse the dataframe on a time index.

# In[45]:


# Select only what we need
df_actors = df[['award_year', 'male_cast', 'female_cast']]
df_actors


# In[46]:


df_actors = df_actors.set_index('award_year')
df_actors


# Then simply call `.plot()` on your newly created DataFrame!

# In[47]:


df_actors.plot(figsize=(15,10))


# There are tons of parameters, functions, methods, transformations you can use on DataFrames and also on this plotting function. Luckily, plenty of guides and examples can be found on the internet.

# ### Grouping

# In[48]:


df


# Some directors have won multiple Oscars. To find out which, we have to count the number of rows in the DataFrame that include the same director. There is a Pandas function for this: `.count()`. Calling this on the DataFrame itself would give us the total number of rows only, per column. Therefore, we have to tell Pandas that we want to group by a particular column, say 'directors'.

# In[49]:


df.groupby('directors')


# It does not give back something nicely formatted or interpretable. It's just another Python object. The object returned by `groupby` is a `DataFrameGroupBy` **not** a normal `DataFrame`.
# 
# However, some methods of the latter work also on the former, e.g. `.head()` and `.tail()`. Let's call the `.count()` on this object:

# In[50]:


df.groupby('directors').count()


# Remember that this counts the numer of rows. As we know that each row is one movie, we can trim this down to:

# In[51]:


director_counts = df.groupby('directors').count()['movie']
director_counts


# Now, get all directors that have won an Oscar more than once by specifying a conditional operator:

# In[52]:


director_counts[director_counts > 1]


# In[53]:


list(director_counts.items())


# In[54]:


for i, value in director_counts.items():
    print(i, value)


# ### Adding a column

# If we want to get the total number of actors per movie, we have to sum the values from the `male_cast` and `female_cast` columns. 
# 
# You can do this in a for loop, by going over every row (like we saw above), but you can also sum the individual columns. Pandas will then add up the values with the same index and will return a new Series of the same length with the values summed.

# In[55]:


df


# In[56]:


df['male_cast'] + df['female_cast']


# In[57]:


total_cast = df['male_cast'] + df['female_cast']
total_cast


# Then, we add it as a column in our original dataframe. The only requirement for adding a column to a DataFrame is that the length of the Series or list is the same as that of the DataFrame.

# In[58]:


df['total_cast'] = total_cast
df


# Optionally, we can sort the DataFrame by column. For instance, from high to low (`ascending=False`) for the newly created `total_cast` column.

# In[59]:


df_sorted = df.sort_values('total_cast', ascending=False)
df_sorted


# ### Saving back the file

# Use one of the `.to_csv()` or `.to_excel` functions to save the DataFrame. Again, no `with` statement needed, just a file path (and an encoding).

# In[60]:


df_sorted.to_csv('stuff/academyawards_sum.csv', encoding='utf-8')


# In[61]:


df_sorted.to_excel('stuff/academyawards_sum.xlsx')


# You need to specify `index=False` if you want to prevent a standard index (0,1,2,3...) to be saved in the file as well.

# In[62]:


df_sorted.to_csv('stuff/academyawards_sum.csv', encoding='utf-8', index=False)


# Open the contents in Excel, LibreOffice Calc, or another program to read spreadsheets!

# ---

# # Data wrangling (example)
# 
# We can take a look at another example. We consider a dataset of tweets from Elon Musk, SpaceX and Tesla founder, and ask the following questions:
# * When is Elon most actively tweeting?
# 
# While this question is a bit trivial, it will allow us to learn how to wrangle data.

# In[63]:


import pandas as pd


# ### Load dataset

# Let's read in a CSV file containing an export of [Elon Musk's tweets](https://twitter.com/elonmusk), exported from Twitter's API.

# In[64]:


dataset_path = 'data/elonmusk_tweets.csv'
df = pd.read_csv(dataset_path, encoding='utf-8')


# In[65]:


df


# In[66]:


df.info()


# Let's give this dataset a bit more structure:
# - The `id` column can be transformed into the dataframe's index, thus enabling us e.g. to select a tweet by id;
# - The column `created_at` contains a timestamp, thus it can easily be converted into a `datetime` value

# In[67]:


df.set_index('id', drop=True, inplace=True)


# In[68]:


df


# In[69]:


df.created_at = pd.to_datetime(df.created_at)


# In[70]:


df.info()


# In[71]:


df


# ---

# ### Selection

# #### Renaming columns

# An operation on dataframes that you'll find yourself doing very often is to rename the columns. The first way of renaming columns is by manipulating directly the dataframe's index via the `columns` property.

# In[72]:


df.columns


# We can change the column names by assigning to `columns` a list having as values the new column names.
# 
# ```{note}
# The size of the list and new number of colums must match!
# ```

# In[73]:


# here we renamed the column `text` => `tweet`
df.columns = ['created_at', 'tweet']


# In[74]:


# let's check that the change did take place
df.head()


# The second way of renaming colums is to use the method `rename()` of a dataframe. The `columns` parameter takes a dictionary of mappings between old and new column names.
# 
# ```python
# mapping_dict = {
#     "old_column_name": "new_column_name"
# }
# ```

# In[75]:


# let's change column `tweet` => `text`
df = df.rename(columns={"tweet": "text"})


# In[76]:


df.head()


# **Question**: in which cases is it more convenient to use the second method over the first?

# #### Selecting columns

# In[77]:


# this selects one single column and returns as a Series
df["created_at"].head()


# In[78]:


type(df["created_at"])


# In[79]:


# whereas this syntax selects one single column
# but returns a Dataframe
df[["created_at"]].head()


# In[80]:


type(df[["created_at"]])


# ####  Selecting rows
# 
# Filtering rows in `pandas` is done by means of `[ ]`, which can contain the row number as well as a condition for the selection.

# In[81]:


df[0:2]


# ### Transformation
# 
# 
# The two main functions used to manipulate and transform values in a dataframe are:
# - `.map()` (on Series only!)
# - `.apply()`
# 
# In this section we'll be using both to enrich our datasets with useful information (useful for exploration, for later visualizations, etc.).

# #### Add link to original tweet

# The `map()` method can be called on a column, as well as on the dataframe's index.
# 
# When passed as a parameter to `map`, an 'anonymous' lambda function `lambda` can be used to transform any value from that column into another one.

# In[82]:


df['tweet_link'] = df.index.map(lambda x: f'https://twitter.com/i/web/status/{x}')


# Or, maybe it is easier with a list comprehension:

# In[83]:


df['tweet_link'] = [f'https://twitter.com/i/web/status/{x}' for x in df.index]


# In[84]:


df


# #### Add colums with mentions

# In[85]:


import re

def find_mentions(tweet_text):
    """
    Find all @ mentions in a tweet and 
    return them as a list.
    """
    
    regex = r'@[a-zA-Z0-9_]{1,15}'
    mentions = re.findall(regex, tweet_text)
    
    return mentions


# In[86]:


df['tweet_mentions'] = df.text.apply(find_mentions)


# In[87]:


df['n_mentions'] = df.tweet_mentions.apply(len)


# In[88]:


df.head()


# #### Add column with week day and hour

# In[89]:


def day_of_week(t):
    """
    Get the week day name from a week day integer.
    """
    
    if t == 0:
        return "Monday"
    elif t == 1:
        return "Tuesday"
    elif t == 2:
        return "Wednesday"
    elif t == 3:
        return "Thursday"
    elif t == 4:
        return "Friday"
    elif t == 5:
        return "Saturday"
    elif t == 6:
        return "Sunday"


# In[90]:


df["week_day"] = df.created_at.dt.weekday


# In[91]:


df["week_day_name"] = df["week_day"].apply(day_of_week)


# Or, there is a built-in function in Pandas that gives back the day name:

# In[92]:


df["week_day_name"] = df.created_at.dt.day_name()


# In[93]:


df.head(3)


# #### Add column with day hour

# In[94]:


get_ipython().run_line_magic('pinfo', 'df.created_at.dt')


# In[95]:


df.created_at.dt.hour.head()


# In[96]:


df["day_hour"] = df.created_at.dt.hour


# In[97]:


display_cols = ['created_at', 'week_day', 'day_hour']
df[display_cols].head(4)


# ##### Multiple conditions

# In[98]:


# AND condition with `&`

df[
    (df.week_day_name == 'Saturday') & (df.n_mentions == 0)
].shape


# In[99]:


# Equivalent expression with `query()`

df.query("week_day_name == 'Saturday' and n_mentions == 0").shape


# In[100]:


# OR condition with `|`

df[
    (df.week_day_name == 'Saturday') | (df.n_mentions == 0)
].shape


# ### Aggregation

# In[101]:


df.agg({'n_mentions': ['min', 'max', 'sum']})


# #### Grouping

# In[102]:


group_by_day = df.groupby('week_day')


# In[103]:


# The head of a DataFrameGroupBy consists of the first
# n records for each group (see `help(grp_by_day.head)`)

group_by_day.head(1)


# `agg` is used to pass an aggregation function to be applied to each group resulting from `groupby`.
# 
# Here we are interested in how many tweets there are for each group, so we pass `len()` to an 'aggregate'. This is similar to the `.count()` method.

# In[104]:


group_by_day.agg(len)


# However, we are not interested in having the count for all columns. Rather we want to create a new dataframe with renamed column names.

# In[105]:


group_by_day.agg({'text': len}).rename({'text': 'tweet_count'}, axis='columns')


# ##### By label (column)

# Previously we've added a column indicating on which day of the week a given tweet appeared.

# In[106]:


groupby_result_as_series = df.groupby('day_hour')['text'].count()


# In[107]:


groupby_result_as_series


# In[108]:


groupby_result_as_df = df.groupby('day_hour')[['text']]    .count()    .rename({'text': 'count'}, axis='columns')


# In[109]:


groupby_result_as_df.head()


# ##### By series or dict

# In[110]:


get_ipython().run_line_magic('pinfo', 'df.groupby')


# In[111]:


# here we pass the groups as a series
df.groupby(df.created_at.dt.day).agg({'text':len}).head()


# In[112]:


# here we pass the groups as a series
df.groupby(df.created_at.dt.day)[['text']].count().head()


# In[113]:


df.groupby(df.created_at.dt.hour)[['text']].count().head()


# ##### By multiple labels (columns)

# In[114]:


# Here we group based on the values of two columns
# instead of one

x = df.groupby(['week_day', 'day_hour'])[['text']].count()


# In[115]:


x.head()


# #### Aggregation methods
# 
# **Summary**:
# 
# - `count`: Number of non-NA values
# - `sum`: Sum of non-NA values
# - `mean`: Mean of non-NA values
# - `median`: Arithmetic median of non-NA values
# - `std`, `var`: standard deviation and variance
# - `min`, `max`: Minimum and maximum of non-NA values

# You can also use these in an aggregation functions within a groupby:

# In[116]:


df.groupby('week_day').agg(
    {
        # each key in this dict specifies
        # a given column
        'n_mentions':[
            # the list contains aggregation functions
            # to be applied to this column
            'count',
            'mean',
            'min',
            'max',
            'std',
            'var'
        ]
    }
)


# #### Sorting

# To sort the values of  a dataframe we use its `sort_values` method:
# - `by`: specifies the name of the column to be used for sorting
# - `ascending` (default = `True`): specifies whether the sorting should be *ascending* (A-Z, 0-9) or `descending` (Z-A, 9-0)

# In[117]:


df.sort_values(by='created_at', ascending=True).head()


# In[118]:


df.sort_values(by='n_mentions', ascending=False).head()


# ### Save
# 
# Before continuing with the plotting, let's save our enhanced dataframe, so that we can come back to it without having to redo the same manipulations on it.
# 
# `pandas` provides a number of handy functions to export dataframes in a variety of formats.

# Here we use `.to_pickle()` to serialize the dataframe into a binary format, by using behind the scenes Python's `pickle` library.

# In[119]:


df.to_pickle("stuff/musk_tweets_enhanced.pickle")


# ## Part 2

# In[120]:


df = pd.read_pickle("stuff/musk_tweets_enhanced.pickle")


# ### `describe()`

# The default behavior is to include only column with numerical values

# In[121]:


df.describe()


# A trick to include more values is to exclude the datatype on which it breaks, which in our case is `list`.

# In[122]:


df.describe(exclude=[list])


# In[123]:


df.created_at.describe(datetime_is_numeric=True)


# In[124]:


df['week_day_name'] = df['week_day_name'].astype('category')


# In[125]:


df.describe(exclude=['object'])


# ### Plotting

# In[126]:


# Not needed in newest Pandas version
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt


# #### Histograms
# 
# They are useful to see the distribution of a certain variable in your dataset.

# In[127]:


df.groupby(['n_mentions'])[['text']].count()


# In[128]:


plt.figure(figsize=(10, 6))
plt.hist(df.n_mentions, bins='auto', rwidth=1.0)
plt.title('Distribution of the number of mentions per tweet')
plt.ylabel("Tweets")
plt.xlabel("Mentions (per tweet)")
plt.show()


# In[129]:


plt.figure(figsize=(10, 6))
plt.hist(df.day_hour, bins='auto', rwidth=0.6)
plt.title('Distribution of the number of mentions per tweet')
plt.ylabel("Tweets")
plt.xlabel("Hour of the day")
plt.show()


# In[130]:


df_2017 = df[df.created_at.dt.year == 2017]


# In[131]:


plt.figure(figsize=(10, 6))
plt.hist(df_2017.day_hour, bins='auto', rwidth=0.6)
plt.title('Year 2017')
plt.ylabel("Tweets")
plt.xlabel("Hour of the day")
plt.show()


# So far we have used directly `matplotlib` to generate our plots.
# 
# `pandas`'s dataframes provide some methods that directly call `matplotlib`'s API behind the scenes:
# - `hist()` for histograms
# - `boxplot()` for boxplots
# - `plot()` for other types of plots (specified with e.g. `any='scatter'`)

# By passing the `by` parameter to e.g. `hist()` it is possible to produce one histogram plot of a given variable for each value in another column.

# Let's see how we can plot the number of mentions by year:

# In[132]:


df['year'] = df.created_at.dt.year


# In[133]:


axes = df.hist(column='day_hour', by='year', figsize=(10,10))


# #### Bar charts
# 
# They are useful to plot categorical data.

# In[134]:


get_ipython().run_line_magic('pinfo', 'plt.bar')


# In[135]:


tweets_by_weekday = df.groupby(df.created_at.dt.weekday)[['text']].count()


# In[136]:


week_days = [
    "Mon",
    "Tue",
    "Wed",
    "Thur",
    "Fri",
    "Sat",
    "Sun"
]


# In[137]:


plt.figure(figsize=(8, 6))

# specify the type of plot and the labels
# for the y axis (the bars)
plt.bar(
    tweets_by_weekday.index,
    tweets_by_weekday.text,
    tick_label=week_days,
    width=0.5
)

# give a title to the plot
plt.title('Elon Musk\'s week on Twitter')

# give a label to the axes
plt.ylabel("Number of tweets")
plt.xlabel("Week day")
plt.show()


# #### Box plots
# 
# ```{image} images/eda-boxplot.png
# :alt: edaboxplot
# ```

# ### Outliers, missing values
# 
# An *outlier* is an observation far from the center of mass of the distribution. It might be an error or a genuine observation: this distinction requires domain knowledge. Outliers infuence the outcomes of several statistics and machine learning methods: it is important to decide how to deal with them.
# 
# A *missing value* is an observation without a value. There can be many reasons for a missing value: the value might not exist (hence its absence is informative and it should be left empty) or might not be known (hence the value is existing but missing in the dataset and it should be marked as NA).
# 
# ```{admonition} Tip
# :class: tip
# One way to think about the difference is with this Zen-like koan: An explicit missing value is the presence of an absence; an implicit missing value is the absence of a presence.
# ```

# In[138]:


tweets_by_weekday


# In[139]:


tweets_by_weekday.describe()


# In[140]:


tweets_by_weekday.boxplot()


# In[141]:


get_ipython().run_line_magic('pinfo', 'plt.bar')


# In[142]:


df.head(3)


# In[143]:


df[['day_hour']].describe()


# In[144]:


df[['day_hour']].quantile(.25)


# In[145]:


get_ipython().run_line_magic('pinfo', 'df.boxplot')


# In[146]:


df[['day_hour', 'week_day_name']].boxplot(
    by='week_day_name',
    grid=False,
    figsize=(8,6),
    fontsize=10
)

# give a title to the plot
plt.title('')

# give a label to the axes
plt.xlabel("Day of the week")
plt.show()


# In[147]:


df[['day_hour', 'week_day']].boxplot(
    by='week_day',
    grid=True, # just to show the difference with/without
    figsize=(8,6),
    fontsize=10
)

# give a title to the plot
plt.title('')

# give a label to the axes
plt.xlabel("Day of the week")
plt.show()


# ### Exercise 1.
# 
# * Create a function that calculates the frequency of hashtags in tweets.
# * Test it on toy examples, to make sure it works.
# * Apply it to Elon Musk's tweets.
# * List the top 10 hashtags in the dataset.

# In[148]:


# Your code here.


# ### Exercise 2.
# 
# Read the file `data/adams-hhgttg.txt` and:
# 
# - Count the number of occurrences per distinct word in the text.
# 
# - Create a data frame with two columns: word and counts.
# 
# - Plot the histogram of the word frequencies and think about what is happening.

# In[149]:


# Your code here.


# ---
