# Import libraries
import numpy as np
import pandas as pd
from time import time
from sklearn.cross_validation import train_test_split
from sklearn.metrics import f1_score
from sklearn import tree

# Tuning libraries

from sklearn.metrics import make_scorer
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import f1_score

#Import supervised learning model
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import GradientBoostingClassifier

#Import Graphing modules
import matplotlib.pyplot as plt
from sklearn import datasets
from tkinter import *
import tkinter.filedialog
import plotly
import plotly.plotly as pyGraphThing
import plotly.graph_objs as goGraphThing

#All about UI
from tkinter import *
import tkinter.filedialog
import Screens


#Initialize the models

clf = GaussianNB()
clf2 = svm.SVC(max_iter=1000)
clf3 = SGDClassifier(loss = "hinge",max_iter=1000)
clf4 = GradientBoostingClassifier(n_estimators=100, learning_rate = 2.0, max_depth =1, random_state =0 )
clf5 = tree.DecisionTreeClassifier()


#Data Visualization Values
from pandas.tools.plotting import scatter_matrix
import pylab

plotly.tools.set_credentials_file(
    username='chaitanyabaranwal', api_key='pqvxsmZCfXcFkGFdhIRu')

pyGraphThing.sign_in('chaitanyabaranwal', 'pqvxsmZCfXcFkGFdhIRu')
#Training and Testing Functions

def train_classifier(clf, X_train, y_train):
    ''' Fits a classifier to the training data. '''
    
    start = time()
    clf.fit(X_train, y_train)
    end = time()
    
    #print ("Trained model in {:.4f} seconds".format(end,start))

    
def predict_labels(clf, features, target):
    ''' Makes predictions using a fit classifier based on F1 score. '''
    
    start = time()
    y_pred = clf.predict(features)
    end = time()
    
    #print ("Made predictions in {:.4f} seconds.".format(end, start))
    return f1_score(target.values, y_pred, pos_label=1)


def train_predict(clf, X_train, y_train, X_test, y_test):
    ''' Train and predict using a classifer based on F1 score. '''
    
    print ("Training a {} using a training set size of {}. . .".format(clf.__class__.__name__, len(X_train)))
    
    train_classifier(clf, X_train, y_train)
    
    return [(predict_labels(clf, X_train, y_train)),
     (predict_labels(clf, X_test, y_test))]


# Tuning / Optimization Functions

def performance_metric(y_true, y_predict):
    error = f1_score(y_true, y_predict, pos_label=1)
    return error

def fit_model(X, y):
  
    classifier = svm.SVC()

    parameters = {'kernel':['poly', 'rbf', 'sigmoid'], 'degree':[1, 2, 3], 'C':[0.1, 1, 10]}


    f1_scorer = make_scorer(performance_metric,
                                   greater_is_better=True)

    clf = GridSearchCV(classifier,
                       param_grid=parameters,
                       scoring=f1_scorer)

    clf.fit(X, y)

    return clf

#get the patient input to predict data
def predictInput(filename):
    print("Data training complete: reading patient info for prediction")
    clf5.fit(X_all, y_all)
    input_data= pd.read_csv(filename)
    print("Read input data")
    avgPatientVocal = "{0:.{1}f}".format(input_data.ix[0,1],2)
    maxPatientVocal = "{0:.{1}f}".format(input_data.ix[0,2],2)
    minPatientVocal = "{0:.{1}f}".format(input_data.ix[0,3],2)
    input_features= list(input_data.columns[1:22])
    x_input= input_data[input_features]
    prediction= clf5.predict(x_input)
    if(prediction == 1):
        return ["Yes",avgPatientVocal,maxPatientVocal,minPatientVocal]
    else:
        return ["No",avgPatientVocal,maxPatientVocal,minPatientVocal]

parkinson_data = pd.read_csv("parkinsons.csv")


#Data Exploration

#Number of patients
n_patients = parkinson_data.shape[0]

#Number of features
n_features = parkinson_data.shape[1]-1

#With Parkinsons
n_parkinsons = parkinson_data[parkinson_data['status'] == 1].shape[0]

#Without Parkinsons
n_healthy = parkinson_data[parkinson_data['status'] == 0].shape[0]

#Result Output
print ("Total number of patients: {}".format(n_patients))
print ("Number of features: {}".format(n_features))
print ("Number of patients with Parkinsons: {}".format(n_parkinsons))
print ("Number of patients without Parkinsons: {}".format(n_healthy))

#Preparing the Data

# Training and Testing Data Split
num_all = parkinson_data.shape[0] 
num_train = 150 # about 75% of the data
num_test = num_all - num_train

# Select features and corresponding labels for training/test sets

# Extract feature columns
feature_cols = list(parkinson_data.columns[1:22])
target_col = parkinson_data.columns[23]

# Separate the data into feature data and target data (X_all and y_all, respectively)
X_all = parkinson_data[feature_cols]
y_all = parkinson_data[target_col]

###################

#Data Visualization

#Tuning model (Support Vector Machine)
pd.plotting.scatter_matrix(parkinson_data[['MDVP:Fo(Hz)','MDVP:Fhi(Hz)','MDVP:Flo(Hz)','MDVP:Jitter(%)','MDVP:Jitter(Abs)']], alpha=0.1, figsize=(7,7), diagonal='kde')
pylab.savefig("scatter" + ".png")

def graph(a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4):
    trace1 = goGraphThing.Bar(
        x=['Naive Bayes','SVM','SGD','GBT'],
        y=[a1[0], a2[0],a3[0],a4[0]],
        name='50'
    )
    trace2 = goGraphThing.Bar(
        x=['Naive Bayes','SVM','SGD','GBT'],
        y=[b1[0], b2[0],b3[0],b4[0]],
        name='100'
    )
    trace3 = goGraphThing.Bar(
        x=['Naive Bayes', 'SVM', 'SGD', 'GBT'],
        y=[c1[0], c2[0], c3[0], c4[0]],
        name='150'
    )
    data = [trace1, trace2,trace3]
    layout = goGraphThing.Layout(
        barmode='group',
        title=' training data score'
    )
    fig = goGraphThing.Figure(data=data, layout=layout)
    pyGraphThing.image.save_as(fig, filename='score_train.png')


    trace5 = goGraphThing.Bar(
        x=['Naive Bayes','SVM','SGD','GBT'],
        y=[a1[1], a2[1],a3[1],a4[1]],
        name='50'
    )
    trace6 = goGraphThing.Bar(
        x=['Naive Bayes','SVM','SGD','GBT'],
        y=[b1[1], b2[1],b3[1],b4[1]],
        name='100'
    )
    trace7 = goGraphThing.Bar(
        x=['Naive Bayes', 'SVM', 'SGD', 'GBT'],
        y=[c1[1], c2[1], c3[1], c4[1]],
        name='150'
    )
    data = [trace5, trace6,trace7]
    layout = goGraphThing.Layout(
        barmode='group',
        title='test_data_score'
    )
    fig = goGraphThing.Figure(data=data, layout=layout)
    pyGraphThing.image.save_as(fig, filename='score_test.png')


def predictInputBigData(filename):

    parkinson_data = pd.read_csv(filename)

    # Extract feature columns
    feature_cols = list(parkinson_data.columns[1:22])
    target_col = parkinson_data.columns[23]

    # Separate the data into feature data and target data (X_all and y_all, respectively)
    X_all = parkinson_data[feature_cols]
    y_all = parkinson_data[target_col]
    
    # begin splitting data into various sets for comparision
    X_train, X_test, y_train, y_test = train_test_split(
        X_all, y_all, test_size=num_test, random_state=5)
    print("Shuffling of data into test and training sets complete!")

    print("Training set: {} samples".format(X_train.shape[0]))

    print("Test set: {} samples".format(X_test.shape[0]))
    #start training data
    X_train_50 = X_train[:50]
    y_train_50 = y_train[:50]

    X_train_100 = X_train[:100]
    y_train_100 = y_train[:100]

    X_train_150 = X_train[:150]
    y_train_150 = y_train[:150]

    #Training the data

    #50 set
    print("Naive Bayes:")
    a1=train_predict(clf, X_train_50, y_train_50, X_test, y_test)

    print("Support Vector Machines:")
    a2=train_predict(clf2, X_train_50, y_train_50, X_test, y_test)

    print("Stochastic Gradient Descent:")
    a3=train_predict(clf3, X_train_50, y_train_50, X_test, y_test)

    print("Gradient Tree Boosting:")
    a4=train_predict(clf4, X_train_50, y_train_50, X_test, y_test)

    #100 set
    print("Set score details for 100 set")
    print("Naive Bayes:")
    b1=train_predict(clf, X_train_100, y_train_100, X_test, y_test)

    print("Support Vector Machines:")
    b2=train_predict(clf2, X_train_100, y_train_100, X_test, y_test)

    print("Stochastic Gradient Descent:")
    b3=train_predict(clf3, X_train_100, y_train_100, X_test, y_test)

    print("Gradient Tree Boosting:")
    b4=train_predict(clf4, X_train_100, y_train_100, X_test, y_test)

    #150 set
    print("Score details for 150 set: ")
    print("Naive Bayes 150 : ")
    c1=train_predict(clf, X_train_150, y_train_150, X_test, y_test)

    print("Support Vector Machines:")
    c2=train_predict(clf2, X_train_150, y_train_150, X_test, y_test)

    print("Stochastic Gradient Descent:")
    c3=train_predict(clf3, X_train_150, y_train_150, X_test, y_test)

    print("Gradient Tree Boosting:")
    c4=train_predict(clf4, X_train_150, y_train_150, X_test, y_test)
    graph(a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4)












