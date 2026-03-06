from flask import Flask
from auth.routes import auth_bp
from blog.routes import blog_bp

app = Flask(__name__)

app.register_blueprint(auth_bp,url_prefix="/auth")
app.register_blueprint(blog_bp,url_prefix="/blog")

if __name__ == '__main__':
	app.run(debug=True)

##
# /auth/login
# /blog/posts


# user Requests -->Flask App -->Blueprint Router --> .. View Function -->Response 
#
# /auth/login --->Flask --->auth blueprint --->login() -->return response 
#