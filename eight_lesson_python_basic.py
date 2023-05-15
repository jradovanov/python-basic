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
After that, with one "tab" 



'''
atrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

Как да вземем конкретен индекс:

value = matrix[0][1]

print(value)

Как да обходим матрица с вложени цикли:

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=' ')
    print()