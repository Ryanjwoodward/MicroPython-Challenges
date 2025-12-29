# MicroPython-Challenges
This Repo contains the coding challenges I wrote for the Micropython Workshop I hosted at GCU
***

Below is a **progressive, challenge-based curriculum**, ordered from **absolute beginner → advanced**, focused on:

- Core Python/MicroPython syntax
- Data structures
- Control flow
- Functions & modules
- Memory awareness (important for MicroPython)
- Built-in libraries (`sys`, `gc`, `time`, `math`, etc.)
- REPL fluency
- Writing clean, testable code _on-device_
- No GPIO, no sensors, no Wi-Fi, no peripherals—just the ESP32 running MicroPython.

---

# Level 1: Absolute Beginner (REPL Mastery)

**Goal:** Become fluent in the REPL and basic syntax.
### REPL & Basics
1. Print “Hello, MicroPython” in three different ways
2. Use the REPL as a calculator (add, subtract, multiply, divide)
3. Find the MicroPython version using `sys.version`
4. Print available built-in modules using `help('modules')`
5. Write a one-line program that swaps two variables
6. Experiment with integer vs float division
7. Convert between `int`, `float`, and `str`
8. Practice multiline input in the REPL
9. Trigger and catch a `SyntaxError`
10. Restart the REPL and re-run previous commands
    

---

# Level 2: Variables & Control Flow

**Goal:** Understand execution flow and decision making.
### Conditionals

11. Write a program that checks if a number is even or odd
12. Implement a temperature classifier (cold/warm/hot)
13. Use nested `if` statements
14. Rewrite nested `if`s using `elif` 
15. Use a conditional expression (`x if y else z`)
16. Compare strings lexicographically
17. Compare integers vs strings (observe the error)
18. Create a menu system using `if/elif`
### Loops
19. Print numbers 1–10 using `while`
20. Print numbers 1–10 using `for`
21. Print only even numbers between 1–100
22. Implement a countdown timer (no delays yet)
23. Break out of a loop early
24. Skip items using `continue`
25. Create an infinite loop and safely exit it
26. Nest loops to generate a multiplication table

---

# Level 3: Functions (Core of Good MicroPython)

**Goal:** Write reusable, readable code.
27. Write a function that returns the square of a number
28. Write a function with default arguments
29. Write a function that accepts arbitrary arguments (`*args`)
30. Write a function that accepts keyword arguments (`**kwargs`)
31. Return multiple values from a function
32. Write a function that validates input types
33. Write a recursive function (factorial)
34. Convert a recursive function to iterative
35. Measure execution time of a function using `time.ticks_ms()`
36. Write a function that modifies a mutable argument
37. Write a function that _does not_ modify a mutable argument
38. Document a function using a docstring
39. Print a function’s docstring using `help()`

---

# Level 4: Data Structures

**Goal:** Learn memory-efficient and idiomatic data handling.
### Lists & Tuples
40. Create and modify a list
41. Slice a list in three different ways
42. Reverse a list without using `.reverse()`
43. Remove duplicates from a list
44. Sort a list manually (bubble sort)
45. Use list comprehensions
46. Compare memory usage of list vs tuple
47. Use tuples for immutable configuration data
### Dictionaries
48. Create a dictionary of settings
49. Safely access keys using `.get()`
50. Iterate over keys, values, and items
51. Merge two dictionaries
52. Count word occurrences in a string
53. Use a dictionary as a lookup table
54. Implement a simple state machine using dicts
### Sets
55. Remove duplicates using a set
56. Perform union, intersection, difference
57. Use sets to detect repeated inputs
58. Compare set vs list membership performance

---

# Level 5: Strings & Text Processing

**Goal:** Master string manipulation (very common in MicroPython).

59. Parse a CSV string manually
60. Count vowels in a string
61. Reverse words in a sentence
62. Implement a Caesar cipher
63. Validate a password (length, symbols, digits)
64. Use `startswith()` and `endswith()`
65. Format strings using `.format()`
66. Format strings using f-strings
67. Build a text-based menu system
68. Strip whitespace from user input
69. Convert numbers in strings safely

---

# Level 6: Modules & Imports

**Goal:** Organize code like a real embedded project.
70. Create a custom module (`utils.py`)
71. Import a single function from a module
72. Import a module under an alias
73. Use `__name__ == "__main__"`
74. Reload a module from the REPL
75. Create a constants module
76. Create a configuration module
77. Measure RAM usage before and after importing a module
78. Create a module that logs events
79. Build a simple plugin architecture

---

# Level 7: Exceptions & Robust Code

**Goal:** Write fault-tolerant MicroPython code.

80. Catch specific exceptions
81. Use `try/except/else/finally`
82. Create a custom exception class
83. Validate user input with exceptions
84. Gracefully recover from runtime errors
85. Log exceptions to a list
86. Retry logic using exceptions
87. Fail fast vs fail safe comparison
88. Handle `MemoryError`
89. Write a function that never crashes

---

# Level 8: Memory & Performance (MicroPython-Specific)

**Goal:** Think like an embedded developer.

90. Use `gc.collect()` and observe behavior
91. Measure free heap using `gc.mem_free()`
92. Create a memory leak intentionally
93. Fix the memory leak
94. Compare list growth strategies    
95. Pre-allocate buffers
96. Measure execution time differences
97. Compare recursion vs iteration
98. Avoid unnecessary object creation
99. Analyze stack vs heap usage
100. Write a memory-safe algorithm

---

# Level 9: File System (On-Board Flash)

**Goal:** Persist data without peripherals.

101. Create and write a file
102. Read a file line by line
103. Append to a file
104. Delete a file
105. Implement a simple logger
106. Store configuration in a file
107. Parse a config file
108. Handle missing files gracefully
109. Implement file rotation
110. Measure flash write cycles (theoretical)

---

# Level 10: Advanced Python Concepts (MicroPython Flavor)

**Goal:** Master the deeper language features.

111. Use generators
112. Write a custom iterator
113. Use `yield` for streaming data
114. Understand closures
115. Implement decorators
116. Use decorators for logging
117. Use decorators for timing
118. Monkey-patch a function
119. Dynamically import modules
120. Build a command interpreter

---

# Level 11: Architecture & Clean Design

**Goal:** Write production-quality MicroPython code.

121. Implement MVC-style separation
122. Build a command dispatcher
123. Create a task scheduler (no RTOS)
124. Implement cooperative multitasking
125. Write a state machine engine
126. Design a message-passing system
127. Implement dependency injection
128. Write unit-test-like assertions
129. Simulate events
130. Refactor for readability & memory

---

# Final Boss Challenges

131. Build a full REPL-driven application
132. Write a MicroPython shell
133. Implement a mini standard library
134. Create a configuration-driven app
135. Write documentation for your firmware
136. Build a profiling tool
137. Create a code linter (basic)
138. Implement a plugin system
139. Write self-testing firmware
140. Optimize until memory usage is minimal

---

## How I’d Suggest You Use This

- Treat each challenge as a **small Git commit**
- Keep everything on the ESP32, not your PC
- Regularly inspect:
    - `gc.mem_free()`
    - execution time
- Write **short programs**, not one giant script
- When ready, _then_ add peripherals
