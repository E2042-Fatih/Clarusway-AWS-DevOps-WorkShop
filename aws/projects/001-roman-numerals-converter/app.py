
from flask import Flask, render_template, request , redirect, url_for

app = Flask (__name__)

@app.route("/", methods = ['GET'])
def main_get ():
    return render_template ("index.html", not_valid = False, developer_name = "E2042-Fatih")


@app.route ("/", methods = ["POST"])
def main_post ():
    if request.method == "POST":
        number = request.form["number"]
        if number.isdigit() == False or not 0<int(number)<4000:
            return render_template("index.html" , not_valid = True , developer_name = "E2042-Fatih")
        else:
            L100 = {"0":"","1":"C", "2":"CC", "3":"CCC", "4":"CD", "5":"D", "6":"DC", "7":"DCC", "8":"DCCC", "9":"CM"}
            L10 = {"0":"","1":"X", "2":"XX", "3":"XXX", "4":"XL", "5":"L", "6":"LX", "7":"LXX", "8":"LXXX", "9":"XC"}
            L1 = {"0":"","1":"I", "2":"II", "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX"}
            
            def conv(num):
                if len(num)==4:
                    roman = int(num[0])*"M" + L100[num[1]] + L10[num[2]] + L1[num[3]]
                    
                elif len(number)==3:
                    roman = L100[num[0]] + L10[num[1]] + L1[num[2]]
                    
                elif len(number)==2:
                    roman = L10[num[0]] + L1[num[1]]
                    
                else :
                    roman = L1[num[0]]
                return roman

            
        return render_template("result.html", number_decimal=number , number_roman = conv(number) , developer_name = "E2042-Fatih")

if __name__ == "__main__":
#    app.run(debug = True)
    app.run(host = '0.0.0.0', port = 80)


# farklı çözüm yöntemi-1
# def convert(decimal_num):
#    roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
#    num_to_roman = ''
#    for i in roman.keys():
#        num_to_roman += roman[i]*(decimal_num//i)
#        decimal_num %= i
#    return num_to_roman

# farklı çözü yöntemi-2
#def convert_to_roman(num):
#    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
#	sayi = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#    romanvalue = ""
#    for i,d in enumerate(sayi):
#        while (num >= d):
#            num -= d
#            romanvalue += roman[i]
#    return romanvalue
#print(convert_to_roman(3100))

# farklı çözü yöntemi-3
#def convert(num):
#    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#    number_roman = ''
#    i = 0
#    while  num > 0:
#        for _ in range(num // val[i]):
#            number_roman += syb[i]
#            num -= val[i]
#        i += 1
#    return (number_roman)

# farklı çözü yöntemi-4
#def InttoRoman(number):
#    romandict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V': 5, 'IV':4, 'I':1}
#    if (not number.isdigit()) or ((int(number) > 3999) or (int(number) < 1)):
#        return 0
#    number = int(number)    
#    result = ""
#    for key, value in romandict.items():
#        while number >= value:
#            quotient = number // value 
#            result += key * quotient
#            number %= value
#    return result