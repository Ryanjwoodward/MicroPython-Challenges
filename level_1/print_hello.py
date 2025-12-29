# Challenge: Print "Hello, Micropython" using three different methods
# NOTE: this requires the use of Micropy REPL (i.e. via Picocom)

# 1. Print to the terminal in the classic way
print("Hello, MicroPython")

# 2. Print using the lower-level version
import sys
hello = sys.stdout.write("Hello, MicroPython\n") # if you omit the 'hello =' you will see the byte count appended (18)

# 3. Directly using REPL features
"Hello, MicroPython"
