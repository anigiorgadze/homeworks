geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    new_array = []
    for element in birds:
        if element in geese:
            continue
        else:
            new_array.append(element)
    return new_array
            