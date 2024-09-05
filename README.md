# CFB Extended Records

This is an algorithm used to rank college football teams using only who each team has played and who won.
*65.9% successful predictions*

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
    *   Adding command line argument `printAll` to output all of the data
        *   `printC` to print the conference extended results
        *   `printP` to show the predictions for the next week
*   run `updateCSV.py` to update `data/record.csv` from https://www.sports-reference.com/cfb/years/2022-schedule.html
    *   Add `2019`, `2020`, `2021`, `2022`, `2023` to use that year's data

## Current Rankings

[Full Rankings](results/resultsSorted.csv)

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate |
| --- | :---: | --- | --- | --- | --- |
| 1 | ![Michigan](logos/michigan.png) | Michigan | 15-0 | 112-0 | 1.0 |
| 2 | ![Washington](logos/washington.png) | Washington | 14-1 | 103-0 | 1.0 |
| 3 | ![Florida State](logos/florida-st.png) | Florida State | 13-1 | 79-1 | 0.9875 |
| 4 | ![Georgia](logos/georgia.png) | Georgia | 13-1 | 84-2 | 0.97674 |
| 5 | ![Alabama](logos/alabama.png) | Alabama | 12-2 | 83-2 | 0.97647 |
| 6 | ![Liberty](logos/liberty.png) | Liberty | 13-1 | 73-2 | 0.97333 |
| 7 | ![Oregon](logos/oregon.png) | Oregon | 12-2 | 70-2 | 0.97222 |
| 8 | ![Ohio State](logos/ohio-st.png) | Ohio State | 11-2 | 67-2 | 0.97101 |
| 9 | ![Texas](logos/texas.png) | Texas | 12-2 | 86-4 | 0.95556 |
| 10 | ![Mississippi](logos/ole-miss.png) | Mississippi | 11-2 | 64-3 | 0.95522 |
| 11 | ![Missouri](logos/missouri.png) | Missouri | 11-2 | 66-4 | 0.94286 |
| 12 | ![Penn State](logos/penn-st.png) | Penn State | 10-3 | 57-4 | 0.93443 |
| 13 | ![Louisiana State](logos/lsu.png) | Louisiana State | 10-3 | 58-5 | 0.92063 |
| 14 | ![James Madison](logos/james-madison.png) | James Madison | 11-2 | 63-9 | 0.875 |
| 15 | ![Oklahoma](logos/oklahoma.png) | Oklahoma | 10-3 | 68-11 | 0.86076 |
| 16 | ![Memphis](logos/memphis.png) | Memphis | 10-3 | 48-8 | 0.85714 |
| 17 | ![Troy](logos/troy.png) | Troy | 11-3 | 62-11 | 0.84932 |
| 18 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 10-3 | 53-10 | 0.84127 |
| 19 | ![Tulane](logos/tulane.png) | Tulane | 11-3 | 54-11 | 0.83077 |
| 20 | ![Toledo](logos/toledo.png) | Toledo | 11-3 | 57-14 | 0.80282 |
| 21 | ![Iowa](logos/iowa.png) | Iowa | 10-4 | 57-14 | 0.80282 |
| 22 | ![Arizona](logos/arizona.png) | Arizona | 10-3 | 52-13 | 0.8 |
| 23 | ![Kansas State](logos/kansas-st.png) | Kansas State | 9-4 | 54-14 | 0.79412 |
| 24 | ![Tennessee](logos/tennessee.png) | Tennessee | 9-4 | 46-12 | 0.7931 |
| 25 | ![Miami (OH)](logos/miami-oh.png) | Miami (OH) | 11-3 | 48-14 | 0.77419 |

## With Ratings

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate | Rating |
| --- | :---: | --- | --- | --- | --- | --- |
| 1 | ![Michigan](logos/michigan.png) | Michigan | 15-0 | 112-0 | 1.0 | 1.05477 |
| 2 | ![Georgia](logos/georgia.png) | Georgia | 13-1 | 84-2 | 0.97674 | 1.03564 |
| 3 | ![Washington](logos/washington.png) | Washington | 14-1 | 103-0 | 1.0 | 1.02631 |
| 4 | ![Alabama](logos/alabama.png) | Alabama | 12-2 | 83-2 | 0.97647 | 1.00338 |
| 5 | ![Florida State](logos/florida-st.png) | Florida State | 13-1 | 79-1 | 0.9875 | 0.99789 |
| 6 | ![Mississippi](logos/ole-miss.png) | Mississippi | 11-2 | 64-3 | 0.95522 | 0.98887 |
| 7 | ![Missouri](logos/missouri.png) | Missouri | 11-2 | 66-4 | 0.94286 | 0.98331 |
| 8 | ![Oregon](logos/oregon.png) | Oregon | 12-2 | 70-2 | 0.97222 | 0.97953 |
| 9 | ![Ohio State](logos/ohio-st.png) | Ohio State | 11-2 | 67-2 | 0.97101 | 0.97249 |
| 10 | ![Texas](logos/texas.png) | Texas | 12-2 | 86-4 | 0.95556 | 0.94992 |
| 11 | ![Liberty](logos/liberty.png) | Liberty | 13-1 | 73-2 | 0.97333 | 0.94437 |
| 12 | ![Louisiana State](logos/lsu.png) | Louisiana State | 10-3 | 58-5 | 0.92063 | 0.93869 |
| 13 | ![Penn State](logos/penn-st.png) | Penn State | 10-3 | 57-4 | 0.93443 | 0.92141 |
| 14 | ![James Madison](logos/james-madison.png) | James Madison | 11-2 | 63-9 | 0.875 | 0.88419 |
| 15 | ![Oklahoma](logos/oklahoma.png) | Oklahoma | 10-3 | 68-11 | 0.86076 | 0.8677 |
| 16 | ![Arizona](logos/arizona.png) | Arizona | 10-3 | 52-13 | 0.8 | 0.86247 |
| 17 | ![Tennessee](logos/tennessee.png) | Tennessee | 9-4 | 46-12 | 0.7931 | 0.84669 |
| 18 | ![Troy](logos/troy.png) | Troy | 11-3 | 62-11 | 0.84932 | 0.84543 |
| 19 | ![Iowa](logos/iowa.png) | Iowa | 10-4 | 57-14 | 0.80282 | 0.83747 |
| 20 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 10-3 | 53-10 | 0.84127 | 0.82472 |
| 21 | ![Memphis](logos/memphis.png) | Memphis | 10-3 | 48-8 | 0.85714 | 0.81238 |
| 22 | ![Tulane](logos/tulane.png) | Tulane | 11-3 | 54-11 | 0.83077 | 0.80793 |
| 23 | ![Kansas State](logos/kansas-st.png) | Kansas State | 9-4 | 54-14 | 0.79412 | 0.8031 |
| 24 | ![Louisville](logos/louisville.png) | Louisville | 10-4 | 61-21 | 0.7439 | 0.79184 |
| 25 | ![Toledo](logos/toledo.png) | Toledo | 11-3 | 57-14 | 0.80282 | 0.79041 |

## Predictions:

| Year | Wins | Losses | Win Rate |
| --- | --- | --- | --- |
| 2019 | 514 | 258 | 66.6% |
| 2020 | 350 | 179 | 66.2% |
| 2021 | 500 | 266 | 65.3% |
| 2022 | 464 | 263 | 63.7% |
| 2023 | 609 | 292 | 67.6% |

## 2023

## With Ratings

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate | Rating |
| --- | :---: | --- | --- | --- | --- | --- |
| 1 | ![Michigan](logos/michigan.png) | Michigan | 15-0 | 112-0 | 1.0 | 1.05477 |
| 2 | ![Georgia](logos/georgia.png) | Georgia | 13-1 | 84-2 | 0.97674 | 1.03564 |
| 3 | ![Washington](logos/washington.png) | Washington | 14-1 | 103-0 | 1.0 | 1.02631 |
| 4 | ![Alabama](logos/alabama.png) | Alabama | 12-2 | 83-2 | 0.97647 | 1.00338 |
| 5 | ![Florida State](logos/florida-st.png) | Florida State | 13-1 | 79-1 | 0.9875 | 0.99789 |
| 6 | ![Mississippi](logos/ole-miss.png) | Mississippi | 11-2 | 64-3 | 0.95522 | 0.98887 |
| 7 | ![Missouri](logos/missouri.png) | Missouri | 11-2 | 66-4 | 0.94286 | 0.98331 |
| 8 | ![Oregon](logos/oregon.png) | Oregon | 12-2 | 70-2 | 0.97222 | 0.97953 |
| 9 | ![Ohio State](logos/ohio-st.png) | Ohio State | 11-2 | 67-2 | 0.97101 | 0.97249 |
| 10 | ![Texas](logos/texas.png) | Texas | 12-2 | 86-4 | 0.95556 | 0.94992 |
| 11 | ![Liberty](logos/liberty.png) | Liberty | 13-1 | 73-2 | 0.97333 | 0.94437 |
| 12 | ![Louisiana State](logos/lsu.png) | Louisiana State | 10-3 | 58-5 | 0.92063 | 0.93869 |
| 13 | ![Penn State](logos/penn-st.png) | Penn State | 10-3 | 57-4 | 0.93443 | 0.92141 |
| 14 | ![James Madison](logos/james-madison.png) | James Madison | 11-2 | 63-9 | 0.875 | 0.88419 |
| 15 | ![Oklahoma](logos/oklahoma.png) | Oklahoma | 10-3 | 68-11 | 0.86076 | 0.8677 |
| 16 | ![Arizona](logos/arizona.png) | Arizona | 10-3 | 52-13 | 0.8 | 0.86247 |
| 17 | ![Tennessee](logos/tennessee.png) | Tennessee | 9-4 | 46-12 | 0.7931 | 0.84669 |
| 18 | ![Troy](logos/troy.png) | Troy | 11-3 | 62-11 | 0.84932 | 0.84543 |
| 19 | ![Iowa](logos/iowa.png) | Iowa | 10-4 | 57-14 | 0.80282 | 0.83747 |
| 20 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 10-3 | 53-10 | 0.84127 | 0.82472 |
| 21 | ![Memphis](logos/memphis.png) | Memphis | 10-3 | 48-8 | 0.85714 | 0.81238 |
| 22 | ![Tulane](logos/tulane.png) | Tulane | 11-3 | 54-11 | 0.83077 | 0.80793 |
| 23 | ![Kansas State](logos/kansas-st.png) | Kansas State | 9-4 | 54-14 | 0.79412 | 0.8031 |
| 24 | ![Louisville](logos/louisville.png) | Louisville | 10-4 | 61-21 | 0.7439 | 0.79184 |
| 25 | ![Toledo](logos/toledo.png) | Toledo | 11-3 | 57-14 | 0.80282 | 0.79041 |

## 2022

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate | Rating |
| --- | :---: | --- | --- | --- | --- | --- |
| 1 | ![Georgia](logos/georgia.png) | Georgia | 15-0 | 111-0 | 1.0 | 1.10323 |
| 2 | ![Tennessee](logos/tennessee.png) | Tennessee | 11-2 | 72-5 | 0.93506 | 1.00478 |
| 3 | ![Michigan](logos/michigan.png) | Michigan | 13-1 | 83-2 | 0.97647 | 1.00117 |
| 4 | ![Alabama](logos/alabama.png) | Alabama | 11-2 | 67-6 | 0.91781 | 0.99702 |
| 5 | ![Ohio State](logos/ohio-st.png) | Ohio State | 11-2 | 69-1 | 0.98571 | 0.96823 |
| 6 | ![Texas Christian](logos/tcu.png) | Texas Christian | 13-2 | 81-4 | 0.95294 | 0.95806 |
| 7 | ![Penn State](logos/penn-st.png) | Penn State | 11-2 | 68-3 | 0.95775 | 0.95565 |
| 8 | ![Louisiana State](logos/lsu.png) | Louisiana State | 10-4 | 63-12 | 0.84 | 0.90266 |
| 9 | ![Oregon](logos/oregon.png) | Oregon | 10-3 | 56-5 | 0.91803 | 0.8954 |
| 10 | ![Tulane](logos/tulane.png) | Tulane | 12-2 | 76-11 | 0.87356 | 0.89182 |
| 11 | ![Troy](logos/troy.png) | Troy | 12-2 | 78-11 | 0.8764 | 0.88623 |
| 12 | ![Washington](logos/washington.png) | Washington | 11-2 | 58-13 | 0.8169 | 0.88451 |
| 13 | ![Southern California](logos/southern-california.png) | Southern California | 11-3 | 66-10 | 0.86842 | 0.88049 |
| 14 | ![Mississippi State](logos/mississippi-st.png) | Mississippi State | 9-4 | 51-12 | 0.80952 | 0.87906 |
| 15 | ![Oregon State](logos/oregon-st.png) | Oregon State | 10-3 | 54-9 | 0.85714 | 0.868 |
| 16 | ![Clemson](logos/clemson.png) | Clemson | 11-3 | 66-11 | 0.85714 | 0.86113 |
| 17 | ![Kansas State](logos/kansas-st.png) | Kansas State | 10-4 | 61-11 | 0.84722 | 0.84192 |
| 18 | ![Florida State](logos/florida-st.png) | Florida State | 10-3 | 56-13 | 0.81159 | 0.82438 |
| 19 | ![Texas-San Antonio](logos/utsa.png) | Texas-San Antonio | 11-3 | 61-12 | 0.83562 | 0.81482 |
| 20 | ![Utah](logos/utah.png) | Utah | 10-4 | 58-16 | 0.78378 | 0.81027 |
| 21 | ![South Alabama](logos/south-ala.png) | South Alabama | 10-3 | 40-11 | 0.78431 | 0.80523 |
| 22 | ![Mississippi](logos/ole-miss.png) | Mississippi | 8-5 | 44-21 | 0.67692 | 0.78477 |
| 23 | ![UCLA](logos/ucla.png) | UCLA | 9-4 | 48-17 | 0.73846 | 0.77998 |
| 24 | ![South Carolina](logos/south-carolina.png) | South Carolina | 8-5 | 46-24 | 0.65714 | 0.77587 |
| 25 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 9-4 | 59-18 | 0.76623 | 0.75634 |

## 2021:

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

## 2020:

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

## 2019:

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
