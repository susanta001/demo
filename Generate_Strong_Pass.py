import random
import string
#input how many digit of password you want
n = int(input("Enter how many digit password you want? "))

#write a funtion to generate strong password
def strong_password(length=12):
    #Take one char from each different string
    password_list = [
    random.choice(string.ascii_lowercase),
    random.choice(string.ascii_uppercase),
    random.choice(string.punctuation)
  ]
    #concatinate different types of char
    special_char = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    #extend the password_list with special_char
    password_list.extend(random.choice(special_char) for _ in range(length - 3))
    #convert list to string using 'join' function
    password = ''.join(password_list)
    return password
#call the 'strong_password' function
print_pass = strong_password(n)
print(print_pass)

