print("Hello, World!, Virtual Studio Code is ready!")

x=input("Enter your name: ")
y=int(input("Enter your age: "))

a=18
b=65

if y>=a and y<=b:
    print("Welcome to the club,",x)
elif y>b: # type: ignore
    print("You are too old to enter the club,",x)      
else:
    print("You are too young to enter the club,",x)     


print("Goodbye,",x)
      
    