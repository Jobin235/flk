from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.htm")

@app.route('/registration')
def registration():
    return render_template("registration.htm")

@app.route('/course')
def course():
    return render_template("course.htm")

@app.route('/login')
def login():
    return render_template("login.htm")

@app.route('/feedback')
def feedback():
    return render_template("feedback.htm")
if __name__ =='__main__':
    app.run()