# CFB Extended Records

This is an algorithm used to rank college football teams using only who each team has played and who won.
*27-10 on Bowl predictions for 2021*

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
    *   Adding command line argument `week##` runs the program through that week
*   run `updateCSV.py` to update `data/record.csv` from https://www.sports-reference.com/cfb/years/2022-schedule.html
    *   Add `2019`, `2020`, `2021` to use that year's data

## Current Rankings

[Full Rankings](results/resultsSorted.csv)

//To add after week 1

## With Ratings

//To add after week 1

## After the 2020 Season:

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate | Rating |
| --- | :---: | --- | --- | --- | --- | --- |
| 1 | ![Georgia](logos/georgia.png) | Georgia | 14-1 | 100-2 | 0.98039 | 1.04057 |
| 2 | ![Alabama](logos/alabama.png) | Alabama | 13-2 | 90-5 | 0.94737 | 0.99571 |
| 3 | ![Michigan](logos/michigan.png) | Michigan | 12-2 | 78-3 | 0.96296 | 0.97941 |
| 4 | ![Oklahoma](logos/oklahoma.png) | Oklahoma | 11-2 | 55-4 | 0.9322 | 0.96035 |
| 5 | ![Ohio State](logos/ohio-st.png) | Ohio State | 11-2 | 72-6 | 0.92308 | 0.95651 |
| 6 | ![Oklahoma State](logos/oklahoma-st.png) | Oklahoma State | 12-2 | 81-8 | 0.91011 | 0.95536 |
| 7 | ![Michigan State](logos/michigan-st.png) | Michigan State | 11-2 | 66-6 | 0.91667 | 0.95363 |
| 8 | ![Cincinnati](logos/cincinnati.png) | Cincinnati | 13-1 | 74-2 | 0.97368 | 0.95185 |
| 9 | ![Baylor](logos/baylor.png) | Baylor | 12-2 | 82-9 | 0.9011 | 0.9513 |
| 10 | ![Louisiana](logos/la-lafayette.png) | Louisiana | 13-1 | 69-7 | 0.90789 | 0.92636 |
| 11 | ![San Diego State](logos/san-diego-st.png) | San Diego State | 12-2 | 66-6 | 0.91667 | 0.92591 |
| 12 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 11-2 | 62-3 | 0.95385 | 0.91 |
| 13 | ![Mississippi](logos/ole-miss.png) | Mississippi | 10-3 | 55-11 | 0.83333 | 0.90055 |
| 14 | ![Kentucky](logos/kentucky.png) | Kentucky | 10-3 | 49-13 | 0.79032 | 0.88119 |
| 15 | ![Houston](logos/houston.png) | Houston | 12-2 | 50-7 | 0.87719 | 0.87629 |
| 16 | ![Clemson](logos/clemson.png) | Clemson | 10-3 | 51-7 | 0.87931 | 0.86181 |
| 17 | ![Texas-San Antonio](logos/utsa.png) | Texas-San Antonio | 12-2 | 64-9 | 0.87671 | 0.85788 |
| 18 | ![Air Force](logos/air-force.png) | Air Force | 10-3 | 45-9 | 0.83333 | 0.84885 |
| 19 | ![Pittsburgh](logos/pittsburgh.png) | Pittsburgh | 11-3 | 58-12 | 0.82857 | 0.84639 |
| 20 | ![Coastal Carolina](logos/coastal-caro.png) | Coastal Carolina | 11-2 | 39-9 | 0.8125 | 0.84635 |
| 21 | ![Wake Forest](logos/wake-forest.png) | Wake Forest | 11-3 | 60-13 | 0.82192 | 0.8434 |
| 22 | ![Iowa](logos/iowa.png) | Iowa | 10-4 | 53-13 | 0.80303 | 0.84316 |
| 23 | ![Utah State](logos/utah-st.png) | Utah State | 11-3 | 57-14 | 0.80282 | 0.84254 |
| 24 | ![Arkansas](logos/arkansas.png) | Arkansas | 9-4 | 46-13 | 0.77966 | 0.84178 |
| 25 | ![Wisconsin](logos/wisconsin.png) | Wisconsin | 9-4 | 59-14 | 0.80822 | 0.8356 |

## After the 2020 Season:

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate | Rating |
| --- | :---: | --- | --- | --- | --- | --- |
| 1 | ![Alabama](logos/alabama.png) | Alabama | 13-0 | 78-0 | 1.0 | 1.01444 |
| 2 | ![Texas A&M](logos/texas-am.png) | Texas A&M | 9-1 | 39-0 | 1.0 | 0.96944 |
| 3 | ![Coastal Carolina](logos/coastal-caro.png) | Coastal Carolina | 11-1 | 59-1 | 0.98333 | 0.9691 |
| 4 | ![Louisiana](logos/la-lafayette.png) | Louisiana | 10-1 | 55-1 | 0.98214 | 0.96516 |
| 5 | ![Brigham Young](logos/byu.png) | Brigham Young | 11-1 | 45-1 | 0.97826 | 0.95272 |
| 6 | ![Ohio State](logos/ohio-st.png) | Ohio State | 7-1 | 35-0 | 1.0 | 0.94714 |
| 7 | ![Ball State](logos/ball-st.png) | Ball State | 7-1 | 26-1 | 0.96296 | 0.94449 |
| 8 | ![Cincinnati](logos/cincinnati.png) | Cincinnati | 9-1 | 43-2 | 0.95556 | 0.93067 |
| 9 | ![Buffalo](logos/buffalo.png) | Buffalo | 6-1 | 13-1 | 0.92857 | 0.92098 |
| 10 | ![San Jose State](logos/san-jose-st.png) | San Jose State | 7-1 | 26-1 | 0.96296 | 0.92016 |
| 11 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 10-2 | 44-2 | 0.95652 | 0.90543 |
| 12 | ![Liberty](logos/liberty.png) | Liberty | 10-1 | 25-4 | 0.86207 | 0.89702 |
| 13 | ![Clemson](logos/clemson.png) | Clemson | 10-2 | 48-3 | 0.94118 | 0.89405 |
| 14 | ![Georgia](logos/georgia.png) | Georgia | 8-2 | 37-4 | 0.90244 | 0.88054 |
| 15 | ![Oklahoma](logos/oklahoma.png) | Oklahoma | 9-2 | 44-9 | 0.83019 | 0.86859 |
| 16 | ![Iowa State](logos/iowa-st.png) | Iowa State | 9-3 | 42-6 | 0.875 | 0.85807 |
| 17 | ![Appalachian State](logos/appalachian-st.png) | Appalachian State | 9-3 | 30-5 | 0.85714 | 0.83732 |
| 18 | ![Oklahoma State](logos/oklahoma-st.png) | Oklahoma State | 8-3 | 39-9 | 0.8125 | 0.81972 |
| 19 | ![Miami (OH)](logos/miami-oh.png) | Miami (OH) | 2-1 | 8-1 | 0.88889 | 0.81741 |
| 20 | ![Northwestern](logos/northwestern.png) | Northwestern | 7-2 | 25-6 | 0.80645 | 0.81629 |
| 21 | ![Southern California](logos/southern-california.png) | Southern California | 5-1 | 9-3 | 0.75 | 0.80586 |
| 22 | ![Boise State](logos/boise-st.png) | Boise State | 5-2 | 12-2 | 0.85714 | 0.80022 |
| 23 | ![Nevada](logos/nevada.png) | Nevada | 7-2 | 18-5 | 0.78261 | 0.79525 |
| 24 | ![Texas](logos/texas.png) | Texas | 7-3 | 32-9 | 0.78049 | 0.79305 |
| 25 | ![Kent State](logos/kent-st.png) | Kent State | 3-1 | 3-1 | 0.75 | 0.79241 |

## After the 2019 Season:

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