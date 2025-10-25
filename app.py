from flask import Flask, render_template, request
import math
import re

app = Flask(__name__)

# ---------- MAIN PAGES ----------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/internships')
def internships():
    return render_template('internships.html')

@app.route('/works')
def works():
    return render_template('works.html')

# ---------- TOOL PAGES ----------
@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    uppercase_result = None
    if request.method == 'POST':
        text = request.form['inputString']
        uppercase_result = text.upper()
    return render_template('touppercase.html', uppercase_result=uppercase_result)

@app.route('/areaOfCircle', methods=['GET', 'POST'])
def areaOfCircle():
    circle_area = None
    if request.method == 'POST':
        radius = float(request.form['radius'])
        circle_area = math.pi * (radius ** 2)
    return render_template('areaOfCircle.html', circle_area=circle_area)

@app.route('/areaOfRectangle', methods=['GET', 'POST'])
def areaOfRectangle():
    rectangle_area = None
    if request.method == 'POST':
        length = float(request.form['length'])
        width = float(request.form['width'])
        rectangle_area = length * width
    return render_template('areaOfRectangle.html', rectangle_area=rectangle_area)

def precedence (op):
    if op == '+' or op == '-':
        return 1 
    if op == '*' or op == '/':
        return 2 
    if op == '^':
        return 3 
    return 0

def infix_to_postfix (expression):
    stack = []
    output =[]
    tokens = re.findall(r"[A-Za-z0-9]+|[()+\-*/^]", expression)
    for token in tokens:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:  
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return " ".join(output)

@app.route('/infixtopostfix', methods=['GET', 'POST'])
def infixtopostfix():
    postfix_result = None
    if request.method =='POST':
        expression = request.form['inputString']
        postfix_result = infix_to_postfix(expression)
    return render_template('infixtopostfix.html', postfix_result=postfix_result)



# ---------- RUN SERVER ----------
if __name__ == '__main__':
    app.run(debug=True)
