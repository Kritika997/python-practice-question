# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic4 = dic1.copy()
# for i , j in dic2.items():
#     dic4[i]=j
# for k , l in dic3.items():
#     dic4[k]=l
# print(dic4)

num=input("Enter the number of length:")
num.split()
x=list(num)
i=0
count=0
while i<len(x)-1:
    if x[i] == x[i+1]:
        count+=1
    i+=1
print(count)
