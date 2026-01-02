# Challenge: Compare the results between dividing with integer vs float-point values
# NOTE: this requires the use of Micropy REPL (i.e. via Picocom)

#NOTE: Python 3 uses 'true' division, it will always be float result
result = 10 / 5 # 2.0 (float)
print(result)

result = 10.5 / 5.2 # 2.019... (float)
print(result)

#If we want true 'integer' division we must use 'floor' division operator:
# Floor division is integer if bother operands are ints, result will be float any other time
result = 10 // 5
print(result) # 2 (int)

result = 12 // 3 # 4 (int)
print(result)

result = 12.0 // 3 # 4.0 (float)
print(result)
