# Challenge: Swap two variables and display the contents as verification
# NOTE: this requires the use of Micropy REPL (i.e. via Picocom)

var1 = "Hello"
var2 = "MicroPy"
temp = var1
print(var1)
print(var2)
print(temp)
var1 = var2
var2 = temp
