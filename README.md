# ParkinsonAnalysis

NOTE: To run the program, enter the command "python3 Screens.py" from the program directory in your terminal. 

A program that uses Machine Learning and Regressions to predict the presence of Parksinson's Disease in a patient. It can be used by doctors who can enter the observations for a patient in a CSV file, and the program can then read the CSV file to predict the presence of Parkinson's. The regression is constructed on the basis of a dataset published in the UC Irvine Machine Learning repository. The dataset was created by Max Little of the University of Oxford, in collaboration with the National Centre for Voice and Speech, Denver, Colorado, who recorded the speech signals.

For more info about the database, go to: https://archive.ics.uci.edu/ml/datasets/parkinsons

The program has two modes: one to predict Parkinson's in an individual patient (based on an input CSV) which uses a Simple Tree Regression Model to classify patients on the basis of their measurements. The measurements are fitted against the values from the main database. 

The second mode is used with the entire original database, creating a model based on the accumulation of four distinct ML algorithms, which are: Support Vector Machine (SVM), Stochastic Gradient Descent Classifier (SGD), the Gaussian Naive Bayes (NB), and the Gradient Boosting Classifier. The results from the four are collated over three distinct datasets having 50, 100 and 150 values respectively. There's also an option to display a Scatter Matrix to show the relationships between the parameters of the original dataset. 

The UI has been developed by using the Tkinter extension in Python. 
