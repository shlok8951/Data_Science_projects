def decimal_to_binary(n):
    if n==0 :
        return "0"

    result = ""
    while n>0 :
       rem = n%2
       result = str(rem)+result
       n = int(n/2)

    return result    

def decimal_to_octal(n):
    if n==0 :
     return "0"
     
    result = ""
    while n>0 :
       rem = n%8
       result = str(rem)+result
       n = int(n/8)

    return result  

#decimal_to_octal(28)    

def decimal_to_hexadecimal(n):
    if n==0 :
        return "0"
    result = ""
    while n>0 :
       rem = n%16
       if(rem>9):
           p = rem-9
           rem = chr(64+p)
       result = str(rem)+result
       n = int(n/16)

    return result   

# decimal_to_hexadecimal(27)   

def binary_to_decimal(n):
    result = 0
    c = len(n)
    for i in n:
        c = c-1
        if(int(i)==0):
            continue
        p = int(i)*(2**c)
        result = result+p

    return result    

# binary_to_decimal("1000") 
   
def octal_to_decimal(n):
    result = 0
    c = len(n)
    for i in n:
        c = c-1
        p = int(i)*(8**c)
        result = result+p

    return result

# octal_to_decimal("31")   

def hexadecimal_to_decimal(n):
    result = 0
    c = len(n)
    for i in n:
        c = c-1
        if(ord(i)>64):
            x = ord(i)-64
            p = (9+x)*(16**c)
        else:    
         p = int(i)*(16**c)
        result = result+p

    return result   

# hexadecimal_to_decimal("1A")

def  binary_to_octal(n):
    result = ""
    chunks = [n[max(0,i-3):i] for i in range(len(n),0,-3)][::-1]
    for i in chunks:
      p =  binary_to_decimal(i)
      result = result + str(p)

    return result

# binory_to_octal("1011")

def binary_to_hexadecimal(n):
    result = ""
    chunks = [n[max(0,i-4):i] for i in range(len(n),0,-4)][::-1]
    for i in chunks:
      p =  binary_to_decimal(i)
      if(p>9):
          p = chr(64+(p-9))
      result = result + str(p)

    return result

# binary_to_hexadecimal("11001111")


def octal_to_binary(n):
    result = ""
    for i in n:
        p = decimal_to_binary(int(i))
        if(len(p)<3):
            x= 3-len(p)
            p = ("0"*x)+p
        result = result + p

    return result   

# octal_to_binary("21")
#010001

def hexadecimal_to_binary(n):
    result = ""
    for i in n:
        if(ord(i)>64):
            i = 9+(ord(i)-64)
            
        p = decimal_to_binary(int(i))
        if(len(p)!=4):
            x = 4-len(p)
            p = ("0"*x)+p
        result = result + p

    return result

# hexadecimal_to_binary("3A")    
#00111010

def octal_to_hexadecimal(n):
    x = octal_to_binary(n)
    result = binary_to_hexadecimal(x)

    return result
    
#x =  octal_to_hexadecimal("21")
#print(x)
#010001-> 11

def hexadecimal_to_octal(n):
    x = hexadecimal_to_binary(n)
    result = binary_to_octal(x)

    return result

# hexadecimal_to_octal("3A")    
#00111010 -> 71
print("               Base Converter                   ")
mylist = '''1.Binary to decimal
2.Binary to Octal
3.Binary to Hexadecimal
4.Decimal to Binary
5.Decimal to Octal
6.Decimal to Hexadecimal
7.Octal to Binary
8.Octal to Decimal
9.Octal to Hexadecimal
10.Hexadecimal to binary
11.Hexadecimal to Octal
12.Hexadecimal to Decimal'''
print(mylist)

i = int(input("Enter your choice : "))
while i!=0 :
     n = input("Enter the data : ")
     match i :
         case 1 : x = binary_to_decimal(n)
         case 2 : x = binary_to_octal(n)   
         case 3 : x = binary_to_hexadecimal(n)  
         case 4 : x = decimal_to_binary(abs(int(n)))
         case 5 : x = decimal_to_octal(abs(int(n)))
         case 6 : x = decimal_to_hexadecimal(abs(int(n)))  
         case 7 : x = octal_to_binary(n)
         case 8 : x = octal_to_decimal(n)
         case 9 : x = octal_to_hexadecimal(n)
         case 10 : x = hexadecimal_to_binary(n)
         case 11 : x = hexadecimal_to_octal(n)
         case 12 : x = hexadecimal_to_decimal(n)
         case _ : 
             print("Wrong choice ...")
             i = int(input("Enter your choice : "))  
             continue
             

     print(x)
     print("For exit enter 0")
     i = int(input("Enter your choice : "))    

print("Thanku for visiting ......")     
