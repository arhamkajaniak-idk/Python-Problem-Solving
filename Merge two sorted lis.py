
def merge_list(list_1, list_2):
    list_3 = []
    for num in list_1:
        list_3.append(num)
    for num in list_2:
        list_3.append(num)

    n = len(list_3)
    for i in range(n):
        for j in range(0, n - i - 1):  
            if list_3[j] > list_3[j + 1]:
                list_3[j], list_3[j + 1] = list_3[j + 1], list_3[j]
    return list_3
    
x= eval(input("Enter your list: "))
y= eval(input("Enter your 2 list: "))
combined_list= merge_list(x,y)
print(combined_list)



