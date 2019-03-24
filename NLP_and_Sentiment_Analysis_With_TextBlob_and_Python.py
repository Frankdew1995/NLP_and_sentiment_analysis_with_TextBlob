
# coding: utf-8

# # NLP_and_Sentiment_Analysis_With_TextBlob

# In[81]:


from textblob import TextBlob
import nltk


# Install "brown" and "wordnet" using NLTK:

# In[82]:


nltk.download("wordnet")
nltk.download("brown")


# ### sample text data: zen of Python

# In[76]:


text1 = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Errors should never pass silently.'''


# ## 1. Create a TextBlob object

# In[77]:


blob = TextBlob(text1)


# ## 2. noun_phrases

# In[78]:


blob.noun_phrases


# ## 3. Sentiment Analysis

# Access the polarity and subjectivity of a TextBlob object via returned named tuple. 

# In[85]:


polarity = blob.sentiment[0]

subjectivity = blob.sentiment[1]

print(polarity, subjectivity)


# Or the following will also work:

# In[84]:


polarity = blob.polarity
subjectivity = blob.subjectivity

print(polarity, subjectivity)


# ## 4. Tokenization

# Tokenization is a NLP technique to split text data into list of single words or sentences. 

# In[65]:


blob.words


# In[66]:


blob.sentences


# ## 5. Words Lemmatization

# **lemmatization is a NLP technique to reduce inflectional or derivational forms of a word to be the base form so that they can be analyzed as one single word**
# 
# Examples of lemmatization: 
# 
# **
# went > go
# gone > go
# organizes > organize
# organized > organize
# **

# In[74]:



# import textblob Word object
from textblob import Word


word = "organizes"

word1 = "went" 


# Convert a Python string to a textblob Word()
blob_word = Word(word)

print(blob_word.lemmatize("v"))
print(Word(word1).lemmatize("v"))


# ## 6. Spell Check

# In[73]:


blob = TextBlob("My spellin is aways corect")


# Unfortunately only 50% accuracy. You will need a ML model to train for a better accuracy

# In[72]:


blob.correct() 


# ## 7. Translation

# In[63]:


blob = TextBlob("Beautiful is better than ugly. Explicit is better than implicit.")


# In[64]:



# Translate to German from English
blob.translate(to="de")

