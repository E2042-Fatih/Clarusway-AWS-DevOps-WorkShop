

from flask import Flask, render_template, request , redirect, url_for

app = Flask (__name__)

@app.route("/")
def home ():
    return render_template ("index.html", not_valid = False, developer_name = "E2042-Fatih")


@app.route ("/", methods = ["GET","POST"])
def calc ():
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

    app.run(debug = True)
    #app.run(host = '0.0.0.0', port = 80)