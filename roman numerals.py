
numeral_dict={"I":1,"V":5, "X":10,"L":50, "C":100, "D":500, "M":1000}
def conversion_Type1():
    global numeral_dict
    roman_num= input('Enter the roman number: ')
    integer_num =0
    for i in range(len(roman_num)):
        if i < len(roman_num) - 1 and numeral_dict[roman_num[i]] < numeral_dict[roman_num[i+1]]:
            integer_num -= numeral_dict[roman_num[i]]  
        else:
            integer_num += numeral_dict[roman_num[i]]
    print(integer_num)
            
conversion_Type1()    



