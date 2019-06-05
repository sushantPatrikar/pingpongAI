import numpy as np
import math
import random
import pickle
class NeuralNetwork():
    def __init__(self,input_nodes,hidden_nodes1,output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes1 = hidden_nodes1
        # self.hidden_nodes2 = hidden_nodes2
        self.output_nodes = output_nodes
        self.in_hidden1_weights = np.random.rand(self.hidden_nodes1,self.input_nodes)
        # self.h1_h2_weights = np.random.rand(self.hidden_nodes2,self.hidden_nodes1)
        self.hidden1_output_weights = np.random.rand(self.output_nodes,self.hidden_nodes1)
        self.in_hidden1_biases = np.random.rand(self.hidden_nodes1,1)
        # self.h1_h2_biases = np.random.rand(self.hidden_nodes2,1)
        self.hidden1_output_biases = np.random.rand(self.output_nodes,1)
        self.sigmoid_v = np.vectorize(self.sigmoid)

    def sigmoid(self,x):
        return (1/(1+math.exp(-x)))

    def feedforward(self,inputs):
        self.inputs = inputs

        self.hidden_layer1 = self.in_hidden1_weights.dot(self.inputs)
        self.hidden_layer1=self.sigmoid_v(self.hidden_layer1+self.in_hidden1_biases)

        # self.hidden_layer2 = self.h1_h2_weights.dot(self.hidden_layer1)
        # self.hidden_layer2 = self.sigmoid_v(self.hidden_layer2+self.h1_h2_biases)

        self.output = self.hidden1_output_weights.dot(self.hidden_layer1)
        self.output =self.sigmoid_v(self.output+self.hidden1_output_biases)
        return self.output

    def crossover(self,mat1,mat2):
        childMat = np.zeros((mat1.shape[0],mat1.shape[1]))
        x = mat1.shape[0]//2
        childMat[:x],childMat[x:] = mat1[:x],mat2[x:]
        return childMat

    def mutate(self,mat,rate):
        for i in range(mat.shape[0]):
            if rate > (random.uniform(0,1)):
                for j in range(mat.shape[1]):
                    mat[i][j] = random.uniform(0,1)
    def serialize(self):
        return pickle.dumps(self)