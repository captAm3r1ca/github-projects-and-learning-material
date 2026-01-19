import random

greetings=[
    'Hello Git!',
    'Greetings, devleoper!',
    'Welcome to branching!',
    'Hi there, coding friend!',
    'Happy Coding!'
]

def get_random_greeting():
    return random.choice(greetings)

print(get_random_greeting())
print('learning branches now')
