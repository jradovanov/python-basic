'''
In this lesson we will learn about operators.
In Python, operators are "+", "-", "/", "//", "*"
We know them from mathematics. The only exception is "//"
This operator means - integer division.
But what exactly this means. When we divide normal - "/", the result could be fractional number
With "//" the result always will be integer division. It can be very helpfully.
For example:
1. 7 / 2 = 3.5
2. 7 // 2 = 3

Let's see an example for all:
We will receive two integers:

a = 5
b = 8
print(a + b) - The result will be - 13
print(a - b) - The result will be - 3
print(a * b) - The result will be - 40
print(a / b) - The result will be - 0.625
print(a // b) - The result will be - 0

If we have integer division, this mean that we have remainder.
We have to use that somehow. And here comes operator "%"
For example:
7 // 2 = 3 - integer division
7 % 2 = 1 - modular division

'''
python
Copy code
def add_todo():
    title = input("Enter title: ")
    text = input("Enter text: ")
    with open("todos.txt", "a") as f:
        f.write(f"{title}\n{text}\n")


python
Copy code
def read_todos():
    with open("todos.txt", "r") as f:
        todos = f.readlines()
    for i in range(0, len(todos), 2):
        print(f"{todos[i].strip()}: {todos[i+1].strip()}")


python
Copy code
def edit_todo():
    title = input("Enter title of the todo you want to edit: ")
    new_text = input("Enter new text: ")
    with open("todos.txt", "r+") as f:
        todos = f.readlines()
        f.seek(0)
        for i in range(0, len(todos), 2):
            if todos[i].strip() == title:
                f.write(f"{todos[i]}\n{new_text}\n")
            else:
                f.write(f"{todos[i]}{todos[i+1]}")
        f.truncate()
