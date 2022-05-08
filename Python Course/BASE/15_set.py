# Set unordered unique colleciton of elements, something is there or not. Is faster than lists or dicts

# ! not frwquency or order !

# create an empty set:
x = set() # not x = {}
# eventho a set is represetned as following:
s = {4,5,6,4} # no because is a dictionary, if empty
# remember set does not accept duplicates, aka one of the two fours is gonna disappear, len will be len(s) - duplicates
s.add(5)
print(s)
s.remove(5)
print(s)
print(4 in s)
print(5 in s)

sl = [4,33,32,2,2,2]
print(s)
print(33 in s) # this, since sl is a list, happens way slower than in a set


s2 = {4,33,32,2,2,2}
print(s.union(s2)) # unify lists
print(s.difference(s2)) 
print(s.intersection(s2))
# and more... just start writing s. and all options appear

