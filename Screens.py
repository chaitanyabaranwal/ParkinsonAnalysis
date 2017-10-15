#!/usr/bin/env python3

from tkinter import *
import tkinter.filedialog
import parkinson_graph
import time

############################################## Setup UI ############################################################
class Page(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

class IntroScreen(Page):

    def __init__(self, *args, **kwargs):

        Page.__init__(self, *args, **kwargs)
        self.backgroundImage = PhotoImage(file = "What_is_PD.png")
        backgroundLabel = Label(self, image = self.backgroundImage)
        backgroundLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

class IndividualScreen(Page):

    def __init__(self, *args, **kwargs):

        Page.__init__(self, *args, **kwargs)

        self.description = "Predicts the presence of Parkinson's with 86 percent accuracy."
        self.instructions = "Upload the CSV file with all the data for a patient."

        self.descriptionLabel = Label(self, text = self.description, font=("System", 13)).place(x = 140, y = 50)
        self.instructionsLabel = Label(self, text = self.instructions, font=("System", 13)).place(x = 190, y = 80)
        self.genResultButton = Button(self, text = "Upload input file", font=("Arial", 18), command = self.openfile).place(x = 290, y = 130)
        self.resultLabel = Label(self, text = "Parkinson's: ", font = ("Times", 18)).place(x = 310, y = 190)


        self.avgPatientVocal = StringVar()
        self.maxPatientVocal = StringVar()
        self.minPatientVocal = StringVar()
        self.avgPatientVocal.set("")
        self.maxPatientVocal.set("")
        self.minPatientVocal.set("")
        self.averagePatientLabel = Label(self, text = "Values for Patient", font = ("Times bold", 12)).place(x = 40, y = 280)
        self.avgPatientVocalLabel = Label(self, text = "Average Vocal Fundamental Frequency: ", font = ("Times", 12)).place(x = 40, y = 320)
        self.maxPatientVocalLabel = Label(self, text = "Maximum Vocal Fundamental Frequency: ", font = ("Times", 12)).place(x = 40, y = 340)
        self.minPatientVocalLabel = Label(self, text = "Minimum Vocal Fundamental Frequency: ", font = ("Times", 12)).place(x = 40, y = 360)
        self.avgPatientVocalAnswer = Label(self, text = self.avgPatientVocal.get(), textvariable = self.avgPatientVocal, font = ("Times", 12))
        self.maxPatientVocalAnswer = Label(self, text = self.maxPatientVocal.get(), textvariable = self.maxPatientVocal, font = ("Times", 12))
        self.minPatientVocalAnswer = Label(self, text = self.minPatientVocal.get(), textvariable = self.minPatientVocal, font = ("Times", 12))
        self.avgPatientVocalAnswer.place(x = 300, y = 320)
        self.maxPatientVocalAnswer.place(x = 310, y = 340)
        self.minPatientVocalAnswer.place(x = 310, y = 360)

        self.averageLabel = Label(self, text = "Average Values for a Parkinson's Affected", font = ("Times bold", 12)).place(x = 410, y = 280)
        self.avgVocalLabel = Label(self, text = "Average Vocal Fundamental Frequency: 145.18", font = ("Times", 12)).place(x = 410, y = 320)
        self.maxVocalLabel = Label(self, text = "Maximum Vocal Fundamental Frequency: 188.44", font = ("Times", 12)).place(x = 410, y = 340)
        self.minVocalLabel = Label(self, text = "Minimum Vocal Fundamental Frequency: 106.89", font = ("Times", 12)).place(x = 410, y = 360)

        self.result = StringVar()
        self.result.set("")
        self.colour = StringVar()
        self.colour.set("black")
        self.answerLabel = Label(self, text = self.result.get(), textvariable = self.result, fg = self.colour.get(), font = ("Times", 18))
        self.answerLabel.place(x = 430, y = 190)

    # Get the prediction answer by searching for file
    def openfile(self):

        filename = tkinter.filedialog.askopenfilename(parent=self)
        answer = parkinson_graph.predictInput(filename)
        self.result.set(answer[0])
        self.avgPatientVocal.set(answer[1])
        self.maxPatientVocal.set(answer[2])
        self.minPatientVocal.set(answer[3])
        if (self.result.get() == "Yes"):
            self.colour.set("red")
        else:
            self.colour.set("green")
        self.answerLabel.config(fg = self.colour.get())

class BigDataScreen(Page):

    def __init__(self, *args, **kwargs):

        Page.__init__(self, *args, **kwargs)

        self.description = "The first two options generate accuracy graphs for two different sets of data."
        self.instructions = "The third option generates a scatter graph with relations between parameters."

        self.descriptionLabel = Label(self, text = self.description, font=("System", 13)).place(x = 80, y = 50)
        self.instructionsLabel = Label(self, text = self.instructions, font=("System", 13)).place(x = 70, y = 80)
        self.genTrainButton = Button(self, text = "Upload training set", font=("Arial", 18), command = self.openFileTraining).place(x = 40, y = 160)
        self.genTestButton = Button(self, text = "Upload test file", font=("Arial", 18), command = self.openFileTest).place(x = 300, y = 160)
        self.genScatterButton = Button(self, text = "Get Scatter Graph", font=("Arial", 18), command = self.openScatterGraph).place(x = 520, y = 160)
        self.waitingLabel = Label(self, text = "Generate graph.", font=("Arial", 16))
        self.waitingLabel.place(x = 300, y = 240)

    def openFileTraining(self):

        filename = tkinter.filedialog.askopenfilename(parent=self)
        parkinson_graph.predictInputBigData(filename)

        self.waitingLabel.config(text = "Generating graph....")
        self.waitingLabel.update_idletasks()
        time.sleep(5)
        self.waitingLabel.config(text = "Graph generated!")

        graphScreen = Toplevel()
        graph = Canvas(graphScreen, width = 700, height = 500)
        graph.pack(expand = True, fill = "both")
        graphImage = PhotoImage(file = "score_train.png")

        graph.create_image(0, 0, image = graphImage, anchor = "nw")
        graph.graphImage = graphImage

    def openFileTest(self):

        filename = tkinter.filedialog.askopenfilename(parent=self)
        parkinson_graph.predictInputBigData(filename)

        self.waitingLabel.config(text = "Generating graph....")
        self.waitingLabel.update_idletasks()
        time.sleep(5)
        self.waitingLabel.config(text = "Graph generated!")

        graphScreen = Toplevel()
        graph = Canvas(graphScreen, width = 700, height = 500)
        graph.pack(expand = True, fill = "both")
        graphImage = PhotoImage(file = "score_test.png")

        graph.create_image(0, 0, image = graphImage, anchor = "nw")
        graph.graphImage = graphImage
        
    def openScatterGraph(self):

        self.waitingLabel.config(text = "Graph generated!")
        graphScreen = Toplevel()
        graph = Canvas(graphScreen)
        graph.pack(expand = True, fill = "both")
        graphImage = PhotoImage(file = "scatter.png")

        graph.create_image(0, 0, image = graphImage, anchor = "nw")
        graph.graphImage = graphImage



class MainView(Frame):

    def __init__(self, *args, **kwargs):
        
        Frame.__init__(self, *args, **kwargs)
        
        introScreen = IntroScreen(self)
        indiScreen = IndividualScreen(self)
        bigDataScreen = BigDataScreen(self)

        buttonFrame = Frame(self)
        container = Frame(self)
        buttonFrame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        indiScreen.place(in_ = container, x = 0, y = 0, relwidth = 1, relheight = 1)
        introScreen.place(in_ = container, x = 0, y = 0, relwidth = 1, relheight = 1)
        bigDataScreen.place(in_ = container, x = 0, y = 0, relwidth = 1, relheight = 1)
        
        introScreenButton = Button(buttonFrame, text = "Go to Intro Screen", 
                                command = introScreen.lift, width = 30, height = 2)
        indiScreenButton = Button(buttonFrame, text = "Diagnose Individual for Parkinson's", 
                                command = indiScreen.lift, width = 30, height = 2)
        bigDataScreenButton = Button(buttonFrame, text = "Test big data for Parkinson's",
                                command = bigDataScreen.lift, width = 30, height = 2)
        indiScreenButton.pack(side = "left")
        introScreenButton.pack(side = "left")
        bigDataScreenButton.pack(side = "left")

        introScreen.show()
        

##################################################################################################

if __name__ == "__main__":
    root = Toplevel()
    root.geometry("800x500")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()