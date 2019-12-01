"""
CFB Extended Record

Rob Nickel

Description: This program ranks each team by extended record
   Extended Record: Each team's wins = wins of opponents they beat, team's losses = losses of opponents they lost to

url = 'https://www.sports-reference.com/cfb/years/2019-schedule.html'
"""

import csv
import numpy as np

# Wins	Losses	Extended Wins	Extended Losses
my_array = np.zeros([130,4], dtype=int)


# Removes rankings from front of team names
def removeRanking(teamName):
    if teamName[2] == ')':
        return teamName[4:]
    elif teamName[3] == ')':
        return teamName[5:]
    else:
        return teamName

# Cycles through all games and tabs teams' current records
def gatherRecords():
    with open('data/record.txt', mode='r') as csv_in2:
        csv_reader = csv.DictReader(csv_in2)
        game_count = 0
        for game in csv_reader:
            if (game["Pts"] == None or game["Pts"] == ""):
                print(f'\tExiting Loop...')
                break
            
            winnerName = removeRanking(game["Winner"])
            loserName = removeRanking(game["Loser"])

            with open('data/teams.txt', mode='r') as csv_in1:
                teamsList = csv.DictReader(csv_in1)
                rowCount = 0
                winFound = False
                loseFound = False
                for row in teamsList:
                    if winnerName == row["Name"]:
                        my_array[rowCount][0] += 1
                        winFound = True
                        if (winFound and loseFound):
                            break
                    elif loserName == row["Name"]:
                        my_array[rowCount][1] += 1
                        loseFound = True
                        if (winFound and loseFound):
                            break
                    rowCount += 1

            game_count += 1
        print(f'Processed {game_count - 1} games.')

# Cycles through each game of the season again and applies the extended wins and losses accordingly
def gatherERecords():
    with open('data/record.txt', mode='r') as csv_in2:
        csv_reader = csv.DictReader(csv_in2)
        game_count = 0
        for game in csv_reader:
            if (game["Pts"] == None or game["Pts"] == ""):
                print(f'\tExiting Loop...')
                break

            # Removes rankings from front of team names
            winnerName = removeRanking(game["Winner"])
            loserName = removeRanking(game["Loser"])

            with open('data/teams.txt', mode='r') as csv_in1:
                teamsList = csv.DictReader(csv_in1)
                rowCount = 0
                winFound = False
                loseFound = False
                winIndex = 0
                loseIndex = 0
                for row in teamsList:
                    #print(f'trying {row["Name"]} with {winnerName} and {loserName}')
                    if winnerName == row["Name"]:
                        winIndex = rowCount
                        winFound = True
                    elif loserName == row["Name"]:
                        loseIndex = rowCount
                        loseFound = True
                        
                    if (winFound and loseFound):
                        my_array[winIndex][2] += my_array[loseIndex][0]
                        my_array[loseIndex][3] += my_array[winIndex][1]
                        break
                    # if they lost to an FCS team, add the losses=total games played
                    elif (loseFound and row["Name"] == "FCS"):
                        my_array[loseIndex][3] += (my_array[loseIndex][0] + my_array[loseIndex][1])
                        break
                    elif (winFound and row["Name"] == "FCS"):
                        break
                    rowCount += 1
            game_count += 1
        print(f'Updated {((game_count - 1) * 2)} extended records.')

# Outputs a csv file with each team, wins, losses, extended wins, extended losses, and extended percentage
def outputAlphabetical():
    with open('results/resultsAlphabetical.txt', mode='w') as csv_out:
        csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['name','logo','wins','losses','extended_wins','extended_losses','extended_percentage'])

        with open('data/teams.txt', mode='r') as csv_in3:
            teamsListFinal = csv.DictReader(csv_in3)
            rowCount = 0
            for row in teamsListFinal:
                if row['Name'] == 'FCS':
                    break
                percentage = float(my_array[rowCount][2]) /float((my_array[rowCount][2] + my_array[rowCount][3]))
                percentage = round(percentage, 5)
                logo = 'logos/' + row['abbreviation'] + '.png'
                csvrow = [row["Name"], logo, my_array[rowCount][0], my_array[rowCount][1], my_array[rowCount][2], my_array[rowCount][3], percentage]
                """ To output list to terminal
                if (len(row['Name']) <= 5 ):
                    print(f'{row["Name"]}: \t\t\t{my_array[rowCount][0]}-{my_array[rowCount][1]}  {my_array[rowCount][2]}-{my_array[rowCount][3]}  {percentage}')
                elif (len(row['Name']) <= 13):
                    print(f'{row["Name"]}: \t\t{my_array[rowCount][0]}-{my_array[rowCount][1]}  {my_array[rowCount][2]}-{my_array[rowCount][3]}  {percentage}')
                elif (row['Name'] == 'Middle Tennessee State'):
                    print(f'{row["Name"]}: {my_array[rowCount][0]}-{my_array[rowCount][1]}  {my_array[rowCount][2]}-{my_array[rowCount][3]}  {percentage}')
                else:
                    print(f'{row["Name"]}: \t{my_array[rowCount][0]}-{my_array[rowCount][1]}  {my_array[rowCount][2]}-{my_array[rowCount][3]}  {percentage}')
                """
                csv_writer.writerow(csvrow)
                rowCount += 1

    print("The output is finished\n")

# Takes the alphabetical list and sorts it by extended percentage, extended wins, wins
def outputSorted():
    with open('results/resultsAlphabetical.txt', mode='r') as csv_result:
        csv_reader = csv.DictReader(csv_result)
        sortedlist = sorted(csv_reader, key=lambda row:(row['extended_losses'],row['losses']))
        sortedlist = sorted(sortedlist, key=lambda row:(row['extended_percentage'],row['extended_wins'],row['wins'], ), reverse=True)
        with open('results/resultsSorted.txt', mode='w') as csv_out:
            csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['rank','name','logo','wins','losses','extended_wins','extended_losses','extended_percentage'])
            rowCount = 1
            for row in sortedlist:
                csvrow = [rowCount, row["name"], row["logo"], row["wins"], row["losses"], row["extended_wins"], row["extended_losses"], row["extended_percentage"]]
                csv_writer.writerow(csvrow)
                rowCount += 1

    print("The sorted output is finished\n")

def main():
    gatherRecords()
    gatherERecords()
    outputAlphabetical()
    outputSorted()

main()