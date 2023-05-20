'''
In this lesson we will learn about arithmetic operators.
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

This is all for now.
Of course, the operators are not only one type but many. For now, we use the arithmetic and will use
assignment operators later.

Next lesson will be first one as real programmers.
See you!
'''

# Reverse Numbers

# numbers = input().split()
# for index in range(len(numbers) -1, -1, -1):
#     print(numbers[index], end=" ")



# Fashion

# clothes = [int(x) for x in input().split()]
# clothes = input().split()
# rack_capacity = int(input())
#
# used_racks = 1
# current_rack = rack_capacity
#
# while clothes:
#     current_piece = int(clothes[-1])
#
#     if current_piece <= current_rack:
#         clothes.pop()
#         current_rack -= current_piece
#     else:
#         used_racks += 1
#         current_rack = rack_capacity
#
# print(used_racks)

# from collections import deque
#
# kids = deque(input().split())
# n = int(input())
#
# while len(kids) > 1:
#     kids.rotate(-n)
#     print(f"Removed {kids.pop()}")
# print(f"Last is {kids.popleft()}")


# task 3



# task 2

# phrase = input()
# my_list = []
#
# for index in range(len(phrase)):
#     if phrase[index] == "(":
#         my_list.append(index)
#     elif phrase[index] == ")":
#         start_index = my_list.pop()
#         print(phrase[start_index:index + 1])


# task 1
# text = list(input())
# for element in range(len(text)-1, -1, -1):
#     print(text.pop())
#     print(type(text))
# while text:
#     print(text.pop())
# print(text)

# def a():
#     return 5
#
#
# def b():
#     return 6
#
#
# def c():
#     print(a())
#     print(b())
#
#
# c()