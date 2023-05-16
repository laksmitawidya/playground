""" 
ASCII
- Each character is represented by a number between 0 and 256 stored in 8 bits of memory
- We refer 8 bits of memory as a byte of memory
- The ord() function tells us the numeric value of a simple ASCII character
 """

print(ord('H'))
print(ord('e'))
print(ord('\n'))

""" 
- ASCII 
- Unicode : more complex
- Unicode can't be sent through the network as the size is to large
- We need to compress it
- Multi-byte character: to represent the wide range of char computers must handle we represent
characters with more than one byte
- Ascii is only 1 byte
- UTF-8: 1-4 bytes => recommended for encoding data to be exchanged bwtween system
- Auto detection between ASCII & UTF-8
- In py 3, all string are unicode
- Working with string var in python programs and reading data from files usually just works
- When we talk to a network resource using sockets or talk to a database we have to encode and decode data
usually to UTF-8
 """

# Python strings to bytes
""" 
- When we talk to an external resource like a network socket we sends bytes, so we need to encode 
python 3 strings into a given character encoding
- When we read data from an external resource, we must devode it based on the character set
so it is properly represented in Python 3 as a string
 """
