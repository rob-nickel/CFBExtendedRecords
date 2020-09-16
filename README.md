# CFB Extended Records

This is an algorithm used to rank college football teams using only who each team has played and who won.

*   This is an attempt to remove any preseason bias and emphasize teams' records
*   This removes any recency bias by weighing a week 1 win the same as a week 11 win
*   This doesn't make any distinction between close wins or blowouts, as Herm Edwards said best "You play to win the game"
*   An Extended Record is a combination of extended wins and extended losses
    *   Extended Wins = # of wins of opponents they beat
    *   Extended Losses = # of losses of opponents who beat them
    *   Extended Win Rate = Extended Wins / (Extended Wins + Extended Losses)

To run the program: 
*   run `cfbExtendedRecord.py`
    *   Adding command line argument `noFCS` removes FCS games from all records
    *   Adding command line argument `rating` adds a rating to each team using their record, extended record, conference's record and conference's extended record
*   run `updateCSV.py` to update `data/record.csv` from https://www.sports-reference.com/cfb/years/2019-schedule.html

## Current Rankings

[Full Rankings](results/resultsSorted.csv)

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate |
| --- | :---: | --- | --- | --- | --- |
| 1 | ![Memphis](logos/memphis.png) | Memphis | 1-0 | 1-0 | 1.0 |
| 2 | ![Miami (FL)](logos/miami-fl.png) | Miami (FL) | 1-0 | 1-0 | 1.0 |
| 3 | ![Texas](logos/texas.png) | Texas | 1-0 | 1-0 | 1.0 |
| 4 | ![Tulane](logos/tulane.png) | Tulane | 1-0 | 1-0 | 1.0 |
| 5 | ![Kansas State](logos/kansas-st.png) | Kansas State | 0-1 | 0-1 | 0.0 |
| 6 | ![Southern Mississippi](logos/southern-miss.png) | Southern Mississippi | 0-1 | 0-1 | 0.0 |
| 7 | ![Army](logos/army.png) | Army | 2-0 | 0-0 | 0 |
| 8 | ![Appalachian State](logos/appalachian-st.png) | Appalachian State | 1-0 | 0-0 | 0 |
| 9 | ![Brigham Young](logos/byu.png) | Brigham Young | 1-0 | 0-0 | 0 |
| 10 | ![Clemson](logos/clemson.png) | Clemson | 1-0 | 0-0 | 0 |
| 11 | ![Coastal Carolina](logos/coastal-caro.png) | Coastal Carolina | 1-0 | 0-0 | 0 |
| 12 | ![Georgia Southern](logos/ga-southern.png) | Georgia Southern | 1-0 | 0-0 | 0 |
| 13 | ![Georgia Tech](logos/georgia-tech.png) | Georgia Tech | 1-0 | 0-0 | 0 |
| 14 | ![Louisiana](logos/la-lafayette.png) | Louisiana | 1-0 | 0-0 | 0 |
| 15 | ![Louisville](logos/louisville.png) | Louisville | 1-0 | 0-0 | 0 |
| 16 | ![Marshall](logos/marshall.png) | Marshall | 1-0 | 0-0 | 0 |
| 17 | ![North Carolina](logos/north-carolina.png) | North Carolina | 1-0 | 0-0 | 0 |
| 18 | ![North Texas](logos/north-texas.png) | North Texas | 1-0 | 0-0 | 0 |
| 19 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 1-0 | 0-0 | 0 |
| 20 | ![Oklahoma](logos/oklahoma.png) | Oklahoma | 1-0 | 0-0 | 0 |
| 21 | ![Pittsburgh](logos/pittsburgh.png) | Pittsburgh | 1-0 | 0-0 | 0 |
| 22 | ![Southern Methodist](logos/smu.png) | Southern Methodist | 1-0 | 0-0 | 0 |
| 23 | ![South Florida](logos/south-fla.png) | South Florida | 1-0 | 0-0 | 0 |
| 24 | ![Texas Tech](logos/texas-tech.png) | Texas Tech | 1-0 | 0-0 | 0 |
| 25 | ![Texas-San Antonio](logos/utsa.png) | Texas-San Antonio | 1-0 | 0-0 | 0 |

## With Ratings

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate | Rating |
| --- | :---: | --- | --- | --- | --- | --- |
| 1 | ![Memphis](logos/memphis.png) | Memphis | 1-0 | 1-0 | 1.0 | 1.05 |
| 2 | ![Miami (FL)](logos/miami-fl.png) | Miami (FL) | 1-0 | 1-0 | 1.0 | 1.05 |
| 3 | ![Tulane](logos/tulane.png) | Tulane | 1-0 | 1-0 | 1.0 | 1.05 |
| 4 | ![Texas](logos/texas.png) | Texas | 1-0 | 1-0 | 1.0 | 1.01667 |
| 5 | ![Clemson](logos/clemson.png) | Clemson | 1-0 | 0-0 | 0 | 0.6 |
| 6 | ![Georgia Tech](logos/georgia-tech.png) | Georgia Tech | 1-0 | 0-0 | 0 | 0.6 |
| 7 | ![Louisville](logos/louisville.png) | Louisville | 1-0 | 0-0 | 0 | 0.6 |
| 8 | ![North Carolina](logos/north-carolina.png) | North Carolina | 1-0 | 0-0 | 0 | 0.6 |
| 9 | ![Pittsburgh](logos/pittsburgh.png) | Pittsburgh | 1-0 | 0-0 | 0 | 0.6 |
| 10 | ![Southern Methodist](logos/smu.png) | Southern Methodist | 1-0 | 0-0 | 0 | 0.6 |
| 11 | ![South Florida](logos/south-fla.png) | South Florida | 1-0 | 0-0 | 0 | 0.6 |
| 12 | ![Oklahoma](logos/oklahoma.png) | Oklahoma | 1-0 | 0-0 | 0 | 0.56667 |
| 13 | ![Texas Tech](logos/texas-tech.png) | Texas Tech | 1-0 | 0-0 | 0 | 0.56667 |
| 14 | ![West Virginia](logos/west-virginia.png) | West Virginia | 1-0 | 0-0 | 0 | 0.56667 |
| 15 | ![Appalachian State](logos/appalachian-st.png) | Appalachian State | 1-0 | 0-0 | 0 | 0.56 |
| 16 | ![Coastal Carolina](logos/coastal-caro.png) | Coastal Carolina | 1-0 | 0-0 | 0 | 0.56 |
| 17 | ![Georgia Southern](logos/ga-southern.png) | Georgia Southern | 1-0 | 0-0 | 0 | 0.56 |
| 18 | ![Louisiana](logos/la-lafayette.png) | Louisiana | 1-0 | 0-0 | 0 | 0.56 |
| 19 | ![Army](logos/army.png) | Army | 2-0 | 0-0 | 0 | 0.55 |
| 20 | ![Brigham Young](logos/byu.png) | Brigham Young | 1-0 | 0-0 | 0 | 0.55 |
| 21 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 1-0 | 0-0 | 0 | 0.55 |
| 22 | ![Marshall](logos/marshall.png) | Marshall | 1-0 | 0-0 | 0 | 0.49167 |
| 23 | ![North Texas](logos/north-texas.png) | North Texas | 1-0 | 0-0 | 0 | 0.49167 |
| 24 | ![Texas-San Antonio](logos/utsa.png) | Texas-San Antonio | 1-0 | 0-0 | 0 | 0.49167 |
| 25 | ![Arkansas State](logos/arkansas-st.png) | Arkansas State | 1-1 | 0-0 | 0 | 0.335 |


## After the 2019 Season:

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate |
| --- | :---: | --- | --- | --- | --- |
| 1 | ![Louisiana State](logos/lsu.png) | Louisiana State | 15-0 | 114-0 | 1.0 |
| 2 | ![Clemson](logos/clemson.png) | Clemson | 14-1 | 88-0 | 1.0 |
| 3 | ![Ohio State](logos/ohio-st.png) | Ohio State | 13-1 | 98-1 | 0.9899 |
| 4 | ![Florida](logos/florida.png) | Florida | 11-2 | 59-2 | 0.96721 |
| 5 | ![Penn State](logos/penn-st.png) | Penn State | 11-2 | 71-3 | 0.95946 |
| 6 | ![Navy](logos/navy.png) | Navy | 11-2 | 59-4 | 0.93651 |
| 7 | ![Oklahoma](logos/oklahoma.png) | Oklahoma | 12-2 | 70-5 | 0.93333 |
| 8 | ![Air Force](logos/air-force.png) | Air Force | 11-2 | 56-4 | 0.93333 |
| 9 | ![Alabama](logos/alabama.png) | Alabama | 11-2 | 55-4 | 0.9322 |
| 10 | ![Appalachian State](logos/appalachian-st.png) | Appalachian State | 13-1 | 76-6 | 0.92683 |
| 11 | ![Cincinnati](logos/cincinnati.png) | Cincinnati | 11-3 | 62-5 | 0.92537 |
| 12 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 11-2 | 71-6 | 0.92208 |
| 13 | ![Georgia](logos/georgia.png) | Georgia | 12-2 | 86-8 | 0.91489 |
| 14 | ![Memphis](logos/memphis.png) | Memphis | 12-2 | 73-7 | 0.9125 |
| 15 | ![Auburn](logos/auburn.png) | Auburn | 9-4 | 57-6 | 0.90476 |
| 16 | ![Baylor](logos/baylor.png) | Baylor | 11-3 | 55-6 | 0.90164 |
| 17 | ![Oregon](logos/oregon.png) | Oregon | 12-2 | 76-9 | 0.89412 |
| 18 | ![Minnesota](logos/minnesota.png) | Minnesota | 11-2 | 54-7 | 0.88525 |
| 19 | ![Southern Methodist](logos/smu.png) | Southern Methodist | 10-3 | 51-7 | 0.87931 |
| 20 | ![Florida Atlantic](logos/fla-atlantic.png) | Florida Atlantic | 11-3 | 62-9 | 0.87324 |
| 21 | ![Boise State](logos/boise-st.png) | Boise State | 12-2 | 75-11 | 0.87209 |
| 22 | ![Louisiana](logos/la-lafayette.png) | Louisiana | 11-3 | 58-9 | 0.86567 |
| 23 | ![Michigan](logos/michigan.png) | Michigan | 9-4 | 56-9 | 0.86154 |
| 24 | ![Wisconsin](logos/wisconsin.png) | Wisconsin | 10-4 | 68-11 | 0.86076 |
| 25 | ![Iowa](logos/iowa.png) | Iowa | 10-3 | 58-10 | 0.85294 |

## With Ratings

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate | Rating |
| --- | :---: | --- | --- | --- | --- | --- |
| 1 | ![Louisiana State](logos/lsu.png) | Louisiana State | 14-0 | 100-0 | 1.0 | 1.06128 |
| 2 | ![Ohio State](logos/ohio-st.png) | Ohio State | 13-1 | 93-1 | 0.98936 | 1.0093 |
| 3 | ![Clemson](logos/clemson.png) | Clemson | 13-1 | 77-0 | 1.0 | 0.98063 |
| 4 | ![Florida](logos/florida.png) | Florida | 9-2 | 50-2 | 0.96154 | 0.96215 |
| 5 | ![Penn State](logos/penn-st.png) | Penn State | 10-2 | 66-3 | 0.95652 | 0.95167 |
| 6 | ![Alabama](logos/alabama.png) | Alabama | 10-2 | 46-4 | 0.92 | 0.95028 |
| 7 | ![Georgia](logos/georgia.png) | Georgia | 11-2 | 76-8 | 0.90476 | 0.94919 |
| 8 | ![Appalachian State](logos/appalachian-st.png) | Appalachian State | 12-1 | 64-6 | 0.91429 | 0.92195 |
| 9 | ![Oklahoma](logos/oklahoma.png) | Oklahoma | 11-2 | 61-5 | 0.92424 | 0.91729 |
| 10 | ![Navy](logos/navy.png) | Navy | 10-2 | 49-4 | 0.92453 | 0.9166 |
| 11 | ![Minnesota](logos/minnesota.png) | Minnesota | 10-2 | 49-7 | 0.875 | 0.91498 |
| 12 | ![Memphis](logos/memphis.png) | Memphis | 11-2 | 66-7 | 0.90411 | 0.91318 |
| 13 | ![Oregon](logos/oregon.png) | Oregon | 11-2 | 69-9 | 0.88462 | 0.89856 |
| 14 | ![Air Force](logos/air-force.png) | Air Force | 10-2 | 46-4 | 0.92 | 0.89478 |
| 15 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 11-2 | 61-6 | 0.91045 | 0.89047 |
| 16 | ![Cincinnati](logos/cincinnati.png) | Cincinnati | 11-3 | 52-5 | 0.91228 | 0.88966 |
| 17 | ![Iowa](logos/iowa.png) | Iowa | 10-3 | 54-10 | 0.84375 | 0.87207 |
| 18 | ![Boise State](logos/boise-st.png) | Boise State | 11-2 | 64-11 | 0.85333 | 0.87055 |
| 19 | ![Baylor](logos/baylor.png) | Baylor | 10-3 | 47-6 | 0.88679 | 0.86582 |
| 20 | ![Auburn](logos/auburn.png) | Auburn | 8-4 | 49-6 | 0.89091 | 0.86219 |
| 21 | ![Southern Methodist](logos/smu.png) | Southern Methodist | 10-3 | 41-7 | 0.85417 | 0.85609 |
| 22 | ![Wisconsin](logos/wisconsin.png) | Wisconsin | 10-4 | 64-11 | 0.85333 | 0.85166 |
| 23 | ![Michigan](logos/michigan.png) | Michigan | 9-4 | 51-9 | 0.85 | 0.84027 |
| 24 | ![Utah](logos/utah.png) | Utah | 10-3 | 52-12 | 0.8125 | 0.83149 |
| 25 | ![Louisiana](logos/la-lafayette.png) | Louisiana | 10-3 | 47-9 | 0.83929 | 0.81897 |