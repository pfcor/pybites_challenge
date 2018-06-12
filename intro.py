#  Bite 101. f-strings and a simple if/else

MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    """Print name is allowed / not allowed to drive based on MIN_DRIVING_AGE"""
    print(f'{name} is {"not " if age < MIN_DRIVING_AGE else ""}allowed to drive')


# Bite 102. Infinite loop, input, continue and break

VALID_COLORS = ['blue', 'yellow', 'red']

def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        user_input = input('write a color: ').lower()
        if user_input == 'quit':
            print('bye')
            break
        elif user_input not in VALID_COLORS:
            print('Not a valid color')
        else:
            print(user_input)

# if __name__ == '__main__':
#     print_colors()


# Bite 103. Loop through a dictionary and pluralise a word 

games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

def print_game_stats(games_won=games_won):
    """Loop through games_won's dict k, v pairs (items) and
       print how many games each person has won, pluralize
       'game' based on number"""
    for name, wins in games_won.items():
        print(f'{name} has won {wins} game{"s" if wins != 1 else ""}')


# Bite 104. Split and join

message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def split_in_columns(message=message):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output"""
    return '|'.join(message.split('\n'))


# Bite 105. Slice and dice 

from string import ascii_lowercase

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""

another_text = """
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
finally return the results list!
"""

def slice_and_dice(text=text):
    """Strip the whitespace (newlines) off text at both ends,
       split the text string on newline (\n).
       Next check if the first char of each (stripped) line is lowercase,
       if so split the line into words and append the last word to
       the results list. Make sure the you strip off any trailing
       exclamation marks (!) and dots (.), Return the results list."""
    results = []
    text = text.strip().split('\n')
    for line in text:
        if line.strip()[0].islower():
            results.append(line.split()[-1].strip('.').strip('!'))
    return results

# if __name__ == '__main__':
#     print(slice_and_dice(another_text))


# Bite 106. Strip out vowels and count the number of replacements 

text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
vowels = 'aeiou'

def strip_vowels(text=text):
    """Replace all vowels by *, return newly formed string
       and number of replacements done"""
    new_text = ''
    changes = 0
    for char in text:
        if char.lower() not in vowels:
            new_text += char
        else:
            new_text += '*'
            changes += 1
    return new_text, changes

def strip_vowels2(text=text):
    import re
    return re.subn(f'[{vowels}]', '*', text, flags=re.I)

# if __name__ == '__main__':
#     t, c = strip_vowels()
#     print(t)
#     print(c)
#     t, c = strip_vowels2()
#     print(t)
#     print(c)


# Bite 107. Filter numbers with a list comprehension

def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""
    return [x for x in numbers if (x > 0) and (x%2==0)]


# Bite 108. Loop over a dict of namedtuples calculating a total score

from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}


def get_total_points(belts=ninja_belts):
    """Calculate the amount of points rewarded on PyBites given the
       ninja_belts dictionary, formula: belt score x belt owners (aka ninjas)
       (of course there are more points but let's keep it simple)

       Make your code generic so if we update ninja_belts to include
       more belts (which we do in the tests) it will still work.

       Ah and you can get score and ninjas from the namedtuple with nice
       attribute access: belt.score / belt.ninjas (reason why we get
       you familiar with namedtuple here, because we love them and use
       them all over the place!)

       Return the total number of points int from the function."""
    return sum(v.score * v.ninjas for v in belts.values())

# if __name__ == '__main__':
#     print(get_total_points())

# Bite 109. Workout dict lookups and raising an exception 

workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'


def get_workout_motd(day):
    """Title case passed in day argument (monday or MONDAY -> Monday)
       and check if it is in the given workout_schedule dict.

       If it is there retrieve the workout, if not raise a KeyError.

       Return the chill or go_train variable depending the retrieved
       workout value ('Rest' or workout bla)

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'"""
    
    day = day.title()
    if day not in workout_schedule:
        raise KeyError
    todo = workout_schedule[day]
    if todo == 'Rest':
        return chill
    else:
        return go_train.format(todo)


# Bite 110. Type conversion and exception handling

def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    try:
        numerator = int(numerator)
        denominator = int(denominator)
    except ValueError:
        raise
    
    try:
        return numerator/denominator
    except ZeroDivisionError:
        return 0