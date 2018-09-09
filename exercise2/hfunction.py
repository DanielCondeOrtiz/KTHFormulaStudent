import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button, Slider

class Hfunction:

    def __init__(self):
        plt.show()

        #Figure and size
        fig = plt.figure()
        fig.set_figwidth(10, forward=True)
        fig.set_figheight(7, forward=True)


        self.axes = plt.gca()
        self.axes.set_xlim(0, 1.25)
        self.axes.set_ylim(0, 0.1)
        self.axes.grid(color='silver', linestyle='--', linewidth=1)

        self.graph, = self.axes.plot([],[], 'r-')

        plt.xlabel('t')
        plt.ylabel('h(t)')

        #Buttons
        paus = plt.axes([0.81, 0.02, 0.1, 0.075])
        cont = plt.axes([0.7, 0.02, 0.1, 0.075])

        self.bpaus = Button(paus, 'Pause')
        self.bpaus.on_clicked(self.Paus)

        self.bcont = Button(cont, 'Continue')
        self.bcont.on_clicked(self.Cont)

        #Flag for stopping
        self.goflag = True

        #Sliders
        axcolor = 'lightgoldenrodyellow'
        poszx = plt.axes([0.15, 0.01, 0.45, 0.03], facecolor=axcolor)
        poszy = plt.axes([0.15, 0.05, 0.45, 0.03], facecolor=axcolor)

        slidzx = Slider(poszx, 'ZoomY', 0.5, 10.0, valinit=1)
        slidzy = Slider(poszy, 'ZoomX', 0.5, 10.0, valinit=1)


        slidzx.on_changed(self.update)
        slidzy.on_changed(self.update)

        #axbox = plt.axes([0.1, 0.01, 0.8, 0.075])
        #text_box = TextBox(axbox, 'Title', initial="")
        #text_box.on_submit(self.submit)

    #Math function
    @staticmethod
    def function(t):
        lamb = 5 * math.sin(2 * math.pi * t)
        return 3 * math.pi * math.exp(-lamb)

    #Plotting method
    def plot(self):
        #Values for x
        t = np.arange(0,1.25,0.01)
        xdata = []
        ydata = []

        #How many times looped
        cycle = 0

        #Flag for storing the last value after pausing
        savedFlag = False
        lastNumber = 0

        #Infinite loop
        while True:

            #If not paused
            if self.goflag:

                #Each cycle
                for i in t:
                    #Unpaused
                    if self.goflag and not savedFlag:

                        #Add data to x and y sets
                        xdata.append(i + cycle)
                        ydata.append(self.function(i + cycle))

                        #Set zoom for y axis
                        self.axes.set_ylim(0, max(ydata))

                        #Set place for x axis
                        if cycle > 0:
                            self.axes.set_xlim(i + cycle - 1.25, cycle + i)

                        #Add data to graph
                        self.graph.set_xdata(xdata)
                        self.graph.set_ydata(ydata)
                        plt.draw()
                        plt.pause(0.01)

                    #When we continue, we do the loop until we find the last number plotted
                    if i == lastNumber:
                        savedFlag = False

                    #If just paused, we save the last value
                    if not self.goflag and not savedFlag:
                        savedFlag = True
                        lastNumber = i


                if self.goflag:
                    cycle = cycle + 1.25

            #If paused
            if not self.goflag:
                plt.pause(0.1)

        plt.show()

    #For title box (not used)
    @staticmethod
    def submit(text):
        plt.title(text)

    #For continuing
    def Cont(self, event):
        self.goflag = True

    #For pausing
    def Paus(self, event):
        self.goflag = False

    #For the sliders (not working)
    def update(val):
        print("Slider moved")
