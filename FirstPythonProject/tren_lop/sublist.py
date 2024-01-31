# def ischildOrder(a, b):
#     i = 0
#     while(i < len(b)-len(a)):
#         isok = True
#         for j in range(0, len(a)):
#             if(a[j] != b[j+i]):
#                 isok = False
#                 break
#         if(isok):
#             return True
#         i += 1
#     return False

def ischildOrder2(a, b):
    for i in range(0, len(b) - len(a)):
        if(b[i:i+len(a):] == a):
            return True
    return False


a = [1,2,3,'aaa']
b = [1,2,3,'aaa',4,5]

print('a is sublist of b: ' + str(ischildOrder2(a,b)))

a = ['1',2,8]
b = ['1',2,8,9]

print('a is sublist of b: ' + str(ischildOrder2(a,b)))
