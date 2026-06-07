"""
create a 12-15 digit password with as many punctuations as you can
"""
"""
create a 12-15 digit password with as many punctuations as you can
"""
import random
import string
num=random.randint(12,15) #randomly decide number of letters in password
def create_password(num):

    password=""
    try:
        specialCharacters=["!","?","%","$","#","&"]
        for i in range(num):
            choice=random.randint(1,3)
            match choice:
                case 1:
                    password+=random.choice(string.punctuation)
                case 2:
                    password+=random.choice(string.ascii_letters)
                case 3:
                    password+=random.choice(string.digits)
        return password
    except:
        print("error in password creation")

print(create_password(num))

