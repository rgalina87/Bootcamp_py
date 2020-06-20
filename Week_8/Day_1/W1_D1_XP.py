#Exercise 1
class Cat():
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def oldest(self):
        self.max_age = max(self.age)
        print("The oldest cat is {} yaers old".format(self.max_age))

cat1 = Cat("Athos", 5)
cat2 = Cat("Porthos", 2)
cat3 = Cat("Aramis", 4)


#Exercise 2
class Dog():
	def __init__(self, name_dog, height_dog):
		self.name_dog = name_dog
		self.height_dog = height_dog
	def talk(self):
		print("Wouaf")

	# def jump(self):
    #     pass

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)


print(davids_dog.name_dog, davids_dog.height_dog, "cm")
print(sarahs_dog.name_dog, sarahs_dog.height_dog, "cm")


		
