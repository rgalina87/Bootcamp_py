import datetime

cake = '''
  |:H:a:p:p:y:|
__|___________|__
|^^^^^^^^^^^^^^^^^|
|:B:i:r:t:h:d:a:y:|
|                 |
~~~~~~~~~~~~~~~~~~~
'''

candle = "i"
candle_base = "_"
spaces = 11
whitespace = "   "

def make_top_line():
	half_spaces = (spaces - last_digit) / 2
	top = whitespace + candle_base * half_spaces + candle * last_digit + candle_base * half_spaces
	return top

def getAge():
    birthDate = input("Enter your birth date (dd/mm/yyyy)\n>>> ")
    birthDate = datetime.datetime.strptime(birthDate, "%d/%m/%Y").date()
    # print(birthDate)
    currentDate = datetime.datetime.today().date()
    age = currentDate.year - birthDate.year
    monthVeri = currentDate.month - birthDate.month
    dateVeri = currentDate.day - birthDate.day

    age = int(age)
    monthVeri = int(monthVeri)
    dateVeri = int(dateVeri)

    if monthVeri < 0:
        age = age-1
    elif dateVeri < 0 and monthVeri == 0:
        age = age-1
    print(age)
    def leap_year():
        if (birthDate.year % 4) == 0:
            if (birthDate.year % 100) == 0:
                if (birthDate.year % 400) == 0:
                    print(cake)
                else:
                    print(cake)
            else:
                print(cake)
        else:
            print(cake)

age = str(getAge())#?????????
last_digit = age.slice(-1)
bcake = make_top_line() + cake
print(bcake)
# if leap_year():
#     print(bcake)