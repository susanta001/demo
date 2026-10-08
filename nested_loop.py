#WAP to print greater between three number.
num_1 = int(input("Enter Number: "))
num_2 = int(input("Enter Number: "))
num_3 = int(input("Enter Number: "))
if num_1>num_2: # True
    if num_1>num_3: #TRue
        print(f'{num_1} is greater.')
    else: #False
        print(f'{num_3} is greater.')
else:
    if num_2>num_3:
        print(f'{num_2} is greater.')
    else:
        print(f'{num_3} is greater.')