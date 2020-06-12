import time

start_time = time.time()

import sys
sys.path.append('../binary_search_tree')
from binary_search_tree import BSTNode

import pandas as pd

names1 = 'https://raw.githubusercontent.com/LambdaSchool/Sprint-Challenge--Data-Structures-Python/master/names/names_1.txt'

names2 = 'https://raw.githubusercontent.com/LambdaSchool/Sprint-Challenge--Data-Structures-Python/master/names/names_2.txt'

# f = open('names1', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

names_1 = pd.read_csv(names1, error_bad_lines=False)
names_2 = pd.read_csv(names2, error_bad_lines=False)


duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
#no dupes with runtime of:  1.0807971954345703 seconds
            
#solution 1:           
#while name_1 in names_1 == name_2 in names_2:
#    return duplicates.append(name_1)
#duplicates = [i for i in names_1 if i in names_2]
            
#detected 0 dupes with runtime of :0.9477787017822266 seconds

#solution 2
# bst = BSTNode("")

# for name in names_1:
#     bst.insert(name)

# for name in names_2:
#     if bst.contains(name):
#         duplicates.append(name) 

# zero dupes with a runtime of: 2.190727949142456 seconds
        
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")