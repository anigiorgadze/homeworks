# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    new_string = ""
    for i in range(repeat):
        new_string += string
    return new_string