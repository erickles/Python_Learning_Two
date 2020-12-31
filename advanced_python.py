from collections import Counter

my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3]

# Counter({3: 7, 1: 5, 2: 4})
print(Counter(my_list))

print(Counter('aabbcc'))

sentence = 'How many times does each word show up in this sentence with a word'

print(Counter(sentence.lower().split()))

letters = 'aaaaaabbbbbbcccccdddddd'

c = Counter(letters)

# Returns a tupple
print(c.most_common())

# Returns a tupple with the 3 most common
print(c.most_common(3))

print(list(c))

from collections import defaultdict

d = {'a':10}

print(d['a'])

d = defaultdict(lambda : 0)

d['correct'] = 100

print(d['correct'])

my_tuple = (10,20,30)

from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])

brienne = Dog(age=2,breed='Vira Lata',name='Brienne')

print(type(brienne))
print(brienne[0])
print(brienne[1])
print(brienne[2])