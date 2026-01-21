from flask import Flask,redirect,url_for,render_template,jsonify

obj = Flask(__name__)

@obj.route("/")
def f1():
    return render_template("index.html")

@obj.route("/aboutus")
def f2():
    return render_template("index.html")

@obj.route("/mypage")
def f3():
    return "<h2> Mypage content</h2>"

@obj.route("/myview")
def f4():
    return "<h3> My view page </h3>"

@obj.route("/mycourse/<course_name>")
def f5(course_name):
    return f"<h3> My course name is: {course_name}</h3>"

@obj.route("/myinput/<int:code>")
def f6(code):
    if(code >500):
        return redirect(url_for('f3'))
    else:
        return redirect(url_for('f5',course_name = "Ruby"))
@obj.route("/data")
def f7():
    d = {'interface':['eth0','eth1','eth2'],'port':[1234,5000]}
    return jsonify(d)
    
if __name__ == '__main__':
    obj.run(debug = True,port=1234)