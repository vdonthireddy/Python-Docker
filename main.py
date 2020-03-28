def GreetMe(name):
    return "Hello " + name

while True:
    name = input("What is your name (Ctrl+C to exit)? ")
    greeting = GreetMe(name)
    print(greeting)