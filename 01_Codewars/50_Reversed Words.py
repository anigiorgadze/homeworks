def reverse_words(s):
    my_str = s.split()
    my_str.reverse()
    final_str = ""
    for element in my_str:
        final_str += element + " "
    return final_str[:-1]

