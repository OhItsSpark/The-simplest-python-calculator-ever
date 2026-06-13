import math # We import the module math

# Prompts the user to select one option

print("Area Calculator")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")

# We utilize input to receive the user option

choice = input("Choose a shape (1-4): ")

# If user chosed a square we will multiply the square side by 2

if choice == "1":
    side = float(input("Enter the side length: "))
    area = side ** 2
    print("Area =", area)

# If the user chosed a rectangle we obtain the area via multiplying its lenght and width

elif choice == "2":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
    print("Area =", area)

# For the triangle we bultiply its base and height and we divixde it by 2

elif choice == "3":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = (base * height) / 2
    print("Area =", area)

# For the circle we multiply pi by the circle's radius and we utilize the python expression **2 for exponetation

elif choice == "4":
    radius = float(input("Enter the radius: "))
    area = math.pi * radius ** 2
    print("Area =", area)

# If users selects any other option invalid is printed in the terminal

else:
    print("Invalid")


