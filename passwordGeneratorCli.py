"""
create a 12-15 digit password as you can in cli
"""
import random
import string
import argparse
def create_password(length,symbols,digits):
    try:
        password=[]
        for i in range(length):
            choice=random.randint(1,3)
            match choice:
                case 1:
                    if symbols:
                        password.append(random.choice(string.punctuation))
                    else:
                        password.append(random.choice(string.ascii_letters))
                case 2:
                    password.append(random.choice(string.ascii_letters))
                case 3:
                    if digits:
                        password.append(random.choice(string.digits))
                    else:
                        password.append(random.choice(string.ascii_letters))
        random.shuffle(password)
        return "".join(password)


    except:
        print("error in password creation")

parser=argparse.ArgumentParser(description="password generator")
parser.add_argument("--length",default=12, type=int, help="length")
parser.add_argument("--symbols",action="store_true",help="include symbols")
parser.add_argument("--digits",action="store_true",help="include digits")

args=parser.parse_args()
length=args.length if args.length else random.randint(12,15)


print(create_password(length,args.symbols,args.digits))
#pls try in cli

