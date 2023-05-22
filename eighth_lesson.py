'''
Hi all.
This is our eight lesson.
Today we will learn "if - else" construction.
This construction checks if a logical conditions is valid for a given expression.
Examples for such conditions are:
Equals - in Python equals is expressed with "=="
If we write "=" it means that it assign the value.
So, if we want to check "a" is equals or not to "b" have to write "=="
How to check:
First have to use "if" statement followed by condition a == b and ":" for the end.
The whole expression will be: if a == b:
After that, with one "tab" inward we define what happens if it is true
Example:
    if a == b:
        print("Yes! They are equals")
What about if they are not?
Then with "else" we define what should happen
So, the complete code will look something like that:

if a == b:
    print(Yes! They are equals")
else:
    print(No! They are not")
'''

r, c = [int(x) for x in input().split(", ")]
matrix = []
all_sum = 0
for _ in range(r):
    inner_list = [int(x) for x in input().split(" ")]
    matrix.append(inner_list)

for col in range(c):
    sum_col = 0
    for row in range(r):
        sum_col += matrix[row][col]
    print(sum_col)