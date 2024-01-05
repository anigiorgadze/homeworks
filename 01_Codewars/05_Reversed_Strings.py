
def solution(string):
    new_string = ""
    for i in range(len(string)):
        new_string += string[-i-1]
    return new_string