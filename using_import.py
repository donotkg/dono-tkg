# -----------------------
# All Imports at the Top
# -----------------------
import random
import os
import sys
import math
import matplotlib.pyplot as plt
import pyfiglet                       # pyright: ignore[reportMissingImports]


# -----------------------
# Random Example
# -----------------------
number = random.randint(0, 10)        # Generate a random number between 0 and 10
print("Random number:", number)


# -----------------------
# OS Module Examples
# -----------------------
current_dir = os.getcwd()             # Get current directory
print("Current directory:", current_dir)

files = os.listdir(".")               # List all files in this directory
print("Files in this directory:", files)


# -----------------------
# SYS Module Examples
# -----------------------
print("Python version:", sys.version)   # Show Python’s version
print("Script name:", sys.argv[0])      # Show the name of this script


# -----------------------
# Math Module Examples
# -----------------------
print("Pi:", math.pi)
print("Square root of 25:", math.sqrt(25))
print("Cosine of 0:", math.cos(0))


# -----------------------
# PyFiglet Example
# -----------------------
ascii_banner = pyfiglet.figlet_format("Python!")
print(ascii_banner)                     # Prints large ASCII text art


# -----------------------
# Matplotlib Example
# -----------------------
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, marker="o")
plt.title("Simple Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()                              # Display the plot


# -----------------------
# String Manipulation Examples
# -----------------------
text = "Hello Python!"
print(text.upper())
print(text.lower())
print(text.replace("Python", "World"))

sentence = "apple,banana,cherry"
fruits = sentence.split(",")
print("Fruit list:", fruits)

joined = " | ".join(fruits)
print("Joined string:", joined)




