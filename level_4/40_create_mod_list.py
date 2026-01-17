# Challenge: Create and modify a list in Python
# NOTE: this requires the use of Micropy REPL (i.e. via Picocom)

numList = [5, 4, 8, 2, 1, 9]
print(numList)

numList.sort()
print(numList)

myList = ["item1", "item2", "item3"]
print(myList)

myList.append("item4")
print(myList)

newList = ["item1", 2, 3.3, [1, 2, "three"]]
print(newList)

newList.pop(1) # removes and displays
print(newList)
