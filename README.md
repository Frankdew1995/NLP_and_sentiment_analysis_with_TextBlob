---
title: "Natural Language Processing and sentiment analysis with TextBlob: a Python NLP library"
date: 2019-03-24
draft: False
---


## What is NLP(Natural Language Processing)?

### Natural language processing (NLP) is a subfield of computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data. (Wikepedia)

## Dependency to install:

**$ pip install textblob**

<img src="https://textblob.readthedocs.io/en/dev/_static/textblob-logo.png"
     alt="Markdown Monster icon"
     style="margin-right: 10px; height: 300px; width: 350px;" />


## Some features of TextBlob:
  1. Noun Phrase Extraction
  2. Sentiment Analysis
  3. Tokenization
  4. Words Lemmatization
  5. Spell Check
  6. Translation




  # NLP_and_Sentiment_Analysis_With_TextBlob


  ```python
  from textblob import TextBlob
  import nltk
  ```

  Install "brown" and "wordnet" using NLTK:


  ```python
  nltk.download("wordnet")
  nltk.download("brown")
  ```

      [nltk_data] Downloading package wordnet to /Users/frankdu/nltk_data...
      [nltk_data]   Package wordnet is already up-to-date!
      [nltk_data] Downloading package brown to /Users/frankdu/nltk_data...
      [nltk_data]   Package brown is already up-to-date!





      True



  ### sample text data: zen of Python


  ```python
  text1 = '''
  Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.
  Complex is better than complicated.
  Flat is better than nested.
  Sparse is better than dense.
  Readability counts.
  Errors should never pass silently.'''
  ```

  ## 1. Create a TextBlob object


  ```python
  blob = TextBlob(text1)
  ```

  ## 2. noun_phrases


  ```python
  blob.noun_phrases
  ```




      WordList(['beautiful', 'explicit', 'simple', 'complex', 'flat', 'sparse', 'readability', 'errors'])



  ## 3. Sentiment Analysis

  Access the polarity and subjectivity of a TextBlob object via returned named tuple.


  ```python
  polarity = blob.sentiment[0]

  subjectivity = blob.sentiment[1]

  print(polarity, subjectivity)
  ```

      0.14464285714285716 0.5272959183673469


  Or the following will also work:


  ```python
  polarity = blob.polarity
  subjectivity = blob.subjectivity

  print(polarity, subjectivity)
  ```

      0.14464285714285716 0.5272959183673469


  ## 4. Tokenization

  Tokenization is a NLP technique to split text data into list of single words or sentences.


  ```python
  blob.words
  ```




      WordList(['Beautiful', 'is', 'better', 'than', 'ugly', 'Explicit', 'is', 'better', 'than', 'implicit'])




  ```python
  blob.sentences
  ```




      [Sentence("Beautiful is better than ugly."),
       Sentence("Explicit is better than implicit.")]



  ## 5. Words Lemmatization

  **lemmatization is a NLP technique to reduce inflectional or derivational forms of a word to be the base form so that they can be analyzed as one single word**

  Examples of lemmatization:

  **
  went > go
  gone > go
  organizes > organize
  organized > organize
  **


  ```python

  # import textblob Word object
  from textblob import Word


  word = "organizes"

  word1 = "went"


  # Convert a Python string to a textblob Word()
  blob_word = Word(word)

  print(blob_word.lemmatize("v"))
  print(Word(word1).lemmatize("v"))
  ```

      organize
      go


  ## 6. Spell Check


  ```python
  blob = TextBlob("My spellin is aways corect")
  ```

  Unfortunately only 50% accuracy. You will need a ML model to train for a better accuracy


  ```python
  blob.correct()
  ```




      TextBlob("By spelling is away correct")



  ## 7. Translation


  ```python
  blob = TextBlob("Beautiful is better than ugly. Explicit is better than implicit.")
  ```


  ```python

  # Translate to German from English
  blob.translate(to="de")
  ```




      TextBlob("Schön ist besser als hässlich. Explicit ist besser als implizit.")
