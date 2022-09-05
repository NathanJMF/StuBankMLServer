import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle
# Author Nathan Fenwick
# This python file is responsible for all machine learning functionality

# This will train the model with the given data set
def trainModel(modelName, csvName):
    x_train, x_test, y_train, y_test = prepareDataSet(csvName)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    storeModel(modelName, linear)


# This will test the trained model to get it's % accuracy
def testModel(modelName, csvName):
    x_train, x_test, y_train, y_test = prepareDataSet(csvName)
    linear = readModel(modelName)
    acc = linear.score(x_test, y_test)
    acc = round(acc * 100, 2)
    print("Model accuracy: ", acc, "%")
    print("Co: ", linear.coef_)
    print("Intercept: ", linear.intercept_)


# This will get print out predicted and actual values for comparison
def compareModel(modelName, csvName):
    x_train, x_test, y_train, y_test = prepareDataSet(csvName)
    linear = readModel(modelName)
    predictions = linear.predict(x_test)
    for i in range(len(predictions)):
        print("Predicted value: ", predictions[i], "Actual value: ", y_test[i])


def prepareDataSet(csvName):
    data = pd.read_csv(csvName)
    data = data[["amount", "previousBalance", "timeDiff", "dayOfWeek"]]
    predict = "amount"
    x = np.array(data.drop([predict], 1))
    y = np.array(data[predict])
    shuffle(x, y)
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.25)
    return x_train, x_test, y_train, y_test


def prepareUserRecord(previousBalance, timeDiff, dayOfWeek):
    x_userItem = [[previousBalance, timeDiff, dayOfWeek]]
    x = np.array(x_userItem)
    return x


def predictUserRecord(x, modelName):
    linear = readModel(modelName)
    prediction = linear.predict(x)
    return round(prediction[0], 2)


def readModel(modelName):
    pickle_in = open(modelName, "rb")
    return pickle.load(pickle_in)


def storeModel(modelName, linear):
    with open(modelName, "wb") as f:
        pickle.dump(linear, f)
