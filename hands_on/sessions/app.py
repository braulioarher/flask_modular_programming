from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'

# use the route '/login/' to login user
@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('user'))
    return render_template('login.html')

# use the route '/user/' to get the username in the session
@app.route('/user/')
def user():
    return render_template('user.html')
# use the route '/logout/' to logout user
@app.route('/logout/')
def logout():
  session.pop('username', None)
  return ("You've been logged out successfully!")