def myMode(X):
    modes = []
    max_count = 0
    
    unique_numbers = set(X)  
    
    for num in unique_numbers:  
        count = 0
        for n in X:  
            if n == num:
                count += 1
        
        if count > max_count:
            max_count = count
            modes = [num]  
        elif count == max_count:
            modes.append(num)
    
    return modes

def main():
    X = [2,5,7,7,7,9,9,9,10,1,12]
    result = myMode(X)
    print("The mode value(s):", result)

main()
