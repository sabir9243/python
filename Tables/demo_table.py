#this file demonstrates how table.py works
#this file takes a csv file reads it as a dictionary and prints table on command window

import table
import csv

d=[]
with open('Tables\data.csv') as file:
    f=csv.DictReader(file)
    for dict in f :
        d.append(dict)

t=table.table(d)
t.print_table()