# a = {1:2,3:5,5:7}
# def number(num):
#     if num in a:
#         return "yes"
#     else:
#         return "no"
# print(number(8))

# from datetime import date

# today = date.today()
# print("Today's date:", today)
from datetime import date

today = date.today()
print(today)

# dd/mm/YY
# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)

# # Textual month, day and year	
# d2 = today.strftime("%B %d, %Y")
# print("d2 =", d2)

# # mm/dd/y
# d3 = today.strftime("%m/%d/%y")
# print("d3 =", d3)

# # Month abbreviation, day and year	
# d4 = today.strftime("%b-%d-%Y")
# print("d4 =", d4)