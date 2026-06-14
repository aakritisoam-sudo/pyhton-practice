# program to dtect double space in a string

string = input("Enter a string with double  space:")
print(string.find("  ")) #find() method returns the index of first occurence of specified value

#if getting -1 as output then there is no double space in it otherwise it will return some positive string index