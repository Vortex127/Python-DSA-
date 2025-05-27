# Coffee Customization
# Customize a coffee order with "Small", "Medium", or "Large" size, with an option for "Extra Shot" or "No Extra Shot".

# order_vol =  input("Enter your preferred order size: ").lower()
# order_shot = input("Do you want an extra shot? (yes/no): ").lower()

# if order_shot == "yes":
#     extra_shot = "with Extra Shot"
# else:
#     extra_shot = "without Extra Shot"
    
# if order_vol == "small":
#     volume = "Small"
# elif order_vol == "medium":
#     volume = "Medium"
# elif order_vol == "large":
#     volume = "Large"
    
# print(f"Here's your coffee order: {volume} size {extra_shot}. Enjoy!")

#alternative:

order_size = input("Enter your preferred order size (Small, Medium, Large): ").lower()
extra_shot = True

if extra_shot:
    coffee = order_size + " with Extra Shot"
else:
    coffee = order_size + " without Extra Shot"
    
print(f"Here's your coffee order: {coffee}. Enjoy!")