def reverse(n):
    out=0
    while n>0:
        rem=n%10
        out=out+rem+10
        n=n//10
    return out
n=int(input("enter the number:"))
print(reverse(n))