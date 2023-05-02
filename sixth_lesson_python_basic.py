'''
Hello all!
Last lesson we used variables to add, multiply, divide and so on - numbers, as integers.
Same we can do of course with fractional numbers as float
Example:
a = float(input()) - let be 5.45
b = float(input()) - let be 4.38
c = a * b
print(c) - 23.871 will be the answer

Ok, but both examples from lesson 5 and lesson 6 are with numbers. How we can use the strings?
Let see how the system greeting you when you write your name.

Example:
    The user John wants to come inside our system
    We want to say "Hello" to John.
let's make a variable - name
    name = input() - because we expecting a string
    print(f"Hello, {name}!") - This will print to the console "Hello, John!" or the name you wrote.
Here we see a couple new things.
First, we can use the variable in different combination. To do that in the "print" function have to use
figure brackets around it. But this is not enough. Have to use "f" in the beginning and all after that
have to be in quotes.
So, the print will be like this: print(f""). Then, we put all that we want between quotes:
like that: print(f"What ever we want to write here {place for variable} another word or whatever")
In our case, it looks like - print(f"Hello, {name}!") or print("Hi all, I am {name}! Nice to meet you!")

When we want to print string variables in one or many sentences have to write first:
f"" in the print brackets and then to put variable in the figure brackets.
We can use as many variables as we want, just follow the rules.

Let's see another example:
name = input() - Olivia
hour = float(input()) - 17.15
time_for_leaving = int(input()) - 20
print(f"Mrs {name}, please join in our party at {hour}. the party will finish at {time_for_leaving}"

The result will be: Mrs Olivia, please join in our party at 17.15. the party will finish at 20

This is all for lesson 6

See you in lesson seven
'''