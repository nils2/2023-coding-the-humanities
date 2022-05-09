#!/usr/bin/env python
# coding: utf-8

# # Working with Tweets
# 
# In this notebook, we will delve into the analysis of tweet contents.
# 
# We consider the dataset of tweets from Elon Musk, SpaceX and Tesla founder, and ask the following questions:
# * What is Elon most actively tweeting about?
# * Who is Elon most frequently referring to?
# 
# We will explore how to work with the contents of tweets.

# In[1]:


# imports

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Let's get some basics (or a refresher) of working with texts in Python. Texts are sequences of discrete symbols (words or, more generically, tokens).

# ## Import the dataset
# 
# > More info on how to harvest tweets automatically, see Notebook 6. 
# 
# Let us import the Elon Musk's tweets dataset in memory.
# 
# <img src="images/elon_loop.jpeg" width="400px" heigth="400px">

# In[2]:


# Import the dataset using Pandas, and create a data frame

file_path = 'data/elonmusk_tweets.csv'

df_elon = pd.read_csv(file_path, encoding="utf-8")


# In[3]:


df_elon.head(10)


# In[4]:


df_elon.tail(5)


# In[5]:


df_elon.shape  # (number of rows, number of columns)


# In[6]:


tweets = df_elon["text"]
tweets_list = list(tweets)  # convert to Python list

for tweet in tweets_list[:10]:
    print(tweet)


# ## Working with tweet contents

# In[7]:


# import some of the most popular libraries for NLP in Python
import nltk
import string
# import sklearn # for machine learning


# > If it is the first time you run nltk, it could be that you have to download its materials first. You only have to do this once. The error tells you which package needs to be downloaded. 

# In[8]:


# For instance, run this once:
# nltk.download('punkt')


# A typical NLP pipeline might look like the following:
#     
# <img src="images/spacy_pipeline.png" width="600px" heigth="600px">
# 
# * Tokenization: split a text into tokens.
# * Filtering: remove some of the tokens if not needed (e.g., punctuation). If and how to remove is task dependent.
# * Tagger, parser: syntactic structure.
# * NER (Named Entity Recognition): find named entities.
# * ...
# 
# More on this can be found in Notebook 7.
# 

# ### Tokenization: splitting a text into constituent tokens.
# A tokenizer takes a string and outputs a list of tokens.

# In[9]:


# NLTK provides us with a tokenizers for tweets

from nltk.tokenize import TweetTokenizer, word_tokenize

tokenizer = TweetTokenizer(preserve_case=True, reduce_len=False, strip_handles=False)


# In[10]:


example_tweet = df_elon.text[1]
print(example_tweet)


# We compare here two tokenizers: one for general English texts, and one specialized for tweets.

# In[11]:


# This one was defined above and is the 'TweetTokenizer'
result1 = tokenizer.tokenize(example_tweet)
print(result1)

print("\n======\n")

# This is a 'normal' tokenizer
result2 = word_tokenize(example_tweet)
print(result2)


# **Question**: can you spot what the Twitter tokenizer is doing instead of a standard one?

# ### Filtering unnecessary tokens

# In[12]:


string.punctuation


# In[13]:


# Some more pre-processing

tokenizer = TweetTokenizer(preserve_case=True, reduce_len=False, strip_handles=False)

def filter_tweet(tokens):
    """
    Normalize a tweet's text by removing punctuation tokens and URls.
    
    Args:
        tokens (list): List of tokens from a tokenizer
        
    Returns:
        list: List of non-punctuation and URL tokens
    """
    normalized = []
    
    for token in tokens:
        if token in string.punctuation:
            continue
        elif len(token) <= 3:
            continue
        elif token.startswith(('http', 'www')):
            continue
        else:
            normalized.append(token)
  
    return normalized

def tokenize_tweet(tweet, tokenizer=tokenizer):
    
    # This gives a list of tokens
    tokens = tokenizer.tokenize(tweet)
    filtered_tokens = filter_tweet(tokens)
    
    # This returns it back to a string
    normalized_tweet = " ".join(filtered_tokens)
    
    return normalized_tweet


# In[14]:


print(result1)  # recall from some cells above
print("======")
print(filter_tweet(result1))  # the result of our normalization function


# Now, add a column with a normalized version of the `text` column. 
# 
# Let's call it `clean_text`. We get this by applying (using Pandas' `.apply()` method) our just written function on every value of the column. 

# In[15]:


df_elon["clean_text"] = df_elon["text"].apply(tokenize_tweet)


# In[16]:


df_elon.head(5)


# In[17]:


# Save cleaned up version

# df_elon.to_csv("stuff/df_elon.csv", index=False)


# ### Building a dictionary with token occurrences
# 
# We want to build a dictionary of unique tokens, containing the number of times they appear in the corpus.

# In[18]:


from collections import Counter

all_tokens = []  # empty list

for tweet in df_elon["clean_text"]:
    all_tokens += tweet.split()


# In[19]:


all_tokens[:10]


# In[20]:


counter = Counter(all_tokens)


# In[21]:


counter["robots"]


# #### Quiz
# 
# * Find the tokens most used by Elon.
# * Find the Twitter users most referred to by Elon (hint: use the @ handler to spot them).

# In[22]:


# Your code here


# In[23]:


# Your code here


# ---

# ## Data visualization
# 
# The `pandas` methods provide integration with the plotting functionalities provided by the `matplotlib` library.
# 
# This seamless integration – which is very nice! – hides away from users some of the complexities of `matplotlib`.
# 
# However, as there cases where advanced customizations are needed, it's useful to learn the high-level plotting functionalities of `pandas` or `seaborn` as well as being aware of how to perform more advanced customizations by means of `matplotlib`.
# 
# Very useful [`matplotlib` cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf).
# 
# And more information on `Seaborn` here: https://seaborn.pydata.org/

# In[24]:


import numpy as np
import matplotlib.pyplot as plt


# In[25]:


import seaborn as sns

# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(11, 5)})


# Let's plot the number of tweets mentioning one of the top 10 tokens over time.

# In[26]:


df_elon.head(5)


# Right now, the `created_at` column is of type string. Let's convert it to a datetime datatype that can be interpreted as object by Pandas and Python. 
# 

# In[27]:


# Convert the created_at column to datetime

df_elon['created_at'] = pd.to_datetime(df_elon['created_at'])


# In[28]:


df_elon.head(5)


# Visually, nothing has changed. But, since the element in the `created_at` column is now a datetime object, we can ask for separate bits of this datetimestamp, such as the year only:

# In[29]:


# Make a new column with only the year

df_elon["year"] = df_elon['created_at'].dt.year


# In[30]:


df_elon.head()


# Now, make another column that either contains the frequency of the token 'Tesla' in the tweet. 

# You can do this by using pure Python:

# In[31]:


tesla_in_tweet = []

for tweet in df_elon['clean_text']:
    tesla_in_tweet.append(tweet.count('Tesla'))
        
df_elon['tesla_in_tweet'] = tesla_in_tweet


# ... and the variant with a list comprehension:

# In[32]:


tesla_in_tweet = [tweet.count('Tesla') for tweet in df_elon['clean_text']]
df_elon['tesla_in_tweet'] = tesla_in_tweet


# Or, by using a built-in Pandas method:

# In[33]:


df_elon['tesla_in_tweet'] = df_elon['clean_text'].str.count('Tesla')


# The result is yet an extra column:

# In[34]:


df_elon.head(5)


# Then, let's plot this as a bar plot. What we do:
# 1. Group everything by the value in the 'year' column
# 2. Select only the 'tesla_in_tweet' column
# 3. Sum the values (this is done per group [=per year])
# 
# Inspect the result
# 
# 4. Call `.plot(kind='bar')` on the Series.
# 
# What is returned is automatically displayed by Jupyter notebooks

# In[35]:


tesla_per_year = df_elon.groupby('year')['tesla_in_tweet'].sum()
tesla_per_year


# In[36]:


tesla_per_year.plot(kind='bar')


# Alternatively, you can give this Series to Seaborn:

# In[37]:


sns.barplot(x=tesla_per_year.index, y=tesla_per_year.values, color="skyblue")


# Some extra styling, a title and a y-axis label. You can even save the result, for instance as .pdf.

# In[38]:


sns.barplot(x=tesla_per_year.index, y=tesla_per_year.values, color="skyblue")

plt.xlabel("Year", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.title("Number of tweets mentioning Tesla", fontsize=14)
plt.tight_layout()

plt.savefig("stuff/elon_plot.pdf")


# **Another question:** how many tweets are there per month over time? 
# 
# We need to change the index and group. Let's make the datetimestamp the index of our DataFrame. 

# In[39]:


df_elon = df_elon.set_index('created_at')


# In[40]:


df_elon.head(5)


# Pandas has a `Grouper` method that for instance allows you to easily work with datetimestamps. See https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html for some examples. 
# 
# We use it to group per month which we do by specifying `freq='M'`. In steps:
# 1. First, we group by the month using the `pd.Grouper(freq='M'))` method
# 2. Then we count the number of rows per month using `.count()`
# 3. Since we are only interested in the count, we can select any row, for instance 'id'

# In[41]:


tweets_per_month = df_elon.groupby(pd.Grouper(freq='M')).count()['id']
tweets_per_month


# In[42]:


tweets_per_month.plot()


# **Remark**: there is much more to this than plotting. Take a loot at the [Seaborn](https://seaborn.pydata.org/examples/index.html) or [Matplotlib](https://matplotlib.org/gallery.html) galleries for some compelling examples.

# ---

# ### Anatomy of a plot (optional)

# In[43]:


# First we create the figure, which is the 
# container where all plots reside

fig = plt.figure(figsize=(10, 10))

ax1 = fig.add_subplot(2, 2, 1)
plt.plot(np.random.randn(50).cumsum(), 'k--')

ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
plt.show()


# Each plot resides within a `Figure` object.
# 
# Each subsplot resides within an `AxesSubplot` object.

# In[44]:


fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0,1].plot(np.random.randn(50), 'r--')
axes[0,1].plot(np.random.randn(50), 'b--')
axes[1,1].plot(np.random.randn(50), 'k--')
axes[1,0].plot(np.random.randn(50), '.')
axes[0,0].plot(np.random.randn(50), 'y-')
fig.set_size_inches(10, 10)


# ---

# ### Exercise 1.
# 
# With these tweets:
# * Plot the top n words together in a single figure, and show their trends over time.
# * Do the same for the top n users mentioned.

# In[45]:


# Your code here


# ---
