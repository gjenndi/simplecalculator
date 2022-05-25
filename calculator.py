#Calculator of most important parts of math

import time

class basics:

    def adding():
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("First number is: ", a)
        print("Second number is: ", b)
        return print(a, "+", b, "=", a + b)

    def subtraction():
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("First number is: ", a)
        print("Second number is: ", b)
        return print(a, "-", b, "=", a - b)

    def multiplication():
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("First number is: ", a)
        print("Second number is: ", b)
        return print(a, "*", b, "=", a * b)

    def division():
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("First number is: ", a)
        print("Second number is: ", b)
        return print(a, "/", b, "=", a / b)

class geometry:

    def square():
        a = int(input("Enter side A: "))
        perimeter_of_square = (a * 4)
        print("Perimeter of a square with side", a, "centimeters is", perimeter_of_square, "centimeters.")
        area_of_square = (a * a)
        print("Area of a square with side", a, "centimeters is", area_of_square, "centimeters.")


    def triangle():
        a = int(input("Enter side A: "))
        b = int(input("Enter side B: "))
        c = int(input("Enter side C: "))
        h = int(input("Enter height H: "))

        perimeter_of_triangle = (a + b + c)
        print("Perimeter of a triangle with side A=", a, "centimeters, with side B =", b, "centimeters, with side C =", c, "centimeters is", perimeter_of_triangle, "centimeters.")
        area_of_triangle = ((b*h)/2)
        print("Area of a triangle with side B=", b, "centimeters and height", h, "centimeters is", area_of_triangle, "centimeter.")


    def circle():
        r = int(input("Enter radius: "))
        perimeter_of_circle = (3.14 * r)
        print("Perimeter of circle with radius", r, "centimeters is", perimeter_of_circle, "centimeters.")
        area_of_circle = (3.14 * r * r)
        print("Area of circle with daimeter", r * r, "centimeters is", area_of_circle, "centimeters.")

class theorem:

    def pythagoras_hypotenuse():
        a = int(input("Enter side A: "))
        b = int(input("Enter side B: "))
        return print("Hypotenuse is", (a ** 2 + b ** 2) ** 0.5)

    def pythagoras_side():
        c = int(input("Enter hypotenuse: "))
        d = int(input("Enter one side: "))
        return print("The other side is", (c ** 2 - d ** 2) ** 0.5)
    
class others:

    def root():
        a = int(input("Enter a number: "))
        return print(a ** 0.5)

    def power():
        a = int(input("Enter a number: "))
        return print(a ** 2)

    def factors():
        a = int(input("Enter a number: "))
        print("The factors of", a, "are:")
        for i in range(1, a + 1):
            if a % i == 0:
                print(i)


print("Welcome to our CALCULATOR")
time.sleep(1)

print("We offer you some math calculations: ")
time.sleep(0.5)

print("If you want basics like adding, subtraction, multiplication, division type basics")
time.sleep(0.3)

print("In geometry areas and syprines of square, triangle and circle type geometry")
time.sleep(0.3)

print("If you want pythagorean theorem type theorem, and if you want other calculations type other")
time.sleep(0.3)

answer = input("Enter what do you want to know: ").upper()


if answer == "BASICS" :
    operation = (input("Which operation do you need: ").upper())
    
    if operation == "ADDING":
        basics.adding()
    
    if operation == "SUBTRACTION":
        basics.subtraction()

    if operation == "MULTIPLICATION":
        basics.multiplication()

    if operation == "DIVISION":
        basics.division()

if answer == "GEOMETRY":
    figure = (input("Which figure do you need to calculate area and syprine: ").upper())

    if figure == "SQUARE":
        geometry.square()
    
    if figure == "TRIANGLE":
        geometry.triangle()

    if figure == "CIRCLE":
        geometry.circle()

if answer == "THEOREM":
    pythgr = (input("Do you want to know hypotenuse or side: ").upper())

    if pythgr == "HYPOTENUSE":
        theorem.pythagoras_hypotenuse()
    
    if pythgr == "SIDE":
        theorem.pythagoras_side()

if answer == "OTHER":

    print("Here we offer you root, power and factors")
    other = (input("Which one do you choose: ").upper())

    if other == "ROOT":
        others.root()
    
    if other == "POWER":
        others.power()

    if other == "FACTORS":
        others.factors()
     
else:
    print("Sorry, you wrote that wrong!!")
