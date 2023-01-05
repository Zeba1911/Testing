number=0
binary=0
a=1
print("Enter any number :")
n = int(input())
while n>0:
    number=n%2
    binary=binary+number*a
    a=a*10
    n=int(n/2)
print("binary number of ",n,"=",binary)