import sqlite3
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

@obj.route("/myproducts",methods = ['POST','GET'])
def f5():
    if request.method == 'POST':
        try:
            pid = request.form['pid']
            pname = request.form['pname']
            pcost = request.form['pcost']
            
            with sqlite3.connect("test1.db") as conn:
                cur = conn.cursor()
                cur.execute("insert into product(pid,pname,pcost) values(?,?,?)",(pid,pname,pcost))
            conn.commit()
            result = "Record Successfully submitted"
        except:
            conn.rollback()
            result = "Sorry Insert operation is failed"
        finally:
            conn.close()
            return f"<h2>{result}</h2>"
        
@obj.route("/list")
def f6():
    conn = sqlite3.connect("test1.db")
    conn.row_factory = sqlite3.Row
    sth = conn.cursor()
    sth.execute("select *from product")
    records = sth.fetchall()
    return render_template("list.html",t_records = records)

@obj.route("/data")
def f7():
    conn = sqlite3.connect("test1.db")
    sth = conn.cursor()
    sth.execute("select *from product")
    records = sth.fetchall()
    return jsonify({'products':records})

if __name__ == '__main__':
    obj.run(debug = True,port=1234)