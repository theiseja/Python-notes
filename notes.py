# Lists
# group of items we ref by index
# are mutable (mutable can be changed, immutable cannot be changed)
# can have duplicate items

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

# creates tuple
new_tuple = ('item', 'item', 'item')

# prints length of tuple
print( len(new_tuple))

# traverses through tuple
for item in new_tuple:
    # access an item
    print(item)