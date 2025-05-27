distance = int(input("Enter your range: "))

if distance <3:
    option = "walk"
elif distance >3 and distance <15:
    option = "Bike"
elif distance >15:
    option = "Car"

print(f"Since your distance is {distance}km, I guess you should opt for option of {option} ")