'''
Hi all.
This is our eight lesson.
Today we will learn "if - else" construction.
This construction checks if a logical conditions is valid for a given expression.
Examples for such conditions are:
Equals - in Python equals is expressed with "=="
If we write "=" it means that it assign the value.
So, if we want to check "a"is equals or not to "b" have to write "=="
How to check:
First have to use "if" statement followed by condition a == b and ":" for the end.
The whole expression will be: if a == b:
After that we have to point out what happened if they are equal.
if a == b:
    print("Yes!")
As you can see, "print("Yes!")" is one tab inward.
This mean that the entire expression that is inside refer to this "if check"
In Python, when we wants to refer something have to be 4 spaces or 1 tab inward.


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

