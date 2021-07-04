def myfunction():
    b = input("enter key of dictionary")
    dict1={"name":"raju", "marks":56}
    for i , j in dict1.items():
        if b in dict1:
            return "exits"
        else:
            return "not exits"
print(myfunction())