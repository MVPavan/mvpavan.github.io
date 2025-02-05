## 1. Likelihood Function
In a probabilistic model, given some parameters $\theta$ and observed data **x**, the **likelihood function** measures how likely the observed data is under those parameters:

Given observed data \( x \) and model parameters ( $\theta$ ), the likelihood function is:

$$
L(\theta) = P(x | \theta)
$$

## 2. Log-Likelihood
Since likelihoods are often small numbers (fractions close to zero), working with them directly can cause numerical instability. Instead, we take the **log** of the likelihood
Taking the logarithm of the likelihood:

$$
\log L(\theta) = \log P(x | \theta)
$$

## 3. Negative Log-Likelihood (NLL)
Most machine learning models **minimize** loss functions (instead of maximizing likelihood). To turn **log-likelihood maximization** into a **minimization problem**, we take the negative of the log-likelihood.
To turn the maximization problem into a minimization problem:

$$
\text{NLL}(\theta) = - \log P(x | \theta)
$$

### (a) NLL for a Bernoulli Distribution (Binary Classification)
$$
\text{NLL} = - \sum_{i=1}^{n} \left[ y_i \log p_i + (1 - y_i) \log (1 - p_i) \right]
$$

where:
- $y_i$ is the true label (0 or 1),
- $p_i$ is the predicted probability.

### (b) NLL for a Gaussian Distribution (Regression)
$$
\text{NLL} = \sum_{i=1}^{n} \left[ \frac{(x_i - \mu)^2}{2\sigma^2} + \log \sigma + \frac{1}{2} \log(2\pi) \right]
$$

## 4. Cross-Entropy Loss

### General Formula for Cross-Entropy
$$
H(p, q) = - \sum_{i=1}^{C} p_i \log q_i
$$

where:
- $C$ is the number of classes
- $p_i$ is the true probability (usually 1 for the correct class, 0 for others)
- $q_i$  is the predicted probability

### (a) Cross-Entropy for Binary Classification
$$
L(y, \hat{y}) = - \left[ y \log(\hat{y}) + (1 - y) \log(1 - \hat{y}) \right]
$$

where:
- ( $y$ ) is the true label (0 or 1),
- ( $\hat{y}$ ) is the predicted probability for class 1.

### (b) Cross-Entropy for Multi-Class Classification
For multi-class classification with **softmax outputs**:

$$
L(y, \hat{y}) = - \sum_{i=1}^{C} y_i \log(\hat{y}_i)
$$

Since only one  $y_i$ = 1 (one-hot encoding), this simplifies to:

$$
L(y, \hat{y}) = - \log(\hat{y}_{\text{correct}} )
$$

## 5. Relationship Between NLL and Cross-Entropy
Cross-entropy is equivalent to the **negative log-likelihood (NLL)** when using softmax probabilities:

$$
\text{Cross-Entropy Loss} = \text{Negative Log-Likelihood}
$$
