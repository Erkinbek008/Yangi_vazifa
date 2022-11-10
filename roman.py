def roman(x):
    numbers = [1,4,5,9, 10,40,50,90, 100,400,500,900,1000]
    roman_num =['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    i = 12
    roman_numeral = ''
    while x != 0:
        if numbers[i] <= x:
            roman_numeral += roman_num[i] 
            x = x - numbers[i]
        else:
            i = i-1
    return roman_numeral
print(roman(192))
# def solition(roman):
#     rim_and_num = {"I":1 , "V":5 , "X":10 , "L":50}
#     num = 0
#     for i in range(len(roman)):
#         if i + 1 != len(roman) and rim_and_num[roman[i]] < rim_and_num[roman[i+1]]:
#             num = num - rim_and_num[roman[i]]
#         else:
#             num = num + rim_and_num[roman[i]]
#     return num
# print(solition("XIV"))