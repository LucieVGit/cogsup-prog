################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

print("Exercise 4.1")

print(sum(dct.values()))

print("---")

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.
"""

print("Exercise 4.2")

big = max(dct, key=dct.get)
print(big)

print("---")

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.
"""

print("Exercise 4.3")

newdct = {}
for k, v in dct.items():
    newdct[k] = v ** 2
print(newdct)


print("---")

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.
"""

print("Exercise 4.4")

evens = {k: v for k, v in dct.items() if v % 2 == 0}
for k in evens:
    print(k)

# or
# print(events.keys())

print("---")

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.
"""

print("Exercise 4.5")

reverse = {v:k for k, v in dct.items()}
print(reverse)

print("---")

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

s = 'ccctcctttttcc'

print("Exercise 4.6")

count = {'c' : 0, 't' : 0}
for i in s:
    count[i] += 1
print(count)

# we can not use += in print

# count = {}
# for i in s:
#     count[i] = count.get(i, 0) + 1
# print(count)

print("---")

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

print("Exercise 4.7")

music = [responses_mapping[m] for m in responses]
print(music)   

print("---")

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""

print("Exercise 4.8")

one = {'a': 1, 'b': 2} 
two = {'c': 3, 'd': 4}
print({**one, **two})

print("---")

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""

print("Exercise 4.9")

names = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
print({animal: names[animal] for animal in sorted(names)})


print("---")

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""

print("Exercise 4.10")

{
  animal: names
  for animal, names in
  sorted(names.items(), key=lambda item: item[1])
}

print("---")