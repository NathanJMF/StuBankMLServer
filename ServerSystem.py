import MachineLearningSystem
import DataBaseSystem
import socket

# Author Nathan Fenwick
# This python file is responsible for  starting the server and all required functionality


def runServer():
    soc = socket.socket()
    host = "192.168.55.10"
    port = 2004
    soc.bind((host, port))
    soc.listen(5)
    DataBaseSystem.initialiseDBConnection()
    print("Server started!")
    # Checking if a client has sent a message to the server.
    # On message receive read transactions for user
    # Predict user future spending using ML
    # Store predictions in firestore for user
    while True:
        conn, addr = soc.accept()
        print("Got connection from", addr)
        length_of_message = int.from_bytes(conn.recv(2), byteorder='big')
        msg = conn.recv(length_of_message).decode("UTF-8")
        print(msg)
        userPredictions = getUserPredictions(msg)
        DataBaseSystem.storePredictions(msg, userPredictions)
        print("Updated predictions for", msg)
        message_to_send = "Completed".encode("UTF-8")
        conn.send(len(message_to_send).to_bytes(2, byteorder='big'))
        conn.send(message_to_send)


def getUserPredictions(userEmail):
    dayCounters = []
    userPredictions = []
    allCategories = ["Transport", "Groceries", "Eating Out", "Entertainment", "Bills", "University", "Shopping"]
    # Retrieves all user transactions as a list of lists
    allUserTransactions = DataBaseSystem.getTransactions(userEmail)
    # Splits the retrieved transactions into a list of lists by category
    transport, groceries, eatingOut, entertainment, bills, uni, shopping = DataBaseSystem.splitTransactions(
        allUserTransactions)
    Categories = [transport, groceries, eatingOut, entertainment, bills, uni, shopping]
    # Iterates through all categories and works out a possible future dayOfWeek and timeDiff
    # for predicting each category.
    for category in Categories:
        highest, dow = DataBaseSystem.calculateAvgDay(category)
        dayCounters.append([highest, dow])
    # Gets user balance for predictions
    userBalance = DataBaseSystem.getUserBalance(userEmail)
    # Starts machine learning here
    models = ["transportModel.pickle", "groceriesModel.pickle", "eatingOut.pickle", "entertainment.pickle",
              "bills.pickle", "university.pickle", "shopping.pickle"]
    for count in range(0, len(models)):
        if dayCounters[count][0] or dayCounters[count][1] != 0:
            x = MachineLearningSystem.prepareUserRecord(userBalance, dayCounters[count][0], dayCounters[count][1])
            prediction = MachineLearningSystem.predictUserRecord(x, models[count])
            userPredictions.append([allCategories[count], dayCounters[count][0], prediction])
        else:
            userPredictions.append([allCategories[count], 0, 0])
    return userPredictions


if __name__ == '__main__':
    runServer()
