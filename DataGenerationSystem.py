import numpy
# Author Nathan Fenwick
# This system will be responsible for generating data entries for the transactions-groceries.csv
# This will generate amount, previous balance and timeDiff


def CategorySelection(numTotalSets, numIterations, model):
    groceries = [5, 10, 7, 15, 10, 18, 14, 24, 22, 33, 32, 40, 41, 45]
    transport = [1, 3, 1, 3, 2, 4, 2, 4, 3, 5, 5, 7, 6, 8]
    eatOut = [4, 6, 4, 6, 4, 8, 4, 8, 5, 9, 9, 13, 10, 20, 10, 20]
    entertainment = [1, 3, 1, 3, 2, 5, 2, 5, 5, 15, 10, 20, 11, 21]
    shopping = [5, 10, 5, 10, 7, 12, 7, 12, 10, 30, 25, 50, 25, 50]
    bills = [1600, 1750]
    uni = [3000, 3150]
    if model == "groceriesModel.pickle":
        return generateDataSetDayOfWeek(numTotalSets, numIterations, groceries)
    elif model == "transportModel.pickle":
        return generateDataSetDayOfWeek(numTotalSets, numIterations, transport)
    elif model == "eatingOut.pickle":
        return generateDataSetDayOfWeek(numTotalSets, numIterations, eatOut)
    elif model == "entertainment.pickle":
        return generateDataSetDayOfWeek(numTotalSets, numIterations, entertainment)
    elif model == "shopping.pickle":
        return generateDataSetDayOfWeek(numTotalSets, numIterations, shopping)
    elif model == "bills.pickle":
        return generateDataSetTimeDiff(numTotalSets, numIterations, bills)
    else:
        return generateDataSetTimeDiff(numTotalSets, numIterations, uni)


def generateDataSetTimeDiff(numTotalSets, numIterations, spendingRange):
    items = []
    for x in range(numIterations):
        category = "N/A"
        date = "N/A"
        name = "N/A"
        reference = "N/A"
        timeDiff = 0
        # Start by generating starting balance and store it
        newBalance = valueGenerator(300, 2000)
        dayOfWeek = valueGenerator(0, 6)
        # For loop to generate amount, newBalance/previousBalance and time diff and append this list to items
        for y in range(int(numTotalSets / numIterations)):
            previousBalance = newBalance
            if previousBalance <= 0:
                break
            newDayDiff = valueGenerator(100, 130)
            timeDiff += newDayDiff
            dayOfWeek = adjustDayOfWeek(dayOfWeek, newDayDiff)

            amount = valueGenerator(spendingRange[0], spendingRange[1])

            newBalance = adjustPreviousBalance(previousBalance, amount)
            items.append([amount, category, date, name, newBalance, previousBalance, reference, timeDiff, dayOfWeek])
    return items


def generateDataSetDayOfWeek(numTotalSets, numIterations, spendingRange):
    items = []
    for x in range(numIterations):
        category = "N/A"
        date = "N/A"
        name = "N/A"
        reference = "N/A"
        timeDiff = 0
        # Start by generating starting balance and store it
        newBalance = valueGenerator(300, 2000)
        dayOfWeek = valueGenerator(0, 6)
        # For loop to generate amount, newBalance/previousBalance and time diff and append this list to items
        for y in range(int(numTotalSets / numIterations)):
            previousBalance = newBalance
            if previousBalance <= 0:
                break
            newDayDiff = valueGenerator(3, 7)
            timeDiff += newDayDiff
            dayOfWeek = adjustDayOfWeek(dayOfWeek, newDayDiff)
            amount = amountGenerator(dayOfWeek, spendingRange)
            newBalance = adjustPreviousBalance(previousBalance, amount)
            items.append([amount, category, date, name, newBalance, previousBalance, reference, timeDiff, dayOfWeek])
    return items


def valueGenerator(minimum, maximum):
    return numpy.random.randint(minimum, maximum)


# Takes current balance and adjusts it to be stored as newBalance
def adjustPreviousBalance(previousBalance, amount):
    return previousBalance - amount


def adjustDayOfWeek(dayOfWeek, newDayDiff):
    dayOfWeek += newDayDiff
    if dayOfWeek > 6:
        count = dayOfWeek // 6
        dayOfWeek = dayOfWeek - (count * 6)
    return dayOfWeek


def amountGenerator(dayOfWeek, amountGenVals):
    if dayOfWeek == 0:
        return valueGenerator(amountGenVals[0], amountGenVals[1])
    if dayOfWeek == 1:
        return valueGenerator(amountGenVals[2], amountGenVals[3])
    elif dayOfWeek == 2:
        return valueGenerator(amountGenVals[4], amountGenVals[5])
    elif dayOfWeek == 3:
        return valueGenerator(amountGenVals[6], amountGenVals[7])
    elif dayOfWeek == 4:
        return valueGenerator(amountGenVals[8], amountGenVals[9])
    elif dayOfWeek == 5:
        return valueGenerator(amountGenVals[10], amountGenVals[11])
    elif dayOfWeek == 6:
        return valueGenerator(amountGenVals[12], amountGenVals[13])
