import matplotlib.pyplot as plt
from time import sleep
from random import shuffle

plt.ion()
y = [i for i in range(100)]
x = [i for i in range(len(y))]

def myBarPlot():

    fig = plt.figure(1)
    fig.canvas.set_window_title('myBarPlot')

    for i in range(20):       ## Do the following 50 times
        print i
        plt.clf()             ## Clear the plot
        plt.bar(x,y)          ## Plot a bar chart
        plt.pause(0.01)       ## Pause for 1/2 a second
        shuffle(y)            ## Shuffle the data

    plt.show(block=True)      ## Show graph, keep block open

myBarPlot()
