
bin_1 = input("Enter the first binary number: ")
bin_2 = input("Enter the second binary number: ")
counter = 0
for num in range(len(bin_1)):
    char = bin_1[-1 - num]
    counter += int(char) * (2 ** num)
print("Decimal of first:", counter)
counter_2 = 0
for num_2 in range(len(bin_2)):
    char_2 = bin_2[-1 - num_2]
    counter_2 += int(char_2) * (2 ** num_2)
print("Decimal of second:", counter_2)
sum_of_dec = counter + counter_2
print("Sum in decimal:", sum_of_dec)
x = []
while sum_of_dec > 0:
    remainders = sum_of_dec % 2
    x.append(remainders)
    sum_of_dec //= 2
x.reverse()

print("".join(map(str,x)))



