"""
CFB Extended Record

Rob Nickel

Description: This program ranks each team by extended record
   Extended Record: Each team's wins = wins of opponents they beat, team's losses = losses of opponents they lost to

Possible command arguments: 'rating' 'noFCS' 'printA' 'printP' 'printS' 'printC' 'printR' 'printAll' '2019' '2020' '2021' '2022' '2023' '2024'

url = 'https://www.sports-reference.com/cfb/years/2023-schedule.html'
"""

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
        if sys.argv[position].lower() == '2023':
            return 'data/teams2023.txt'
        position += 1
    return 'data/teams2024.txt'

def numTeams():
    return (len(open(teamFileName()).readlines()))

def recordFileName():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == '2019':
            return 'data/record2019.csv'
        if sys.argv[position].lower() == '2020':
            return 'data/record2020.csv'
        if sys.argv[position].lower() == '2021':
            return 'data/record2021.csv'
        if sys.argv[position].lower() == '2022':
            return 'data/record2022.csv'
        if sys.argv[position].lower() == '2023':
            return 'data/record2023.csv'
        position += 1
    return 'data/record2024.csv'

def getYear():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == '2019':
            return '2019'
        if sys.argv[position].lower() == '2020':
            return '2020'
        if sys.argv[position].lower() == '2021':
            return '2021'
        if sys.argv[position].lower() == '2022':
            return '2022'
        if sys.argv[position].lower() == '2023':
            return '2023'
        position += 1
    return '2024'

# Wins	Losses	Extended Wins	Extended Losses
my_array = np.zeros([numTeams(),4], dtype=int)
aac = np.zeros([4], dtype=int)
acc = np.zeros([4], dtype=int)
b10 = np.zeros([4], dtype=int)
b12 = np.zeros([4], dtype=int)
cusa = np.zeros([4], dtype=int)
mac = np.zeros([4], dtype=int)
mw = np.zeros([4], dtype=int)
p12 = np.zeros([4], dtype=int)
sb = np.zeros([4], dtype=int)
sec = np.zeros([4], dtype=int)

def resetArrays(maxTeams):
    for i in range(0,int(maxTeams),1):
        for j in range(0,4,1):
            my_array[i][j]=0
    for i in range(0,3,1):
        aac[i] = 0
        acc[i] = 0
        b10[i] = 0
        b12[i] = 0
        cusa[i] = 0
        mac[i] = 0
        mw[i] = 0
        p12[i] = 0
        sb[i] = 0
        sec[i] = 0

# Toggles the wantRating variable if the 'rating' argument is included
def toIncludeRating():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == 'rating':
            return True
        position += 1
    return False
wantRating = toIncludeRating()

# Removes rankings from front of team names
def removeRanking(teamName):
    if teamName[2] == ')':
        return teamName[4:]
    elif teamName[3] == ')':
        return teamName[5:]
    else:
        return teamName

#Totals a conference's wins
def conferenceWin(conferenceName):
    if conferenceName == 'aac':
        aac[0] += 1
    elif conferenceName == 'acc':
        acc[0] += 1
    elif conferenceName == 'b10':
        b10[0] += 1
    elif conferenceName == 'b12':
        b12[0] += 1
    elif conferenceName == 'cusa':
        cusa[0] += 1
    elif conferenceName == 'mac':
        mac[0] += 1
    elif conferenceName == 'mw':
        mw[0] += 1
    elif conferenceName == 'p12':
        p12[0] += 1
    elif conferenceName == 'sb':
        sb[0] += 1
    elif conferenceName == 'sec':
        sec[0] += 1

#Totals a conference's losses
def conferenceLoss(conferenceName):
    if conferenceName == 'aac':
        aac[1] += 1
    elif conferenceName == 'acc':
        acc[1] += 1
    elif conferenceName == 'b10':
        b10[1] += 1
    elif conferenceName == 'b12':
        b12[1] += 1
    elif conferenceName == 'cusa':
        cusa[1] += 1
    elif conferenceName == 'mac':
        mac[1] += 1
    elif conferenceName == 'mw':
        mw[1] += 1
    elif conferenceName == 'p12':
        p12[1] += 1
    elif conferenceName == 'sb':
        sb[1] += 1
    elif conferenceName == 'sec':
        sec[1] += 1

#Returns the total winning percentage of the conference
def conferenceRating(conferenceName):
    if conferenceName == 'aac':
        if float(aac[1]==0):
            return 1
        return (float(aac[0])/float(aac[1]))
    elif conferenceName == 'acc':
        if float(acc[1]==0):
            return 1
        return (float(acc[0])/float(acc[1]))
    elif conferenceName == 'b10':
        if float(b10[1]==0):
            return 1
        return (float(b10[0])/float(b10[1]))
    elif conferenceName == 'b12':
        if float(b12[1]==0):
            return 1
        return (float(b12[0])/float(b12[1]))
    elif conferenceName == 'cusa':
        if float(cusa[1]==0):
            return 1
        return (float(cusa[0])/float(cusa[1]))
    elif conferenceName == 'mac':
        if float(mac[1]==0):
            return 1
        return (float(mac[0])/float(mac[1]))
    elif conferenceName == 'mw':
        if float(mw[1]==0):
            return 1
        return (float(mw[0])/float(mw[1]))
    elif conferenceName == 'p12':
        if float(p12[1]==0):
            return 1
        return (float(p12[0])/float(p12[1]))
    elif conferenceName == 'sb':
        if float(sb[1]==0):
            return 1
        return (float(sb[0])/float(sb[1]))
    elif conferenceName == 'sec':
        if float(sec[1]==0):
            return 1
        return (float(sec[0])/float(sec[1]))
    else:
        return 1

#Totals a conference's extended wins
def conferenceEWin(conferenceName, EWins):
    if conferenceName == 'aac':
        aac[2] += EWins
    elif conferenceName == 'acc':
        acc[2] += EWins
    elif conferenceName == 'b10':
        b10[2] += EWins
    elif conferenceName == 'b12':
        b12[2] += EWins
    elif conferenceName == 'cusa':
        cusa[2] += EWins
    elif conferenceName == 'mac':
        mac[2] += EWins
    elif conferenceName == 'mw':
        mw[2] += EWins
    elif conferenceName == 'p12':
        p12[2] += EWins
    elif conferenceName == 'sb':
        sb[2] += EWins
    elif conferenceName == 'sec':
        sec[2] += EWins

#Totals a conference's extended losses
def conferenceELoss(conferenceName, ELoss):
    if conferenceName == 'aac':
        aac[3] += ELoss
    elif conferenceName == 'acc':
        acc[3] += ELoss
    elif conferenceName == 'b10':
        b10[3] += ELoss
    elif conferenceName == 'b12':
        b12[3] += ELoss
    elif conferenceName == 'cusa':
        cusa[3] += ELoss
    elif conferenceName == 'mac':
        mac[3] += ELoss
    elif conferenceName == 'mw':
        mw[3] += ELoss
    elif conferenceName == 'p12':
        p12[3] += ELoss
    elif conferenceName == 'sb':
        sb[3] += ELoss
    elif conferenceName == 'sec':
        sec[3] += ELoss

#Returns the total winning percentage of the conference
def conferenceERating(conferenceName):
    if conferenceName == 'aac':
        if float(aac[3]==0):
            return 1
        return (float(aac[2])/float(aac[3]))
    elif conferenceName == 'acc':
        if float(acc[3]==0):
            return 1
        return (float(acc[2])/float(acc[3]))
    elif conferenceName == 'b10':
        if float(b10[3]==0):
            return 1
        return (float(b10[2])/float(b10[3]))
    elif conferenceName == 'b12':
        if float(b12[3]==0):
            return 1
        return (float(b12[2])/float(b12[3]))
    elif conferenceName == 'cusa':
        if float(cusa[3]==0):
            return 1
        return (float(cusa[2])/float(cusa[3]))
    elif conferenceName == 'mac':
        if float(mac[3]==0):
            return 1
        return (float(mac[2])/float(mac[3]))
    elif conferenceName == 'mw':
        if float(mw[3]==0):
            return 1
        return (float(mw[2])/float(mw[3]))
    elif conferenceName == 'p12':
        if float(p12[3]==0):
            return 1
        return (float(p12[2])/float(p12[3]))
    elif conferenceName == 'sb':
        if float(sb[3]==0):
            return 1
        return (float(sb[2])/float(sb[3]))
    elif conferenceName == 'sec':
        if float(sec[3]==0):
            return 1
        return (float(sec[2])/float(sec[3]))
    else:
        return 1

# Returns true unless a command line argument 'noFCS' is included
def includeFCS():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == 'nofcs':
            return False
        position += 1
    return True

# Returns the week number specified
def getWeek():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position][ 0:4 ].lower() == 'week':
            if len(sys.argv[position]) == 5:
                week = int(sys.argv[position][ 4 ])
            elif len(sys.argv[position]) == 6:
                week = int(sys.argv[position][ 4:6 ])
            else:
                week = 99
            return week
        position += 1
    return 99

# Returns false unless the commandline argument printA is included
def printAlphabetical():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == 'printa' or sys.argv[position].lower() == 'printall':
            return True
        position += 1
    return False

# Returns false unless the commandline argument printS is included
def printSorted():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == 'prints' or sys.argv[position].lower() == 'printall':
            return True
        position += 1
    return False

# Prints a team's info to the terminal
def printTeam(teamInfo):
    if wantRating:
        if (len(str(teamInfo[1])) <= 5 ):
            print(f'{teamInfo[0]}\t{teamInfo[1]}: \t\t\t{teamInfo[2]}-{teamInfo[3]}  {teamInfo[4]}-{teamInfo[5]}  {teamInfo[6]} {teamInfo[7]}')
        elif (len(str(teamInfo[1])) <= 13):
            print(f'{teamInfo[0]}\t{teamInfo[1]}: \t\t{teamInfo[2]}-{teamInfo[3]}  {teamInfo[4]}-{teamInfo[5]}  {teamInfo[6]} {teamInfo[7]}')
        elif (str(teamInfo[1]) == 'Middle Tennessee State'):
            print(f'{teamInfo[0]}\t{teamInfo[1]}: {teamInfo[2]}-{teamInfo[3]}  {teamInfo[4]}-{teamInfo[5]}  {teamInfo[6]} {teamInfo[7]}')
        else:
            print(f'{teamInfo[0]}\t{teamInfo[1]}: \t{teamInfo[2]}-{teamInfo[3]}  {teamInfo[4]}-{teamInfo[5]}  {teamInfo[6]} {teamInfo[7]}')
    else:
        if (len(str(teamInfo[1])) <= 5 ):
            print(f'{teamInfo[0]}\t{teamInfo[1]}: \t\t\t{teamInfo[2]}-{teamInfo[3]}  {teamInfo[4]}-{teamInfo[5]}  {teamInfo[6]}')
        elif (len(str(teamInfo[1])) <= 13):
            print(f'{teamInfo[0]}\t{teamInfo[1]}: \t\t{teamInfo[2]}-{teamInfo[3]}  {teamInfo[4]}-{teamInfo[5]}  {teamInfo[6]}')
        elif (str(teamInfo[1]) == 'Middle Tennessee State'):
            print(f'{teamInfo[0]}\t{teamInfo[1]}: {teamInfo[2]}-{teamInfo[3]}  {teamInfo[4]}-{teamInfo[5]}  {teamInfo[6]}')
        else:
            print(f'{teamInfo[0]}\t{teamInfo[1]}: \t{teamInfo[2]}-{teamInfo[3]}  {teamInfo[4]}-{teamInfo[5]}  {teamInfo[6]}')

# Returns false unless the commandline argument printR is included
def toPrintReadme():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == 'printr' or sys.argv[position].lower() == 'printall':
            return True
        position += 1
    return False

# prints to terminal the top 25 in a way to copy paste into the README
def printReadmeRankings():
    with open('results/resultsSorted.csv', mode='r') as csv_result:
        sortedlist = csv.DictReader(csv_result)
        print("\n| Rank | Logo | Name | Record | Extended Record | Extended Win Rate |")
        print("| --- | :---: | --- | --- | --- | --- |")
        for row in sortedlist:
            if row['rank'] == '26':
                break
            else: print(f"| {row['rank']} | ![{row['name']}]({row['logo']}) | {row['name']} | {row['wins']}-{row['losses']} | {row['extended_wins']}-{row['extended_losses']} | {row['extended_record']} |")

# prints to terminal the top 25 in a way to copy paste into the README
def printReadmeRatings():
    with open('results/resultsSorted.csv', mode='r') as csv_result:
        sortedlist = csv.DictReader(csv_result)
        print("\n| Rank | Logo | Name | Record | Extended Record | Extended Win Rate | Rating |")
        print("| --- | :---: | --- | --- | --- | --- | --- |")
        for row in sortedlist:
            if row['rank'] == '26':
                break
            else: print(f"| {row['rank']} | ![{row['name']}]({row['logo']}) | {row['name']} | {row['wins']}-{row['losses']} | {row['extended_wins']}-{row['extended_losses']} | {row['extended_record']} | {row['extended_rating']} |")

def toPrintReact():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == 'printreact' or sys.argv[position].lower() == 'printall':
            return True
        position += 1
    return False

def printReactRankings():
    with open('results/resultsSorted.csv', mode='r') as csv_result:
        sortedlist = csv.DictReader(csv_result)
        for row in sortedlist:
            if row['rank'] == '26':
                break
            elif row['rank'] == '25':
                print(f"{{rank: {row['rank']}, name: '{row['name']}', record: '{row['wins']}-{row['losses']}', extendedRecord: '{row['extended_wins']}-{row['extended_losses']}', extendedWinRate: '{row['extended_record']}'}}")
            else: print(f"{{rank: {row['rank']}, name: '{row['name']}', record: '{row['wins']}-{row['losses']}', extendedRecord: '{row['extended_wins']}-{row['extended_losses']}', extendedWinRate: '{row['extended_record']}'}},")

def printReactRatings():
    with open('results/resultsSorted.csv', mode='r') as csv_result:
        sortedlist = csv.DictReader(csv_result)
        for row in sortedlist:
            if row['rank'] == '26':
                break
            elif row['rank'] == '25':
                print(f"{{rank: {row['rank']}, name: '{row['name']}', record: '{row['wins']}-{row['losses']}', extendedRecord: '{row['extended_wins']}-{row['extended_losses']}', extendedWinRate: '{row['extended_record']}', rating: '{row['extended_rating']}'}}")
            else: print(f"{{rank: {row['rank']}, name: '{row['name']}', record: '{row['wins']}-{row['losses']}', extendedRecord: '{row['extended_wins']}-{row['extended_losses']}', extendedWinRate: '{row['extended_record']}', rating: '{row['extended_rating']}'}},")

# Prints each conference's rating to the terminal
def toPrintConference():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == 'printc' or sys.argv[position].lower() == 'printall':
            return True
        position += 1
    return False

def printConferenceRecords():
    if toPrintConference():
        print('aac  = ' + str(conferenceRating('aac')) + '  |   aac = ' + str(conferenceERating('aac')))
        print('acc  = ' + str(conferenceRating('acc')) + '  |   acc = ' + str(conferenceERating('acc')))
        print('b10  = ' + str(conferenceRating('b10')) + '  |   b10 = ' + str(conferenceERating('b10')))
        print('b12  = ' + str(conferenceRating('b12')) + '  |   b12 = ' + str(conferenceERating('b12')))
        print('cusa = ' + str(conferenceRating('cusa')) + '  |  cusa = ' + str(conferenceERating('cusa')))
        print('mac  = ' + str(conferenceRating('mac')) + '  |   mac = ' + str(conferenceERating('mac')))
        print('mw   = ' + str(conferenceRating('mw')) + '  |    mw = ' + str(conferenceERating('mw')))
        print('p12  = ' + str(conferenceRating('p12')) + '  |   p12 = ' + str(conferenceERating('p12')))
        print('sb   = ' + str(conferenceRating('sb')) + '  |    sb = ' + str(conferenceERating('sb')))
        print('sec  = ' + str(conferenceRating('sec')) + '  |   sec = ' + str(conferenceERating('sec')) + '\n')

def specialGameResult(game):
    if ((game['Winner'] == 'San Jose State') and (game['Loser'] == 'New Mexico State') and (game['WPts'] == '0')): #canceled game in 2022
        return 2
    if ((game['WPts'] == '0') and ((game['Loser'] == 'Virginia') or game['Winner'] == 'Virginia')):
        return 2
    if ((game['WPts'] == '0') and (game['Loser'] == 'Buffalo')):
        return 2
    if (game['WPts'] == '0'):
        return 2
    if ((game['WPts'] == None or game['WPts'] == '')):
        return 1
    return 0

# Cycles through all games and tabs teams' current records
def gatherRecords(predictionAnalysisWeek):
    with open(recordFileName(), mode='r') as csv_record:
        csv_reader = csv.DictReader(csv_record)
        game_count = 0
        if predictionAnalysisWeek == "":
            toWeek = getWeek()
        else:
            toWeek = int(predictionAnalysisWeek)
        FCS = includeFCS()
        for game in csv_reader:
            specGame = specialGameResult(game)
            if specGame == 2:
                continue
            if specGame == 1:
                break
            
            if int(game['Wk']) == toWeek:
                break
            winnerName = removeRanking(game['Winner'])
            loserName = removeRanking(game['Loser'])

            with open(teamFileName(), mode='r') as csv_teams:
                teamsList = csv.DictReader(csv_teams)
                rowCount = 0
                winFound = False
                loseFound = False
                winIndex = 0
                loseIndex = 0
                for row in teamsList:
                    if winnerName == row['name']:
                        my_array[rowCount][0] += 1
                        winFound = True
                        winIndex = rowCount
                        conferenceWin(row['conference'])
                        if (winFound and loseFound):
                            break
                    elif loserName == row['name']:
                        my_array[rowCount][1] += 1
                        loseFound = True
                        loseIndex = rowCount
                        conferenceLoss(row['conference'])
                        if (winFound and loseFound):
                            break
                    
                    if (loseFound and row['name'] == 'FCS' and (not FCS)):
                        my_array[loseIndex][1] += 1
                        break
                    elif (winFound and row['name'] == 'FCS' and (not FCS)):
                        my_array[winIndex][0] -= 1
                        break
                    rowCount += 1

            game_count += 1

# Cycles through each game of the season again and applies the extended wins and losses accordingly
def gatherERecords(predictionAnalysisWeek):
    with open(recordFileName(), mode='r') as csv_record:
        csv_reader = csv.DictReader(csv_record)
        game_count = 0
        if predictionAnalysisWeek == "":
            toWeek = getWeek()
        else:
            toWeek = int(predictionAnalysisWeek)
        for game in csv_reader:
            specGame = specialGameResult(game)
            if specGame == 2:
                continue
            if specGame == 1:
                break
            if int(game['Wk']) == toWeek:
                break
            # Removes rankings from front of team names
            winnerName = removeRanking(game['Winner'])
            loserName = removeRanking(game['Loser'])

            with open(teamFileName(), mode='r') as csv_teams:
                teamsList = csv.DictReader(csv_teams)
                rowCount = 0
                winFound = False
                loseFound = False
                winIndex = 0
                loseIndex = 0
                winConf = ''
                loseConf = ''
                for row in teamsList:
                    #print(f'trying {row['name']} with {winnerName} and {loserName}')
                    if winnerName == row['name']:
                        winIndex = rowCount
                        winFound = True
                        winConf = row['conference']
                    elif loserName == row['name']:
                        loseIndex = rowCount
                        loseFound = True
                        loseConf = row['conference']
                        
                    if (winFound and loseFound):
                        my_array[winIndex][2] += my_array[loseIndex][0]
                        my_array[loseIndex][3] += my_array[winIndex][1]
                        conferenceEWin(winConf, my_array[loseIndex][0])
                        conferenceELoss(loseConf, my_array[winIndex][1])
                        break
                    # if they lost to an FCS team, add the losses=total games played
                    elif (loseFound and row['name'] == 'FCS'):
                        my_array[loseIndex][3] += (my_array[loseIndex][0] + my_array[loseIndex][1])
                        break
                    elif (winFound and row['name'] == 'FCS'):
                        break
                    rowCount += 1
            game_count += 1

# Outputs a csv file with each team, wins, losses, extended wins, extended losses, and extended percentage
def outputAlphabetical():
    with open('results/resultsAlphabetical.csv', mode='w') as csv_out:
        csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['logo','name','wins','losses','extended_wins','extended_losses','extended_record'])

        with open(teamFileName(), mode='r') as csv_teams:
            teamsListFinal = csv.DictReader(csv_teams)
            rowCount = 0
            toPrint = printAlphabetical()
            for row in teamsListFinal:
                if row['name'] == 'FCS':
                    break
                denominator = float(my_array[rowCount][2] + my_array[rowCount][3])
                if denominator == 0:
                    eWinPercentage = 0
                else:
                    eWinPercentage = float(my_array[rowCount][2]) / denominator
                    eWinPercentage = round(eWinPercentage, 5)
                denominator = float(my_array[rowCount][0] + my_array[rowCount][1])
                if denominator == 0:
                    winPercentage = 0
                else:
                    winPercentage = float(my_array[rowCount][0]) / denominator
                    winPercentage = round(winPercentage, 5)
                
                logo = 'logos/' + row['abbreviation'] + '.png'

                if toPrint:
                    printRow = ((rowCount + 1), row['name'], (my_array[rowCount][0]), my_array[rowCount][1], my_array[rowCount][2], my_array[rowCount][3], eWinPercentage)
                    printTeam(printRow) #Prints all teams to terminal alphabetically
                csvrow = [logo, row['name'], my_array[rowCount][0], my_array[rowCount][1], my_array[rowCount][2], my_array[rowCount][3], eWinPercentage]
                csv_writer.writerow(csvrow)
                rowCount += 1

# Takes the alphabetical list and sorts it by extended rating, extended wins, wins
def outputSorted():
    with open('results/resultsAlphabetical.csv', mode='r') as csv_result:
        csv_reader = csv.DictReader(csv_result)
        sortedlist = sorted(csv_reader, key=lambda row:(float(row['extended_losses']),float(row['losses'])))
        sortedlist = sorted(sortedlist, key=lambda row:(float(row['extended_record']),float(row['extended_wins']),float(row['wins']), ), reverse=True)
        with open('results/resultsSorted.csv', mode='w') as csv_out:
            csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['rank','logo','name','wins','losses','extended_wins','extended_losses','extended_record'])
            rowCount = 1
            toPrint = printSorted()
            for row in sortedlist:
                if toPrint:
                    printRow = (rowCount, row['name'], row['wins'], row['losses'], row['extended_wins'], row['extended_losses'], row['extended_record'])
                    printTeam(printRow)
                csvrow = [rowCount, row['logo'], row['name'], row['wins'], row['losses'], row['extended_wins'], row['extended_losses'], row['extended_record']]
                csv_writer.writerow(csvrow)
                rowCount += 1
        
    if toPrintReadme():
        printReadmeRankings()
    if toPrintReact():
        printReactRankings()

# Outputs a csv file with each team, wins, losses, extended wins, extended losses, extended win rate, and rating
def outputAlphabeticalRating():
    with open('results/resultsAlphabetical.csv', mode='w') as csv_out:
        csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['logo','name','wins','losses','extended_wins','extended_losses','extended_record','extended_rating'])

        with open(teamFileName(), mode='r') as csv_teams:
            teamsListFinal = csv.DictReader(csv_teams)
            rowCount = 0
            toPrint = printAlphabetical()
            for row in teamsListFinal:
                if row['name'] == 'FCS':
                    break
                denominator = float(my_array[rowCount][2] + my_array[rowCount][3])
                if denominator == 0:
                    eWinPercentage = 0
                else:
                    eWinPercentage = float(my_array[rowCount][2]) / denominator
                    eWinPercentage = round(eWinPercentage, 5)
                denominator = float(my_array[rowCount][0] + my_array[rowCount][1])
                if denominator == 0:
                    winPercentage = 0
                else:
                    winPercentage = float(my_array[rowCount][0]) / denominator
                    winPercentage = round(winPercentage, 5)
                rating = (eWinPercentage * 9 + winPercentage * 9 + conferenceRating(row['conference']) + conferenceERating(row['conference'])) / 20
                rating = round(rating, 5)
                
                logo = 'logos/' + row['abbreviation'] + '.png'

                if toPrint:
                    printRow = ((rowCount + 1), row['name'], (my_array[rowCount][0]), my_array[rowCount][1], my_array[rowCount][2], my_array[rowCount][3], eWinPercentage, rating)
                    printTeam(printRow) #Prints all teams to terminal alphabetically
                csvrow = [logo, row['name'], my_array[rowCount][0], my_array[rowCount][1], my_array[rowCount][2], my_array[rowCount][3], eWinPercentage, rating]
                
                csv_writer.writerow(csvrow)
                rowCount += 1

# Takes the alphabetical list and sorts it by extended rating, extended wins, wins
def outputSortedRating():
    with open('results/resultsAlphabetical.csv', mode='r') as csv_result:
        csv_reader = csv.DictReader(csv_result)
        sortedlist = sorted(csv_reader, key=lambda row:(float(row['extended_losses']),float(row['losses'])))
        sortedlist = sorted(sortedlist, key=lambda row:(float(row['extended_record']),float(row['extended_wins']),float(row['wins']), ), reverse=True)
        sortedlist = sorted(sortedlist, key=lambda row:(float(row['extended_rating'])), reverse=True)
        with open('results/resultsSorted.csv', mode='w') as csv_out:
            csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['rank','logo','name','wins','losses','extended_wins','extended_losses','extended_record','extended_rating'])

            rowCount = 1
            toPrint = printSorted()
            for row in sortedlist:
                if toPrint:
                    printRow = (rowCount, row['name'], row['wins'], row['losses'], row['extended_wins'], row['extended_losses'], row['extended_record'], row['extended_rating'])
                    printTeam(printRow) #Prints all teams to terminal by ranking
                    
                csvrow = [rowCount, row['logo'], row['name'], row['wins'], row['losses'], row['extended_wins'], row['extended_losses'], row['extended_record'], row['extended_rating']]
                
                csv_writer.writerow(csvrow)
                rowCount += 1
        
    if toPrintReadme():
        printReadmeRatings()
    if toPrintReact():
        printReactRatings()

# Uses the sorted results to predict winners next week.
def toPrintPredict():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == 'printp' or sys.argv[position].lower() == 'printall' or sys.argv[position].lower() == 'printanalyze':
            return True
        position += 1
    return False

def predictNextWeek(predictionAnalysisWeek):
    if not toPrintPredict():
        return
    with open(recordFileName(), mode='r') as csv_record:
        csv_reader = csv.DictReader(csv_record)
        game_count = 0
        printOutput = False
        if predictionAnalysisWeek == "":
            week = str(getWeek()+1) #next week's predictions
            printOutput = True
        else:
            week = str(predictionAnalysisWeek)
        if printOutput:
            print("\nPredictions for the next week:")
        with open('results/predict.csv', mode='w') as csv_out:
            csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['Rk','Wk','Winner','Loser'])

            for game in csv_reader:
                specGame = specialGameResult(game)
                if specGame == 2:
                    continue
                if specGame == 1:
                    if week == str(100):
                        week = game['Wk']
                        if printOutput:
                            print(f"Week {week}:")
                if game['Wk'] == week:
                    name1 = removeRanking(game['Winner'])
                    name2 = removeRanking(game['Loser'])
                    winnerName = ''
                    loserName = ''
                    with open('results/resultsSorted.csv', mode='r') as csv_sorted:
                        sortedTeams = csv.DictReader(csv_sorted)
                        oneFound = False
                        for row in sortedTeams:
                            if name1 == row['name'] and (not oneFound):
                                oneFound = True
                                winnerName = name1
                            elif name2 == row['name'] and (not oneFound):
                                oneFound = True
                                winnerName = name2
                            elif name1 == row['name'] and oneFound:
                                loserName = name1
                                break
                            elif name2 == row['name'] and oneFound:
                                loserName = name2
                                break
                        if loserName == '':
                            loserName = 'an FCS team'

                    if printOutput:
                        if (len(str(winnerName)) <= 6 ):
                            print(f"\t{winnerName} \t\t\tto beat\t{loserName}.")
                        elif (len(str(winnerName)) <= 14):
                            print(f"\t{winnerName} \t\tto beat\t{loserName}.")
                        elif (str(winnerName) == 'Middle Tennessee State'):
                            print(f"\t{winnerName}  to beat\t{loserName}.")
                        else:
                            print(f"\t{winnerName} \tto beat\t{loserName}.")
                    else:
                        csvrow = [game['Rk'], game['Wk'], winnerName, loserName]
                        csv_writer.writerow(csvrow)
              
# Analyze Predictions for the given year.
def toPrintAnalyze():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position].lower() == 'printanalyze':
            return True
        position += 1
    return False

def analyzePredictions():
    if not toPrintAnalyze():
        return
    year=getYear()
    totalWeeks = 0
    with open(recordFileName(), mode='r') as csv_record:
        csv_reader = csv.DictReader(csv_record)
        for game in csv_reader:
            specGame = specialGameResult(game)
            if specGame == 2:
                continue
            if specGame == 1:
                totalWeeks = int(game['Wk']) - 1
                break
            else:
                totalWeeks = int(game['Wk'])
    results_array = np.zeros(((totalWeeks + 1), 2), dtype=int)
    results_array[1][0] = 0
    results_array[1][1] = 0
    for week in range(2, totalWeeks+1):
        resetArrays(numTeams())
        gatherRecords(week)
        gatherERecords(week)
        outputAlphabeticalRating()
        outputSortedRating()
        predictNextWeek(week)

        with open('results/predict.csv', mode='r') as csv_record:
            predict_reader = csv.DictReader(csv_record)
            for game in predict_reader:
                if ((game['Loser'] == 'an FCS team') or (game['Winner'] == 'an FCS team')):
                    continue
                with open(recordFileName(), mode='r') as result_record:
                    sorted_reader = csv.DictReader(result_record)
                    for gameResult in sorted_reader:
                        if game['Rk'] == gameResult['Rk']:
                            if game['Winner'] == removeRanking(gameResult['Winner']):
                                results_array[week][0] += 1
                            else:
                                results_array[week][1] += 1
        #print(f"Week {str(week)}: Wins {results_array[week][0]}  Losses {results_array[week][1]}  Win Rate {results_array[week][0] / (results_array[week][0] + results_array[week][1])}")
        print(f"{str(year)},{str(week)},{results_array[week][0]},{results_array[week][1]},{results_array[week][0] / (results_array[week][0] + results_array[week][1])}")
    print()

def main():
    if toPrintAnalyze():
        analyzePredictions()
    else:
        gatherRecords("")
        gatherERecords("")
        if toIncludeRating():
            outputAlphabeticalRating()
            outputSortedRating()
        else:
            outputAlphabetical()
            outputSorted()
        printConferenceRecords()
        predictNextWeek("")
    if os.path.exists('results/predict.csv'):
        os.remove('results/predict.csv')
    print("All finished\n")

main()
