"""
CFB Extended Record

Rob Nickel

Description: This program ranks each team by extended record
   Extended Record: Each team's wins = wins of opponents they beat, team's losses = losses of opponents they lost to

Possible command arguments: 'noFCS' 'printA' 'printS' 'printC' 'printAll'

url = 'https://www.sports-reference.com/cfb/years/2019-schedule.html'
"""

import csv
import sys
import numpy as np

# Wins	Losses	Extended Wins	Extended Losses
my_array = np.zeros([130,4], dtype=int)
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
        return (float(aac[0])/float(aac[1]))
    elif conferenceName == 'acc':
        return (float(acc[0])/float(acc[1]))
    elif conferenceName == 'b10':
        return (float(b10[0])/float(b10[1]))
    elif conferenceName == 'b12':
        return (float(b12[0])/float(b12[1]))
    elif conferenceName == 'cusa':
        return (float(cusa[0])/float(cusa[1]))
    elif conferenceName == 'mac':
        return (float(mac[0])/float(mac[1]))
    elif conferenceName == 'mw':
        return (float(mw[0])/float(mw[1]))
    elif conferenceName == 'p12':
        return (float(p12[0])/float(p12[1]))
    elif conferenceName == 'sb':
        return (float(sb[0])/float(sb[1]))
    elif conferenceName == 'sec':
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
        return (float(aac[2])/float(aac[3]))
    elif conferenceName == 'acc':
        return (float(acc[2])/float(acc[3]))
    elif conferenceName == 'b10':
        return (float(b10[2])/float(b10[3]))
    elif conferenceName == 'b12':
        return (float(b12[2])/float(b12[3]))
    elif conferenceName == 'cusa':
        return (float(cusa[2])/float(cusa[3]))
    elif conferenceName == 'mac':
        return (float(mac[2])/float(mac[3]))
    elif conferenceName == 'mw':
        return (float(mw[2])/float(mw[3]))
    elif conferenceName == 'p12':
        return (float(p12[2])/float(p12[3]))
    elif conferenceName == 'sb':
        return (float(sb[2])/float(sb[3]))
    elif conferenceName == 'sec':
        return (float(sec[2])/float(sec[3]))
    else:
        return 1

# Returns true unless a command line argument 'noFCS' is included
def includeFCS():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position] == 'noFCS':
            return False
        position += 1
    return True

# Returns false unless the commandline argument printA is included
def printAlphabetical():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position] == 'printA' or sys.argv[position] == 'printAll':
            return True
        position += 1
    return False

# Returns false unless the commandline argument printS is included
def printSorted():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position] == 'printS' or sys.argv[position] == 'printAll':
            return True
        position += 1
    return False

# Prints a team's info to the terminal
def printTeam(teamInfo):
    if (len(str(teamInfo[1])) <= 5 ):
        print(f'{teamInfo[0]}\t{teamInfo[1]}: \t\t\t{teamInfo[2]}-{teamInfo[3]}  {teamInfo[4]}-{teamInfo[5]}  {teamInfo[6]}')
    elif (len(str(teamInfo[1])) <= 13):
        print(f'{teamInfo[0]}\t{teamInfo[1]}: \t\t{teamInfo[2]}-{teamInfo[3]}  {teamInfo[4]}-{teamInfo[5]}  {teamInfo[6]}')
    elif (str(teamInfo[1]) == 'Middle Tennessee State'):
        print(f'{teamInfo[0]}\t{teamInfo[1]}: {teamInfo[2]}-{teamInfo[3]}  {teamInfo[4]}-{teamInfo[5]}  {teamInfo[6]}')
    else:
        print(f'{teamInfo[0]}\t{teamInfo[1]}: \t{teamInfo[2]}-{teamInfo[3]}  {teamInfo[4]}-{teamInfo[5]}  {teamInfo[6]}')

# Prints each conference's rating to the terminal
def printConferenceRecords():
    position = 1
    arguments = len(sys.argv)-1
    while (arguments >= position):
        if sys.argv[position] == 'printC' or sys.argv[position] == 'printAll':
                print('aac  = ' + str(float(aac[0])/float(aac[1])) + '  |   aac = ' + str(float(aac[2])/float(aac[3])))
                print('acc  = ' + str(float(acc[0])/float(acc[1])) + '  |   acc = ' + str(float(acc[2])/float(acc[3])))
                print('b10  = ' + str(float(b10[0])/float(b10[1])) + '  |   b10 = ' + str(float(b10[2])/float(b10[3])))
                print('b12  = ' + str(float(b12[0])/float(b12[1])) + '  |   b12 = ' + str(float(b12[2])/float(b12[3])))
                print('cusa = ' + str(float(cusa[0])/float(cusa[1])) + '  |  cusa = ' + str(float(cusa[2])/float(cusa[3])))
                print('mac  = ' + str(float(mac[0])/float(mac[1])) + '  |   mac = ' + str(float(mac[2])/float(mac[3])))
                print('mw   = ' + str(float(mw[0])/float(mw[1])) + '  |    mw = ' + str(float(mw[2])/float(mw[3])))
                print('p12  = ' + str(float(p12[0])/float(p12[1])) + '  |   p12 = ' + str(float(p12[2])/float(p12[3])))
                print('sb   = ' + str(float(sb[0])/float(sb[1])) + '  |    sb = ' + str(float(sb[2])/float(sb[3])))
                print('sec  = ' + str(float(sec[0])/float(sec[1])) + '  |   sec = ' + str(float(sec[2])/float(sec[3])) + '\n')
        position += 1

# Cycles through all games and tabs teams' current records
def gatherRecords():
    with open('data/record.txt', mode='r') as csv_record:
        csv_reader = csv.DictReader(csv_record)
        game_count = 0
        FCS = includeFCS()
        for game in csv_reader:
            if (game["Pts"] == None or game["Pts"] == ""):
                print(f'\tExiting Loop...')
                break
            
            winnerName = removeRanking(game["Winner"])
            loserName = removeRanking(game["Loser"])

            with open('data/teams.txt', mode='r') as csv_teams:
                teamsList = csv.DictReader(csv_teams)
                rowCount = 0
                winFound = False
                loseFound = False
                winIndex = 0
                loseIndex = 0
                for row in teamsList:
                    if winnerName == row["name"]:
                        my_array[rowCount][0] += 1
                        winFound = True
                        winIndex = rowCount
                        conferenceWin(row['conference'])
                        if (winFound and loseFound):
                            break
                    elif loserName == row["name"]:
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
        print(f'Processed {game_count - 1} games.')

# Cycles through each game of the season again and applies the extended wins and losses accordingly
def gatherERecords():
    with open('data/record.txt', mode='r') as csv_record:
        csv_reader = csv.DictReader(csv_record)
        game_count = 0
        for game in csv_reader:
            if (game["Pts"] == None or game["Pts"] == ""):
                print(f'\tExiting Loop...')
                break

            # Removes rankings from front of team names
            winnerName = removeRanking(game["Winner"])
            loserName = removeRanking(game["Loser"])

            with open('data/teams.txt', mode='r') as csv_teams:
                teamsList = csv.DictReader(csv_teams)
                rowCount = 0
                winFound = False
                loseFound = False
                winIndex = 0
                loseIndex = 0
                winConf = ''
                loseConf = ''
                for row in teamsList:
                    #print(f'trying {row["name"]} with {winnerName} and {loserName}')
                    if winnerName == row["name"]:
                        winIndex = rowCount
                        winFound = True
                        winConf = row['conference']
                    elif loserName == row["name"]:
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
                    elif (loseFound and row["name"] == "FCS"):
                        my_array[loseIndex][3] += (my_array[loseIndex][0] + my_array[loseIndex][1])
                        break
                    elif (winFound and row["name"] == "FCS"):
                        break
                    rowCount += 1
            game_count += 1
        print(f'Updated {((game_count - 1) * 2)} extended records.')

# Outputs a csv file with each team, wins, losses, extended wins, extended losses, and extended percentage
def outputAlphabetical():
    with open('results/resultsAlphabetical.csv', mode='w') as csv_out:
        csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['logo','name','wins','losses','extended_wins','extended_losses','extended_rating'])

        with open('data/teams.txt', mode='r') as csv_teams:
            teamsListFinal = csv.DictReader(csv_teams)
            rowCount = 0
            toPrint = printAlphabetical()
            for row in teamsListFinal:
                if row['name'] == 'FCS':
                    break
                percentage = float(my_array[rowCount][2]) /float((my_array[rowCount][2] + my_array[rowCount][3]))
                percentage = round(percentage, 5)
                logo = 'logos/' + row['abbreviation'] + '.png'
                if toPrint:
                    printRow = ((rowCount + 1), row["name"], (my_array[rowCount][0]), my_array[rowCount][1], my_array[rowCount][2], my_array[rowCount][3], percentage)
                    printTeam(printRow) #Prints all teams to terminal alphabetically
                csvrow = [logo, row["name"], my_array[rowCount][0], my_array[rowCount][1], my_array[rowCount][2], my_array[rowCount][3], percentage]
                csv_writer.writerow(csvrow)
                rowCount += 1

    print("The output is finished\n")

# Takes the alphabetical list and sorts it by extended rating, extended wins, wins
def outputSorted():
    with open('results/resultsAlphabetical.csv', mode='r') as csv_result:
        csv_reader = csv.DictReader(csv_result)
        sortedlist = sorted(csv_reader, key=lambda row:(row['extended_losses'],row['losses']))
        sortedlist = sorted(sortedlist, key=lambda row:(row['extended_rating'],row['extended_wins'],row['wins'], ), reverse=True)
        with open('results/resultsSorted.csv', mode='w') as csv_out:
            csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['rank','logo','name','wins','losses','extended_wins','extended_losses','extended_rating'])
            rowCount = 1
            toPrint = printSorted()
            for row in sortedlist:
                if toPrint:
                    printRow = (rowCount, row["name"], row["wins"], row["losses"], row["extended_wins"], row["extended_losses"], row["extended_rating"])
                    printTeam(printRow) #Prints all teams to terminal by ranking
                csvrow = [rowCount, row["logo"], row["name"], row["wins"], row["losses"], row["extended_wins"], row["extended_losses"], row["extended_rating"]]
                csv_writer.writerow(csvrow)
                rowCount += 1

    print("The sorted output is finished\n")

def main():
    gatherRecords()
    gatherERecords()
    outputAlphabetical()
    outputSorted()
    printConferenceRecords()

main()