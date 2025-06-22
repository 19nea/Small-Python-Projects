import random  # for taking random letters/numbers/special characters
import string  # for having all types of characters


# characters define pool
letters = list(string.ascii_letters)  # a-z, A-Z
numbers = list(string.digits)  # 0-9
special = list(string.punctuation)  # special characters

# Combination of characters under one pool
letnr = letters + numbers
allchar = letters + numbers + special
spelet = letters + special


pwd = ''  # password output

# how long the password should be
paslen = int(input('How many letters do you want to have in the password? '))

nrpwd = range(paslen)

# if numbers should be included
numbers = input('Do you want the password to contain numbers? Y/N ').lower()

if numbers == 'n':
    pwd = ''.join(random.choice(letters) for _ in range(paslen))
elif numbers == 'y':
    pwd = ''.join(random.choice(letnr)
                  for _ in range(paslen))
else:
    print('yes or no?')


# if special characters should be included
specialchar = input(
    'do You want the password to contain special characters? Y/N ').lower()

# if there should be no special characters
if specialchar == 'n':
    print(pwd)
    # if there should be special characters and numbers
elif specialchar == 'y' and numbers == 'y':
    pwd = ''.join(random.choice(allchar)
                  for _ in range(paslen))
    # if there should be special characters but no numbers
elif specialchar == 'y' and numbers == 'n':
    pwd = ''.join(random.choice(spelet)
                  for _ in range(paslen))


# printing out the final password
print(pwd)
