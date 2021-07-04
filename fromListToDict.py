list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
dic1 = {}
for i in range (len(list1)):
    dic1[list1[i]]=list2[i]
print(dic1)