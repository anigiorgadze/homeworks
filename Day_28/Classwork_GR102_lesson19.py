# def zipped (aa,bb,cc):
        
#         final_str = []
#         list = [len(aa), len(bb), len(cc)]

#         for i in range(min(list)):
#                 final_str.append("{}{}{}".format(aa[i],bb[i],cc[i]))
        

#         for i in range(min(list),max(list)):
#             if max(list) == len(aa):
#                 final_str.append(aa[i])
#             elif max(list) == len(bb):
#                 final_str.append(bb[i])
#             elif max(list) == len(cc):
#                 final_str.append(cc[i])
#         print(final_str)
                
                

# zipped(["a", "b", "c", "d", "w", "k"],["1", "2", "3", "4", "5", "6", "7"],["z", "x", "y", "w"])



#1
# def math(a, b, c):
#     return max(a-b+c, a+b*c, (a+b) -c, a*(b+c) )

# print(math(16,15,34)-math(37,21,1)-math(14,1,6)+-69 )  

#3

def math(a,b,c):

    return max(a+b+c, a*b*c, (a+b) *c, c*(a+b), a*(b+c))
print(math(16,15,34)-math(37,21,1) - math(14,1,6)-+-69)