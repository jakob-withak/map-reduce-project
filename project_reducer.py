# Reducer for CSC582 Project
# Authors: Jakob Smith and Jacob Schuh
import sys
import csv

# set up our current key and sales
current_key = sys.stdin.readline().split('\t')[0]
current_sales = float(sys.stdin.readline().split('\t')[1])
for line in sys.stdin:
    # check to see if we are still on same publisher
    key = line.split('\t')[0]
    if key == current_key:
        # add count together
        sales = float(line.split('\t')[1])
        current_sales += sales
    else:
        # new publisher so print out our result
        print(current_key, "\t", round(current_sales, 2))
        # set publisher to be current key and pickup sales
        current_key = key
        current_sales = float(line.split('\t')[1])
# just in case
print(current_key, "\t", round(current_sales, 2))
