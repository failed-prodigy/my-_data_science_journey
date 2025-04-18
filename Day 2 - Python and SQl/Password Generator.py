import random

letter = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^',
    '_', '`', '{', '|', '}', '~'
]

print("Welcome to the Password Generator - Ve Keep...")

letter_values = int(input(" How many letters do you like in you password ? "))
symbol_values = int(input(" How many symbols do you like in you password ? "))
number_values = int(input(" How many numbers do you like in you password ? "))


password_bowl = []
i = 0
j = 0
k = 0
while i < letter_values :
    a = random.randint(0, len(letter)-1)
    if letter[a] not in password_bowl:
        password_bowl.append(letter[a])
        i +=1
while j < number_values :
    b = random.randint(0, len(number)-1)
    if number[b] not in password_bowl :
        password_bowl.append(number[b])
        j +=1

while k < symbol_values :
    c = random.randint(0, len(symbol)-1)
    if symbol[c] not in password_bowl:
        password_bowl.append(symbol[c])
        k +=1


print ( password_bowl )
password = ""
random.shuffle(password_bowl)
for i in password_bowl:
    password += i

print(f"your password is : {password} ")