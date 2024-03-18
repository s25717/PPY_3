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

# Task 5: Exceptions
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range cannot be less than start")
        return [math.sqrt(x**2) for x in range(start, end)]

try:
    print("Task 5:", SquareGenerator().generate_squares(10, 1))
except ValueError as e:
    print("Task 5:", e)

# Task 6: Modules
# Create a new file named square_generator.py and move the SquareGenerator class there.

filename = "square_generator.py"
with open(filename, 'w') as file:
    file.write("class SquareGenerator:\n")
    file.write("    def generate_squares(self, start, end):\n")
    file.write("        if end < start:\n")
    file.write("            raise ValueError(\"End of range cannot be less than start\")\n")
    file.write("        return [x**2 for x in range(start, end)]\n")

print(f"Class 'SquareGenerator' moved to the file '{filename}' successfully.")