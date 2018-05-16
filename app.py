from flask import Flask, request, render_template

app = Flask(__name__)


# @ signifies a decorator: way to wrap a function and modify its behavior
@app.route('/', methods=['GET', 'POST'])
def input():
    # request.method and request.form
    if request.method == 'POST':
        x, y = request.form['input1'], request.form['input2']
        operator = request.form['operator']
        result = compute(x, y, operator)
    else:
        x, y, operator, result = None, None, None, None
    return render_template('homepage.html', result=result, x=x, y=y, operator=operator)


def compute(x, y, operator):
    try:
        x, y = float(x), float(y)
        operator = str(operator)
        if operator == '+':
            return x + y
        elif operator == '-':
            return x - y
        elif operator == '*':
            return x * y
        elif operator == '/':
            return x / y
        elif operator == '%':
            return x % y
        else:
            return "ERROR: Invalid input of operator!"
    except ValueError:
        return "ERROR: Invalid input of x or y!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
