import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# you must run 'python3 -mpip install matplotlib'


class graphPlot:
    def __init__(self):

        self.titles = []
        self.xvalues = []
        self.yvalues = []

    def addValues(self, values: list):

        name = values[0]
        x = values[1]
        y = values[2]

        if self.titles.count(name) == 0:
            self.titles.append(name)
            self.xvalues.append([x])
            self.yvalues.append([y])
        else:
            pos = self.titles.index(name)
            self.xvalues[pos].append(x)
            self.yvalues[pos].append(y)

    def plot(self, title=""):
        plt.style.use("seaborn-darkgrid")

        for i in range(0, len(self.titles)):
            plt.plot(self.xvalues[i], self.yvalues[i])

        plt.xlabel("n bits")
        plt.ylabel("time spent (seconds)")
        plt.title("Criptografia RSA - %s" % title.capitalize())
        plt.xticks(np.arange(8, 25, 8))
        # plt.yscale('linear')
        # plt.yscale('log')
        plt.axis(option="scaled")
        plt.grid(True)
        plt.show()

    @staticmethod
    def new_plot(info):
        #https://python-graph-gallery.com/123-highlight-a-line-in-line-plot/
        plt.style.use("seaborn-darkgrid")
        df=pd.DataFrame(info)
        for column in df.drop('miller', axis=1):
            plt.plot(df['miller'], df[column])
        # Let's annotate the plot
        num=0
        '''
        for i in df.size:
            num+=1
            name=list(df)[num]
            if name != 'y5':
                plt.text(10.2, i, name, horizontalalignment='left', size='small', color='grey')
        '''
        plt.xlabel("n bits")
        plt.ylabel("time spent (seconds)")
        plt.title("Criptografia RSA")

        plt.show()


