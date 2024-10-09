import pandas as pd
import csv
import sys
import os
import datetime

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 2000)

position = 1
arguments = len(sys.argv)-1

def get_year():
   return 2024
    # if len(sys.argv) > 1 and sys.argv[1] in map(str, range(2019, 2025)):
    #     return int(sys.argv[1])
    # else:
    #     current_year = datetime.date.today().year
    #     current_month = datetime.date.today().month
    #     if current_month <= 6:
    #         return current_year - 1
    #     else:
    #         return current_year

# Year URLs
# 2019: "https://www.sports-reference.com/cfb/years/2019-schedule.html"
# 2020: "https://www.sports-reference.com/cfb/years/2020-schedule.html"
# 2021 "https://www.sports-reference.com/cfb/years/2021-schedule.html"
# 2022 "https://www.sports-reference.com/cfb/years/2022-schedule.html"
# 2023 "https://www.sports-reference.com/cfb/years/2023-schedule.html"
# 2024 "https://www.sports-reference.com/cfb/years/2024-schedule.html"

year = get_year()
url = f"https://www.sports-reference.com/cfb/years/{year}-schedule.html"

# Load data
data = pd.read_html(url,header=0,index_col=0)
print(url)


with open('data/testRecord.csv', 'w') as output:
    for item in data:
        item.to_csv(output)
with open('data/testRecord.csv', 'r') as inp, open(f'data/record{year}.csv', 'w') as output:
    writer = csv.writer(output)
    writer.writerow(['Rk','Wk','Winner','WPts','Loc','Loser','LPts'])
    for row in csv.reader(inp):
        if row[0] != 'Rk':
            writer.writerow([row[0], row[1], row[5], row[6], row[7], row[8], row[9]])

if os.path.exists('data/testRecord.csv'):
    os.remove('data/testRecord.csv')

print(f'record{year}.csv has been updated')
