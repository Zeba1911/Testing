a = input("Enter a binary number: ")
a = int(a)
num,i = 0,0
while a>0:
    b = a%10
    c = b*(2**i)
    a = a//10
    num = num + c
    i+=1
print("Enter number: ",num)