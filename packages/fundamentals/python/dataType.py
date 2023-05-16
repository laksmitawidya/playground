""" Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
 """

x = 5
print(type(x))

x = ["apple", "banana", "cherry"]

# display x:
print(x)

# display the data type of x:
print(type(x)) 

""" OPERATOR
is and is not operators
it's a logical expression
similar to, but stronger than ==
0 == 0.0 (true)
0 is 0.0 (false) -> very strong, don't use it in number (just for none and boolean)

LOOPS
break statement ends the current loop and jumps to the statement immidiately following the loop
finishing an iteration with continue: statement end the current iteration and jumps to the top of the loop and starts the next iteration
 """

while True:
	line = input("> ")
	if line[0] == '#':
		continue
	if line == 'done' :
		break
	print(line)
print('Done!')


### Reading and Converting
name = input("Enter:")
print(name)
apple = input("Enter:")
x = int(apple) - 10
print(x)

fruit = 'banana'
print(len(fruit))

word = 'abc'
print(word[1]) # doesn't work

fruit = 'banana'
x = len(fruit)
print(x)

### Looping through String

## using while
fruit = 'banana'
index = 0
while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index+1

## using for statement
letter = 'banana'
for letter in fruit:
	print(letter)



""" STRING
1. Slicing String
We can look at any continue section of string using colon operator
Second number is one beyond the end of slice "up to but not including"
If the second number beyond the end of the string, it stops at the end """

s = 'Monty Python'
print(s[0:4]) ## Mont
print(s[6:7]) ## P

# Eliminate the first or last 
print(s[:2]) ## Mo
print(s[8:]) ## thon
print(s[:]) ## Monty Python


### 2. String Concatenation
fruit = 'Banana'
'n' in fruit
'm' in fruit
'b' in fruit
if 'a' in fruit:
    print('found it')

### 3. String Comparison
if word == 'banana':
    print('all right, bananas')
if word < 'banana':
    print('your word,' + word + ', comes before banana')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right banana')


### 4. String Library
greet = 'Hello Bob'
zap = greet.lower()
print(zap) # hello bob
print ('Hi There'.lower()) # hi there
stuff = 'Hello World'
type(stuff)
dir(stuff)

""" capitalize, casefold, center, count, encode, endswith, expandtabs, find, upper, replace, etc
lstrip(), rstrip() remove whitespace at left or right
strip() removes both beginning and ending whitespace === trim in JS
prefixes : line.startswith -> true/false
Parsing & extracting
ex email """

data = 'From mithawid@gmail.com  Sat Jan    4 09:14:21 2021'
atpos = data.find('@')
print(atpos)

sppos = data.find('  ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

## Two kinds of Strings
## python 3 : all strings are unicode



