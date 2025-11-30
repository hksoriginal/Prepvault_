DL_INTERVIEW_Q = r'''

###  What are autoencoders? Explain the different layers of autoencoders and mention three practical usages of them?
**Answer:**

Autoencoders are one of the deep learning types used for unsupervised learning. The key layers of autoencoders are the input layer, encoder, bottleneck hidden layer, decoder, and output.

The three layers of the autoencoder are:

- **Encoder**: Compresses the input data to an encoded representation, typically much smaller than the input data.
- **Latent Space Representation/Bottleneck/Code**: A compact summary of the input containing the most important features.
- **Decoder**: Decompresses the knowledge representation and reconstructs the data back from its encoded form. A loss function compares the input and output images.

**Practical usages of autoencoders:**
- Text Summarizer and Text Generator (components in Transformers and Big Bird algorithms).
- Image compression.
- Nonlinear version of PCA.


### What is an activation function, and discuss its use? Explain three different types of activation functions?
**Answer:**

An activation function serves as a gate between the current neuron's input and output, deciding whether neurons should be activated. It introduces non-linearity to a model, making it capable of capturing complex variations beyond simple linear models.

**Types of activation functions:**
- **Sigmoid**: $$( f(x) = \frac{1}{1+e^{-x}} )$$. Output values range between 0 and 1; used for classification. It suffers from gradient vanishing issues.
- **ReLU**: $$( f(x) = \max(0, x) )$$. Solves the vanishing gradient problem on the positive side. Fast due to its linear computation.
- **Leaky ReLU**: $$( f(x) = ax,  x < 0;  f(x) = x,  x \geq 0 )$$. Addresses the vanishing gradient problem on both sides by returning a small value $$( a )$$ for negative inputs.



###  How can overfitting in a deep neural network be reduced?
To reduce overfitting, modifications can be made to:

1. **Input data**:
   - Ensure all features are reliable.
   - Align training sample distribution with validation/test set distribution.
   - Avoid contamination or leakage between training and validation data.
   - Use data augmentation if the dataset size is insufficient.
   - Balance the dataset.

2. **Network architecture**:
   - Replace fully connected layers with convolutional and pooling layers where applicable.
   - Add regularization techniques such as L1 (lasso), L2 (ridge), or elastic net.
   - Use dropouts or batch normalization.

3. **Training process**:
   - Implement early stopping using callbacks based on validation loss improvements.



###  Why should we use Batch Normalization?
Batch Normalization (BN) standardizes the inputs to a layer for each mini-batch, helping to combat vanishing/exploding gradients.

**Effects:**
- Enables robust training of deeper layers.
- Reduces covariate shift.
- Adds slight regularization.
- Prevents exploding/vanishing gradients.
- Speeds up training and convergence.



###  How to detect and address exploding gradients?
Exploding gradients occur when updates to weights and biases become excessively large during training, causing instability. Signs include:

- Large changes or instability in loss.
- Model weights becoming very large or NaN.
- Error gradient values exceeding 1 consistently.

**Solutions:**
- Apply gradient clipping.
- Use normalization techniques like Batch Normalization.
- Adopt architectures like LSTMs or GRUs.



###  Can you name and explain a few hyperparameters used for training a neural network?
**Answer:**

Hyperparameters affect model performance and are manually set by users. Examples include:

- **Number of nodes**: Inputs per layer.
- **Batch normalization**: Standardizes inputs within a layer.
- **Learning rate**: Controls weight update magnitude.
- **Dropout rate**: Percentage of nodes dropped temporarily during training.
- **Activation function**: Defines output transformations (e.g., ReLU, softmax).
- **Number of epochs**: Training iterations.
- **Batch size**: Number of samples per training batch.
- **Momentum**: Adds a fraction of past updates to current updates, damping oscillations.
- **Optimizers**: Algorithms for fine-tuning learning rates (e.g., Adagrad, Adam).


###  What is the parameter sharing concept in deep learning?
**Answer:**

Parameter sharing involves reusing the same weights across different neurons or layers, reducing computational cost. It allows more generalization and diverse feature learning. For specific scenarios (e.g., centered face inputs), parameter sharing may be relaxed using locally connected layers.


###  Describe the architecture of a typical Convolutional Neural Network (CNN)?
**Answer:**

A CNN typically consists of:

- Convolutional layers with activation functions like ReLU.
- Pooling layers (e.g., max-pooling, average pooling) for dimensionality reduction.
- Fully connected layers for final feature combination.
- A softmax layer for classification.

Hyperparameters include kernel size, stride, padding, and type of pooling.



###  What is the Vanishing Gradient Problem in Artificial Neural Networks and how to fix it?
**Answer:**

The vanishing gradient problem occurs when gradient values become too small, preventing weight updates and halting learning in earlier layers.

**Fixes:**
- Use skip/residual connections.
- Prefer ReLU or Leaky ReLU over sigmoid and tanh activations.
- Use advanced architectures like GRUs and LSTMs.



###  Why might the loss not decrease during training?
**Answer:**

Possible reasons include:

- Underfitting due to insufficient model complexity.
- High learning rates.
- Improper initialization (e.g., weights initialized to zero).
- Excessive regularization.
- Vanishing gradient issues.


### Why Sigmoid or Tanh is not preferred to be used as the activation function in the hidden layer of the neural network?  
Answer:

A common problem with Tanh or Sigmoid functions is that they saturate. Once saturated, the learning algorithms cannot adapt to the weights and enhance the performance of the model. Thus, Sigmoid or Tanh activation functions prevent the neural network from learning effectively leading to a vanishing gradient problem. The vanishing gradient problem can be addressed with the use of Rectified Linear Activation Function (ReLu) instead of sigmoid and Tanh. Alt_text

### Discuss in what context it is recommended to use transfer learning and when it is not.  
Answer:

Transfer learning is a machine learning method where a model developed for a task is reused as the starting point for a model on a second task. It is a popular approach in deep learning where pre-trained models are used as the starting point for computer vision and natural language processing tasks given the vast computing and time resources required to develop neural network models on these problems and from the huge jumps in a skill that they provide on related problems.

Transfer learning is used for tasks where the data is too little to train a full-scale model from the beginning. In transfer learning, well-trained, well-constructed networks are used which have learned over large sets and can be used to boost the performance of a dataset.

**Transfer Learning can be used in the following cases:**

- The downstream task has a very small amount of data available, then we can try using pre-trained model weights by switching the last layer with new layers which we will train.
- In some cases, like in vision-related tasks, the initial layers have a common behavior of detecting edges, then a little more complex but still abstract features and so on which is common in all vision tasks, and hence a pre-trained model's initial layers can be used directly. The same thing holds for Language Models too, for example, a model trained in a large Hindi corpus can be transferred and used for other Indo-Aryan Languages with low resources available.

**Cases when transfer Learning should not be used:**

- The first and most important is the "COST". So is it cost-effective or we can have a similar performance without using it.
- The pre-trained model has no relation to the downstream task.
- If the latency is a big constraint (Mostly in NLP ) then transfer learning is not the best option. However Now with the TensorFlow lite kind of platform and Model Distillation, Latency is not a problem anymore.

### Discuss the vanishing gradient in RNN and How they can be solved.  
Answer:

In Sequence to Sequence models such as RNNs, the input sentences might have long-term dependencies for example we might say "The boy who was wearing a red t-shirt, blue jeans, black shoes, and a white cap and who lives at ... and is 10 years old ...... etc, is genius" here the verb (is) in the sentence depends on the (boy) i.e if we say (The boys, ......, are genius". When training an RNN we do backward propagation both through layers and backward through time. Without focusing too much on mathematics, during backward propagation we tend to multiply gradients that are either > 1 or < 1, if the gradients are < 1 and we have about 100 steps backward in time then multiplying 100 numbers that are < 1 will result in a very very tiny gradient causing no change in the weights as we go backward in time (0.1 * 0.1 * 0.1 * .... a 100 times = 10^(-100)) such that in our previous example the word "is" doesn't affect its main dependency the word "boy" during learning the meanings of the word due to the long description in between.

Models like the Gated Recurrent Units (GRUs) and the Long short-term memory (LSTMs) were proposed, the main idea of these models is to use gates to help the network determine which information to keep and which information to discard during learning. Then Transformers were proposed depending on the self-attention mechanism to catch the dependencies between words in the sequence.

### What are the main gates in LSTM and what are their tasks?  
Answer: There are 3 main types of gates in a LSTM Model, as follows:

- Forget Gate
- Input/Update Gate
- Output Gate

**Forget Gate:** It helps in deciding which data to keep or thrown out  
**Input Gate:** it helps in determining whether new data should be added in long term memory cell given by previous hidden state and new input data  
**Output Gate:** this gate gives out the new hidden state  

Common things for all these gates are they all take inputs as the current temporal state/input/word/observation and the previous hidden state output and sigmoid activation is mostly used in all of these.

### Is it a good idea to use CNN to classify 1D signal?  
Answer: For time-series data, where we assume temporal dependence between the values, then convolutional neural networks (CNN) are one of the possible approaches. However the most popular approach to such data is to use recurrent neural networks (RNN), but you can alternatively use CNNs, or a hybrid approach (quasi-recurrent neural networks, QRNN).

With CNN, you would use sliding windows of some width, that would look at certain (learned) patterns in the data, and stack such windows on top of each other, so that higher-level windows would look for patterns within the lower-level patterns. Using such sliding windows may be helpful for finding things such as repeating patterns within the data. One drawback is that it doesn't take into account the temporal or sequential aspect of the 1D signals, which can be very important for prediction.

With RNN, you would use a cell that takes as input the previous hidden state and current input value, to return output and another hidden form, so the information flows via the hidden states and takes into account the temporal dependencies.

QRNN layers mix both approaches.

### How does L1/L2 regularization affect a neural network?  
Answer:

Overfitting occurs in more complex neural network models (many layers, many neurons) and the complexity of the neural network can be reduced by using L1 and L2 regularization as well as dropout, Data augmentation, and Dropout. L1 regularization forces the weight parameters to become zero. L2 regularization forces the weight parameters towards zero (but never exactly zero|| weight decay)

Smaller weight parameters make some neurons neglectable therefore neural network becomes less complex and less overfitting.

Regularisation has the following benefits:

- Reducing the variance of the model over unseen data.
- Makes it feasible to fit much more complicated models without overfitting.
- Reduces the magnitude of weights and biases.
- L1 learns sparse models that is many weights turn out to be 0.
[GitHub Link](https://github.com/youssefHosni/Data-Science-Interview-Questions-Answers/tree/main)

### How would you change a pre-trained neural network from classification to regression?  
Answer: Using transfer learning where we can use our knowledge about one task to do another. The first set of layers of a neural network are usually feature extraction layers and will be useful for all tasks with the same input distribution. So, we should replace the last fully connected layer and Softmax responsible for classification with one neuron for regression-or fully connected-layer for correction then one neuron for regression.

We can optionally freeze the first set of layers if we have few data or to converge fast. Then we can train the network with the data we have and using the suitable loss for the regression problem, making use of the robust feature extraction -first set of layers- of a pre-trained model on huge data.

### What might happen if you set the momentum hyperparameter too close to 1 (e.g., 0.9999) when using an SGD optimizer?  
Answer:

If the momentum hyperparameter is set too close to 1 (e.g., 0.99999) when using an SGD optimizer, then the algorithm will likely pick up a lot of speed, hopefully moving roughly toward the global minimum, but its momentum will carry it right past the minimum.

Then it will slow down and come back, accelerate again, overshoot again, and so on. It may oscillate this way many times before converging, so overall it will take much longer to converge than with a smaller momentum value.

Also, since the momentum is used to update the weights based on an "exponential moving average" of all the previous gradients instead of the current gradient only, this in some sense, combats the instability of the gradients that comes with stochastic gradient descent, the higher the momentum term, the stronger the influence of previous gradients to the current optimization step (with the more recent gradients having even stronger influence), setting a momentum term close to 1, will result in a gradient that is almost a sum of all the previous gradients basically, which might result in an exploding gradient scenario.

### What are the hyperparameters that can be optimized for the batch normalization layer?  
Answer: The **γ** and **β** hyperparameters for the batch normalization layer are learned end to end by the network. In batch-normalization, the outputs of the intermediate layers are normalized to have a mean of 0 and standard deviation of 1. Rescaling by **γ** and shifting by **β** helps us change the mean and standard deviation to other values.

### What is the effect of dropout on the training and prediction speed of your deep learning model?  
Answer: Dropout is a regularization technique, which zeroes down some weights and scales up the rest of the weights by a factor of 1/(1-p). Let's say if



'''
