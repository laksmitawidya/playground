""" Tuples are another kind of sequence that functions
much like a list - they have elements which are indexed starting at 0 """

nameTuple = ('Glenn', 'Sally', 'Joseph')
print(nameTuple[2])
numberTuple = (1, 2, 5)
print(numberTuple)
print(max(numberTuple))

for iter in numberTuple:
    print(iter)

""" Tupples are immutable 
unlke list, once you create a tuple, you can not alter its contents
similar to string
"""
# numberTupple[2] = 4 -> will be error

numberList = [1,2,5]
numberList[2] = 10 # it won't be error

""" Things not to do with tuples """
# nameTuple.sort()
# numberTuple.append(10)
# numberTuple.reverse()

dir(list())
dir(tuple()) # only count and index

""" Tupple simple list """
# Tupple more efficient
# better memory used & performance
# Temproary variable

""" Tuples and assignment """
# put tuple on the left-hand side of assignment statement
# we can even omit the parentheses
# should be having similar total value
(number,word) = (4, 'fred')
print(number)
print(word)

# The items() method in dictionaries return a list of (key, value) tuples
wordDict = dict()
wordDict['apple'] = 1
wordDict['mango'] = 2
for(k,v) in wordDict.items():
    print(k,v)
tups = wordDict.items()
print(tups)

""" Tuples are comparable """
# The comparison operators work with tuples and other sequences
# if the first item is equal, python goes on to the next element
# and so on until it finds elements that differ
# scan first char, if found then it returns true/false
compareN=(0,1,2) < (5,1,2)
compareW=('Jones', 'Sally') > ('Maria', 'Bob')
compareW2=('John', 'Sally') < ('John', 'Sam')

print(compareN, compareW, compareW2)

""" Sorting lists of tupples """
# We can take advantage to sort a list of tuples to get a sorted version of dictionary
# First we sort the dictionary by the key using the items() method and sorted() function
print(wordDict.items())
print(sorted(wordDict.items()))
for k,v in sorted(wordDict.items()):
    print(k, v)

""" Sort by values """
sortedNumber = {'a': 10, 'b':10, 'c': 20}
list = list()
for k,v in sortedNumber.items():
    list.append((v,k)) #reverse key & value
    print(list)
sortedList = sorted(list, reverse=True)
print(list)
for k,v in sortedList[:1]:
    print(k,v)

# alternative  - shorted version
print(sorted([v,k] for k,v in sortedNumber.items()))

# List comperhension creates a dynamic list. In this case, we make a list of reversed tupples and then sort it
