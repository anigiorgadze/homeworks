# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

#1
def smash(words):
    finally_sentence = ""
    for i in range(len(words)):
        if i == 0:
            finally_sentence +=words[i]
        else:
            finally_sentence += " "+words[i]
    return finally_sentence


#2

def smash(words):
    return " ".join(words)