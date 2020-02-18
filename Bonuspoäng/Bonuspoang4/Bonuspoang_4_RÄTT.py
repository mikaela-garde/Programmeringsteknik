#Skriva till fil
def create_file_from_string (my_filename, my_string):
    file = open(my_filename, 'w')
    file.write(my_string)
    file.close()

#Läsa från fil
def print_file_on_screen(my_filename):
    file = open(my_filename, 'r')
    print(file.read())
    file.close()

