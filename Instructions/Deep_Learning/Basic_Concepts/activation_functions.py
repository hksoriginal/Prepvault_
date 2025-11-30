activation_function_markdown = \
    r"""
# Activation Functions in Deep Learning

Activation functions are crucial components in deep learning models, as they introduce non-linearity into the network, allowing it to learn complex patterns. Here's an overview of the most commonly used activation functions:

## 1. Sigmoid (Logistic) Function

**Equation**:
$$ \sigma(x) = \frac{1}{1 + e^{-x}} $$

**Characteristics**:
- Range: (0, 1)
- Used in: Binary classification problems
- Output can be interpreted as probability.

**Pros**:
- Smooth gradient.
- Output is bounded, useful for probabilistic interpretation.

**Cons**:
- Vanishing gradient problem (for large negative or positive inputs, gradients become very small).
- Can saturate and slow down learning.

---

## 2. Hyperbolic Tangent (Tanh) Function

**Equation**:
$$ \tanh(x) = \frac{2}{1 + e^{-2x}} - 1 $$

**Characteristics**:
- Range: (-1, 1)
- Used in: Hidden layers
- Similar to sigmoid, but output is centered around zero.

**Pros**:
- Centered at zero, which helps in faster convergence.
- Strong gradients for mid-range values.

**Cons**:
- Also suffers from the vanishing gradient problem for extreme values of x.



---

## 3. ReLU (Rectified Linear Unit)

**Equation**:
$$ \text{ReLU}(x) = \max(0, x) $$

**Characteristics**:
- Range: [0, ∞)
- Used in: Most hidden layers in deep networks.

**Pros**:
- Computationally efficient.
- Does not saturate for positive inputs, which helps alleviate the vanishing gradient problem.
- Sparse activation: activates only for positive inputs.

**Cons**:
- "Dying ReLU" problem: Neurons can get stuck during training if their inputs consistently result in negative values.


---

## 4. Leaky ReLU

**Equation**:
$$ \text{Leaky ReLU}(x) = \max(0.01x, x) $$

**Characteristics**:
- Similar to ReLU, but it allows a small, non-zero gradient when x < 0.

**Pros**:
- Helps mitigate the "dying ReLU" problem.
- Can learn in regions of the parameter space where the ReLU would remain inactive.

**Cons**:
- The slope of the leak (e.g., 0.01) must be tuned.


---

## 5. Parametric ReLU (PReLU)

**Equation**:
$$ \text{PReLU}(x) = \max(\alpha x, x) $$

**Characteristics**:
- Similar to Leaky ReLU, but the parameter α is learned during training.

**Pros**:
- Allows the model to learn the most appropriate negative slope.

**Cons**:
- Additional parameter increases model complexity slightly.

---

## 6. Exponential Linear Unit (ELU)

**Equation**:
$$ \text{ELU}(x) = 
\begin{cases} 
x & \text{if } x > 0 \\
\alpha (e^x - 1) & \text{if } x \leq 0 
\end{cases}
$$

**Characteristics**:
- Range: (-α, ∞)
- Used in: Hidden layers.

**Pros**:
- Unlike ReLU, ELU can produce negative outputs, which helps center activations closer to zero.
- Reduces bias shift and can improve convergence.

**Cons**:
- Computationally more expensive due to the exponential calculation.

---

## 7. Swish

**Equation**:
$$ \text{Swish}(x) = x \cdot \sigma(x) = \frac{x}{1 + e^{-x}} $$

**Characteristics**:
- Range: (-∞, ∞)
- Used in: Newer deep learning models, e.g., Google's EfficientNet.

**Pros**:
- Smooth and non-monotonic.
- Empirically shown to work better in some deeper models compared to ReLU.

**Cons**:
- Higher computational cost compared to ReLU.

---

## 8. Softmax Function

**Equation**:
$$ \text{Softmax}(x_i) = \frac{e^{x_i}}{\sum_{j=1}^{N} e^{x_j}} $$

**Characteristics**:
- Range: (0, 1), with the sum of all outputs equal to 1.
- Used in: Output layer for multi-class classification.

**Pros**:
- Converts raw logits into a probability distribution, useful for multi-class problems.

**Cons**:
- Outputs are relative probabilities; high confidence in one class can diminish confidence in others.


---
"""
