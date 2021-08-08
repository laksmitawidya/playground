from io import StringIO
from os import times
import re

""" Regular Expression 
matching strings of text such as particular char, words
patterns of characters. A regular exp is written in formal language that can be
interpreted by a regular expression processor
a.k.a expression for smart searching """

""" Regular Expression Module
1. Import library using "import re"
2. Use re.search() to see if a string matches a regular expression, similar to using the find()
method for string
3. Use re.findall() to extract portions of string that match the
regular expression, similar to a cobination of find() and
slicing: var[5:10]
 """

# using find in string
count = 0
text = open('test.txt')
for line in text:
    line = line.rstrip()
    if line.find('Lorem') >= 0:
        count = count + 1
        print(count)
        print("using find\n" + line)

#  using regex
text = open('test.txt')
count = 0
for line in text:
    line = line.rstrip()
    if re.search('Lorem', line):
        count = count + 1
        print(count)
        print("using regex\n" + line)


# using re.search() like startswith()
# if line.startswith('Lorem'): 
# it will return true/false

""" Wild - card characters """
# dot character match any character
# if you add asterisk character, the character is "any number of times"

""" 
^X.*: 
^X : match the start of the line 
. : match any character
* : many times
: : end with semi-colon
ex: x-Sieve: CMU Sieve 2.3 => matched
 """

""" 
^X-\S+:
^X- : match the start of the line
\S : match any non-whitespace character
\s : match any whitespace character
+ : one or more times non white space character
: : end with semicolon 
ex :
1. X-Sieve: CMU Sieve 2.3 => matched
2. X-Plane is behind the schedule: two weeks => not matched
"""

""" 
From matching to extracting
- re.search() returns a true/false depens on thether the String
matches the regular expression
- If we actually want the matching strings to be extracted, we use re.findall()
 """

""" 
Example:
[0-9]+ => one or more digits
[AEIOU]+ => one or more AEIOU letter
 """

word = 'my: 2 favorite numbers are: 19 and 42'
findNumber = re.findall('[0-9]+', word)
print(findNumber)
findLetter = re.findall('[AIUEO]+', word)
print(findLetter) # return empty array

""" 
WARNING: Greedy matching
the repeat character (* and +) push outward in both directions
(greedy) to match the largest possible string
 """

greedyMatching = re.findall('^m.+:', word) # it matches in both words after semicolon :
print(greedyMatching)


""" 
Non greedy matching
if we add ? character, the + and * chill out a bit
 """

lazyMatching = re.findall('^m.+?:', word)
print(lazyMatching)

""" 
Fine tuning string extraction
\S+@\S+ => at least one non whitespace character (have a blank char in both side)
 """
email = "From Stephen.mar@uct.ac.za Sat Jan  5 09:14;16 2008"
findEmail = re.findall('\S+@\S+', email)
print(findEmail)
findPreciseEmail = re.findall('^From (\S+@\S+)', email)
print(findPreciseEmail)

