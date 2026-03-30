# from flask import Flask, request, render_template

# app = Flask(__name__)


# @app.route('/')
# def login():
#     return render_template("login.html")

# @app.route("/submit", methods = ['POST'])
# def submit():
#     username = request.form.get("username")
#     password = request.form.get("password")

#     if username == "Admin" and password == "1234":
#         return render_template("welcome.html", name = username)
#     else:
#         return "In-valid credentials. Try again"