Alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def codage_cesar(a,message):
   #Fonction qui code en César à partir d'une clé
    code=""                                 
    for caractere in message:             
        if caractere in Alphabet:         
            x = Alphabet.index(caractere) 
            y = (a+x)%26                 
            code += Alphabet[y]           
        else:                            
            code += " "                   
    return code                       

                                          
print(codage_cesar(1,"CIEL"))

def decodage_cesar(a,message):
   
    code=""                                 
    for caractere in message:             
        if caractere in Alphabet:         
            x = Alphabet.index(caractere) 
            y = (x-a)%26                 
            code += Alphabet[y]           
        else:                            
            code += " "                   
    return code                       

                                          
print(decodage_cesar(1,"DJFM"))