# strings are generally the same everywhere, some additions in python are:

#1. triple quotes for multi-line strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#2. Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# moving onto other operations:

#1. slicing:
name = "Asfandyar"
print(name[0:6]) # last number is not included i.e. excluded
n1 = "AsfandAmanRameezAhmed"
print(n1[0:10:2]) # 2 means it'll hop over 1 element and come on to the next

#2. replace:
n2 = "Asfand Baig"
print(n2.replace("i", " "))

#3. split:

print(n3.split(", ")) # breaks it down to individual items, converting it from list to string

#4. strip:
n4 = "Hui  hui  hui"
print(n4.strip()) # lstrip() removes whitespace from left side only and rstrip() removes whitespace from right side only

#5. format:
drink_type = "Cold"
quantity = 4
order = "I ordered {} glasses of {} drinks "
print(order.format(quantity, drink_type))

price = 9.8756
print(f'The price is {price:.4f} dollars')  # f-string with 2 decimal places

#6. join:
drinks = ["Hello", "World", "Howl"]
print(", ".join(drinks))

n3 = "Hello, World, Cool, Galaxy"
for letters in n3:
    print(letters, end="") # end doesn't take print to the next line

