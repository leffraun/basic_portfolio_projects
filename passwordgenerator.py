"""
create a 12-15 digit password with as many punctuations as you can
"""
import random
import string
num=random.randint(12,15) #randomly decide number of letters in password
def create_password(num):

    password=""
    specialCharacters=["!","?","%","$","#","&"]
    for i in range(num):
        choice=random.randint(1,2)
        match choice:
            case 1:
                specialChoice=random.choice(specialCharacters)
                password+=specialChoice
            case 2:
                password+=random.choice(string.ascii_letters)
    return password

print(create_password(num))

