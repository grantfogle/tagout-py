import math
from tabula import read_pdf
import re

input = '../../data/colorado/draw_reports/2023ElkDrawnOut.pdf'
output = '../../data/colorado/draw_reports/outputs/2023_elk_draw_stats.json'
pattern = r'E[EFM]\d{3}[A-Z]\d[A-Z]'
endPageText = 'Hunts shaded gray'
firstPage = 0
lastPage = 1

df = read_pdf(input, pages=1)

def isHuntCode(line):
    # Check if line is a string
    if isinstance(line, str):
        # regex match
        print('new unittttt', line)
        return re.match(pattern, line)
    else:
        return False

# def assignNewUnitStats

# Print the DataFrame
# print(df)
for table in df:
    currentUnit = ''
    counter = 1
    ### first unit row will also include grabbing data for whether unit is pref/2nd choice/third choice/etc
    ### second unit row will 
    ### stat collection

    for index, row in table.iterrows():
        # first row is the headers
        ## if divisible by 3 then skip
        ## if odd then get unit headers
        ## if even then get the stats
        if index == table.index[0] or (counter-1) % 3 == 0:
            counter += 1
            continue
        
        print('THIS GUYYYY', row.iloc[0])
        firstItem = row.iloc[0]
        if firstItem != 'NaN' and isHuntCode(row.iloc[0]):
            # assign new unit
            print('====')
            # print('NEW UNIT', row)
        else:
            # assign result data
            print('DATA COLLECTION', row)
        # value = row['Unnamed: 0']
        # valueTwo = row.iloc[1]

        print(row)
        counter += 1
        # print(value, valueTwo)
        print('----------------')

        #### are there three rows per hunt code?

        # Unnamed: 0          EE004W1R
        #Unnamed: 1                 A
        # Adult           Drawn Out At
        # Youth         9 Pref\rPoints
        # Landowner            No Apps
        # Unnamed: 2       None\rDrawn
        # Unnamed: 3           No Apps
        # Unnamed: 4               N/A
        # Unnamed: 5               N/A

    # i am going to have a tracker for each row
    # adult is what you think it is
    # print(table)
# use this command to test this script /opt/homebrew/bin/python3.10 tabula_draw_odds.py