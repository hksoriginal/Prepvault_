word_embedding = r"""
# Word Embeddings in Natural Language Processing (NLP)

Word embeddings are a type of word representation used in NLP that allow words to be represented as vectors of real numbers. These vectors capture the semantic meaning of words based on their context in a corpus, allowing machines to understand relationships between words.

## What are Word Embeddings?

In traditional NLP, words were represented as unique indices or one-hot vectors, where each word was represented by a vector with a 1 in the position corresponding to the word and 0s elsewhere. However, this method doesn't capture any information about the relationships between words. Word embeddings, on the other hand, represent words as dense vectors in a continuous vector space, where semantically similar words are mapped to nearby points.

### Example:
- In a one-hot encoding, the word "cat" might be represented as a vector like `[0, 0, 1, 0]`, while "dog" would be `[0, 0, 0, 1]`. These vectors do not capture any similarity between "cat" and "dog."
- In contrast, with word embeddings, "cat" and "dog" would have similar vectors because they share similar meanings, e.g., `[0.25, -0.67, 0.89]` for "cat" and `[0.24, -0.65, 0.87]` for "dog."

## Why are Word Embeddings Important?

Word embeddings help capture syntactic and semantic relationships between words, which makes them more useful in NLP tasks. Some key advantages include:
- **Capturing semantic similarity:** Words with similar meanings (e.g., "cat" and "dog") are represented by similar vectors.
- **Handling polysemy:** Words with multiple meanings can have different representations depending on the context in which they appear.
- **Dimensionality reduction:** Word embeddings reduce the high-dimensionality of word representations compared to one-hot vectors, making computations more efficient.

## How Word Embeddings are Learned

Word embeddings are typically learned using neural networks and large text corpora. Popular algorithms for learning word embeddings include:

1. **Word2Vec (Skip-gram and CBOW)**:
   - **Skip-gram**: Trains a model to predict context words given a target word.
   
```python
   # Import the required libraries
from gensim.models import Word2Vec

# Sample corpus: a list of sentences, each sentence is a list of words
sentences = [
    ["dog", "barks"],
    ["cat", "meows"],
    ["dog", "chases", "cat"],
    ["cat", "chases", "mouse"],
    ["dog", "is", "friendly"],
    ["mouse", "runs", "fast"]
]

# Initialize and train the Word2Vec model
model = Word2Vec(sentences, vector_size=10, window=3, min_count=1, workers=4)

# Print the word vector for the word 'dog'
dog_vector = model.wv['dog']
print(f"Word vector for 'dog':\n{dog_vector}\n")

# Find the most similar words to 'dog'
similar_words = model.wv.most_similar('dog', topn=3)
print("Most similar words to 'dog':")
for word, similarity in similar_words:
    print(f"{word}: {similarity}")

   ```
   - **Continuous Bag of Words (CBOW)**: Trains a model to predict the target word given its context words.

   ```python
   # Import the required libraries
from gensim.models import Word2Vec

# Sample corpus: a list of tokenized sentences (each sentence is a list of words)
sentences = [
    ["dog", "barks"],
    ["cat", "meows"],
    ["dog", "chases", "cat"],
    ["cat", "chases", "mouse"],
    ["dog", "is", "friendly"],
    ["mouse", "runs", "fast"]
]

# Initialize and train the Word2Vec model using CBOW (Continuous Bag of Words)
# 'sg=0' specifies that we are using CBOW (skip-gram is sg=1)
model = Word2Vec(sentences, vector_size=10, window=3, min_count=1, workers=4, sg=0)

# Print the word vector for the word 'dog'
dog_vector = model.wv['dog']
print(f"Word vector for 'dog':\n{dog_vector}\n")

# Find the most similar words to 'dog'
similar_words = model.wv.most_similar('dog', topn=3)
print("Most similar words to 'dog':")
for word, similarity in similar_words:
    print(f"{word}: {similarity}")

   ```
2. **GloVe (Global Vectors for Word Representation)**:
   - Instead of using a predictive approach like Word2Vec, GloVe is based on matrix factorization methods, where the co-occurrence matrix of words is factorized to find word vectors.

```python
# Import required libraries
import numpy as np
from glove import Glove
from glove import Corpus

# Step 1: Prepare the corpus (tokenized text data)
# This is a small sample corpus of sentences
sentences = [
    ["dog", "barks"],
    ["cat", "meows"],
    ["dog", "chases", "cat"],
    ["cat", "chases", "mouse"],
    ["dog", "is", "friendly"],
    ["mouse", "runs", "fast"]
]

# Step 2: Build the Corpus object from the tokenized sentences
corpus = Corpus()
corpus.fit(sentences, window=3)

# Step 3: Train the GloVe model
glove = Glove(no_components=10, learning_rate=0.05)
glove.fit(corpus.matrix, epochs=30, no_threads=4, verbose=True)

# Step 4: Add the word vectors to the model
glove.add_dictionary(corpus.dictionary)

# Step 5: Print the word vector for the word 'dog'
dog_vector = glove.word_vectors[glove.dictionary['dog']]
print(f"Word vector for 'dog':\n{dog_vector}\n")

# Step 6: Find most similar words to 'dog'
similar_words = glove.most_similar('dog', number=3)
print("Most similar words to 'dog':")
for word, similarity in similar_words:
    print(f"{word}: {similarity}")

```

3. **FastText**:
   - An extension of Word2Vec that represents words as bags of character n-grams. This allows it to better handle out-of-vocabulary words by looking at subword information.

4. **ELMo, BERT, GPT**:
   - These are contextual embeddings, meaning the representation of a word depends on the entire context in which it appears. They are pre-trained using large corpora and fine-tuned on specific NLP tasks.

## Applications of Word Embeddings

Word embeddings are used in many NLP applications, including:
- **Sentiment Analysis**: Understanding the sentiment behind a text by analyzing the relationships between words.
- **Machine Translation**: Translating text from one language to another by mapping similar words in different languages.
- **Named Entity Recognition (NER)**: Identifying proper names and entities in a text.
- **Text Classification**: Categorizing text into predefined labels.
- **Word Similarity**: Identifying words with similar meanings.

## Evaluating Word Embeddings

Word embeddings can be evaluated in two main ways:
1. **Intrinsic Evaluation**: Testing how well the embeddings perform on tasks like word similarity or analogy tasks. For example, the well-known "king - man + woman = queen" analogy.
2. **Extrinsic Evaluation**: Testing how well embeddings perform on downstream NLP tasks like sentiment analysis or named entity recognition.

## Conclusion

Word embeddings have revolutionized NLP by providing a more efficient and semantically meaningful representation of words. Through continuous learning from vast amounts of text data, word embeddings have become foundational to most modern NLP models and applications.

"""
