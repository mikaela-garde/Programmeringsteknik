#uppgift 1
def rectangle_area(height, width):
    area = height*width
    return area

#uppgift 2
def rectangle_circumference(height, width):
    circumference = 2*height+2*width
    return circumference

#uppgift 3
def third_character_of_string(string):
    if len(string) > 2:
        return string[2]
    else:
        return False
