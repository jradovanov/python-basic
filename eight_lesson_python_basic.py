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
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)

numbers = input().split()
for index in range(len(numbers) -1, -1, -1):
    print(numbers[index], end=" ")


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
