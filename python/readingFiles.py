### FILE PROCESSING
# A text file can be thought as a sequence of lines

# BACKSLASH for NEW LINE
stuff = 'Hello\nWorld!'
print(stuff)
print(len(stuff))

# Reading File
# Using open()
# Dealing with bad files
# Searching for lines
fname = input("Enter FileName: ")
try: 
    fhand = open(fname)
except: 
    print('File Cannot be opened', fname)
    quit()

count = 0
for line in fhand:
    if(line.startswith('Lorem')):
        count= count +1
print('There were', count, 'Lorem lines in', fname)


f = open('test.txt', 'r')
inp = f.read()
print(len(inp))
count = 0
for line in f:
    if line.startswith('Lorem '):
        print(line)
        count = count + 1
print('lineCount :', count)



