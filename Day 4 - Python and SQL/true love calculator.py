def calculate_love_score(name1,name2):
    a=[]
    c=['T','R','U','E','t','r','u','e']
    d=['L','O','V','E','l','o','v','e']
    true_counter = 0
    love_counter = 0
    love_score = 0
    for i in range (0,len(name1)):
        a.append(name1[i])
    for j in range (0,len(name2)):
        a.append(name2[j])
    for k in range (0,len (a)) :
        if a[k] in c :
            true_counter +=1
        if a[k] in d :
            love_counter +=1
    love_score=str(true_counter)+str(love_counter)
    return print(love_score)

name1=input("Enter the first person name : ")
name2=input("Enter the second person name : ")
calculate_love_score(name1,name2)