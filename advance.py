# enumerate is function That used object can then be directly in loops
# to access both the item and its corresponding index (or count). 

# mylist = [1,3,5,6,8,9,10,12]

# for i, item in enumerate(mylist):
#     if i == 2 or i== 4 or i== 6:
#         print(item)

# (normal method)        
# squaredlist = []
# for item in mylist:
#     squaredlist.append(item*item) 

# (using list comprehension)
# squaredlist = [i*i for i in mylist]  
    
# print(squaredlist) 

n = int(input("enter a number:"))

table = [n*i for i in range (1,11)]
print(table)      