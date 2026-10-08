# List is mutable
# List can store various data types(int,float,string etc.)
list_1 = [10,20,30,40,50,60,70,80,90,100]
mul = 1
for x in range(len(list_1)): # range(0,11) # 1
    mul = mul*list_1[x]
print(mul)
    