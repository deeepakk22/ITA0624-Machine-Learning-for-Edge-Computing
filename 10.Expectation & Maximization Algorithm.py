import numpy as np
from scipy.stats import norm

np.random.seed(42)
data = np.concatenate([np.random.normal(0, 1, 100), np.random.normal(5, 1, 100)])

mu1, mu2 = np.random.rand(2) * 10
sigma1, sigma2 = np.random.rand(2) * 5
pi = 0.5

for _ in range(100):
    l1 = norm.pdf(data, mu1, sigma1)
    l2 = norm.pdf(data, mu2, sigma2)
    w1 = pi * l1 / (pi * l1 + (1 - pi) * l2)
    w2 = 1 - w1
    mu1 = np.sum(w1 * data) / np.sum(w1)
    mu2 = np.sum(w2 * data) / np.sum(w2)
    sigma1 = np.sqrt(np.sum(w1 * (data - mu1)**2) / np.sum(w1))
    sigma2 = np.sqrt(np.sum(w2 * (data - mu2)**2) / np.sum(w2))
    pi = np.mean(w1)

print(f"Cluster 1: Mean={mu1:.2f}, Std={sigma1:.2f}")
print(f"Cluster 2: Mean={mu2:.2f}, Std={sigma2:.2f}")
print(f"Weights: {pi:.2f}, {1-pi:.2f}")
