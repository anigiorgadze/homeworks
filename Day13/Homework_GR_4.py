# # It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

# s = "ok"
# new_s =""
# length = len(s)



# if len(s) > 2:
#     for i in range(length):
#         if i != (length-1) and i != 0:
#             new_s += s[i]
#     print(new_s)
# else: 
#     print(s)


# #in codewors
# def remove_char(s):
#     new_s = ""
#     length = len(s)
    
#     if len(s) > 2:
#         for i in range(len(s)):
#             if i != (length-1) and i != 0:
#                 new_s += s[i]
#     return new_s
#     return(s)