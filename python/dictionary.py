""" Collection
variables have one value in the, hen we put new value in the variable - the lod value is written
with collection we can have bunch of values in a single variable
- we do this by having more than one place in the variable
- we have ways of finding the different places in the variable
- we can put more than one value in it and carry them all around in one convinient package
 """

""" Story of two collection
list : linear collection of values that stay in order (ex: pringle)
dictionary : bag pf values, each with it's own label (ex: toy box with labeled toy and toy)
 """


""" Dictionaries 
are python's most poweful data collection
 - allows us to do fast database-like operations in python
 - have different name in different languages ex:
    - Assosiative Arrays : Perl/PHP
    - Properties or Map or HashMap : Java
    - Property Bag : C# / .Net 
 """


""" How to?
- Lists index their entries based on the position in the list
- Dictionaries are like bags - no order
- So we index the things we put in the dictionary with a lookup tag
"""

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

""" Comparing List and Dictionary 
Dictionaries are like lists except that they use keys instead of numbers to look up values
"""
print("with list")
list = list()
list.append(21)
list.append(183)
print(list)
list[0] = 23
print(list)

print("with dictionary")
dictionary = dict()
dictionary['age'] = 21
dictionary['course'] = 182
print(dictionary)
dictionary['age'] = 23
print(dictionary)



""" Dictionary Literals (Constants) 
- Dictionary literals use curly braces and have a list of key:value pairs
- You can make an empty dictionary using empty curly braces
"""

jjj =  {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)
ooo = {}
print(ooo)

""" Dictionary count Most Common Name 
count the occurence number
it is an error to reference a key which is not in the dictionary
we can use in operator to see if key is in the dictionary


Get Method in dictionary
 the pattern of checking to see if a key is already in a dictionary
 and assuming a default value if the key is not there
 is so common that there is a method called get() that does
 this for us

 Default value if key does not exist (and no traceback)
  
Dictionary counter using Js (too much hassle :())
const count = new Map()
const sweets = ['candy', 'candy', 'chocolate', 'icecream'];
sweets.map((key)=> {
    if(!count.has(key)){
        count.set(key, 1)
    } else {
        count.set(key, count.get(key) + 1)
    }
})
console.log("count", count) """


sweetbox = dict()
counts = dict()
sweetbox['candy'] = 1
sweetbox['cookies'] = 1
print(sweetbox)
sweetbox['candy'] = sweetbox['candy'] + 2
print(sweetbox)
# print(sweetbox['chocolate']) -> traceback key error
print('chocolate' in sweetbox) # solve it by checking the value first
sweets = ['candy', 'cookies', 'cookies', 'chocolate', 'icecream']
for sweet in sweets:
    if sweet not in counts:
        counts[sweet] = 1
    else :
        counts[sweet] = counts[sweet] + 1 

if sweet in counts:
    x = counts[sweet]
else :
    x = 0
x = counts.get(sweet, 0) # traceback if there is no sweet, so 0 will be assign on the value of key


# alternative (easier way)
for sweet in sweets:
    counts[sweet] = counts.get(sweet, 0) + 1
print(counts)



""" Dictionaries and Loops """
# Counting pattern
text = dict()
print('Enter a line of text:')
line = input('')
words = line.split() # split by whitespace to array
print('Words:', words)
print('Counting ...')
for word in words:
    text[word] = text.get(word,0) + 1
print('Counts', text)


""" Definite loops and dictionaries
Even though dictionaries are not stored in order, we can write a for
loop that goes through all the entries in a dictionary
actually it goes through all of the keys in dictionary and looks up
the values
 """

for key in text:
    print(key, text[key])

""" Retrieving lists of keys and values """
print(text.keys())
print(text.values())
print(text.items())

# Two Itertion variables - iterate paired key and value
#  We loop through the key value pairs in a dictionary using two iteration variable
for key, value in text.items():
    print(key, value)