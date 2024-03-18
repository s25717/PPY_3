import os

# Task 1: List Comprehensions
squares_list = [x**2 for x in range(1, 11)]
print("Task 1:", squares_list)

# Task 2: Functions
def generate_squares(start, end):
    return [x**2 for x in range(start, end)]

print("Task 2:", generate_squares(1, 11))

# Task 3: Classes
class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end)]

print("Task 3:", SquareGenerator().generate_squares(1, 11))

# Task 4: Libraries
import math

class SquareGenerator:
    def generate_squares(self, start, end):
        return [math.sqrt(x**2) for x in range(start, end)]

print("Task 4:", SquareGenerator().generate_squares(1, 11))
