def solution(a, b):
    new_str = ""
    if len(a)> len(b):
        new_str += b+a+b
    else:
        new_str += a+b+a
    return new_str