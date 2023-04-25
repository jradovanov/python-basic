'''
Will start with Python rules for names we have to use.
As we mentioned in second lesson, it is important to use names,
which will tell to the readers what the name it tings do.
Usually, one program had been written from many programmers
Everyone have to understand from the name what it is about.
Other rule connected to names is "snake_case".
This mean to write only with lower letters and to use "_" between the words

So, after we find out what the function "print" do, it's time to understand what
kind of data we are working with.
All data we work for is called "string". This including letters, words, numbers,
fractional numbers. If we not change them they will always been a string.
If the data came outside, this happened usually when we solve tasks
in the university. Then we just write "input()" which mean: I expected strings to
come from outside. All the data that will come in this way have to be used as a
string.
If we want to work with numbers or fractional numbers, then we have to use:
"int" - for numbers or "float" - for fractional numbers.
The syntax will be: "int(input())" for numbers, or 'float(input())" for fractional
numbers.
These commands will change data in the wanted format.

So, if we receive data which is not a numbers, have to write "input()"
Here is the example:
a = input()
print(a)

In this example, if we receive data - "Hello world", on display will
be shown - Hello world.
Note: If we receive numbers, it will not be shown as error but the numbers will be converted to symbols.
They will be a string, and we will not be able to operate with them as a numbers.


If we receive data which is number, have to write "int(input())"
Here is the example:
a = int(input())
print(a)

In this example, if we receive data - 234, on the display will be shown - 234
Note: In this case if we receive data which is a string or fractional numbers, an error will be displayed:
"The error will be: "invalid literal for int()"
This mean that if you say to your IDE that you expect numbers, numbers must enter!
If we are not sure what kind of data will be given, then is better to write "input()" and after that, when
we see the data will be possible to convert in numbers.

If we receive data which is fractional numbers, have to write "float(input()).
Here is the example:
a = float(input())
print(a)

In this example, if we receive data - 234.56, on the display will be shown - 234.56
Note: Same rules as for the numbers are valid here.
'''