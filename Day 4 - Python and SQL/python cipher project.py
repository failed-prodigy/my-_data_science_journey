def game_logic():
    game = input("Do you want to continue ? : Yes (Y/y) or No (N/n) ")
    if game == "Y" or game == "y":
        looped_value = True
        return looped_value
    elif game == "N" or game == "n":
        print("GGwp... Bye bye!")
        exit()
    else:
        print("typed wrong options. Bye bye!")
        exit()



def encode(statement,number_shift):
    a=[]
    l = len(statement)
    encoded_message = ""
    for i in range (0,l):
        a.append(statement[i])
        if a[i] != ' ':
            a[i]= chr(ord(a[i])+number_shift)
        else :
            continue
    for k in a:
        encoded_message = encoded_message+k
    return print(f" Your encoded message is : \n  {encoded_message}")

def decode(statement,number_shift):
    a=[]
    l = len(statement)
    decoded_message = ""
    for i in range (0,l):
        a.append(statement[i])
        if a[i] != ' ':
            a[i]= chr(ord(a[i])-number_shift)
        else :
            continue
    for k in a:
        decoded_message = decoded_message+k
    return print(f" Your decoded message is : \n  {decoded_message}")


print("""                                                    
           88             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                                    
                                                                
                                          88          88  
                                          88          88  
8b      db      d8  ,adPPYba,  8b,dPPYba, 88  ,adPPYb,88  
`8b    d88b    d8' a8"     "8a 88P'   "Y8 88 a8"    `Y88  
 `8b  d8'`8b  d8'  8b       d8 88         88 8b       88  
  `8bd8'  `8bd8'   "8a,   ,a8" 88         88 "8a,   ,d88  
    YP      YP      `"YbbdP"'  88         88  `"8bbdP"Y8  """)

print("Welcome to the cipher world \n"
      "what do you want me to do ? DECODE or Encode? ")
looped_value = True
while looped_value is True :
    request = input("Your choice : ")
    if request == "decode" or request == "DECODE":
        statement = input("The statement that needs to be decoded: ")
        number_shift = int(input("number shift :"))
        decode(statement, number_shift)
        game_logic()
    elif request == "encode" or request ==  "ENCODE":
        statement = input("The statement that needs to be encoded: ")
        number_shift = int(input("number shift :"))
        encode(statement,number_shift)
        game_logic()
    else:
        print("Please choose from the given options only. \n Please type using either all lower case or all upper case")
        game_logic()



#     statement = input("The statement that needs to be decoded: ")
#     number_shift = int(input(" The shift number is :"))
#
#     for i in (0,len(statement)):
#     #     statement[i] = str(chr(ord(statement[i]) - number_shift))
#
#         print(chr(ord(statement[i]) - number_shift))
# elif request == "encode" or "ENCODE" :
#     statement = input("The statement that needs to be decoded: ")
#     number_shift = int(input(" The shift number is :"))
#     encoded_statement = ""
#     for i in (0,len(statement)):
#         ord(encoded_statement[i]) = ord(statement[i]) + number_shift
#
#     print("Encoded statement is : "encoded_statement)