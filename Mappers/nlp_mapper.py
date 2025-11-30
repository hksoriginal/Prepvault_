
from Instructions.NLP.tokenization import tokenization_markdown
from Instructions.NLP.text_preprocessing import text_preprocessing
from Instructions.NLP.word_embedding import word_embedding
from Instructions.NLP.bert_arch import bert_arch
from Instructions.NLP.bert_pre_train import bert_pre_train
from Instructions.NLP.fine_tuning import finetuning_bert


NLP_CONCEPTS_MAPPER = {
    "Tokenization": [
        tokenization_markdown,
        [],
        "https://www.youtube.com/results?search_query=tokenization+in+nlp"
    ],
    "Text Preprocessing": [
        text_preprocessing,
        [],
        "https://www.youtube.com/results?search_query=tokenization+in+nlp"
    ],
    "Word Embedding": [
        word_embedding,
        [],
        "https://www.youtube.com/results?search_query=word+embedding+in+nlp"
    ],

}


BERT_MAPPER = {
    "Architecture": [
        bert_arch,
        [
            "./Instructions/NLP/BERT.jpg"
        ],
        "https://www.youtube.com/results?search_query=bert+architecture"
    ],
    "Pretraining in BERT": [
        bert_pre_train,
        [
            "./Instructions/NLP/pre_train.png"
        ],
        "https://www.youtube.com/results?search_query=bert+pretraining"
    ],
    "Fine Tuning in BERT": [
        finetuning_bert,
        [
            "./Instructions/NLP/fine_tuning.png"
        ],
        "https://www.youtube.com/results?search_query=bert+fine+tuning"
    ],
}
