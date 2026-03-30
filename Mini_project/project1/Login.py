from flask import Flask, request, redirect, url_for, Response, session

# app = Flask(__name__)
# app.secret_key = "supersecretkey"

# @app.route('/', methods = ['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")

#         if username == "Ankush" and password == "1234":
#             session["user"] = username 
#             return redirect(url_for("welcome"))
#         else:
#             return Response("In-valid credentials. Try again", mimetype="text/plain")
        
#     return '''
#             <h2>Login Page</h2>
#             <form method="POST">
#             username: <input type="text" name="username"><br>
#             password: <input type="text" name="password"><br>
#             <input type="submit" value="Login">
#             </form>
# '''
# @app.route("/welcome")
# def welcome():
#     if "user" in session:
#         return f'''
#         <h2>Wlcome, {session["user"]}!</h2>
#         <a href="{url_for("logout")}">Logout</a>
#     '''
#     return redirect(url_for('login'))

# @app.route("/logout")
# def logout():
#     session.pop("user", None)
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)


