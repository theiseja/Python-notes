# Lists
# uses []
# group of items we ref by index
# are mutable (mutable can be changed, immutable cannot be changed)
# can have duplicate items
# sets can not have duplicates

# creates a new list
new_list = ["red", "orange", "yellow"]

# add vs insert
new_list.append("blue") # adds new item to end
new_list.insert("green") # insert at i

# remove vs pop vs del
new_list.remove("orange") # simply removes an item
new_list.pop() # removes the last item in the list
del new_list[1] # removes item at i


# Tuples
# uses ()
# creates tuple
new_tuple = ('item', 'item', 'item')

# prints length of tuple
print( len(new_tuple))

# traverses through tuple
for item in new_tuple:  # Python for loop example
    # access an item
    print(item)
    
    
# Function example
def my_function(): # functions are defined using the def keyword
    print("Hello, I'm a function!")
    
# print the data type of variable
x = 10
print(type(x))



#cspt5 day 1 problem
# Can you use pieces of both of the above examples to...
# Create a new list containing only the names that start with `s` so that they 
# are properly capitalized (regardless of how the name originally appears) 
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]
print(names)
# TODO
s_names = [n.capitalize() for n in names if n[0].lower() == '']
print(s_names)

# Python math operators list
+	Addition
-	Subtraction
*	Multiplication
/	Division
%	Modulo (remainder)
**	Exponentiation (power)
=	Assignment
+=	Addition assignment
-=	Subtraction assignment
*=	Multiplication assignment
/=	Division assignment
%=	Modulo assignment

# UPER - Given a number of people, number of pizzas and slices per pizza, write a function to evenly divide the slices between each person.
# 1. Understand the problem
# - how do we know #s? (passed as args in function)
#
#
#
#
#
#
#
#

    #
    
    
# UPER - Prompt a user to enter three, uique numbers as input, print out 
# which number is the largest of the three. 
# 1. Understand
# - What kind of numbers?
# 2. Plan
# 3. Execute
def calc_largest():
    # TODO
    pass
# 4. Reflect

# basic class structure for future ref
class Name:
    def __init__(self, name, age):
        self.name = name,
        self.age = age