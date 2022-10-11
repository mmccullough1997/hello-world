import random
# animals = [ "Triceratops", "Gorilla", "Corgi", "Toucan"]

# for animal in animals:
#     if len(animal) > 5:
#       print(animal)

# greetings = ['howdy', 'whaddup wid it', 'hallo']
# select_greeting = input(f'select greeting from list: {greetings}: ')
# print(select_greeting)

i = 1
animal_name_input = input('List out some funny animal names: ').split(', ')
print('Hi there! These are the names you\'ve submitted: ')
for animal in animal_name_input:
  print(str(i) + '.' + ' ' + animal)
  i+=1
# use split?
color_input = input('What is your favorite color? ')
print(f'Would you like a {color_input} {random.choice(animal_name_input)}')
