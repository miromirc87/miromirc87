#Nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

rows = int(input("Enter # of rows: "))
columns = int(input("Enter # of columns: "))
symbol = input("Enter a symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()


# --- Explanation ---

# 1. Input Gathering:
#    - rows: The user is prompted to enter the number of rows for the grid. It is converted from a string to an integer using int().
#    - columns: Similarly, the user is prompted to enter the number of columns for the grid, also converted to an integer.
#    - symbol: The user is prompted to enter a symbol (a character or string) that will be displayed in the grid.

# 2. Outer for loop:
#    - The "for x in range(rows):" loop iterates through the rows.
#    - range(rows) generates numbers from 0 to rows-1, meaning the loop will execute rows times.

# 3. Inner for loop:
#    - Inside the outer loop, "for y in range(columns):" iterates through the columns.
#    - For each iteration of the outer loop (one row), this inner loop runs columns times to print the symbols in that row.

# 4. print(symbol, end=" "):
#    - The print() function outputs the symbol with a space (" ") after it, instead of starting a new line (end=" ").

# 5. print():
#    - After the inner loop completes (a row is printed), this statement moves the cursor to a new line.
#      Without it, all rows would print on the same line.

# Example Run:
# Input:
# Enter # of rows: 3
# Enter # of columns: 5
# Enter a symbol: *

# Execution:
# 1. Outer loop (x) starts. x = 0, then enters the inner loop:
#    * * * * *
#    - Inner loop (y) runs 5 times, printing * with spaces.

# 2. Outer loop (x = 1), inner loop runs again:
#    * * * * *
#    * * * * *

# 3. Outer loop (x = 2), inner loop runs again:
#    * * * * *
#    * * * * *
#    * * * * *

# Final Output:
# * * * * *
# * * * * *
# * * * * *
