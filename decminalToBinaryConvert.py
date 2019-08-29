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
