#Exercise 

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove(basket[0])
basket.remove(basket[-1])
basket.append('Kiwi')
basket.insert(0,"Apple")
basket.count("Apple")
basket.clear()
print(basket)

#Exercise 1

my_fav_numbers = {2, 9, 8, 7}
my_fav_numbers.add(13)
my_fav_numbers.add(33)
my_fav_numbers.remove(33)
# print(my_fav_numbers)
friend_fav_numbers = {25, 45, 20, 90}
our_fav_numbers = my_fav_numbers.copy()
our_fav_numbers.update(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 2

my_fav_numbers = (2,9,8,7)
my_fav_numbers = my_fav_numbers + (33, 13)
# print(my_fav_numbers)
friends_fav_numbers = (20,90,80,70)
our_fav_numbers = my_fav_numbers + friends_fav_numbers
print(our_fav_numbers)

#Exercise 3

2, 3, 5, 100 - int
2.2, 55.7, 33.6 - float

#Exercise 4

topping = input("Enter a topping:" '''
(if you finish enter 'quit')
''')

while topping != ("quit"):
    print("You add" + " " + topping)
    topping = input("Enter a toppping: ")
print(topping)

#Exercise 6

list = [33, 45, 68, 99]
list.reverse()
print(list)

#Exercise 7

get_age = input("How old are you?\n")
get_age = int(get_age)
total = 0
for x in get_age:
    if x < 3:
        total = 0
    elif 3 < x > 12:
        total = 10
    elif x > 12:
        total = 15
print(total)

#Exercise 8

numbers = []
while numbers % 2 == 0:
	print(numbers)

#Exercise 9

teenagers = []
allowed_people = []
for allowed_people in teenagers:
    age = input("How old are you?\n")
    age = int(age)
    if age <= 16 or age >= 20:
        allowed_people.append(people)
        print("You can watch this movie")
print()


#Exercise 10

visit = ["ID", "Ego", "Superego", "Alterego"]
visit_copy = visit.copy()
total = 0
for persone in visit:
    get_age = input("How old are you?\n")
    get_age = int(get_age)
    if get_age < 16:
        visit_copy.remove(persone)
print()
