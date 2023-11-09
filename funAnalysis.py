import csv
import sys
import numpy as np
import os

def teamFileName():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == '2019':
            return 'data/teams2021.txt'
        if sys.argv[position].lower() == '2020':
            return 'data/teams2021.txt'
        if sys.argv[position].lower() == '2021':
            return 'data/teams2021.txt'
        if sys.argv[position].lower() == '2022':
            return 'data/teams2022.txt'
        position += 1
    return 'data/teams2023.txt'

def numTeams():
    return (len(open(teamFileName()).readlines()))

# Analyze Predictions for the given year.
def toPrint(string):
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == string:
            return True
        position += 1
    return False

def printBoringAndWild():
    if not toPrint('boring'):
        return
    with open('results/resultsSorted.csv', mode='r') as csv_result:
        sortedlist = csv.DictReader(csv_result)
        my_array = np.zeros([numTeams(),4], dtype=int)
        rowCount=0
        # print("\n| Rank | Logo | Name | Record | Extended Record | Extended Win Rate |")
        # print("| --- | :---: | --- | --- | --- | --- |")
        # for row in sortedlist:
        #     my_array[rowCount][0]=row['rank']
        #     my_array[rowCount][1]=row['extended_wins']
        #     my_array[rowCount][2]=row['extended_losses']
        #     my_array[rowCount][3]=(my_array[rowCount][1])+my_array[rowCount][2]
        sortArray = sorted(sortedlist, key=lambda row:int(row['extended_losses'])+int(row['extended_wins'])) 
        print('\nRank: Team -> Extended games: (Wins-Losses)   Games: (Wins-Losses)')
        for row in sortArray:
            print(str(rowCount+1) + ': ' + str(row['name']) + ' -> ' + str(int(row['extended_losses'])+int(row['extended_wins'])) + ': ' + str(row['extended_wins']) + '-' + str(row['extended_losses']) + '   ('+str(row['wins'])+'-'+str(row['losses'])+')' )
            rowCount=rowCount+1
        

def main():
    printBoringAndWild()
        
    print("All finished\n")

main()