# Hash table example
import random
# def how_many_before_collisions(buckets):

#     tried = set()
#     tries = 0

#     random_key = str(random.random())
#     hashed_key_index = hash(random_key) % buckets

#     if hashed_key_index not in tried:
#         tried.add(hashed_key_index)
#         tries += 1

#     else:
#         break

# print("We had this many buckets: ", buckets)
# print("We had this man tries: ", tries)

# how_many_before_collisions(10000)


# load factor: keys / buckets
def longest_linked_list(keys, buckets):

    key_counts = {}

    for i in range(buckets):
        key_counts[i] = 0

    for i in range(keys):
        random_key = str(random.random())
        hashed_key = hash(random_key) % buckets

        key_counts[hashed_key] += 1

    longest_chain = 0
    for key in key_counts:
        if key_counts[key] > longest_chain:
            longest_chain = key_counts[key]
        
    print("Number of keys: ", keys)
    print("Number of buckets: ", buckets)
    print("Length of longest chain: ", longest_chain)

longest_linked_list(8, 16) # load factor of 50%

# longest_linked_list(800, 1600) # load factor of 50%

# longest_linked_list(16, 16)
# longest_linked_list(32, 16)

longest_linked_list(1024, 64)

longest_linked_list(7, 10)
longest_linked_list(70, 100)
longest_linked_list(7000, 10000)


# hash table lecture notes



