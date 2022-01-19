from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def head():
    return render_template('index.html', number1=34, number2 =14)

@app.route('/function')
def function():
   
    return render_template('body.html', vari1=2, vari2=3)




if __name__ == '__main__':
    app.run(debug=True)