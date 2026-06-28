a = int(input("Enter your age: "))

# if elif else ladder

if(a>=18):
    print("you are eligible to vote")
    print("good for you")
    
elif(a<0):
    print("you are entering invalid age")    

elif(a==0):
    print("you are not born yet dumb")    

else:
    print("you are not eligible to vote")

print("end of this program")