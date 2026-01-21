from flask import Flask,redirect,url_for,render_template,jsonify,request

obj = Flask(__name__)

@obj.route("/")
def f1():
    return render_template("index.html")

@obj.route("/mypage/<course_name>")
def f2(course_name):
    return f"<h2>Selected Course name is:{course_name}</h2>"

@obj.route("/mycourse")
def f3():
    return render_template("display.html",T_course_name="ansible")

@obj.route("/myresult/<int:score>")
def f4(score):
    return render_template("view.html",t_score = score)

@obj.route("/myservers",methods = ['POST','GET'])
def f5():
    if(request.method == 'POST'):
        login_name = request.form['n1']
        if(login_name == 'root'):
            d={'S1':'RHL5','S2':'OL5','S3':'DEB14'}
            return render_template("report.html",T_servers=d)
        else:
            return "<h2> Sorry your not root user</h2>"


if __name__ == '__main__':
    obj.run(debug = True,port=1234)