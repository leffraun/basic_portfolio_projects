import csv
import os
import argparse
file="expenses.csv"
parser=argparse.ArgumentParser(description="expense tracker")
parser.add_argument("--expense",type=str, help="expense name")
parser.add_argument("--amount",type=int,default=0,help="amount for each expense")
args=parser.parse_args()
amount=args.amount
expense=args.expense

def createAndAddToCsv (file,expense,amount):
    if not os.path.exists(file) or os.stat(file).st_size==0:
        with open(file,"w",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["expenses","amount"])

    with open(file,"a",newline="") as f:
        writer=csv.writer(f)
        writer.writerow([expense,amount])
        print("-----------")
        print(f"\nADDED {expense}:{amount}\n")
    total=0
    total_expenses={}
    with open(file,"r",newline="") as f:
        reader=csv.DictReader(f)
        for row in reader:
            amt=float(row["amount"])
            name=row["expenses"]
            total+=amt
            if name not in total_expenses:
                total_expenses[name]=0
            total_expenses[name]+=amt


    print("total breakdown:")
    for name,subtotal in total_expenses.items():
        print(f"{name}:{subtotal}")
    print(f"grand total:{total}")
    print("-----------")


createAndAddToCsv(file,args.expense, args.amount)




