#Exercise 1
3 <= 3 < 9 #True
3 == 3 == 3 #True
bool(0) #False
bool(5 == "5") #False
bool(4 == 4) == bool("4" == "4") #True
bool(bool(None)) #False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
print("x is", x) #x is True
print("y is", y) #y is False
print("a:", a)   #a: 5
print("b:", b)   #b: 10

#Exercise 2
a = input()
a = int(a)
b = input()
b = int(b)
if a > b:
	print("Hello World")

#Exercise 3
season = input("Enter a month (from 1 to 12): ")
season = int(season)
if season == 3 or season == 4 or season == 5:
	print("Spring")
elif season == 6 or season == 7 or season == 8:
	print("Summer")
elif season == 9 or season == 10 or season == 11:
	print("Autumn")
elif season == 12 or season == 1 or season == 2:
	print("Winter")