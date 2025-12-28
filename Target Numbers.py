def target_num(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return f"Sum found {numbers[i]} + {numbers[j]} = {target}"
    return "No such pair of integers exist"
print(target_num([1,3,5,6,7],9))


