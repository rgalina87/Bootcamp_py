#Exercise 1
line_1 = "Hello world"
print(line_1 * 4)

#Exercise 2
print((99^3) * 8) #768


#Exercise 3
name = 'Gali'
age = 33
shoe_size = "don't know"
info = "My name is {} and I'm {} years old. I {} my shoe size!".format(name, age, shoe_size)
print(info)

#Exercise 4
computer_brand = "Sony Vaio"
print("i have a razer computer" " " +computer_brand)

#Exerise 5
5 > 3 #True
3 == 3 #True
3 == "3" #False
"3" > 3 #Error
"Hello" == "hello"#False

#Exercise 6
hight = input("What is your hight?")
hight = int(hight)
if hight >= 35:
	print("You can ride")
else:
	print("Soory you can't ride")	

#Exercise 7
number = input("Set a number")
number = int(number)
if(number %2) ==0:
	print("Number is even")
else:
	print("Number is odd")