
import my_module


# Uppgift 1 (givet)
y = 222
x = 111
x_list = [111, 222, 333, 444]
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
my_module.scope_testing_function(x, x_list)
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

# Uppgift 2
print(my_module.my_function(2))
print(my_module.my_function(5))


# Uppgift 3 (att skrivas)
print(my_module.roll_dice(5))

# Uppgift 4 (att skrivas)
print(my_module.my_sort_list([3, 7, 5, 2, 1]))
print(my_module.my_sort_list([5, 2, 1, 11, 10]))
print(my_module.my_sort_list([1, 2, 3]))

# Uppgift 5 (att skrivas)
print(my_module.bandit_language("hej jag heter mikaela"))
print(my_module.bandit_language("vad heter du?"))


# Uppgift 6 (givet)
animals = {'tiger': ['claws', 'sharp teeth', 'four legs', 'stripes'],
           'elephant': ['trunk', 'four legs', 'big ears', 'gray skin'],
           'human': ['two legs', 'funny looking ears', 'a sense of humor']
           }

# Uppgift 6 (att skrivas)
def make_bandit_dictionary(animals):
    new_dict = {}
    for item in animals:
        new_list = []
        for i in animals[item]:
            new_list.append(my_module.bandit_language(i))
        new_dict[item] = new_list
    return new_dict

print(make_bandit_dictionary(animals))