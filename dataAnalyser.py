import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os
from pathlib import Path
"""
Student Performance Analyzer (CLI) – Built a Python
command-line application using pandas and matplotlib
to analyze CSV datasets, generate summary statistics,
identify top and bottom performers, and visualize results 
through bar charts.
"""
parser=argparse.ArgumentParser(description="csv analyser")
parser.add_argument("--file",type=str)
args=parser.parse_args()

def createAndEditCsv():

    args.file=Path(args.file)
    if not os.path.exists(args.file):
        print("file not found")
        return
    if args.file.suffix.lower()!=".csv":
        print("csv files only")
        return

    dd=pd.read_csv(args.file)
    dd.index=range(1,len(dd)+1)
    #print(dd)
    print("===== STUDENT REPORT =====")
    print("Total students:",dd['Marks'].count(),"\n")
    print(f"Average Marks:{dd['Marks'].mean():.2f}")
    print("Highest marks:",dd['Marks'].max())
    print("Lowest marks:",dd['Marks'].min())
    max_row=dd.loc[dd['Marks'].idxmax()]
    print("Top student:",max_row['Name'],"(",dd['Marks'].max(),")")
    min_row=dd.loc[dd['Marks'].idxmin()]
    print("Lowest student:",min_row['Name'],"(",dd['Marks'].min(),")")
    print("\nAdditional Statistics:\n")
    print("total marks of all students: ",dd['Marks'].sum())
    scored_above_average=dd.loc[dd['Marks']>dd['Marks'].mean()]
    print("Students score above average:",scored_above_average['Name'].count())
    print("==========================")
    plt.bar(dd['Name'],dd['Marks'])
    plt.title("Marks scored by students")
    plt.xlabel("Name")
    plt.ylabel("Marks")
    plt.show()

createAndEditCsv()


"""
inputted in cli:  python main.py --file students.csv

input in students.csv:

     Name  Marks
1     Ali     80
2    Sara     95
3    John     70
4   Aisha     85
5   David     60
6  Fatima     92

output:
===== STUDENT REPORT =====
Total students: 6

Average Marks:80.33
Highest marks: 95
Lowest marks: 60
Top student: Sara ( 95 )
Lowest student: David ( 60 )

Additional Statistics:

total marks of all students:  482
Students score above average: 3
==========================


"""
