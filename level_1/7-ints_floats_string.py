# Challenge: Convert between 'int' 'float' and 'string'
# NOTE: this requires the use of Micropy REPL (i.e. via Picocom)

intNum = 12
print(intNum)

floatNum = float(intNum)
print(floatNum) # 12.0

floatNum = 12.3
intNum = int(floatNum)
print(intNum)   # 12

stringNum = str(intNum)
print(stringNum)
stringNum = str(floatNum)
print(stringNum)

stringNum = "15.3"
intNum = int(stringNum) # CAUSES ERROR!

floatNum = float(stringNum)
print(floatNum)

intNum = int(floatNum)
print(intNum)
