# n = [1,1,1,1,3,4,6,8,8,0,3,2,0,1,10]
# i = 0
# while i<len(n):
#     j = 1
#     while j<len(n):
#         if n[i]==n[j]:
#             n.remove(n[i])
#         j+=1
#     i+=1
# print(n)

# n = [1,1,1,1,3,4,6,8,8,0,3,2,0,1,10]
# a = []
# for i in range (len(n)):
#     if n[i] not in a:
#         a.append(n[i])
# print(a)
# n = [1,1,1,1,3,4,6,8,8,0,3,2,0,1,10]
# n = list(dict.fromkeys(n))
# print(n)