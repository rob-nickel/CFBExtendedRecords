# CFB Extended Records

This is an algorithm used to rank college football teams using only who each team has played and who won. 

*   This is an attempt to remove any preseason bias and emphasize a teams' record
*   This removes any recency bias by weighing a week 1 win the same as a week 11 win
*   This doesn't make any distinction between close wins or blowouts. As Jim Mora said best "You play to win the game"
*   An Extended Record is a combination of extended wins and extended losses
*       Extended wins = # of wins of opponents they beat
*       Extended losses = # of losses of opponents who beat them
*       Extended rating = Extended wins / (Extended wins + Extended losses)

To run the program: 
*   update `data/record.txt` from https://www.sports-reference.com/cfb/years/2019-schedule.html
*   then execute `python3 cfbExtendedRecord.py`

## Current Rankings

After the 2019 regular season:

[Full Rankings](results/resultsSorted.csv)

| rank | logo | name | wins | losses | extended_wins | extended_losses | extended_rating |
| --- | ---| --- | --- | --- | --- | --- | --- |
| 1 |  | ![Ohio State](logos/ohio-st.png) | Ohio State | 12 | 0 | 82 | 0 | 1.0 |
| 2 |  | ![Louisiana State](logos/lsu.png) | Louisiana State | 12 | 0 | 72 | 0 | 1.0 |
| 3 |  | ![Clemson](logos/clemson.png) | Clemson | 12 | 0 | 63 | 0 | 1.0 |
| 4 |  | ![Baylor](logos/baylor.png) | Baylor | 11 | 1 | 54 | 1 | 0.98182 |
| 5 |  | ![Cincinnati](logos/cincinnati.png) | Cincinnati | 10 | 2 | 54 | 1 | 0.98182 |
| 6 |  | ![Florida](logos/florida.png) | Florida | 10 | 2 | 48 | 1 | 0.97959 |
| 7 |  | ![Penn State](logos/penn-st.png) | Penn State | 10 | 2 | 55 | 2 | 0.96491 |
| 8 |  | ![Auburn](logos/auburn.png) | Auburn | 9 | 3 | 51 | 3 | 0.94444 |
| 9 |  | ![Southern Methodist](logos/smu.png) | Southern Methodist | 10 | 2 | 49 | 3 | 0.94231 |
| 10 |  | ![Air Force](logos/air-force.png) | Air Force | 10 | 2 | 48 | 3 | 0.94118 |
| 11 |  | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 10 | 2 | 61 | 4 | 0.93846 |
| 12 |  | ![Navy](logos/navy.png) | Navy | 9 | 2 | 44 | 3 | 0.93617 |
| 13 |  | ![Alabama](logos/alabama.png) | Alabama | 10 | 2 | 44 | 3 | 0.93617 |
| 14 |  | ![Memphis](logos/memphis.png) | Memphis | 11 | 1 | 58 | 4 | 0.93548 |
| 15 |  | ![Oklahoma](logos/oklahoma.png) | Oklahoma | 11 | 1 | 58 | 4 | 0.93548 |
| 16 |  | ![Utah](logos/utah.png) | Utah | 11 | 1 | 57 | 4 | 0.93443 |
| 17 |  | ![Michigan](logos/michigan.png) | Michigan | 9 | 3 | 53 | 4 | 0.92982 |
| 18 |  | ![Boise State](logos/boise-st.png) | Boise State | 11 | 1 | 62 | 5 | 0.92537 |
| 19 |  | ![Appalachian State](logos/appalachian-st.png) | Appalachian State | 11 | 1 | 54 | 5 | 0.91525 |
| 20 |  | ![Wisconsin](logos/wisconsin.png) | Wisconsin | 10 | 2 | 64 | 6 | 0.91429 |
| 21 |  | ![Minnesota](logos/minnesota.png) | Minnesota | 10 | 2 | 44 | 5 | 0.89796 |
| 22 |  | ![Georgia](logos/georgia.png) | Georgia | 11 | 1 | 69 | 8 | 0.8961 |
| 23 |  | ![Iowa](logos/iowa.png) | Iowa | 9 | 3 | 48 | 7 | 0.87273 |
| 24 |  | ![Louisiana](logos/la-lafayette.png) | Louisiana | 10 | 2 | 47 | 7 | 0.87037 |
| 25 |  | ![Oregon](logos/oregon.png) | Oregon | 10 | 2 | 53 | 8 | 0.86885 |