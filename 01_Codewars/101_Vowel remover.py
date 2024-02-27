def shortcut( s ):
    new_str = ""
    for char in s:
        if char not in "aeiou":
            new_str += char
    return new_str


