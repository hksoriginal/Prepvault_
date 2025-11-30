bert_pre_train = r"""
# Pretraining in BERT

BERT (Bidirectional Encoder Representations from Transformers) is a powerful language model that uses two major techniques during pretraining:
1. **Masked Language Modeling (MLM)**
2. **Next Sentence Prediction (NSP)**

## 1. Masked Language Modeling (MLM)

In a standard language model, words are predicted in a unidirectional way, i.e., from left to right or right to left. BERT, however, uses a bidirectional approach by predicting words within the context of both left and right surroundings. This is achieved through **Masked Language Modeling (MLM)**, where a percentage of the input tokens are masked randomly, and the model is trained to predict these masked tokens based on their surrounding context.

### How MLM Works:
- During pretraining, 15% of the words in each input sentence are chosen randomly for masking.
  - Out of these chosen words:
    - 80% are replaced with the `[MASK]` token.
    - 10% are replaced with a random word.
    - 10% remain unchanged.
- BERT is then trained to predict these masked words by understanding the context provided by the unmasked words.

This technique enables BERT to learn bidirectional representations of text, capturing context from both directions rather than just one.

## 2. Next Sentence Prediction (NSP)

In addition to word-level predictions, BERT is trained to understand the relationship between sentences. This is where **Next Sentence Prediction (NSP)** comes into play. NSP is a binary classification task where BERT learns whether a second sentence follows a first sentence in a text.

### How NSP Works:
- BERT takes two sentences as input, A and B.
  - 50% of the time, B is the actual next sentence following A (labeled as "IsNext").
  - 50% of the time, B is a random sentence from the corpus (labeled as "NotNext").
- BERT is then trained to predict whether B is the actual next sentence following A.

This helps BERT in tasks that require understanding the relationship between sentences, such as question answering and sentence pair classification.

## Pretraining Objective

The overall objective of BERT’s pretraining is to minimize the combined loss from both MLM and NSP:
- **MLM Loss**: Encourages the model to accurately predict masked tokens within sentences.
- **NSP Loss**: Encourages the model to correctly identify if two sentences are sequentially related.

By using these two pretraining tasks, BERT is able to learn rich language representations that are useful for downstream NLP tasks.

## Summary

- **MLM** allows BERT to understand words in both left and right contexts, enabling bidirectional training.
- **NSP** enables BERT to understand relationships between sentences.
- The combination of these tasks during pretraining makes BERT highly effective for a wide range of NLP applications.

"""
