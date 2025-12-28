def prime_no(num):
    if num <= 1:
        return "Not a prime no."  
    for i in range(2, num):
        if num % i == 0:
            return "Not a prime no."
    return "Prime no."


def main():
    n=int(input("Enter a number n"))
    for n in range(1,n):
        x=prime_no(n)
    return x
main()
 

    

