#Binary Test

#Run and type "main(your decimal value here)" and hit enter
#doesnt work with fractions yet.
def main(decimal):
    r = 0
    n = decimal
    result = ""
    remainder = 0
    while((2**r) <= n):
        r = r+ 1
        #print(r)
    print("amount of bits is " + str(r))
    while(n != 0):
        remainder = int(n % 2)
        #print(remainder)
        n = int(n / 2)
        #print(n)
        result = str(remainder)+ result
    print("Binary:")
    print(result)
                            
def main2(decimal):
    r = 0
    n = decimal
    result = ""
    remainder = 0
    while((8**r) <= n):
        r = r+ 1
        #print(r)
    print("amount of bits is " + str(r))
    while(n != 0):
        remainder = int(n % 8)
        #print(remainder)
        n = int(n / 8)
        #print(n)
        result = str(remainder)+ result
    print("Octal:")
    print(result)



#thisll be for numbers like 37.45
def main3(number):
    r = 0
    t = 0
    n = number
    result = ""
    remainder = 0
    n = int(n / 1)
    z = number % 1 
    #print("Z: " + str(z)[:10])
    #print(len(str(z)[:10]))
    z = z*(10 ** len(str(z)[:10]))
    z = int(z)
    #print("Z final: " + str(z))
    #print(n)
    while((2**r) <= n):
        r = r+ 1
        #print(r)
    print("Amount of none fraction bits is: " + str(r))
    while(n != 0):
        remainder = int(n % 2)
        #print(remainder)
        n = int(n / 2)
        #print(n)
        result = str(remainder)+ result
    #Now for second half--------------------------------
    while((2**t) <= z):
        t = t+ 1
        #print(t)
    print("Amount of fraction bits is: " + str(t))
    while(z != 0):
        remainder = int(z % 2)
        #print(remainder)
        z = int(z / 2)
        #print(z)
        result = result + str(remainder)
    print("Amount of total bits is: " + str(r+t))
    print("Binary:")
    print(result)
    
