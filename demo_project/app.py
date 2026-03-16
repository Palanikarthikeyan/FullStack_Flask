from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite database configuration

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db" # Sqlite3 

# mysql
# mysql+pymysql://user:password@localhost/dbname
# postgreqSQL
# postgresql://user:password@localhost/dbname
# --------------------------------------------------
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create SQLAlachemy  class instance
db = SQLAlchemy(app)

# Model(Table)
class myUser(db.Model): # inheritance - Model class is pre-defined from SqlAlchemy 
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(100)) 
	age =  db.Column(db.Integer)

# Create tables
#--------------------
with app.app_context():
	db.create_all()

# Route - add user
@app.route("/users",methods = ["POST"])
def f1_add_user():
	data = request.json
	
	user = myUser(name = data["name"],age = data['age'])
	db.session.add(user)
	db.session.commit()
	return jsonify({"message":"User added"})

# Route - Get all users
@app.route("/users",methods = ["GET"])
def f1_get_users():
	users = myUser.query.all()
	results = []
	for var in users:
		results.append({'id':var.id,'name':var.name,'age':var.age})

	return jsonify(results)

if __name__ == '__main__':
	app.run(debug=True)


	

'''
POST
C:\Users\karth>curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d "{\"name\":\"anu\",\"age\":20}"
{
  "message": "User added"
}
---
using requests:
>>> import requests
>>>
>>> requests.get('http://127.0.0.1:5000/users').json()
[{'age': 20, 'id': 1, 'name': 'anu'}]
>>>
>>>
>>> d = { "name":"kumar","age":15}
>>>
>>> response = requests.post("http://127.0.0.1:5000/users",json = d)
>>>
>>> response.json()
{'message': 'User added'}
>>>
>>> requests.get('http://127.0.0.1:5000/users').json()
[{'age': 20, 'id': 1, 'name': 'anu'}, {'age': 15, 'id': 2, 'name': 'kumar'}]
>>>
'''

	






