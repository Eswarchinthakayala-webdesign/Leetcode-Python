def intToRoman(num):
    romans={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
    roman=''
    for key in sorted(romans.keys(),reverse=True):
        while num>=key:
            roman+=romans[key]
            num-=key
    return roman



num=58
print(intToRoman(num))