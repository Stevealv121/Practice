
#List
alphabet = ['a', 'b', 'c', 'd', 'e']

#for letter in alphabet:
#    print(letter)

print(alphabet[0])
alphabet[0] = 'A'
print(alphabet[0])        

#Tuple
codes = ('alpha', 'bravo', 'charlie', 'delta', 'echo')
print(codes[0])
#    codes[0] = 'ALPHA'
#    ~~~~~^^^
#TypeError: 'tuple' object does not support item assignment, immutable
#codes[0] = 'ALPHA'``
#print(codes[0])

#Set

ids = {1, 2, 3, 4, 5}
print(ids)
#TypeError: 'set' object is not subscriptable
#print(ids[0])

#Dictionary
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

print(person['name'])
person['name'] = 'Bob'
print(person['name'])