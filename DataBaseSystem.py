import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import DataGenerationSystem
from operator import itemgetter
import math
# Author Nathan Fenwick
# This python file is responsible for reading a users transactions from fire store
# manipulating the read data into useful forms for ML
# Storing predicted spending

def initialiseDBConnection():
    cred = credentials.Certificate('stuBankPrivateKey.json')
    firebase_admin.initialize_app(cred)


def getTransactions(userEmail):
    transactionList = []
    db = firestore.client()
    collections = db.collection('Students').document(userEmail).collections()
    for collection in collections:
        if collection.id == "Transactions":
            for doc in collection.stream():
                transaction = doc.to_dict()
                temp = [transaction["amount"], transaction["category"], transaction["dayOfWeek"],
                        transaction["timeDiff"]]
                transactionList.append(temp)
    return transactionList


def splitTransactions(transactionList):
    transport = []
    groceries = []
    eatingOut = []
    entertainment = []
    bills = []
    uni = []
    shopping = []
    for transaction in transactionList:
        if transaction[1] == "Transport":
            transport.append(transaction)
        elif transaction[1] == "Groceries":
            groceries.append(transaction)
        elif transaction[1] == "Eating Out":
            eatingOut.append(transaction)
        elif transaction[1] == "Entertainment":
            entertainment.append(transaction)
        elif transaction[1] == "Bills":
            bills.append(transaction)
        elif transaction[1] == "University":
            uni.append(transaction)
        elif transaction[1] == "Shopping":
            shopping.append(transaction)
        else:
            pass
    return transport, groceries, eatingOut, entertainment, bills, uni, shopping


def calculateAvgDay(currentList):
    # If less than 2 transactions for category return 0s since prediction cant be made.
    if len(currentList) < 2:
        return 0, 0
    # Sort list of transactions from lowest to highest
    currentList = sorted(currentList, key=itemgetter(3), reverse=True)
    # Reversed so its now highest to lowest in terms of timeDiff
    # Sets highest as first transaction timeDiff since it should be latest transaction.
    # Sets dow as dayOfWeek of latest transaction
    deltaDay = 0
    highest = currentList[0][3]
    dow = currentList[0][2]
    previousDay = currentList[0][3]
    # next(currentList)
    for item in currentList[1:len(currentList)]:
        # In case first transaction is not actually the latest this adjusts highest and dow to be that of the latest.
        if highest < item[3]:
            highest = item[3]
            dow = item[2]
        # Sums the difference in timeDiff between transactions.
        deltaDay += (previousDay - item[3])
        # Adjusts previous day for next iteration.
        previousDay = item[3]
    # Calculates the average difference in days between transactions.
    avgDeltaDay = deltaDay / len(currentList)
    avgDeltaDay = math.floor(avgDeltaDay)
    # Adjusts highest to now be the timeDiff of the future transaction to be predicted.
    highest += avgDeltaDay
    # Works out the day of the week for the future transaction to be predicted.
    dow = DataGenerationSystem.adjustDayOfWeek(dow, avgDeltaDay)
    return highest, dow


def getUserBalance(userEmail):
    db = firestore.client()
    results = db.collection('Students').document(userEmail).get()
    items = results.to_dict()
    return items["balance"]


def storePredictions(userEmail, userPredictions):
    db = firestore.client()
    for count in range(0, len(userPredictions)):
        db.collection('Students').document(userEmail).collection('Predictions').document(userPredictions[count][0]).set(
            {'timeDiff': userPredictions[count][1], 'predictedAmount': userPredictions[count][2]})
