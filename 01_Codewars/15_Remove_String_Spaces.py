def no_space(x):
    new_string = ""
    for char in x:
        if char != " ":
            new_string += char
    return new_string



#2
def no_space(x):
    return x.replace(' ', '')