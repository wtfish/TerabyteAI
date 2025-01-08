from flask import Flask
app=Flask(__name__)
from markupsafe import escape
from flask import render_template
from flask import Flask, flash, redirect, render_template, \
     request, url_for

@app.after_request
def minimize_headers(response):
    headers_to_remove = ['X-Powered-By', 'X-Runtime', 'X-Version']
    for header in headers_to_remove:
        response.headers.pop(header, None)
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/test')
def run_test():
    return render_template("baseTest.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)