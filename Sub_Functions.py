import re
import random
import string
from string import ascii_uppercase


emailtest = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
   

def isValid(email):
    if re.fullmatch(emailtest, email):
      return True
    else:
      return False

def isValidpass(pwd):
    lowercount=0
    majuscount=0
    numbercounter=0
    symbolcounter=0
    if (len(pwd)>=8):
        for c in pwd :
            if (c.islower()):
                lowercount+=1
            if (c.isupper()):
                majuscount+=1
            if (c.isdigit()):
                numbercounter+=1        
            if re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\]', pwd):
                symbolcounter+=1 
    else :
        print("entrer un password de longuer 8 au minimum") 
        return 0           
    if(lowercount==0):
        print("utiliser au minimum un caractere miniscule")
    if(majuscount==0):
        print("utiliser au minimum un caractere majuscule")
    if(numbercounter==0):
        print("utiliser au minimum un chiffre")
    if(symbolcounter==0):
        print("utiliser au minimum un symbol")            
    if (lowercount != 0 and majuscount != 0 and numbercounter != 0 and symbolcounter!= 0):
       return 1
    return 0                        

def genererpass():
    while True :
        test='1'
        pwd=""
        x=random.randint(8,10)
        for i in range(x) :
            p=random.randint(1,4)
            if(p==1):
                pwd+=random.choice(string.ascii_lowercase)
            elif(p==2):
                pwd+=random.choice(string.ascii_uppercase)
            elif(p==3):
                pwd+=random.choice(string.digits)
            elif(p==4):
                pwd+=random.choice(string.punctuation)
        lowercount=0
        majuscount=0
        numbercounter=0
        symbolcounter=0
        for c in pwd :
            if (c.islower()):
                lowercount+=1
            if (c.isupper()):
                majuscount+=1
            if (c.isdigit()):
                numbercounter+=1        
            if (not c.isalnum()):
                symbolcounter+=1                      
        if (lowercount != 0 and majuscount != 0 and numbercounter != 0 and symbolcounter!= 0):
            test ='0'
        if (test =='0'):
            return(pwd)
        






    



