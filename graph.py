import matplotlib.pyplot as plt
import numpy as np 

# you must run 'python3 -mpip install matplotlib'

class graphPlot:
    def __init__(self):
        
        self.titles = []
        self.xvalues = []
        self.yvalues = []


    def addValues(self,values: list):

        name = values[0]
        x = values[1]
        y = values[2]

        if (self.titles.count(name) == 0):
            self.titles.append(name)
            self.xvalues.append([x])
            self.yvalues.append([y])
        else:
            pos = self.titles.index(name)
            self.xvalues[pos].append(x)
            self.yvalues[pos].append(y)


    def plot(self):

        for i in range(0,len(self.titles)):
            plt.plot( self.xvalues[i], self.yvalues[i] )

        plt.xlabel('n bits')
        plt.ylabel('time spent (ms)')
        plt.title('Criptografia RSA')
        plt.xticks(np.arange(8, 25, 8)) 
        plt.show() 