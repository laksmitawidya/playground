abc = 'with three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

for w in stuff:
    print(w)

line='first;second;third'
thing = line.split(';') ## split with delimiter, default: whitespace

line = 'From stephen.matquard@uct.ac.za Sat Jan   5 09:14:16 2008'
f = open('test.txt', 'r')
for line in f:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print("ABVCCCCCC" + words[2])

print(line.split())


words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
print(pieces)
parts = pieces[3].split('-')
print(parts)
n = parts[1]
print("n" + n)
