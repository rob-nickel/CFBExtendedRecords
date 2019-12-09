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
*   update `data/record.txt` from https://www.sports-reference.com/cfb/years/2019-schedule.html
*   then execute `python3 cfbExtendedRecord.py`
    *   Command line argument `noFCS` removes FCS games from all records
    *   Command line argument `rating` adds a rating to each team using their record, extended record, conference's record and conference's extended record

## Current Rankings

After the 2019 conference championships:

[Full Rankings](results/resultsSorted.csv)

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate |
| --- | ---| --- | --- | --- | --- |
| 1 | ![Ohio State](logos/ohio-st.png) | Ohio State | 13-0 | 94-0 | 1.0 |
| 2 | ![Louisiana State](logos/lsu.png) | Louisiana State | 13-0 | 83-0 | 1.0 |
| 3 | ![Clemson](logos/clemson.png) | Clemson | 13-0 | 72-0 | 1.0 |
| 4 | ![Penn State](logos/penn-st.png) | Penn State | 10-2 | 55-2 | 0.96491 |
| 5 | ![Cincinnati](logos/cincinnati.png) | Cincinnati | 10-3 | 55-2 | 0.96491 |
| 6 | ![Baylor](logos/baylor.png) | Baylor | 11-2 | 54-2 | 0.96429 |
| 7 | ![Florida](logos/florida.png) | Florida | 10-2 | 48-2 | 0.96 |
| 8 | ![Oklahoma](logos/oklahoma.png) | Oklahoma | 12-1 | 69-4 | 0.94521 |
| 9 | ![Memphis](logos/memphis.png) | Memphis | 12-1 | 68-4 | 0.94444 |
| 10 | ![Southern Methodist](logos/smu.png) | Southern Methodist | 10-2 | 49-3 | 0.94231 |
| 11 | ![Air Force](logos/air-force.png) | Air Force | 10-2 | 48-3 | 0.94118 |
| 12 | ![Navy](logos/navy.png) | Navy | 9-2 | 44-3 | 0.93617 |
| 13 | ![Alabama](logos/alabama.png) | Alabama | 10-2 | 44-3 | 0.93617 |
| 14 | ![Boise State](logos/boise-st.png) | Boise State | 12-1 | 71-5 | 0.93421 |
| 15 | ![Auburn](logos/auburn.png) | Auburn | 9-3 | 52-4 | 0.92857 |
| 16 | ![Appalachian State](logos/appalachian-st.png) | Appalachian State | 12-1 | 64-5 | 0.92754 |
| 17 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 10-2 | 61-5 | 0.92424 |
| 18 | ![Wisconsin](logos/wisconsin.png) | Wisconsin | 10-3 | 64-6 | 0.91429 |
| 19 | ![Michigan](logos/michigan.png) | Michigan | 9-3 | 53-5 | 0.91379 |
| 20 | ![Utah](logos/utah.png) | Utah | 11-2 | 57-6 | 0.90476 |
| 21 | ![Georgia](logos/georgia.png) | Georgia | 11-2 | 69-8 | 0.8961 |
| 22 | ![Oregon](logos/oregon.png) | Oregon | 11-2 | 64-8 | 0.88889 |
| 23 | ![Minnesota](logos/minnesota.png) | Minnesota | 10-2 | 44-6 | 0.88 |
| 24 | ![Florida Atlantic](logos/fla-atlantic.png) | Florida Atlantic | 10-3 | 51-7 | 0.87931 |
| 25 | ![Iowa](logos/iowa.png) | Iowa | 9-3 | 49-8 | 0.85965 |