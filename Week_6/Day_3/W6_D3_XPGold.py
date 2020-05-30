#Exercise 1
You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

Sort based on name
Then sort based on age
Then sort by score

#Exercise 2

guest_name = input("Guest name is ")
waiter_name = input("Waiter name is ")
item_name = input("Item name is ")
price = input("Price of the item is ")
price = int(price)
amount = input("Amount of item is ")
amount = int(amount)
discount = input("Discount is ")
discount = int(discount) #code for discount
total = price * amount
if (discount > 0):
    print(total)
else:
    print(total - discount)
vat = total * 1.17 # not exactly what i want
print("Including VAT",  vat)

#Exercise 3

number1 = input("Enter number ")
number1 = int(number)
number2 = input("Enter number ")
number2 = int(number2)
number3 = input("Enter number ")
number3 = int(number3)
if (number1 >= numnumber2) and (number1 >= number3):
   largest = number1
elif (number2 >= number1) and (number2 >= number3):
   largest = number2
else:
   largest = number3
print("The largest number is", largest)

#Exercise 4

letter = input("Enter a letter: ")

if(letter == 'A' or letter == 'a' or letter == 'E' or letter == 'e' or letter =='I'
 or letter == 'i' or letter == 'O' or letter == 'o' or letter == 'U' or letter == 'u'):
    print(letter, "is a Vowel")
else:
    print(letter, "is a Consonant")

#Exercise 5

import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')

#Exercise 6

numbers = list(range(1, 21))

for number in numbers:
    print(number)

#Exercise 7

millions = range(1,1000001)
for million in millions:
    print(million)

#Exercise 8

max( millions )
min( millions )
print("Sum of elements is :", sum(millions))

#Exercise 9

Write a program that returns the index of the first occurrence of an item in a list.

#Exercise 10

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
	for x in list2:
		list1.append(x)
		