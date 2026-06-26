marks = {
    "Alice": 300,
    "Bob": 250,
    "Charlie": 34,
}
print(marks.items()) # it will return a list of tuples 

print(marks.keys()) # it will return a list of keys 

marks.update({"Alice": 23})
print(marks) # it will update the value of alice marks to 23

print(marks.get("Bob")) # it will return the value of bob marks

