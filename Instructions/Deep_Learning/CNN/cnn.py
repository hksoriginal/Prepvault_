cnn_markdown = r"""
# Convolutional Neural Networks (CNNs) in Deep Learning

Convolutional Neural Networks (CNNs) are a specialized type of neural network designed for processing structured grid data, such as images. They have been pivotal in advancing the fields of computer vision and image recognition.

## Key Components of CNNs

### 1. Convolution Layer
The core building block of a CNN, the convolution layer, applies convolution operations to the input. The main components include:

- **Filters/Kernels:** Small matrices that slide over the input data to detect features. Each filter detects different features such as edges, textures, or shapes.
  
- **Stride:** The number of pixels by which the filter moves over the input. A larger stride reduces the spatial dimensions of the output.

- **Padding:** Adding extra pixels around the input data to control the spatial size of the output. This helps preserve spatial information, especially at the borders.

**Mathematical Representation:**

The convolution operation can be mathematically represented as:

$$ (I * K)(i, j) = \sum_m \sum_n I(m, n) \cdot K(i - m, j - n) $$

Where:
- $$ I $$ is the input image,
- $$ K $$ is the kernel/filter,
- $$ i, j $$ are the coordinates of the output feature map.

### 2. Activation Function
After the convolution operation, an activation function is applied to introduce non-linearity. The most common activation function used in CNNs is the Rectified Linear Unit (ReLU):

$$ f(x) = \max(0, x) $$

### 3. Pooling Layer
Pooling layers reduce the spatial dimensions of the feature maps, which helps to reduce computational load and control overfitting. The most common types of pooling are:

- **Max Pooling:** Takes the maximum value from a patch of the feature map.
  
- **Average Pooling:** Takes the average value from a patch of the feature map.

### 4. Fully Connected Layer
After several convolution and pooling layers, the high-level reasoning is done by fully connected layers. Each neuron in this layer is connected to every neuron in the previous layer, allowing the model to make predictions.

### 5. Output Layer
The final layer produces the output, usually through a softmax activation function for multi-class classification tasks.




## Architecture of CNNs

A typical CNN architecture can be summarized as follows:

1. **Input Layer:** The raw input image.
2. **Convolution Layer:** Applies multiple filters.
3. **Activation Layer:** Applies the activation function (e.g., ReLU).
4. **Pooling Layer:** Reduces spatial dimensions (e.g., Max Pooling).
5. **Convolution and Pooling Layers:** Repeat as necessary to extract features.
6. **Fully Connected Layer:** Classifies the features extracted by previous layers.
7. **Output Layer:** Final predictions.


## Tensorflow Implementation
```python
import tensorflow as tf
from tensorflow.keras import layers, models

# Load and preprocess the CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalize to [0, 1]

# Create the CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 classes for CIFAR-10
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

```

## Pytorch Implementation
```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# Transform to normalize the data
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

# Load CIFAR-10 dataset
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True)

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=32, shuffle=False)

# Define the CNN model
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)  # 32 filters
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)  # 64 filters
        self.conv3 = nn.Conv2d(64, 64, kernel_size=3, padding=1)  # 64 filters
        self.fc1 = nn.Linear(64 * 4 * 4, 64)  # Adjust the input size based on pooling
        self.fc2 = nn.Linear(64, 10)  # 10 classes for CIFAR-10

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 64 * 4 * 4)  # Flatten the tensor
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Create the model, define loss function and optimizer
model = CNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
num_epochs = 10
for epoch in range(num_epochs):
    for images, labels in trainloader:
        # Zero the gradients
        optimizer.zero_grad()
        
        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward pass and optimization
        loss.backward()
        optimizer.step()
    
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Testing the model can be added similarly.

```



### Example CNN Architecture

Input Image → Convolution Layer → Activation (ReLU) → Pooling Layer → 
Convolution Layer → Activation (ReLU) → Pooling Layer → Fully Connected Layer → Output

### Explanation:

1.  **Initialization**: The `LassoRegression` class is initialized with parameters for the learning rate, number of iterations, and the regularization parameter $$\lambda$$.

2.  **Fitting the Model**:

    -   The `fit` method adds a bias term to the feature matrix and initializes the coefficients.
    -   In the gradient descent loop, the predicted values are computed, and the gradients are calculated. The L1 penalty is added to the gradients using a subgradient approach (considering the sign of each coefficient).
    -   The coefficients are updated based on the calculated gradients.
3.  **Making Predictions**:

    -   The `predict` method adds the bias term and computes the predicted values based on the learned coefficients.
4.  **Example Usage**:

    -   A synthetic linear regression dataset is generated using `make_regression`.
    -   The dataset is split into training and testing sets.
    -   The model is fitted to the training data, predictions are made on the test data, and the Mean Squared Error (MSE) is calculated for evaluation.Applications of CNNs
--------------------

CNNs have wide-ranging applications, including:

-   **Image Classification:** Identifying objects in images (e.g., classifying dogs vs. cats).
-   **Object Detection:** Locating and classifying objects within an image (e.g., YOLO, SSD).
-   **Image Segmentation:** Classifying each pixel in an image (e.g., U-Net).
-   **Facial Recognition:** Identifying and verifying faces in images.

Conclusion
----------

Convolutional Neural Networks are a powerful tool for image and pattern recognition tasks. Their ability to automatically detect features from raw input data significantly reduces the need for manual feature extraction, leading to state-of-the-art performance in various applications.


"""
