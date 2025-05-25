fruit = input("Enter a fruit: ")
color = input("Enter a color: ")

if color == "green":
    status = "Unripe"
elif color == "yellow":
    status = "Ripe"
elif color == "brown":
    status = "Overripe"

print(f"The {fruit} is {status}.")