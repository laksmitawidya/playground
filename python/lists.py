### Algorithm
# Set rules or steps used to solce a problem

### Data Structure
# A particular way of organizing data in computer

### Collection
# if the variable is replacing another variable it is not a variable
# collection allows us to put many values in a single variable
# a collection is nice because we can carry all many calues around in one convinient package

friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']


# List Constants
# Surrounded by square brackets and elements in the list are separated by commas
# A list element can be any Python objet - even another list
# A list can be empty

for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')

# List are mutable
# Strings are immutable, we cannot change the ontents of a string - we must make a new string to make any change
# List are mutable - we can change the element of a list using the index operator

# How long is a list?
# len() function takes a list aas a param and returns the number of elements in the list
# len() tells us the number of elements of any set or sequence


# Using the range function
# Range function returns a list of numbers that range from zero to one less than the paramter
# We can construct an index loop using for and an integer iterator 
print(range(4))
for friend in friends:
    print('Happy new year', friend)
print(range(len(friends))) # [0,1,2]
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)