import math
import numpy as np

'''
Reference https://databoys.github.io/Feedforward/
'''

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(y)
    return y * (1.0 - y)

# using tanh over logistic sigmoid is recommended ??
def tanh(x):
    return math.tanh(x)
    
# derivative for tanh sigmoid
def dtanh(y):
    return 1 - y*y

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
   
        
class MLP_NeuralNetwork:
    def __init__(self, input, hidden, output, iterations, learning_rate, momentum, rate_decay):
        """
        :param input: number of input neurons
        :param hidden: number of hidden neurons
        :param output: number of output neurons
        """
        # initialize parameters
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.rate_decay = rate_decay
        
        # initialize arrays
        self.input = input + 1 # add 1 for bias node
        self.hidden = hidden
        self.output = output

        # set up array of 1s for activations
        self.activeInput = [1.0] * self.input
        self.activeHidden = [1.0] * self.hidden
        self.activeOutput = [1.0] * self.output
        
        # create randomized weights
        # use scheme from 'efficient backprop to initialize weights
        input_range = 1.0 / self.input ** (1/2)
        output_range = 1.0 / self.hidden ** (1/2)
        self.weightInput = np.random.normal(loc = 0, scale = input_range, size = (self.input, self.hidden))
        self.weightOutput = np.random.normal(loc = 0, scale = output_range, size = (self.hidden, self.output))
        
        # create arrays of 0 for changes
        # this is essentially an array of temporary values that gets updated at each iteration
        # based on how much the weights need to change in the following iteration
        self.changeInput = np.zeros((self.input, self.hidden))
        self.changeOutput = np.zeros((self.hidden, self.output))
        
        
 def feedForward(self, inputs):
        """
        The feedforward algorithm loops over all the nodes in the hidden layer and
        adds together all the outputs from the input layer * their weights
        the output of each node is the sigmoid function of the sum of all inputs
        which is then passed on to the next layer.
        :param inputs: input data
        :return: updated activation output vector
        """
        if len(inputs) != self.input-1:
            raise ValueError('Wrong number of inputs!')

        # input activations
        for i in range(self.input -1): # -1 is to avoid the bias
            self.activeInput[i] = inputs[i]

        # hidden activations
#         for j in range(self.hidden):
#             sum = 0.0
#             for i in range(self.input):
#                 sum += self.activeInput[i] * self.weightInput[i][j]
#             self.activeHidden[j] = tanh(sum)
            
        self.activeHidden = tanh(np.dot(self.activeInput, self.weightInput))  #为什么要tanh ?? 

        # output activations
#         for k in range(self.output):
#             sum = 0.0
#             for j in range(self.hidden):
#                 sum += self.activeHidden[j] * self.weightOutput[j][k]
#             self.activeOutput[k] = sigmoid(sum)
        
        self.activeOutput = sigmoid(np.dot(self.activeHidden, self.weightOutput))
            
        return self.activeOutput[:]

        
        
if __name__ == "__main__":
    x = np.array([[0,1,0],
                  [0,1,1],
                  [1,0,1],
                  [1,1,1]])
    y = np.array([[0],[1],[1],[0]])
    
    nn = NeuralNetwork(X,y)


    for i in range(2000):
        nn.feedforward()
        nn.backprop()
    
    print(nn.output)
