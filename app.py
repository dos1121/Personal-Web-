from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route ('/contact')
def contact():
    return render_template('contact.html')

@app.route ('/works')
def works():
    return render_template('works.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfCircle', methods=['GET', 'POST'])
def areaOfCircle():
    result = None 
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            result = round(math.pi * radius ** 2, 2 )
        except ValueError:
            result = "Invalid input! Please enter a number."
    return render_template('areaOfCircle.html' , result=result)

@app.route('/areaOfRectangle', methods=['GET', 'POST'])
def areaOfRectangle():
    result = None
    if request.method == 'POST':
        try:
            length = float(request.form.get('length', 0))
            width = float(request.form.get('width', 0))
            result = round(length * width, 2)
        except ValueError:
            result = "Invalid input! Please enter numbers."
    return render_template('areaOfRectangle.html', result = result)

if __name__ == "__main__":
    app.run(debug=True)
