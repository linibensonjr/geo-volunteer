from email import message
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # message = {
    #     'greeting': 'Hello World'
    # }
    # return (message)
    return render_template('pages/index.html')

@app.route('/org')
def org():
    # message = {
    #     'greeting': 'Hello World'
    # }
    # return (message)
    return render_template('pages/index.html')

if __name__ == '__main__':
    app.run(debug=True, port=81)