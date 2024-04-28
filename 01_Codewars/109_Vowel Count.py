def get_count(sentence):
    count_vowels = 0
    
    for char in sentence:
        if char in 'aeiou':
            count_vowels +=1
    return count_vowels
        