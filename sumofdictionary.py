my_dict = {
        'data1':100,
        'data2': -54,
        'data3': 247
       } 
sum = 0
value =  list(my_dict.values())
for i in range (len(value)):
    sum+=value[i]
print(sum)
