# tuples are unchangeable or immutable, so to change their values, you convert it to a list first, update the value(s) and then convert back to a tuple.

#1. updation
x = ("apple", "banana", "cherry")
print(x)
y = list(x) # type casting
y[1] = "kiwi"
x = tuple(y)
print(x)

#2. deletion
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#3. unpacking tuples
fruits1 = ("apple", "banana", "cherry")

(green1, yellow1, red1) = fruits1

print(green1)
print(yellow1)
print(red1)

# asterisk (*) is used to collect the remaining values as a list when variables don't match the number of values in the tuple
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green2, yellow2, *red2) = fruits2

print(green2)
print(yellow2)
print(red2)

#4. looping
fruits3 = ("apple", "mango", "papaya", "pineapple", "cherry")
for x in fruits3:
  print(x)

#5 joining tuples

tuple1 = ("a","b","c","d")
tuple2 = (1,2,3)

t3 = tuple1 + tuple2
print(t3)

f = ("A","B", "C")
mytuple = f * 2
print(mytuple) # multiples the output, 2 A's , 2 B's....
del mytuple
print(mytuple)