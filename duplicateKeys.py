dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
}
# #  {“ball”:”red”,”bat”:4,”wickets”:8}
# new_dic = {}
# # print(new_dic)
# for ket, value in dic.items():
#     if dic[ket] not in new_dic:
#         new_dic[ket] = value
# print(new_dic)
# for i  in dic.keys():
#     print(i)
new = {2:3,4:5}
# dic.update(new)
a = {}
for i in dic,new:
    print(i)
    a.update(i)
print(a)

    