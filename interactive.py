print("Answer the following questions:")

name=input("What is your name? ")
age=int(input("How old are you? "))
height=float(input("How tall are you in meters? "))

print("\nSummary:") # \n = new line
print("Name:", name)
print("Age:", age)
print("Height:", height, "meters")

years_to_100=100-age
print("Hi", name + ", you will turn 100 in", years_to_100, "years!")
