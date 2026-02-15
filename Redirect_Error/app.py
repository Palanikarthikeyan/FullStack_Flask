from flask import Flask, redirect, url_for, render_template, request, abort

app = Flask(__name__)

# Fake login flag (for demo)
is_logged_in = False


@app.route("/")
def home():
    return "<h2>Home Page</h2><a href='/dashboard'>Go to Dashboard</a>"


@app.route("/login", methods=["GET", "POST"])
def login():
    global is_logged_in

    if request.method == "POST":
        is_logged_in = True
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if not is_logged_in:
        return redirect(url_for("login"))
    return render_template("dashboard.html")


@app.route("/admin")
def admin():
    abort(403)   # Forbidden access


@app.route("/crash")
def crash():
    1 / 0        # Force 500 error


# -------------------
# Error Handlers
# -------------------

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(403)
def forbidden(error):
    return render_template("403.html"), 403


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)

