"""
Create a CSV file from your Python program called sales.csv.

The file should contain:

Month,Sales
Jan,1200
Feb,1500
Mar,1800
Apr,1600
May,2200
Jun,2500
Your Tasks
Create the CSV file automatically using Python.
Read the CSV file back into your program.
Calculate:
Average monthly sales
Highest sales
Lowest sales
Determine:
Which month had the highest sales
Which month had the lowest sales
Print a report:
===== SALES REPORT =====

Average Sales: xxxx
Highest Sales: xxxx (Month)
Lowest Sales: xxxx (Month)

========================
Create a graph showing sales by month.

Use a line graph because:

Months have an order.
You want to see the trend over time.
"""

import pandas as pd
import matplotlib.pyplot as pyt
import csv
import os
file="sales.csv"
def createAndWriteFile(file):
    if not os.path.exists(file):
        with open(file,"w",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(['Month','Sales'])

    with open(file,'a',newline='') as f:
        writer=csv.writer(f)
        n=int(input("how many records would you like to input into the file:"))
        for i in range(n):
            month=input(f"month {i+1}")
            sales=input(f"sales {i+1}")
            writer.writerow([month,sales])
def makeGraph(file):
    graph=pd.read_csv(file)
    max_row=graph.loc[graph['Sales'].idxmax()]
    min_row=graph.loc[graph['Sales'].idxmin()]
    print("===== SALES REPORT =====")
    print("average:",graph['Sales'].mean())
    print("Highest sales:",graph['Sales'].max(),max_row['Month'])
    print("Lowest sales:",graph['Sales'].min(),min_row['Month'])
    print("========================")
    pyt.plot(graph['Month'],graph['Sales'])
    pyt.title("Sales by month")
    pyt.xlabel("month")
    pyt.ylabel("sales")
    pyt.show()

createAndWriteFile(file)
makeGraph(file)
"""
input:
Month,Sales
Jan,1200
Feb,1500
Mar,1800
Apr,1600
May,2200
Jun,2500



output:
how many records would you like to input into the file:0
===== SALES REPORT =====
average: 1800.0
Highest sales: 2500 Jun
Lowest sales: 1200 Jan
========================

Process finished with exit code 0


"""
