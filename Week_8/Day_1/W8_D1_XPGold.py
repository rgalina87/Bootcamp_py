#Exercise 1
class Circle():
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return self.radius**2**3.14

    def area(self):
        return 2*self.radius*3.14

ncircle = Circle()
print(ncircle.area())
print(ncircle.perimeter())

#Exercise 2