#write a python program to display a user entered name followed by good afternoon using input() function

name = input("Enter your name: ")
print("Good afternoon, " + name + "!")
print(f"Good afternoon, {name}!") #using f-string for better readability it will automatically replace the variable name with its value in the string.
