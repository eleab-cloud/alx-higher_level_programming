#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
print(f"last digit of {number} is {last} and ", end="")
if last > 5:
    print(f"is greater than 5")
elif last == 0:
    print(f"is 0")
else:
    print(f"is not 0")
