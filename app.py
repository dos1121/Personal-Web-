from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Main Pages
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
    
@app.route('/works')
def works():
    return render_template('works.html')

# Tool Pages
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

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
