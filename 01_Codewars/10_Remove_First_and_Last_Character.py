#1
def remove_char(s):
    new_s = ""
    length = len(s)
    
    if len(s) > 2:
        for i in range(len(s)):
            if i != (length-1) and i != 0:
                new_s += s[i]
    return new_s
    return(s)


#2
def remove_char(s):
    new_s = ""
    i = 1
    while i < len(s)-1:
        new_s += s[i]
        i += 1
    return new_s    


#3
def remove_char(s):
    return s[1:len(s)-1]