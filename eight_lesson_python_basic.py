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
r, c = [int(x) for x in input().split(", ")]
matrix = []
all_sum = 0
for _ in range(r):
    inner_list = [int(x) for x in input().split(", ")]
    # all_sum += sum(inner_list)
    matrix.append(inner_list)
print(matrix, sep="\n")
for i in range(r):

# print(all_sum)
# print(matrix)

