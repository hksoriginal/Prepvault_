vae_markdown = r'''
# Variational Autoencoders (VAE)

## Introduction
Variational Autoencoders (VAEs) are a type of generative model used in unsupervised machine learning to learn a probabilistic mapping between an input data space and a latent space. VAEs are a powerful tool for generating new data samples similar to a given training set, such as images, text, or audio.

Unlike traditional autoencoders, which learn a deterministic mapping, VAEs learn a probabilistic one by incorporating a latent variable model. The model allows for sampling from a latent space, which enables the generation of new data.

## Components of a VAE
A VAE consists of two main components:

### 1. Encoder (Recognition Model)
The encoder takes an input $$ x $$ and maps it to a latent space, typically a distribution. Instead of mapping to a fixed vector as in traditional autoencoders, the encoder in VAEs outputs parameters of a probability distribution, such as the mean $$ \mu(x) $$ and the standard deviation $$ \sigma(x) $$, which define a Gaussian distribution.

Mathematically:
- Encoder: $$q(z|x) = \mathcal{N}(\mu(x), \sigma(x)^2) $$

### 2. Decoder (Generative Model)
The decoder samples from the latent distribution and reconstructs the input data from the sampled latent variable $$ z $$. This process aims to generate data similar to the original input $$ x $$, given the latent representation.

Mathematically:
- Decoder: $$ p(x|z) $$  is the likelihood of data $$  x $$ given latent variable $$  z $$.

## Objective: Maximizing the ELBO
The goal of training a VAE is to maximize the Evidence Lower Bound (ELBO) to approximate the true posterior distribution of the latent variables. The ELBO provides a lower bound on the log-likelihood of the data and is used as a surrogate loss function.

### ELBO Formula:
The ELBO can be written as:

$$
\mathbb{E}_{q(z|x)}[\log p(x|z)] - D_{KL}(q(z|x) || p(z))
$$

Where:

- $$( \mathbb{E}_{q(z|x)}[\log p(x|z)] )$$ is the expected log-likelihood (reconstruction loss).
- $$( D_{KL}(q(z|x) || p(z)) )$$ is the Kullback-Leibler divergence between the posterior distribution $$( q(z|x) )$$ and the prior $$( p(z) $$.


The first term encourages good reconstruction of the data, while the second term regularizes the latent space by ensuring that the learned distribution is close to the prior distribution.

## Training the VAE
Training a VAE involves minimizing the negative ELBO, which consists of:
1. **Reconstruction Loss**: Measures how well the model reconstructs the input data. This is typically the binary cross-entropy or mean squared error between the original and reconstructed data.
2. **KL Divergence**: A regularization term that ensures the distribution of the latent variables does not deviate significantly from the prior distribution (usually a standard Gaussian distribution).

### Loss Function:
The total loss for a VAE is:

$$
\mathcal{L} = \mathbb{E}_{q(z|x)}[\log p(x|z)] - D_{KL}(q(z|x) || p(z))
$$

### Reparameterization Trick:
Since direct sampling from the distribution $$  q(z|x)  $$ is not differentiable, the reparameterization trick is used. Instead of sampling $$ z \sim \mathcal{N}(\mu, \sigma^2) $$ directly, we express it as:

$$
z = \mu(x) + \sigma(x) \cdot \epsilon
$$

where $$ \epsilon \sim \mathcal{N}(0, 1) $$ is a random noise vector. This allows the model to backpropagate through the sampling process and optimize the parameters of the model.

## Applications of VAEs
- **Data Generation**: VAEs can generate new samples from the learned latent space, such as new images similar to those in the training set.
- **Image Denoising**: By learning a probabilistic mapping, VAEs can remove noise from corrupted images by reconstructing clean images from noisy inputs.
- **Anomaly Detection**: VAEs can be used to detect anomalies by measuring the reconstruction error. High reconstruction errors may indicate anomalies in the data.
- **Latent Space Exploration**: Since VAEs learn a continuous latent space, they allow for smooth interpolations between data points, making them useful for exploring the data distribution.

## Example Code (PyTorch)

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

class VAE(nn.Module):
    def __init__(self, input_dim, latent_dim):
        super(VAE, self).__init__()
        self.fc1 = nn.Linear(input_dim, 400)
        self.fc21 = nn.Linear(400, latent_dim)  # Mean of latent space
        self.fc22 = nn.Linear(400, latent_dim)  # Log variance of latent space
        self.fc3 = nn.Linear(latent_dim, 400)
        self.fc4 = nn.Linear(400, input_dim)
        
    def encode(self, x):
        h1 = torch.relu(self.fc1(x))
        return self.fc21(h1), self.fc22(h1)  # mean and log variance
    
    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5*logvar)
        eps = torch.randn_like(std)
        return mu + eps*std
    
    def decode(self, z):
        h3 = torch.relu(self.fc3(z))
        return torch.sigmoid(self.fc4(h3))  # Sigmoid to output in range [0, 1]
    
    def forward(self, x):
        mu, logvar = self.encode(x.view(-1, 784))  # Flatten input (e.g. 28x28 image)
        z = self.reparameterize(mu, logvar)
        return self.decode(z), mu, logvar

def loss_function(recon_x, x, mu, logvar):
    BCE = nn.BCELoss(reduction='sum')(recon_x, x.view(-1, 784))  # Binary cross-entropy loss
    # KL Divergence between the learned distribution and the prior
    # D_KL(q(z|x) || p(z)) = -0.5 * sum(1 + log(sigma^2) - mu^2 - sigma^2)
    # For simplicity, assuming prior p(z) = N(0, I)
    # KL Divergence term
    # logvar is log(sigma^2)
    # sum over all latent dimensions
    # calculate KL divergence
    # Note: mu and logvar are already output from the encoder (q(z|x))
    # with shape (batch_size, latent_dim)
    DKL = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return BCE + DKL

# Model initialization
model = VAE(input_dim=784, latent_dim=20)  # Example for MNIST dataset (28x28 images flattened)
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# Example training loop
for epoch in range(epochs):
    model.train()
    train_loss = 0
    for batch_idx, (data, _) in enumerate(DataLoader(train_dataset, batch_size=64, shuffle=True)):
        data = data.view(-1, 784)  # Flatten input
        optimizer.zero_grad()
        recon_batch, mu, logvar = model(data)
        loss = loss_function(recon_batch, data, mu, logvar)
        loss.backward()
        train_loss += loss.item()
        optimizer.step()
    print(
        f"Epoch {epoch} Average Loss: {train_loss / len(DataLoader(train_dataset))}")
```
'''
