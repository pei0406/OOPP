from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField,validators

app = Flask(__name__)

class RegisterUser(Form):
    SpId = StringField('SingPass ID', [validators.Length(min=9, max=9), validators.DataRequired()])
    SpPass = StringField('SingPass Password', [validators.Length(min=1, max=150), validators.DataRequired()])


@app.route('/')
def root():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

@app.route('/fundTransfer')
def fundtransfer():
    return render_template('fundtransfer.html')

@app.route('/giro')
def giro():
    return render_template('giro.html')

@app.route('/spendinganalytics')
def spendinganalytics():
    return render_template('spendinganalytics.html')

@app.route("/transaction")
def transaction():
    return render_template("transaction.html")

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.run()
