name = "aakriti"

print(len(name)) #it will tell you the length of string

print(name.endswith("iti")) #tell you if it starts with this string 

print(name.startswith("aakr")) # checks if this string satrts with these alphabets or not

print(name.capitalize()) #capitiliaze only the starting word of the given string first alphabet will be capital

# Case manipulation
name = "aakriti soam"

print(name.upper())        # AAKRITI SOAM
print(name.lower())        # aakriti soam
print(name.title())        # Aakriti Soam
print(name.capitalize())   # Aakriti soam
print(name.swapcase())     # AAKRITI SOAM → aakriti soam

# Modify and clean
messy = "  Hello World!  "

print(messy.strip())                       # "Hello World!"
print(messy.lstrip())                      # "Hello World!  "
print(messy.rstrip())                      # "  Hello World!"
print(messy.replace("World", "Python"))   # "  Hello Python!  "

tag = "unhappy"
print(tag.removeprefix("un"))             # "happy"
print(tag.removesuffix("py"))             # "unha"


# Split and join
csv_data = "Meerut,Delhi,Jaipur,Mumbai"

cities = csv_data.split(",")      # ['Meerut', 'Delhi', 'Jaipur', 'Mumbai']
print(cities)

result = " → ".join(cities)         # "Meerut → Delhi → Jaipur → Mumbai"
print(result)

lines = "line1\nline2\nline3"
print(lines.splitlines())        # ['line1', 'line2', 'line3']

# Format and pad
user = "Aakriti"
score = 95

print(f"Welcome, {user}! Your score: {score}")   # f-string (modern)
print("Hello {}".format(user))                    # .format() style

print("42".zfill(6))           # "000042"
print("AI".center(10, "*"))   # "****AI****"
print("ML".ljust(8, "-"))    # "ML------"
print("ML".rjust(8, "-"))    # "------ML"

print("2026".isdigit())      # True
print("Python".isalpha())    # True
print("AI2026".isalnum())   # True
print("   ".isspace())       # True
print("HELLO".isupper())    # True
print("hello".islower())    # True
print("hello123".isdigit()) # False — mixed
