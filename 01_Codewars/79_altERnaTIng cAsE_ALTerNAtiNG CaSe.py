def to_alternating_case(string):
    new_str = ""
    for char in string:
        if char == char.upper():
            new_str += char.lower()
        else:
            new_str += char.upper()
    return new_str