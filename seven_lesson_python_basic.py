'''
We are in seven lesson
numbers = [int(x) for x in input().split()]
count = int(input())

for _ in range(count):
    # number_to_remove = min(numbers)
    min_num = float("inf")
    for el in numbers:
        if el < min_num:
            min_num = el
    print(min_num)

'''