# Challenge: Using if-else check if a number is odd or even
# NOTE: this requires the use of Micropy REPL (i.e. via Picocom)

def even_odd(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


even_odd(12)
even_odd(13)
