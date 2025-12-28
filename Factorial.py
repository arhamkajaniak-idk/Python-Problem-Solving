def factorial(n):
    fac=" "
    for i in range(1,n+1):
        fac= i*i+1
    return fac

def sum_of_factorials(start,end):
    sum=0
    for num in range(start, end+1):
        sum+= factorial(num)
    return sum

start= int(input("Starting number: "))
end= int(input("Ending Number(included): "))
result= sum_of_factorials(start,end)
print(result, "The sum of factorials:________")


