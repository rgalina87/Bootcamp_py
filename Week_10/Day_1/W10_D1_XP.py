#Exercise 1

import 


#Exercise 2

import random

def num():
    given_num = int(input("Enter a number\n>>>"))
    random_number = random.randint(1, 100)
    print(random_number)
    if given_num == random_number:
        return "Success"
    else:
        return "Try again"
print(num())


# Exercise 3
# import random
# import string
#
# def randomString(stringLength):
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for i in range(stringLength))
#
# print(randomString(5))