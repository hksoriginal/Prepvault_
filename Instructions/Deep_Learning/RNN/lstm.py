lstm_explanation = r"""
# Long Short-Term Memory (LSTM) in Deep Learning

## Introduction

LSTM (Long Short-Term Memory) is a type of Recurrent Neural Network (RNN) architecture designed to capture long-range dependencies and overcome the vanishing gradient problem that often affects traditional RNNs. LSTMs are widely used in time-series forecasting, natural language processing (NLP), and any tasks involving sequential data.

## Why LSTM?

The key limitation of vanilla RNNs is their inability to retain information for long periods. As sequences grow longer, the gradients during backpropagation tend to either shrink or explode, making it difficult for the network to learn long-term dependencies. This problem is called the **vanishing/exploding gradient problem**.

LSTM networks are explicitly designed to avoid this issue by incorporating a **memory cell** that can maintain its state over time. They achieve this by using gates to control the flow of information.

## LSTM Architecture
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240208053129/lstm.webp" alt="Image" width="600" height="300">

An LSTM unit consists of four key components, which are interconnected through gates:

### 1. **Cell State**:
   The cell state is the "memory" part of the LSTM, which runs through the entire sequence and retains important information. It allows the LSTM to remember or forget data.

### 2. **Forget Gate**:
   The forget gate decides what portion of the previous cell state should be retained and what should be discarded. It uses a sigmoid activation function.
   
   <img src="https://media.geeksforgeeks.org/wp-content/uploads/20231123171949/newContent2.jpg" alt="Image" width="200" height="300">

   $$ f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f) $$

   - $$( f_t )$$ is the forget gate activation.
   - $$( h_{t-1} )$$ is the previous hidden state.
   - $$( x_t )$$ is the current input.
   - $$( W_f )$$ and $$( b_f )$$ are the weights and bias of the forget gate.

### 3. **Input Gate**:
   The input gate decides which values from the current input will update the cell state. It consists of two steps:
   - A **sigmoid layer** that determines which values will be updated.
   - A **tanh layer** that creates new candidate values for the cell state.
   
   <img src="https://media.geeksforgeeks.org/wp-content/uploads/20240208104902/bruh.webp" alt="Image" width="600" height="300">

   $$ i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i) $$

   $$ \tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C) $$

   - $$( i_t )$$ is the input gate activation.
   - $$( \tilde{C}_t )$$ is the candidate cell state update.

### 4. **Cell State Update**:
   The new cell state is updated by combining the forget gate's output with the input gate’s output. This step determines what to forget from the previous cell state and what new information to add.

   $$ C_t = f_t \cdot C_{t-1} + i_t \cdot \tilde{C}_t $$

   - $$( C_t )$$ is the updated cell state.

### 5. **Output Gate**:
   The output gate controls what the next hidden state should be. This hidden state is also the output of the LSTM unit for the current timestep.
   
   <img src="https://media.geeksforgeeks.org/wp-content/uploads/20240208104902/bruh.webp" alt="Image" width="600" height="300">

   $$ o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o) $$

   $$ h_t = o_t \cdot \tanh(C_t) $$

   - $$( o_t )$$ is the output gate activation.
   - $$( h_t )$$ is the new hidden state (also the output for the current timestep).

## LSTM in Action

Let’s break down how LSTMs work step by step:
1. **Forget Gate**: Decides how much of the previous memory should be carried forward.
2. **Input Gate**: Takes new input and updates the cell state with relevant information.
3. **Cell State Update**: Updates the memory of the network.
4. **Output Gate**: Produces the hidden state for the next time step and outputs information based on the updated cell state.

## Key Equations

To summarize, here are the main equations for LSTM:
- Forget gate: 
  $$ f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f) $$

- Input gate:
  $$ i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i) $$

  $$ \tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C) $$

- Cell state update:
  $$ C_t = f_t \cdot C_{t-1} + i_t \cdot \tilde{C}_t $$

- Output gate:
  $$ o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o) $$

  $$ h_t = o_t \cdot \tanh(C_t) $$
  
## LSTM in Tensorflow

```python
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Generate dummy sequence data
X_train = np.random.rand(1000, 10, 1)  # 1000 sequences, each with 10 timesteps and 1 feature
y_train = np.random.randint(2, size=(1000, 1))  # 1000 labels (binary classification)

# Build the LSTM model
model = Sequential()

# Add an LSTM layer
model.add(LSTM(50, input_shape=(10, 1)))  # 50 LSTM units, input shape: 10 timesteps, 1 feature

# Add a fully connected output layer with a single neuron (for binary classification)
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

```

## LSTM in PyTorch
```python
import torch
import torch.nn as nn
import torch.optim as optim

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)  # Fully connected layer
    
    def forward(self, x):
        # Initialize hidden state and cell state (h0, c0) to zeros
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)

        # Forward pass through LSTM
        out, _ = self.lstm(x, (h0, c0))  # LSTM output and hidden states

        # Only take the output from the last time step (sequence length dimension)
        out = self.fc(out[:, -1, :])
        return out
# Hyperparameters
input_size = 10  # Number of features
hidden_size = 20  # Number of hidden units
num_layers = 2    # Number of LSTM layers
output_size = 1   # Number of outputs (e.g., regression)
learning_rate = 0.001

# Create the model, loss function, and optimizer
model = LSTMModel(input_size, hidden_size, num_layers, output_size)
criterion = nn.MSELoss()  # Mean squared error for regression tasks
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Dummy data
seq_len = 5
batch_size = 16
x = torch.randn(batch_size, seq_len, input_size)  # Random input data
y = torch.randn(batch_size, output_size)  # Random target data

# Training loop
num_epochs = 100
for epoch in range(num_epochs):
    model.train()
    
    # Forward pass
    outputs = model(x)
    loss = criterion(outputs, y)
    
    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

```

## Conclusion

LSTMs have become a cornerstone of modern deep learning approaches, especially for handling sequence data. Their gating mechanisms allow them to selectively remember and forget information, making them particularly effective for tasks like time series forecasting, language modeling, and speech recognition.

"""
