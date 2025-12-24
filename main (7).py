def reverse(n):
    out=0
    store=n
    while n>0:
        rem=n%10
        out=out+rem+10
        n=n//10
    if store==out:
        return "palindromic number"
    else:
        return "not a palindromic number"
n=int(input("enter the number:"))
print(reverse(n))