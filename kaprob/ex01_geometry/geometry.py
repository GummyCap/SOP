"""Ask user a shape and a radius or a side length and calculate the shape area."""
import math

shape = input("Please insert geometric shape: ")  # Get Shape of Geometric object
if shape == "circle":  # Calculate for circle
    lng = float(input("Please insert radius in cm: "))  # Get User input and turn from str to float
    print("The area is " + str(round(lng ** 2 * math.pi, 2)) + " cm^2")
elif shape == "square":  # Calculate for square
    lng = float(input("Please insert side length in cm: "))  # Get User input and turn from str to float
    print("The area is " + str(round(lng ** 2, 2)) + " cm^2")
elif shape == "triangle":  # Calculate for triangle
    lng = float(input("Please insert side length in cm: "))  # Get User input and turn from str to float
    print("The area is " + str(round(math.sqrt(3) / 4 * lng ** 2, 2)) + " cm^2")
else:
    print("Shape is not supported.")  # Print for wrong input
