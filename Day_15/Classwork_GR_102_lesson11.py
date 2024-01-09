#შექმენით ფუნქცია რომელიც გაიგებს რომელ პოზიციებზეა სიმბოლოები


def find_index_of_chars(any_char,sentence):
    symbol_index = []
    for i in range(len(sentence)):
        if sentence[i] == any_char:
            symbol_index.append(i)
    print(any_char,"simbolo gvxvdeba",symbol_index, "adgilebze")
    
find_index_of_chars("a","ana giorgadze")
