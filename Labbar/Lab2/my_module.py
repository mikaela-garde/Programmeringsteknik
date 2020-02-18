
import copy
import math
import random

# Uppgift 1 (givet)
def scope_testing_function(x, x_list):
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x = 1
    x_list[0] = 1
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x_list = [1, 2, 3, 4]
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    return x #Varför???

x_list = [11, 22, 33, 44]
x = 11
y = 22
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

scope_testing_function(x, x_list)
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

# Uppgift 2 - sinus funktion
def my_function(x):
    return math.pow(math.sin(x), 2) + math.pow(x, 2)

# Uppgift 3 - täningar
def roll_dice(n):
    sum = 0
    for i in range(n):
        sum += random.randint(1,6)
    return sum

# Uppgift 4 - Bubbelsort
def my_sort_list(list):
    for j in range(len(list)-1, 0, -1):
        for i in (range(j)):
            if list[i] > list[i+1]:
                temp = list[i+1]
                list[i+1] = list[i]
                list[i] = temp
    return list

# Uppgift 5 - Rövarspråket
def bandit_language(string):
    consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    new_string = ""

    for i in range(len(string)):
        char = string[i]
        if char in consonant:
            char += "o" + string[i]
        new_string += char
    return new_string

