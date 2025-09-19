import math
import random 
from decimal import Decimal

h1 = "chia" 
h2 = "seeds"
print (h1 + " " + h2) #Called string concatenation or operator overloading where operator decides what to do

h3 = "asfand"
print(repr(h3)) #It returns a string representation of an object that is meant to be unambiguous and ideally could be used to recreate the object.

h4 = 59
print(str(h4)) #returns a string object

print(math.floor(3.5)) #prints number below it, 3 in this case
print(math.floor(-3.5)) #prints -4

print(math.trunc(2.4)) #prints number closest to 0, 2 in this case
print(math.trunc(-2.4)) #prints -2

print(random.randint(1,10))

l1 = ['lemon', 'orange', 'grape', 'apple']
print(random.choice(l1)) #prints random element from the list
random.shuffle(l1) #shuffles the list randomly
print(l1)

# True == 1 in python but is not literally 1, it corresponds to the value.
