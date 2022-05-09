---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Working with Tweets

In this notebook, we will delve into the analysis of tweet contents.

We consider the dataset of tweets from Elon Musk, SpaceX and Tesla founder, and ask the following questions:
* What is Elon most actively tweeting about?
* Who is Elon most frequently referring to?

We will explore how to work with the contents of tweets.

```{code-cell} ipython3
# imports

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
```

Let's get some basics (or a refresher) of working with texts in Python. Texts are sequences of discrete symbols (words or, more generically, tokens).

+++

## Import the dataset

```{note}
More info on how to harvest tweets automatically, see Notebook 6. 
```

Let us import the Elon Musk's tweets dataset in memory.

```{image} images/elon_loop.jpeg
:alt: elon
```

```{code-cell} ipython3
# Import the dataset using Pandas, and create a data frame

file_path = 'data/elonmusk_tweets.csv'

df_elon = pd.read_csv(file_path, encoding="utf-8")
```

```{code-cell} ipython3
df_elon.head(10)
```

```{code-cell} ipython3
df_elon.tail(5)
```

```{code-cell} ipython3
df_elon.shape  # (number of rows, number of columns)
```

```{code-cell} ipython3
tweets = df_elon["text"]
tweets_list = list(tweets)  # convert to Python list

for tweet in tweets_list[:10]:
    print(tweet)
```

## Working with tweet contents

```{code-cell} ipython3
# import some of the most popular libraries for NLP in Python
import nltk
import string
# import sklearn # for machine learning
```

```{admonition} Tip
:class: tip
If it is the first time you run nltk, it could be that you have to download its materials first. You only have to do this once. The error tells you which package needs to be downloaded. 
```


```{code-cell} ipython3
# For instance, run this once:
# nltk.download('punkt')
```

A typical NLP pipeline might look like the following:
    
```{image} images/spacy_pipeline.png
:alt: spacypipeline
```

* Tokenization: split a text into tokens.
* Filtering: remove some of the tokens if not needed (e.g., punctuation). If and how to remove is task dependent.
* Tagger, parser: syntactic structure.
* NER (Named Entity Recognition): find named entities.
* ...

More on this can be found in Notebook 7.

+++

### Tokenization: splitting a text into constituent tokens.
A tokenizer takes a string and outputs a list of tokens.

```{code-cell} ipython3
# NLTK provides us with a tokenizers for tweets

from nltk.tokenize import TweetTokenizer, word_tokenize

tokenizer = TweetTokenizer(preserve_case=True, reduce_len=False, strip_handles=False)
```

```{code-cell} ipython3
example_tweet = df_elon.text[1]
print(example_tweet)
```

We compare here two tokenizers: one for general English texts, and one specialized for tweets.

```{code-cell} ipython3
# This one was defined above and is the 'TweetTokenizer'
result1 = tokenizer.tokenize(example_tweet)
print(result1)

print("\n======\n")

# This is a 'normal' tokenizer
result2 = word_tokenize(example_tweet)
print(result2)
```

**Question**: can you spot what the Twitter tokenizer is doing instead of a standard one?

+++

### Filtering unnecessary tokens

```{code-cell} ipython3
string.punctuation
```

```{code-cell} ipython3
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
```

```{code-cell} ipython3
print(result1)  # recall from some cells above
print("======")
print(filter_tweet(result1))  # the result of our normalization function
```

Now, add a column with a normalized version of the `text` column. 

Let's call it `clean_text`. We get this by applying (using Pandas' `.apply()` method) our just written function on every value of the column. 

```{code-cell} ipython3
df_elon["clean_text"] = df_elon["text"].apply(tokenize_tweet)
```

```{code-cell} ipython3
df_elon.head(5)
```

```{code-cell} ipython3
# Save cleaned up version

# df_elon.to_csv("stuff/df_elon.csv", index=False)
```

### Building a dictionary with token occurrences

We want to build a dictionary of unique tokens, containing the number of times they appear in the corpus.

```{code-cell} ipython3
from collections import Counter

all_tokens = []  # empty list

for tweet in df_elon["clean_text"]:
    all_tokens += tweet.split()
```

```{code-cell} ipython3
all_tokens[:10]
```

```{code-cell} ipython3
counter = Counter(all_tokens)
```

```{code-cell} ipython3
counter["robots"]
```

#### Quiz

* Find the tokens most used by Elon.
* Find the Twitter users most referred to by Elon 

```{admonition} Tip
:class: tip
Use the @ handler to spot users.
```

```{code-cell} ipython3
# Your code here
```

```{code-cell} ipython3
# Your code here
```

---

+++

## Data visualization

The `pandas` methods provide integration with the plotting functionalities provided by the `matplotlib` library.

This seamless integration – which is very nice! – hides away from users some of the complexities of `matplotlib`.

However, as there cases where advanced customizations are needed, it's useful to learn the high-level plotting functionalities of `pandas` or `seaborn` as well as being aware of how to perform more advanced customizations by means of `matplotlib`.

Very useful [`matplotlib` cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf).

And more information on `Seaborn` here: https://seaborn.pydata.org/

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
import seaborn as sns

# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(11, 5)})
```

Let's plot the number of tweets mentioning one of the top 10 tokens over time.

```{code-cell} ipython3
df_elon.head(5)
```

Right now, the `created_at` column is of type string. Let's convert it to a datetime datatype that can be interpreted as object by Pandas and Python. 

```{code-cell} ipython3
# Convert the created_at column to datetime

df_elon['created_at'] = pd.to_datetime(df_elon['created_at'])
```

```{code-cell} ipython3
df_elon.head(5)
```

Visually, nothing has changed. But, since the element in the `created_at` column is now a datetime object, we can ask for separate bits of this datetimestamp, such as the year only:

```{code-cell} ipython3
# Make a new column with only the year

df_elon["year"] = df_elon['created_at'].dt.year
```

```{code-cell} ipython3
df_elon.head()
```

Now, make another column that either contains the frequency of the token 'Tesla' in the tweet. 

+++

You can do this by using pure Python:

```{code-cell} ipython3
tesla_in_tweet = []

for tweet in df_elon['clean_text']:
    tesla_in_tweet.append(tweet.count('Tesla'))
        
df_elon['tesla_in_tweet'] = tesla_in_tweet
```

... and the variant with a list comprehension:

```{code-cell} ipython3
tesla_in_tweet = [tweet.count('Tesla') for tweet in df_elon['clean_text']]
df_elon['tesla_in_tweet'] = tesla_in_tweet
```

Or, by using a built-in Pandas method:

```{code-cell} ipython3
df_elon['tesla_in_tweet'] = df_elon['clean_text'].str.count('Tesla')
```

The result is yet an extra column:

```{code-cell} ipython3
df_elon.head(5)
```

Then, let's plot this as a bar plot. What we do:
1. Group everything by the value in the 'year' column
2. Select only the 'tesla_in_tweet' column
3. Sum the values (this is done per group [=per year])

Inspect the result

4. Call `.plot(kind='bar')` on the Series.

What is returned is automatically displayed by Jupyter notebooks

```{code-cell} ipython3
tesla_per_year = df_elon.groupby('year')['tesla_in_tweet'].sum()
tesla_per_year
```

```{code-cell} ipython3
tesla_per_year.plot(kind='bar')
```

Alternatively, you can give this Series to Seaborn:

```{code-cell} ipython3
sns.barplot(x=tesla_per_year.index, y=tesla_per_year.values, color="skyblue")
```

Some extra styling, a title and a y-axis label. You can even save the result, for instance as .pdf.

```{code-cell} ipython3
sns.barplot(x=tesla_per_year.index, y=tesla_per_year.values, color="skyblue")

plt.xlabel("Year", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.title("Number of tweets mentioning Tesla", fontsize=14)
plt.tight_layout()

plt.savefig("stuff/elon_plot.pdf")
```

**Another question:** how many tweets are there per month over time? 

We need to change the index and group. Let's make the datetimestamp the index of our DataFrame. 

```{code-cell} ipython3
df_elon = df_elon.set_index('created_at')
```

```{code-cell} ipython3
df_elon.head(5)
```

Pandas has a `Grouper` method that for instance allows you to easily work with datetimestamps. See https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html for some examples. 

We use it to group per month which we do by specifying `freq='M'`. In steps:
1. First, we group by the month using the `pd.Grouper(freq='M'))` method
2. Then we count the number of rows per month using `.count()`
3. Since we are only interested in the count, we can select any row, for instance 'id'

```{code-cell} ipython3
tweets_per_month = df_elon.groupby(pd.Grouper(freq='M')).count()['id']
tweets_per_month
```

```{code-cell} ipython3
tweets_per_month.plot()
```

**Remark**: there is much more to this than plotting. Take a loot at the [Seaborn](https://seaborn.pydata.org/examples/index.html) or [Matplotlib](https://matplotlib.org/gallery.html) galleries for some compelling examples.

+++

---

+++

### Anatomy of a plot (optional)

```{code-cell} ipython3
# First we create the figure, which is the 
# container where all plots reside

fig = plt.figure(figsize=(10, 10))

ax1 = fig.add_subplot(2, 2, 1)
plt.plot(np.random.randn(50).cumsum(), 'k--')

ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
plt.show()
```

Each plot resides within a `Figure` object.

Each subsplot resides within an `AxesSubplot` object.

```{code-cell} ipython3
fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0,1].plot(np.random.randn(50), 'r--')
axes[0,1].plot(np.random.randn(50), 'b--')
axes[1,1].plot(np.random.randn(50), 'k--')
axes[1,0].plot(np.random.randn(50), '.')
axes[0,0].plot(np.random.randn(50), 'y-')
fig.set_size_inches(10, 10)
```

---

+++

### Exercise 1.

With these tweets:
* Plot the top n words together in a single figure, and show their trends over time.
* Do the same for the top n users mentioned.

```{code-cell} ipython3
# Your code here
```

---
