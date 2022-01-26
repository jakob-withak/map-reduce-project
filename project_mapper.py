# Mapper for CSC582 Project
# Authors: Jakob Smith and Jacob Schuh
import sys
import csv

reader = csv.reader(sys.stdin, delimiter=',')
# hold our global sales data
sales = 0.0

for line in reader:
    try:
        # try to cast as a float
        sales = float(line[9])
    except:
        continue
    # print out publisher name, tab, global sales
    print(line[4], "\t", round(sales, 2))
