def my_List(X):
    total = 0
    for row in X:                 
        num_1 = row[len(row) - 2]
        num_2 = row[len(row) - 1]
        total += num_1 + num_2
    print(total)

my_List([[1,2,3,4,5,6],
         [7,8,9,10,11,12],
         [13,14,15,16,17,18]])
