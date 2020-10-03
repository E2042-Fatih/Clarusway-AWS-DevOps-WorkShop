

from flask import Flask, render_template, request 



app = Flask (__name__)



@app.route("/")
def home ():
    return render_template ("index.html", not_valid = False, developer_name = "E2042-Fatih")




@app.route ("/", methods = ["POST"])
def calc ():
    if request.method == "POST":
        own_number = request.form["number"]

        
        if own_number.isdigit() == False or  not 0<int(own_number):
            return render_template("index.html" , not_valid = True , developer_name = "E2042-Fatih")


            
        else:
            def convert(num):
                word = ""
                a = num // 3600000
                if a != 0:
                    word = str(a) + " hour/s  "
                num %= 3600000
                b = num // 60000
                if b!=0:
                    word += str(b) + " minute/s  "
                num %= 60000
                c = num // 1000
                if c != 0:
                    word += str(c) + " second/s"
                if word == "":
                    word = "just " + str(num) + " milisecond/s"
                    return word
                else:
                    return word

            
    return render_template("result.html", milliseconds = own_number , result = convert(int(own_number)) , developer_name = "Albert")



if __name__ == "__main__":

#    app.run(debug = True)
    app.run(host = '0.0.0.0', port = 80)