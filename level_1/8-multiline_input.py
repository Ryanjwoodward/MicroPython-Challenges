# Challenge: Practive Multiline input in the Micropy REPL
# NOTE: this requires the use of Micropy REPL (i.e. via Picocom)

def greet(name):
     print("Hello,", name)
     print("Welcome to MicroPython!")

# to get out of multi-line entry it may reuqire pressing enter multiple times
greet("Alice")


def number_check(number):
    if number > 10:
        print("number larger than 10")
    else:
        print("number smaller than 10")

number_check(12)

number_check(5)
