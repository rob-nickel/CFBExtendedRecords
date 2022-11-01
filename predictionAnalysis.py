"""
Analyzing the results of predicting games 
"""

import csv
import sys
import numpy as np
import os

year_array = np.zeros([4,4], dtype=int)
week_array = np.zeros([21,4], dtype=int)

def returnYearIndex(year):
    if (year == '2019'):
        return 0
    elif (year == '2020'):
        return 1
    elif (year == '2021'):
        return 2
    elif (year == '2020'):
        return 3
    else:
        return 3

def gameToNumber(games):
    if games == '':
        return 0
    else:
        return int(games)

# populates the year_array prediction results by year
def calcYearResults():
    with open('data/byWeek.csv', mode='r') as csv_result: # year,week,wins,losses,win-rate
        sortedlist = csv.DictReader(csv_result)

        for row in sortedlist:
            yearIndex = returnYearIndex(row['year'])
            year_array[yearIndex][0] = row['year']
            year_array[yearIndex][1] += gameToNumber(row['wins'])
            year_array[yearIndex][2] += gameToNumber(row['losses'])
        for i in range(0,len(year_array)):
            winRate = (year_array[i][1] + 1) / (year_array[i][1] + year_array[i][2] + 1)
            year_array[i][3] = winRate

# populates the week_array prediction results by week
def calcWeekResults():
    with open('data/byWeek.csv', mode='r') as csv_result: # year,week,wins,losses,win-rate
        sortedlist = csv.DictReader(csv_result)

        for row in sortedlist:
            weekIndex = int(row['week'])-2
            week_array[weekIndex][0] = row['week']
            week_array[weekIndex][1] += gameToNumber(row['wins'])
            week_array[weekIndex][2] += gameToNumber(row['losses'])
        for i in range(0,len(week_array)):
            winRate = (week_array[i][1] + 1) / (week_array[i][1] + week_array[i][2] + 1)
            week_array[i][3] = winRate


def printWeeks():
    rows = len(week_array)
    print()
    print("Week:\tWins:\tLosses:\tWin Rate:")
    print("-----------------------------------------")
    for i in range(0,rows):
        winRate = week_array[i][1] / (week_array[i][1] + week_array[i][2])
        print(f"{week_array[i][0]}\t{week_array[i][1]}\t{week_array[i][2]}\t{winRate}")
    print()

def printYears():
    rows = len(year_array)
    print("Year:\tWins:\tLosses:\tWin Rate:")
    print("-----------------------------------------")
    for i in range(0,rows):
        winRate = year_array[i][1] / (year_array[i][1] + year_array[i][2])
        print(f"{year_array[i][0]}\t{year_array[i][1]}\t{year_array[i][2]}\t{winRate}")
    print()

def printTotals():
    rows = len(year_array)
    wins = 0
    losses = 0
    print("Totals:")
    for i in range(0,rows):
        wins += year_array[i][1]
        losses += year_array[i][2]
    winRate = wins / (wins + losses)
    print(f"Correct: {wins}\tIncorrect: {losses}\tWin Rate: {winRate}")
    print()

def printSortedWeeks():
    print(week_array)

def printArrays():
    printWeeks()
    printYears()
    printTotals()
    #printSortedWeeks()

def main():
    calcYearResults()
    calcWeekResults()
    printArrays()

main()