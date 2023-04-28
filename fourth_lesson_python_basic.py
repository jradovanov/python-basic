'''
This is our fourth lesson.
Let's do something with our knowledge so far.
One of the first task is to print the numbers from 1 to 10.
With all that we know, the only way is to say "print" and corresponding number.
Example:
    print(1)
    print(2)
    print(3)
Of course, this is not the only way to print numbers, even this is not a way at all but for now...

Here is the moment to introduce the 'variable"
The variable is the place where we store data. As the name suggest, the stored data can be modified.
Let see one example:

a = 5
print(a)
a = 6
print(a)

In this example first we assign a value to the variable and then modify it.
Python allow this. In many other language this is not possible.

How this can help us in this case where have to print numbers from 1 to 10?
If the condition is like this, the answer is - not at all.
But, if we expect numbers to be handed one after the others, then we can use the variable. Let see how.
First we will say to computer that our variable expecting a number.
Then we want this number to be printed. All this will look like this:

a = int(input())
print(a)

First we remember that have to use int when we expect a number
Then, first row say - I am expecting a number. When it comme, store it in the variable "a"
After that print it.

If the given number is 7, then 7 will be printed. If after that the given number is 2, 2 will be printed.
What is the use?
In first example, we have to write print() 10 times. When the variable is used, this will be only this
two rows because every time the variable "a" will be modified.

So, in this lesson we understand how to use the function "print", how to use "variable" and that variable
in python can be modified many times, something that the other languages cannot do.

See you in next lesson - five
'''