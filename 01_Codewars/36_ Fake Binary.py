# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string


def fake_bin(x):
    final_str = ""
    for char in x:
        if int(char) < 5:
            final_str += "0"
        else:
            final_str += "1"
    return final_str