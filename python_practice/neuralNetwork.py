import math
import numpy as np

'''
Reference https://databoys.github.io/Feedforward/
'''

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(y)
    return y * (1.0 - y)

class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 4)
        self.weights2 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(y.shape)
        #简单的两层神经网络

    def feedforword(self):
        #前向传播
        #激活函数 sigmoid 可以提换成其他的激活函数 active function
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        #反向传播
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T, (np.dot(2* (self.y - self.output) * sigmoid_derivative(self.output), 
            self.weights2.T) * sigmoid_derivative(self.layer1)))

        #update the weights by the derivative of the slope of loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2
        