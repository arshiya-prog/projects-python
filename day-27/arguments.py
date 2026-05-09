# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(1, 2, 3, 4))

# def func(**kwargs):
#     print(kwargs)

# func(add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        print(kwargs)

car = Car(make = "Nissan", model = "GT-R")
car = Car(make = "Audi", model = "Q5")
print(car.make, car.model)