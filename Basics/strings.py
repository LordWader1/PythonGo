
# ============================================================
# STRINGS IN PYTHON
# Topics: String Basics, Indexing, Slicing, Escape Sequences,
#         Concatenation, and Built-in String Methods
# ============================================================


# 1. INTRODUCTION TO STRINGS

# A string is a sequence of characters enclosed in quotes.

letter = "P"
greeting = "Hello, World!"
sentence = "I hope you are enjoying the 30 Days of Python Challenge."

print("\n--- STRING BASICS ---")
print(letter)
print(greeting)
print(sentence)

# Finding the length of a string
print(len(letter))       # 1
print(len(greeting))     # 13
print(len(sentence))


# 2. MULTILINE STRINGS

# Using triple single quotes
multiline_string = '''I am a teacher and enjoy teaching.
I believe education empowers people.
That is why I created the 30 Days of Python Challenge.'''

print("\n--- MULTILINE STRING ---")
print(multiline_string)

# Using triple double quotes
multiline_string = """Python is easy to learn.
It is powerful and beginner-friendly.
Practice regularly to improve your skills."""

print(multiline_string)


# 3. STRING CONCATENATION

# Concatenation means joining two or more strings.

first_name = "Asabeneh"
last_name = "Yetayeh"

full_name = first_name + " " + last_name

print("\n--- STRING CONCATENATION ---")
print(full_name)

# Checking string lengths
print(len(first_name))                  # 8
print(len(last_name))                   # 7
print(len(full_name))                   # 15

# Comparing string lengths
print(len(first_name) > len(last_name)) # True


# 4. UNPACKING CHARACTERS

# Assigning individual characters to separate variables.

language = "Python"

a, b, c, d, e, f = language

print("\n--- CHARACTER UNPACKING ---")
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n


# 5. ACCESSING CHARACTERS USING INDEXING

# Python uses zero-based indexing.

language = "Python"

print("\n--- POSITIVE INDEXING ---")
print(language[0])  # P
print(language[1])  # y
print(language[2])  # t

# Accessing the last character
last_index = len(language) - 1
print(language[last_index])  # n

# Negative indexing starts from the right.
print("\n--- NEGATIVE INDEXING ---")
print(language[-1])  # n
print(language[-2])  # o
print(language[-3])  # h


# 6. STRING SLICING

# Syntax: string[start:end:step]
# The ending index is excluded.

language = "Python"

print("\n--- STRING SLICING ---")
print(language[0:3])   # Pyt
print(language[3:6])   # hon
print(language[-3:])   # hon
print(language[:3])    # Pyt
print(language[3:])    # hon

# Slicing with step
print(language[0:6:2]) # Pto

# Reversing a string
print(language[::-1])  # nohtyP


# 7. ESCAPE SEQUENCES

# Escape sequences are special characters used for formatting.

print("\n--- ESCAPE SEQUENCES ---")

# New line
print("Hello, Python!\nWelcome to programming.")

# Horizontal tab
print("Day\tTopics\tExercises")
print("Day 1\t3\t5")
print("Day 2\t3\t5")
print("Day 3\t3\t5")

# Printing a backslash
print("This is a backslash: \\")

# Printing quotation marks
print("Python starts with \"Hello, World!\"")


# 8. STRING METHODS

# 8.1 capitalize()
# Converts the first character to uppercase.

text = "thirty days of python"
print("\n--- capitalize() ---")
print(text.capitalize())
# Output: Thirty days of python


# 8.2 count()
# Counts occurrences of a substring.

text = "thirty days of python"
print("\n--- count() ---")
print(text.count("y"))          # 3
print(text.count("y", 7, 14))   # 1
print(text.count("th"))         # 2


# 8.3 endswith()
# Checks whether a string ends with a specified value.

text = "thirty days of python"
print("\n--- endswith() ---")
print(text.endswith("on"))      # True
print(text.endswith("tion"))    # False


# 8.4 expandtabs()
# Replaces tab characters with spaces.

text = "Python\tProgramming\tLanguage"
print("\n--- expandtabs() ---")
print(text.expandtabs())
print(text.expandtabs(10))


# 8.5 find()
# Returns the index of the first occurrence.
# Returns -1 if the substring is not found.

text = "thirty days of python"
print("\n--- find() ---")
print(text.find("y"))       # 5
print(text.find("th"))      # 0
print(text.find("java"))    # -1


# 8.6 format()
# Inserts values into string placeholders.

first_name = "Asabeneh"
last_name = "Yetayeh"
profession = "Teacher"
country = "Finland"

sentence = "I am {} {}. I am a {}. I live in {}.".format(
    first_name, last_name, profession, country
)

print("\n--- format() ---")
print(sentence)

# Modern alternative: f-strings

sentence = (
    f"I am {first_name} {last_name}. "
    f"I am a {profession}. I live in {country}."
)

print(sentence)


# 8.7 index()
# Returns the index of a substring.
# Raises ValueError if the substring is not found.

text = "thirty days of python"
print("\n--- index() ---")
print(text.index("y"))    # 5
print(text.index("th"))   # 0


# 8.8 isalnum()
# Checks whether all characters are letters or numbers.

print("\n--- isalnum() ---")
print("ThirtyDaysPython".isalnum())  # True
print("30DaysPython".isalnum())      # True
print("thirty days".isalnum())       # False
print("Python@123".isalnum())        # False


# 8.9 isalpha()
# Checks whether all characters are alphabetic.

print("\n--- isalpha() ---")
print("Python".isalpha())        # True
print("Python123".isalpha())     # False
print("Hello World".isalpha())   # False


# 8.10 isdecimal()
# Checks whether all characters are decimal characters.

print("\n--- isdecimal() ---")
print("123".isdecimal())      # True
print("10.5".isdecimal())     # False
print("Python".isdecimal())   # False


# 8.11 isdigit()
# Checks whether all characters are digits.

print("\n--- isdigit() ---")
print("123".isdigit())     # True
print("30".isdigit())      # True
print("Thirty".isdigit())  # False


# 8.12 isidentifier()
# Checks whether a string is a valid Python identifier.

print("\n--- isidentifier() ---")
print("30DaysOfPython".isidentifier())       # False
print("thirty_days_of_python".isidentifier()) # True
print("Python".isidentifier())               # True


# 8.13 islower()
# Checks whether all cased characters are lowercase.

print("\n--- islower() ---")
print("thirty days of python".islower())  # True
print("Thirty days of python".islower())  # False


# 8.14 isupper()
# Checks whether all cased characters are uppercase.

print("\n--- isupper() ---")
print("thirty days of python".isupper())  # False
print("THIRTY DAYS OF PYTHON".isupper())  # True


# 8.15 isnumeric()
# Checks whether all characters are numeric.

print("\n--- isnumeric() ---")
print("123".isnumeric())  # True
print("10".isnumeric())   # True
print("ten".isnumeric())  # False


# 8.16 join()
# Joins elements of an iterable using a separator.

web_technologies = ["HTML", "CSS", "JavaScript", "React"]

result = ", ".join(web_technologies)

print("\n--- join() ---")
print(result)
# Output: HTML, CSS, JavaScript, React


# 8.17 strip()
# Removes whitespace or specified characters from both ends.

text = "   thirty days of python   "

print("\n--- strip() ---")
print(text.strip())

text = "yyyPythonyyy"
print(text.strip("y"))  # Python


# 8.18 replace()
# Replaces an existing substring with another substring.

text = "thirty days of python"

print("\n--- replace() ---")
print(text.replace("python", "coding"))
# Output: thirty days of coding


# 8.19 split()
# Splits a string into a list.

text = "thirty days of python"

print("\n--- split() ---")
print(text.split())
# Output: ['thirty', 'days', 'of', 'python']

# Splitting using a specific separator
text = "HTML,CSS,JavaScript"
print(text.split(","))
# Output: ['HTML', 'CSS', 'JavaScript']


# 8.20 title()
# Converts the first character of each word to uppercase.

text = "thirty days of python"

print("\n--- title() ---")
print(text.title())
# Output: Thirty Days Of Python


# 8.21 swapcase()
# Converts uppercase to lowercase and vice versa.

text = "thirty days of python"

print("\n--- swapcase() ---")
print(text.swapcase())
# Output: THIRTY DAYS OF PYTHON

text = "Thirty Days Of Python"
print(text.swapcase())
# Output: tHIRTY dAYS oF pYTHON


# 8.22 startswith()
# Checks whether a string begins with a specified value.

text = "thirty days of python"

print("\n--- startswith() ---")
print(text.startswith("thirty"))  # True
print(text.startswith("python"))  # False


# END OF PYTHON: STRINGS
# ============================================================
