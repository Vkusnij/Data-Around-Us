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