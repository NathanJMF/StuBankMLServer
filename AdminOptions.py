import DataGenerationSystem
import CSVSystem
import MachineLearningSystem
import DataBaseSystem
import ServerSystem
# Author Nathan Fenwick
# This python file is responsible for running admin commands
# this is so that the admin can manually update a user's prediction without the server
# Generate and store a new data set for selected category
# Retrain, test and compare the ML models

def main():
    DataBaseSystem.initialiseDBConnection()
    while True:
        print("\nAdmin inputs:\n"
              "1) Manual update prediction\n"
              "2) Generate and store new dataset\n"
              "3) Retrain model and store it\n"
              "4) Test model\n"
              "5) Compare model\n"
              "6) Exit\n")
        userInput = input()
        if userInput == "1":
            print("Enter the email of the account you would like to update predictions for:")
            userEmail = input()
            userPredictions = ServerSystem.getUserPredictions(userEmail)
            DataBaseSystem.storePredictions(userEmail, userPredictions)
        elif userInput == "2":
            model, dataset = getCategory()
            items = DataGenerationSystem.CategorySelection(15000, 500, model)
            CSVSystem.appendCSV(dataset, items)
        elif userInput == "3":
            model, dataset = getCategory()
            MachineLearningSystem.trainModel(model, dataset)
        elif userInput == "4":
            model, dataset = getCategory()
            MachineLearningSystem.testModel(model, dataset)
        elif userInput == "5":
            model, dataset = getCategory()
            MachineLearningSystem.compareModel(model, dataset)
        elif userInput == "6":
            exit()
        else:
            print("Please enter a valid input")


def getUserValues():
    currentBalance = None
    timeDiff = None
    dayOfWeek = None
    while True:
        try:
            print("Please enter your current balance")
            currentBalance = int(input())
            print("Please enter the time diff")
            timeDiff = int(input())
            print("Please enter day of week")
            dayOfWeek = int(input())
        except ValueError:
            print("Please enter valid values")
            continue
        if not (0 <= dayOfWeek <= 6):
            print("Please enter a valid dayOfWeek")
            continue
        else:
            break
    return currentBalance, timeDiff, dayOfWeek


def getCategory():
    while True:
        print("Please select a category:\n"
              "1) Transport\n"
              "2) Groceries\n"
              "3) Eating out\n"
              "4) Entertainment\n"
              "5) Bills\n"
              "6) University\n"
              "7) Shopping"
              # "8) General"
              )
        userInput = input()
        if userInput == "1":
            return "transportModel.pickle", "transaction-transport.csv"
        elif userInput == "2":
            return "groceriesModel.pickle", "transaction-groceries.csv"
        elif userInput == "3":
            return "eatingOut.pickle", "transaction-eatingOut.csv"
        elif userInput == "4":
            return "entertainment.pickle", "transaction-entertainment.csv"
        elif userInput == "5":
            return "bills.pickle", "transaction-bills.csv"
        elif userInput == "6":
            return "university.pickle", "transaction-university.csv"
        elif userInput == "7":
            return "shopping.pickle", "transaction-shopping.csv"
        else:
            print("Please enter a valid input")


if __name__ == '__main__':
    main()
