def fibonacci_ratio():
    n = int(input("Enter n (>= 3): "))

    if n < 3:
        return "Golden ratio not possible for n < 3"

    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    ratio = b / a   
    return ratio

print(fibonacci_ratio())


# As n becomes large, the ouput is aprroximately 1.618...


       
