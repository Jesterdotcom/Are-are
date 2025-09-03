def capitalizer() :
    sent = input("Enter the sentence you want to capitalize :")
    ch = ""
    c3 = ""
    var = "n"
    for char in sent : 
        if char == ".":
            var = "n"
        elif var == "n":
            b = char.capitalize()
            char = b
            var = "m"
        ch += char
    for c2 in ch :
        c3 += c2   
    print(c3)    
capitalizer()
