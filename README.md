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
    *   Adding command line argument `week##` runs the program through that week
*   run `updateCSV.py` to update `data/record.csv` from https://www.sports-reference.com/cfb/years/2020-schedule.html
    *   Add `2019` to use that year's data

## Current Rankings

[Full Rankings](results/resultsSorted.csv)

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate |
| --- | :---: | --- | --- | --- | --- |
| 1 | ![Coastal Carolina](logos/coastal-caro.png) | Coastal Carolina | 10-0 | 47-0 | 1.0 |
| 2 | ![Louisiana](logos/la-lafayette.png) | Louisiana | 9-1 | 41-0 | 1.0 |
| 3 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 10-0 | 39-0 | 1.0 |
| 4 | ![Alabama](logos/alabama.png) | Alabama | 9-0 | 38-0 | 1.0 |
| 5 | ![Clemson](logos/clemson.png) | Clemson | 9-1 | 37-0 | 1.0 |
| 6 | ![Brigham Young](logos/byu.png) | Brigham Young | 9-1 | 34-0 | 1.0 |
| 7 | ![Cincinnati](logos/cincinnati.png) | Cincinnati | 8-0 | 33-0 | 1.0 |
| 8 | ![Texas A&M](logos/texas-am.png) | Texas A&M | 7-1 | 23-0 | 1.0 |
| 9 | ![Ohio State](logos/ohio-st.png) | Ohio State | 5-0 | 14-0 | 1.0 |
| 10 | ![Indiana](logos/indiana.png) | Indiana | 6-1 | 12-0 | 1.0 |
| 11 | ![San Jose State](logos/san-jose-st.png) | San Jose State | 5-0 | 11-0 | 1.0 |
| 12 | ![Colorado](logos/colorado.png) | Colorado | 4-0 | 9-0 | 1.0 |
| 13 | ![Buffalo](logos/buffalo.png) | Buffalo | 4-0 | 5-0 | 1.0 |
| 14 | ![Miami (OH)](logos/miami-oh.png) | Miami (OH) | 2-1 | 5-0 | 1.0 |
| 15 | ![Southern California](logos/southern-california.png) | Southern California | 4-0 | 2-0 | 1.0 |
| 16 | ![Kent State](logos/kent-st.png) | Kent State | 3-1 | 2-0 | 1.0 |
| 17 | ![Miami (FL)](logos/miami-fl.png) | Miami (FL) | 8-1 | 34-1 | 0.97143 |
| 18 | ![Florida](logos/florida.png) | Florida | 8-1 | 26-1 | 0.96296 |
| 19 | ![Georgia](logos/georgia.png) | Georgia | 6-2 | 18-1 | 0.94737 |
| 20 | ![Marshall](logos/marshall.png) | Marshall | 7-1 | 25-2 | 0.92593 |
| 21 | ![Appalachian State](logos/appalachian-st.png) | Appalachian State | 7-3 | 18-2 | 0.9 |
| 22 | ![Tulsa](logos/tulsa.png) | Tulsa | 6-1 | 26-3 | 0.89655 |
| 23 | ![Iowa State](logos/iowa-st.png) | Iowa State | 8-2 | 33-4 | 0.89189 |
| 24 | ![Boise State](logos/boise-st.png) | Boise State | 4-1 | 8-1 | 0.88889 |
| 25 | ![Ball State](logos/ball-st.png) | Ball State | 4-1 | 7-1 | 0.875 |

## With Ratings

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate | Rating |
| --- | :---: | --- | --- | --- | --- | --- |
1 | ![Cincinnati](logos/cincinnati.png) | Cincinnati | 8-0 | 33-0 | 1.0 | 1.01131 |
2 | ![Colorado](logos/colorado.png) | Colorado | 4-0 | 9-0 | 1.0 | 1.00842 |
3 | ![Southern California](logos/southern-california.png) | Southern California | 4-0 | 2-0 | 1.0 | 1.00842 |
4 | ![Coastal Carolina](logos/coastal-caro.png) | Coastal Carolina | 10-0 | 47-0 | 1.0 | 1.00529 |
5 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 10-0 | 39-0 | 1.0 | 1.0 |
6 | ![Alabama](logos/alabama.png) | Alabama | 9-0 | 38-0 | 1.0 | 1.0 |
7 | ![Ohio State](logos/ohio-st.png) | Ohio State | 5-0 | 14-0 | 1.0 | 1.0 |
8 | ![Buffalo](logos/buffalo.png) | Buffalo | 4-0 | 5-0 | 1.0 | 1.0 |
9 | ![San Jose State](logos/san-jose-st.png) | San Jose State | 5-0 | 11-0 | 1.0 | 0.9954 |
10 | ![Clemson](logos/clemson.png) | Clemson | 9-1 | 37-0 | 1.0 | 0.96458 |
11 | ![Louisiana](logos/la-lafayette.png) | Louisiana | 9-1 | 41-0 | 1.0 | 0.96029 |
12 | ![Brigham Young](logos/byu.png) | Brigham Young | 9-1 | 34-0 | 1.0 | 0.955 |
13 | ![Miami (FL)](logos/miami-fl.png) | Miami (FL) | 8-1 | 34-1 | 0.97143 | 0.94672 |
14 | ![Texas A&M](logos/texas-am.png) | Texas A&M | 7-1 | 23-0 | 1.0 | 0.94375 |
15 | ![Indiana](logos/indiana.png) | Indiana | 6-1 | 12-0 | 1.0 | 0.93571 |
16 | ![Florida](logos/florida.png) | Florida | 8-1 | 26-1 | 0.96296 | 0.93333 |
17 | ![Tulsa](logos/tulsa.png) | Tulsa | 6-1 | 26-3 | 0.89655 | 0.90047 |
18 | ![Marshall](logos/marshall.png) | Marshall | 7-1 | 25-2 | 0.92593 | 0.89244 |
19 | ![Kent State](logos/kent-st.png) | Kent State | 3-1 | 2-0 | 1.0 | 0.8875 |
20 | ![Liberty](logos/liberty.png) | Liberty | 9-1 | 13-3 | 0.8125 | 0.87063 |
21 | ![Iowa State](logos/iowa-st.png) | Iowa State | 8-2 | 33-4 | 0.89189 | 0.86582 |
22 | ![Georgia](logos/georgia.png) | Georgia | 6-2 | 18-1 | 0.94737 | 0.86382 |
23 | ![Boise State](logos/boise-st.png) | Boise State | 4-1 | 8-1 | 0.88889 | 0.8554 |
24 | ![Ball State](logos/ball-st.png) | Ball State | 4-1 | 7-1 | 0.875 | 0.85375 |
25 | ![Miami (OH)](logos/miami-oh.png) | Miami (OH) | 2-1 | 5-0 | 1.0 | 0.85 |


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