a = 31
t = type(a) # class<int>
print(t)

b = 3.114
t = type(b) # class<float>
print(t)

c  = "aakriti"
t = type(c) #class<str>
print(t)  #with the help of type function we can find the datatype of a variable

a = "31.2"
t = type(a)
print(t) #class<str> even if we assign a number to a variable but if it is in double quotes then it is considerd as a string and not a number

a = "321.2"
b = float(a) #typecasting a string to a float
t = type(b)
print(t) #class<float>
