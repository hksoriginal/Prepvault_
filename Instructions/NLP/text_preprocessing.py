text_preprocessing = r"""
# Text Preprocessing in NLP

Text preprocessing is a crucial step in Natural Language Processing (NLP) as it cleans and prepares raw text for machine learning or deep learning models. It involves transforming text data into a format that algorithms can work with, improving both the quality and efficiency of the model. Below are the main steps involved in text preprocessing:

## 1. Tokenization

**Tokenization** is the process of breaking down a text into individual units, such as words, subwords, or sentences. It helps in reducing large blocks of text into manageable parts. Tokenization can be:
- **Word-level Tokenization:** Splits text by words (e.g., "Hello world!" → ["Hello", "world"]).
- **Sentence-level Tokenization:** Splits text by sentences (e.g., "Hello world! How are you?" → ["Hello world!", "How are you?"]).
- **Subword Tokenization:** Breaks down words into smaller units, which can be helpful for languages with rich morphology.

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello world! How are you?"
# Word-level tokenization
words = word_tokenize(text)
# Sentence-level tokenization
sentences = sent_tokenize(text)

print("Words:", words)
print("Sentences:", sentences)
```

## 2. Lowercasing

Converting text to lowercase helps reduce the size of the vocabulary by making words case-insensitive. For example, "Machine" and "machine" would be treated as the same word. However, some applications may require preserving capitalization, especially if the case conveys meaning (e.g., proper nouns).

```python
text = "Hello World!"
lower_text = text.lower()
print("Lowercased Text:", lower_text)
```

## 3. Removing Punctuation

Punctuation like commas, periods, and question marks are often removed as they don't contribute to the meaning in many NLP tasks. However, in some tasks, such as sentiment analysis, punctuation can convey emotion (e.g., "Wow!"). The decision to remove punctuation depends on the application.
```python
import string

text = "Hello, world!"
no_punct_text = text.translate(str.maketrans("", "", string.punctuation))
print("Without Punctuation:", no_punct_text)
```


## 4. Removing Stop Words

Stop words are common words (e.g., "the", "and", "is") that are often removed because they do not carry significant meaning. Removing stop words helps reduce noise and focuses on words that matter more in context. However, for some tasks, stop words may be kept if they contribute to the meaning (e.g., in language translation).

```python
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words("english"))

text = "This is a sample sentence with some common words."
filtered_words = [word for word in word_tokenize(text) if word.lower() not in stop_words]
print("Without Stop Words:", filtered_words)
```

## 5. Stemming and Lemmatization

Both techniques reduce words to their base or root form:
- **Stemming:** Cuts off prefixes or suffixes to get the root form. It is a crude heuristic process that can lead to non-standard words. For example, "running" → "run".

```python
from nltk.stem import PorterStemmer

ps = PorterStemmer()
text = "running runner runs"
stemmed_words = [ps.stem(word) for word in word_tokenize(text)]
print("Stemmed Words:", stemmed_words)
```

- **Lemmatization:** Converts words to their base or dictionary form (lemma). It uses vocabulary and morphological analysis, ensuring the root word is meaningful. For example, "running" → "run".

```python
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
text = "running runner runs"
lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in word_tokenize(text)]
print("Lemmatized Words:", lemmatized_words)

```

## 6. Removing Special Characters and Numbers

Special characters (e.g., "@", "#", "$") and numbers are often removed as they may not be useful in text analysis. However, in some contexts, numbers or specific symbols may hold meaning (e.g., dates, product IDs), so this step is task-dependent.

```python
import re

text = "Hello @world! The price is $100 #exciting"
cleaned_text = re.sub(r"[^a-zA-Z\s]", "", text)
print("Without Special Characters and Numbers:", cleaned_text)
```

## 7. Handling Emojis and Emoticons

Emojis and emoticons can convey sentiment and emotion, so they might be converted to text descriptions (e.g., "😊" → "happy"). For sentiment analysis, this step can provide valuable insights.

```python
import emoji

text = "I love pizza 😊"
emoji_text = emoji.demojize(text)
print("With Emojis Converted:", emoji_text)

```

## 8. Text Normalization

**Normalization** involves converting text into a consistent format. This includes expanding contractions (e.g., "can't" → "cannot") and correcting spelling variations. This step helps standardize the text and improves model performance.

```python
from contractions import fix

text = "I can't believe it's already 2024!"
normalized_text = fix(text)
print("Normalized Text:", normalized_text)

```

## 9. Vectorization

After cleaning and normalizing text, it needs to be converted into numerical format for modeling. Common methods include:
- **Bag of Words (BoW):** Represents text as a vector of word frequencies or occurrences.
```python
from sklearn.feature_extraction.text import CountVectorizer

text = ["This is a sample text", "Text preprocessing is important"]
vectorizer = CountVectorizer()
bow = vectorizer.fit_transform(text)
print("Bag of Words:\n", bow.toarray())
print("Feature Names:", vectorizer.get_feature_names_out())

```
- **TF-IDF (Term Frequency-Inverse Document Frequency):** Weights words based on their importance in the document relative to the corpus.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(text)
print("TF-IDF:\n", tfidf.toarray())
print("Feature Names:", vectorizer.get_feature_names_out())

```
- **Word Embeddings:** Pretrained embeddings (e.g., Word2Vec, GloVe) capture semantic meaning by representing words in dense vectors.
```python
from gensim.models import Word2Vec

sentences = [word_tokenize("This is a sample sentence"),
             word_tokenize("Text preprocessing is essential")]
word2vec_model = Word2Vec(sentences, vector_size=10, min_count=1, window=5)
print("Word2Vec Embedding for 'text':", word2vec_model.wv["text"])

```
- **Contextual Embeddings:** Models like BERT and GPT create embeddings that capture context-sensitive meaning.
```python
from transformers import BertTokenizer, BertModel
import torch

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")
text = "This is a sample sentence."

# Tokenize and convert to input IDs
input_ids = tokenizer.encode(text, return_tensors="pt")
# Get embeddings
outputs = model(input_ids)
last_hidden_states = outputs.last_hidden_state
print("BERT Embedding Shape:", last_hidden_states.shape)

```
## Conclusion

Each step of text preprocessing enhances the quality of data fed into an NLP model, which can lead to better performance and insights. The choice of preprocessing steps depends on the NLP task, domain, and model requirements.
"""
