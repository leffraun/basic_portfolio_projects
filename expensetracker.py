"""
create an expense tracker using csv
"""
import csv
from datetime import datetime
file="customers.csv"
with open(file,"w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["name","mail","time"])

n=int(input("how many:"))
with open(file,"a",newline="") as f:
    writer=csv.writer(f)
    for i in range(n):
        name=input("name:")
        mail=input("mail:")
        time=datetime.now().strftime("%Y-%m-%d")
        writer.writerow([name,mail,time])
print(name,mail,time)
