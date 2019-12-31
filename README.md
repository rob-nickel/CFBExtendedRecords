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

Halfway through the 2019 Bowl Season:

[Full Rankings](results/resultsSorted.csv)

| Rank | Logo | Name | Record | Extended Record | Extended Win Rate |
| --- | ---| --- | --- | --- | --- |
| 1 | ![Ohio State](logos/ohio-st.png) | Ohio State | 13-1 | 97-0 | 1.0 |
| 2 | ![Louisiana State](logos/lsu.png) | Louisiana State | 14-0 | 96-0 | 1.0 |
| 3 | ![Clemson](logos/clemson.png) | Clemson | 14-0 | 87-0 | 1.0 |
| 4 | ![Florida](logos/florida.png) | Florida | 10-2 | 48-2 | 0.96 |
| 5 | ![Penn State](logos/penn-st.png) | Penn State | 11-2 | 71-3 | 0.95946 |
| 6 | ![Oklahoma](logos/oklahoma.png) | Oklahoma | 12-2 | 69-4 | 0.94521 |
| 7 | ![Alabama](logos/alabama.png) | Alabama | 10-2 | 45-3 | 0.9375 |
| 8 | ![Notre Dame](logos/notre-dame.png) | Notre Dame | 11-2 | 69-5 | 0.93243 |
| 9 | ![Air Force](logos/air-force.png) | Air Force | 11-2 | 55-4 | 0.9322 |
| 10 | ![Auburn](logos/auburn.png) | Auburn | 9-3 | 54-4 | 0.93103 |
| 11 | ![Baylor](logos/baylor.png) | Baylor | 11-2 | 54-4 | 0.93103 |
| 12 | ![Navy](logos/navy.png) | Navy | 10-2 | 50-4 | 0.92593 |
| 13 | ![Appalachian State](logos/appalachian-st.png) | Appalachian State | 13-1 | 74-6 | 0.925 |
| 14 | ![Cincinnati](logos/cincinnati.png) | Cincinnati | 10-3 | 56-5 | 0.91803 |
| 15 | ![Memphis](logos/memphis.png) | Memphis | 12-2 | 69-7 | 0.90789 |
| 16 | ![Michigan](logos/michigan.png) | Michigan | 9-3 | 56-6 | 0.90323 |
| 17 | ![Georgia](logos/georgia.png) | Georgia | 11-2 | 72-8 | 0.9 |
| 18 | ![Wisconsin](logos/wisconsin.png) | Wisconsin | 10-3 | 67-8 | 0.89333 |
| 19 | ![Utah](logos/utah.png) | Utah | 11-2 | 58-7 | 0.89231 |
| 20 | ![Oregon](logos/oregon.png) | Oregon | 11-2 | 65-8 | 0.89041 |
| 21 | ![Minnesota](logos/minnesota.png) | Minnesota | 10-2 | 45-6 | 0.88235 |
| 22 | ![Southern Methodist](logos/smu.png) | Southern Methodist | 10-3 | 50-7 | 0.87719 |
| 23 | ![Iowa](logos/iowa.png) | Iowa | 10-3 | 57-8 | 0.87692 |
| 24 | ![Florida Atlantic](logos/fla-atlantic.png) | Florida Atlantic | 11-3 | 61-9 | 0.87143 |
| 25 | ![Boise State](logos/boise-st.png) | Boise State | 12-2 | 74-11 | 0.87059 |