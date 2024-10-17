# The following line is an example of how you can add a string (aka text) value to a variable.
exampleVariable = "This is a string added to the variable named exampleVariable"

'''
Explanation:

[variable name] [equal sign] [value]

[variable name]: `exampleVariable`
You can give almost any name to a variable, but be careful with two things:
1. Don't use special characters in it.
2. Use the "snake_case" form where words are separated by underscores, 
   and all letters are in lowercase (e.g., this_is_a_snake_case_text).
   Alternatively, Python also allows "camelCase" like JavaScript, but "snake_case" is more common in Python for variable names.
It is recommended to use the English language throughout your code, especially (but not exclusively) for variable names.

[equal sign]: `=`
Remember, the equal sign between the variable name and the value is crucial.
This serves as the "assignment operator" which assigns the value to the variable.

[value]: `"This is a string added to the variable named exampleVariable"`
The value is the piece of data you want to assign (save) to the variable for later use.

In Python, there's no need for a semicolon at the end of the line.
'''

# The following line is just an example of how you can print text to the console using `print()`.
# You have to write a value or a variable name inside the parentheses.
print(exampleVariable)

# WRITE YOUR CODE HERE

# Set title

title = "One Piece"
print(title)

# Set author

author = "Eiichiro Oda"
print(author)

# Set publication year

year = 1997
print(year)

# Set millennial flag

is_Newer_Than_2000 = False
print(is_Newer_Than_2000)

# Set age

current_year = 2024
age = current_year - year
print(age)

# Set characters

characters = ["luffy", "Zoro", "Ussop", "Chopper"]
print(characters)

# Display specific characters

print(characters[0])
print(characters[2])

# Set favorite book

favorites_books = {
        "title": "One Piece",
        "author":"Eiichiro Oda",
        "year": 1997,
        "is_Newer_Than_2000": False,
        "age": 27,
        "characters": ["luffy", "Zoro", "Ussop", "Chopper"]
}

# Display specific properties

print(favorites_books["author"])
print(favorites_books["year"])

# Display array item through an object

print(favorites_books["characters"][2])

# Set list of books

favorites_books = [
   {
        "title": "One Piece",
        "author":"Eiichiro Oda",
        "year": 1997,
        "is_Newer_Than_2000": False,
        "age": 27,
        "characters": ["luffy", "Zoro", "Ussop", "Chopper"]
   },
   {
        "title": "Naruto",
        "author":"Masashi Kishimoto",
        "year": 1999,
        "is_Newer_Than_2000": False,
        "age": 25,
        "characters": ["Naruto", "Saske", "Itachi", "Shino"]
   }
]

# Display object properties through an array

print(favorites_books[1]["title"])
print(favorites_books[1]["characters"][0])

# Calculate age difference between books

age_difference = favorites_books[1]["year"] - favorites_books[0]["year"]
print(age_difference)