a = {
"product": [
{"name": "lux Soap","price": 20},
{"name": "T shirt","price": 500},
{"name": "Jeans","price": 999},
{"name": "headphone","price": 2000},
{"name": "TV","price": 49999},
{"name": "5star","price": 10}
    ]
}
# i = 0
# product_Values = (a['product'])
# keysvalues = []
# lowest = 0
# highest = 0
# while i<len(product_Values):
#     c = product_Values[i]["price"]
#     keysvalues.append(c)
#     j = 0 
#     while j<len(keysvalues):
#         if highest<keysvalues[i]:
#             highest = keysvalues[j]
#         j+=1
#     i+=1
# lowest = min(keysvalues)
# print(highest, lowest)
# k = 0
# while k<len(keysvalues):
#     if keysvalues[k]>lowest and keysvalues[k]<highest:
#         lowest = keysvalues[k]
#     k+=1
# print(highest,lowest)
b = []
for i in a["product"]:
    b.append(i["price"])
sum = 0
for j in b:
    sum+=j
print(sum)
