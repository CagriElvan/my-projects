from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 1172000, number2 = 2290400)
                            # index değişkenine değer verdik
@app.route('/sum')
def number():
    var1, var2 = 1577210, 3778960
    return render_template('body.html', value1 = var1, value2 = var2, sum = var1+var2)
                            # body değişkenine değer verdik

if __name__ == '__main__':
    app.run(debug=True)