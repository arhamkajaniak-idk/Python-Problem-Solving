def is_perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return True
    else:
        return False
    
def find_perfect_in_range(start, end):
    list_num=[]
    for i in range(start, end+1):
        if is_perfect(i):
            list_num.append(i)
    return list_num

def main():
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))
    perfects = find_perfect_in_range(start, end)
    print(f"Perfect numbers between {start} and {end}: {perfects}")

if __name__ == "__main__":
    main()


        
    


