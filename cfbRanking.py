#CFB Extended Record
#
#Rob Nickel
#
#Description: This program ranks each team by extended record
#   Extended Record: Each team's wins = wins of opponents they beat, team's loses = loses of opponents they lost to

#url = 'https://www.sports-reference.com/cfb/years/2019-schedule.html'



import csv
import numpy as np

#Wins	Losses	Extended Wins	Extended Losses
my_array = np.zeros([130,4], dtype=int)

week_number = 14 # Most recent week to finish

with open('data/record.txt', mode='r') as csv_in2:
    csv_reader = csv.DictReader(csv_in2)
    game_count = 0
    for game in csv_reader:
        if (game["Wk"] == str(week_number + 1) ):
            print(f'\tExiting Loop...')
            break
        #if game_count == 0:
            #print(f'\nColumn names are {", ".join(game)}')
        
        #removes rankings from front of team names
        winnerName = game["Winner"]
        if winnerName[2] == ')':
            #print(f'name {winnerName} changed to .{winnerName[4:]}.')
            winnerName = winnerName[4:]
        elif winnerName[3] == ')':
            #print(f'name {winnerName} changed to .{winnerName[5:]}.')
            winnerName = winnerName[5:]

        loserName = game["Loser"]
        if loserName[2] == ')':
            #print(f'name {loserName} changed to .{loserName[4:]}.')
            loserName = loserName[4:]
        elif loserName[3] == ')':
            #print(f'name {loserName} changed to .{loserName[5:]}.')
            loserName = loserName[5:]

        with open('data/teams.txt', mode='r') as csv_in1:
            teamsList = csv.DictReader(csv_in1)
            rowCount = 0
            winFound = False
            loseFound = False
            for row in teamsList:
                #print(f'trying {row["Name"]} with {winnerName} and {loserName}')
                if winnerName == row["Name"]:
                    my_array[rowCount][0] += 1
                    winFound = True
                    #print(f'\tGame # {game["Rk"]}: Winner {winnerName}: {my_array[rowCount][0]}-{my_array[rowCount][1]}')
                    if (winFound and loseFound):
                        break
                elif loserName == row["Name"]:
                    my_array[rowCount][1] += 1
                    loseFound = True
                    #print(f'\tGame # {game["Rk"]}: Loser {loserName}: {my_array[rowCount][0]}-{my_array[rowCount][1]}')
                    if (winFound and loseFound):
                        break
                rowCount += 1
            

        game_count += 1
    print(f'Processed {game_count - 1} games.')

with open('data/record.txt', mode='r') as csv_in2:
    csv_reader = csv.DictReader(csv_in2)
    game_count = 0
    for game in csv_reader:
        if (game["Wk"] == '15' ):
            print(f'\tExiting Loop...')
            break
        #removes rankings from front of team names
        winnerName = game["Winner"]
        if winnerName[2] == ')':
            #print(f'name {winnerName} changed to .{winnerName[4:]}.')
            winnerName = winnerName[4:]
        elif winnerName[3] == ')':
            #print(f'name {winnerName} changed to .{winnerName[5:]}.')
            winnerName = winnerName[5:]
        loserName = game["Loser"]
        if loserName[2] == ')':
            #print(f'name {loserName} changed to .{loserName[4:]}.')
            loserName = loserName[4:]
        elif loserName[3] == ')':
            #print(f'name {loserName} changed to .{loserName[5:]}.')
            loserName = loserName[5:]

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
                #if they lost to an FCS team, add the loses=total games played
                elif (loseFound and row["Name"] == "FCS"):
                    my_array[loseIndex][3] += (my_array[loseIndex][0] + my_array[loseIndex][1])
                    break
                elif (winFound and row["Name"] == "FCS"):
                    break
                rowCount += 1




with open('results/results.txt', mode='w') as csv_out:
    csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['name','wins','loses','extended_wins','extended_loses','extended_percentage'])

    with open('data/teams.txt', mode='r') as csv_in3:
        teamsListFinal = csv.DictReader(csv_in3)
        rowCount = 0
        for row in teamsListFinal:
            if row['Name'] == 'FCS':
                break
            percentage = float(my_array[rowCount][2]) /float((my_array[rowCount][2] + my_array[rowCount][3]))
            percentage = round(percentage, 5)
            csvrow = [row["Name"], my_array[rowCount][0], my_array[rowCount][1], my_array[rowCount][2], my_array[rowCount][3], percentage]
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

with open('results/results.txt', mode='r') as csv_result:
    csv_reader = csv.DictReader(csv_result)
    sortedlist = sorted(csv_reader, key=lambda row:(row['extended_percentage'],row['extended_wins'],row['wins']), reverse=True)
    with open('results/results_sorted.txt', mode='w') as csv_out:
        csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['rank','name','wins','loses','extended_wins','extended_loses','extended_percentage'])
        rowCount = 1
        for row in sortedlist:
            csvrow = [rowCount, row["name"], row["wins"], row["loses"], row["extended_wins"], row["extended_loses"], row["extended_percentage"]]
            csv_writer.writerow(csvrow)
            rowCount += 1

print("The sorted output is finished\n")
