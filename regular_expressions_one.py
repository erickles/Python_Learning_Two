text = "The agent´s phone number is 408-555-1234. Call soon!"

print('phone' in text)

import re

pattern = 'phone'

match = re.search(pattern,text)

print(match.span())
print(match.start())
print(match.end())

text2 = "my phone once, my phone twice"

matches = re.findall('phone',text2)

print(matches)

for match in re.finditer('phone', text2):
    print(match.span())
    print(match.group())

text = "My phone number is 408-555-7777"

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)

print(phone)
print(phone.group())

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)

print(phone)
print(phone.group())

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results = re.search(phone_pattern, text)

print(results.group())

print(results.group(1))
print(results.group(2))
print(results.group(3))

# additional regex syntax
results2 = re.search('cat|dog','The cat is here')
print(results2)

results3 = re.findall(r'at','The cat in the hat sat there')
print(results3)

results4 = re.findall(r'.at','The cat in the hat sat there')
print(results4)

results5 = re.findall(r'...at','The cat in the hat went splat')
print(results5)

results6 = re.findall(r'^\d','1 is a number')
print(results6)

results6 = re.findall(r'\d$','number is 2')
print(results6)

phrase = 'there are 3 numbers 34 inside 5 this sentence'

pattern = r'[^\d]'

results7 = re.findall(pattern,phrase)
print(results7)

pattern = r'[^\d]+'

results7 = re.findall(pattern,phrase)
print(results7)

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

clean = re.findall(r'[^!.? ]+',test_phrase)
print(clean)

new_phrase = ' '.join(clean)
print(new_phrase)

new_text = 'Only find the hyphen-words in this sentence. But you do not know how long-ish they are'

pattern = r'[\w]+-[\w]+'

results9 = re.findall(pattern,new_text)
print(results9)

text_one = 'Hello, would you like some catfish?'
text_two = 'Hello, would you like to take a catnap?'
text_three = 'Hello, have you seen this caterpillar?'

results10 = re.search(r'cat(fish|nap|claw)',text_one)
print(results10)


