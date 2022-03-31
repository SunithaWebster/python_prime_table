# python_prime_table


**Description**

A simple Python application, taking in user input of a positive integer, N and returning a multiplication table - with N primes as the factors in the header row and first column.


**How To Run**

Navigate to the root directory and use CLI to run the following command:

`python -m prime_table_app`

Tests can be run individually at present.

**Pleased with:**

- Application works and produces the envisaged output
- Algorithm is performant for larger values of N - it can produce a table for N = 100
- No external libraries or dependencies


**Areas for Development Given Further Time:**

- Rethink argument input in functions, to enable test suite automation
- Refactor code into a class, enabling re-use in other programs
- Perform speed benchmarking to establish actual times of execution of each function, for various values of N
- Undertake big O space / time analysis to see where refactoring could improve memory use and run times, e.g., the nested
for-loop in the app's display_multiplication_table function 
- Strengthen input validation to incorporate better exception handling for textual input
- Design as a Flask app for deployment online 
