
    
#2. Movie ticket pricing 
# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesdays.

# day = input ("Enter the day of the week: ")
# age = input("Enter your age: ")
# int_age = int(age)

# if day == "Wednesday":
#     discount = 2
# else:
#     discount = 0
    
# if int_age >= 18:
#     price = 12 - discount
# else:
#     price = 8 - discount

# print(f"The ticket price is ${price}.")

#an alternative way to write the above code

age = int(input("Enter your age: "))
day = input("Enter the day of the week: ")

price = 12 if age >= 18 else 8
if day == "Wednesday":
    price -= 2
print(f"The ticket price is ${price}.")
