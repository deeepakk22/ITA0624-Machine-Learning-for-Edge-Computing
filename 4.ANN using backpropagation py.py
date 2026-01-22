import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, i, h, o):
        self.w1 = np.random.rand(i, h)
        self.b1 = np.zeros((1, h))
        self.w2 = np.random.rand(h, o)
        self.b2 = np.zeros((1, o))

    def forward(self, x):
        self.h = sigmoid(x @ self.w1 + self.b1)
        self.o = sigmoid(self.h @ self.w2 + self.b2)
        return self.o

    def backward(self, x, y, lr):
        oe = y - self.o
        od = oe * sigmoid_derivative(self.o)
        he = od @ self.w2.T
        hd = he * sigmoid_derivative(self.h)
        self.w2 += self.h.T @ od * lr
        self.b2 += od.sum(axis=0, keepdims=True) * lr
        self.w1 += x.T @ hd * lr
        self.b1 += hd.sum(axis=0, keepdims=True) * lr

    def train(self, x, y, e, lr):
        for _ in range(e):
            for i in range(len(x)):
                self.forward(x[i:i+1])
                self.backward(x[i:i+1], y[i:i+1], lr)

    def predict(self, x):
        return self.forward(x)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

nn = NeuralNetwork(2, 4, 1)
nn.train(X, y, 10000, 0.1)

for i in range(len(X)):
    print(X[i], nn.predict(X[i:i+1]))
