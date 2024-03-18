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

# 7
# Task 7: Packages
# Specify the package directory
package_directory = "square_package"
if not os.path.exists(package_directory):
    os.makedirs(package_directory)

# Create an empty __init__.py file in the package directory
init_file_path = os.path.join(package_directory, "__init__.py")
open(init_file_path, 'a').close()

# Move the square_generator.py file into the package directory
square_generator_file_path = "square_generator.py"
os.rename(square_generator_file_path, os.path.join(package_directory, square_generator_file_path))

print("Empty __init__.py file created and square_generator.py moved to the package directory.")

class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range cannot be less than start")
        return [x**2 for x in range(start, end)]

# Define the CubicGenerator class as a subclass of SquareGenerator
class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if end < start:
            raise ValueError("End of range cannot be less than start")
        return [x**3 for x in range(start, end)]

# Test the CubicGenerator class
cubic_gen = CubicGenerator()
print("Cubes from 1 to 5:", cubic_gen.generate_cubes(1, 6))

# Define the SquareGenerator class
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range cannot be less than start")
        return [x**2 for x in range(start, end)]

# Define the CubicGenerator class as a subclass of SquareGenerator
class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if end < start:
            raise ValueError("End of range cannot be less than start")
        return [x**3 for x in range(start, end)]

    # Override generate_squares method to generate squares
    def generate_squares(sealf, start, end):
        if end < start:
            raise ValueError("End of range cannot be less than start")
        return [x**2 for x in range(start, end)]

# Test the CubicGenerator class
cubic_gen = CubicGenerator()
print("Squares from 1 to 5:", cubic_gen.generate_squares(1, 6))
