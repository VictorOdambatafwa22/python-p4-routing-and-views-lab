#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:username>')
def print_string(username):
    print(username)
    return f'{username}'

@app.route('/count/<int:num>')
def count(num):
    numbers=''
    for i in range(num):
        numbers+= str(i)+'\n'
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation,num2):
    if operation =='+':
        result=num1+num2

    elif operation =='-':
        result=num1-num2

    elif operation =='*':
        result=num1*num2

    elif operation =='div':
        result=num1/num2    

    else:
        result=num1%num2   

    return str(result)    

if __name__ == '__main__':
    app.run(port=5555)
