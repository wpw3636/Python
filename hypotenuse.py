print("Welcome to the right triange hypotenuse solver. To find the length of your hypotenuse, please provide the length of the two triangle legs.")
a = int(input("Enter the length of leg a: "))
b = int(input("Enter the length of leg b: "))
c = (a ** 2 + b ** 2) ** 0.5
print("The length of the hyoptenuse is",c)