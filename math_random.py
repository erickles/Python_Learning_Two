import math

value = 4.35

print(math.floor(value))

print(math.ceil(value))

print(round(value))

print(round(4.51))

print(math.pi)

print(math.e)

print(math.log(100,10))

print(math.sin(10))

print(math.degrees(math.pi/2))

print(math.radians(180))

import random

print(random.randint(0,100))

random.seed(101)

print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))

my_list = list(range(0,20))

the_choices = random.choices(population=my_list,k=10)

print(the_choices)

print(random.uniform(a=0,b=100))

print(random.gauss(mu=0,sigma=1))
