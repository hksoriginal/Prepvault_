from Instructions.Deep_Learning.ANN.neuron import neuron_explanation
from Instructions.Deep_Learning.ANN.perceptron import perceptron_explanation
from Instructions.Deep_Learning.ANN.mlp import mlp_explanation
from Instructions.Deep_Learning.ANN.ann import ann_markdown_text
from Instructions.Deep_Learning.Basic_Concepts.optimizers import optimizers_markdown_code
from Instructions.Deep_Learning.Basic_Concepts.loss_functions import loss_functions_markdown
from Instructions.Deep_Learning.Basic_Concepts.activation_functions import activation_function_markdown
from Instructions.Deep_Learning.CNN.cnn import cnn_markdown
from Instructions.Deep_Learning.CNN.batch_norm import batch_normalization_markdown
from Instructions.Deep_Learning.CNN.strides import strides_markdown
from Instructions.Deep_Learning.CNN.pooling import pooling_markdown
from Instructions.Deep_Learning.CNN.padding import padding_markdown
from Instructions.Deep_Learning.CNN.dropout import dropout_markdown
from Instructions.Deep_Learning.CNN.flatten import flatten_markdown
from Instructions.Deep_Learning.RNN.rnn import rnn_explanation
from Instructions.Deep_Learning.RNN.lstm import lstm_explanation
from Instructions.Deep_Learning.RNN.gru import gru_markdown
from Instructions.Deep_Learning.TRANSFORMERS.transformers import transformer_architecture_markdown
from Instructions.Deep_Learning.TRANSFORMERS.encoder_decoder import encoder_decoder_markdown_code
from Instructions.Deep_Learning.TRANSFORMERS.attention import attention_mechanism

DL_CONCEPTS_MAPPER = {
    "Optimizers": [
        optimizers_markdown_code,
        [
            "./Instructions/Deep_Learning/Basic_Concepts/sdg.png",
            "./Instructions/Deep_Learning/Basic_Concepts/momentum.png",
            "./Instructions/Deep_Learning/Basic_Concepts/nag.png",
            "./Instructions/Deep_Learning/Basic_Concepts/adagrad.png",
            "./Instructions/Deep_Learning/Basic_Concepts/rmsprop.png",
        ],
        "https://www.youtube.com/results?search_query=Optimizers+in+deep+learning"
    ],
    "Loss Functions": [
        loss_functions_markdown,
        [],
        "https://www.youtube.com/results?search_query=loss+function+in+deep+learning"
    ],
    "Activation Functions": [
        activation_function_markdown,
        [
            "./Instructions/Deep_Learning/Basic_Concepts/sigmoid.png",
            "./Instructions/Deep_Learning/Basic_Concepts/tanh.png",
            "./Instructions/Deep_Learning/Basic_Concepts/relu.png",
            "./Instructions/Deep_Learning/Basic_Concepts/leaky.png",
            "./Instructions/Deep_Learning/Basic_Concepts/prelu.png",
            "./Instructions/Deep_Learning/Basic_Concepts/ELU.png",
            "./Instructions/Deep_Learning/Basic_Concepts/swish.png",
            "./Instructions/Deep_Learning/Basic_Concepts/softmax.png",
        ],
        "https://www.youtube.com/results?search_query=activation+functions+in+deep+learning"
    ],

}

ANN_MAPPER = {
    "Neuron": [
        neuron_explanation,
        "./Instructions/Deep_Learning/ANN/neuron.png",
        "https://www.youtube.com/results?search_query=Neuron+in+deep+learning"
    ],
    "Perceptron": [
        perceptron_explanation,
        "./Instructions/Deep_Learning/ANN/perceptron.png",
        "https://www.youtube.com/results?search_query=perceptron+in+deep+learning"
    ],
    "Multi Layer Perceptron (MLP)": [
        mlp_explanation,
        "./Instructions/Deep_Learning/ANN/mlp.png",
        "https://www.youtube.com/results?search_query=MLP+in+deep+learning"
    ],
    "Artificial Neural Networks (ANN)": [
        ann_markdown_text,
        "./Instructions/Deep_Learning/ANN/ann.png",
        "https://www.youtube.com/results?search_query=ANN+in+deep+learning"
    ],
}


CNN_MAPPER = {
    "Convolutional Neural Network (CNN)": [
        cnn_markdown,
        "./Instructions/Deep_Learning/CNN/cnn.png",
        "https://www.youtube.com/results?search_query=CNN++in+deep+learning"
    ],
    "Batch Normalization": [
        batch_normalization_markdown,
        "./Instructions/Deep_Learning/CNN/batch_norm.png",
        "https://www.youtube.com/results?search_query=batch+normalization+in+deep+learning"
    ],
    "Strides": [
        strides_markdown,
        "./Instructions/Deep_Learning/CNN/strides.png",
        "https://www.youtube.com/results?search_query=stride+in+deep+learning"
    ],
    "Pooling": [
        pooling_markdown,
        "./Instructions/Deep_Learning/CNN/pooling.png",
        "https://www.youtube.com/results?search_query=pooling+in+deep+learning"
    ],
    "Padding": [
        padding_markdown,
        "./Instructions/Deep_Learning/CNN/padding.png",
        "https://www.youtube.com/results?search_query=padding+in+deep+learning"
    ],
    "Dropout": [
        dropout_markdown,
        "./Instructions/Deep_Learning/CNN/dropout.png",
        "https://www.youtube.com/results?search_query=dropout+in+deep+learning"
    ],
    "Flatten": [
        flatten_markdown,
        "./Instructions/Deep_Learning/CNN/flatten.png",
        "https://www.youtube.com/results?search_query=flatten+in+deep+learning"
    ],
}

RNN_MAPPER = {
    "Recurrent Neural Network (RNN)": [
        rnn_explanation,
        "./Instructions/Deep_Learning/RNN/rnn.png",
        "https://www.youtube.com/results?search_query=RNN+in+deep+learning"
    ],
    "Long Short-Term Memory (LSTM)": [
        lstm_explanation,
        "./Instructions/Deep_Learning/RNN/rnn.png",
        "https://www.youtube.com/results?search_query=LSTM+in+deep+learning"
    ],
    "Gated Recurrent Units (GRU)": [
        gru_markdown,
        "./Instructions/Deep_Learning/RNN/gru.png",
        "https://www.youtube.com/results?search_query=GRU+in+deep+learning"
    ],
}


TRANSFORMERS_MAPPER = {
    "Transformers": [
        transformer_architecture_markdown,
        "./Instructions/Deep_Learning/TRANSFORMERS/transformers.png",
        "https://www.youtube.com/results?search_query=RNN+in+deep+learning"
    ],
    "Attention": [
        attention_mechanism,
        "./Instructions/Deep_Learning/TRANSFORMERS/attention.png",
        "https://www.youtube.com/results?search_query=attention+in+transformer+"
    ],
    "Encoder Decoder": [
        encoder_decoder_markdown_code,
        "./Instructions/Deep_Learning/TRANSFORMERS/encoder_decoder.png",
        "https://www.youtube.com/results?search_query=encoder+and+decoder+in+transformer+"
    ],
}


TRANSFORMERS_MAPPER = {
    "Transformers": [
        transformer_architecture_markdown,
        "./Instructions/Deep_Learning/TRANSFORMERS/transformers.png",
        "https://www.youtube.com/results?search_query=RNN+in+deep+learning"
    ],
}
