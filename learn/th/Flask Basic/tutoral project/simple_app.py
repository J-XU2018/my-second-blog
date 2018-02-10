from flask import Flask
# from flask import request

# Create a new Flask instance as a variable named app.
# The name you pass to the Flask app should be __name__.
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="Jack"):
    #Arguments in the query string are automatically converted to
    # their native types (e.g. ints, floats, strs, etc)  ---False
    # What type of object is request? :Global
    # developer want their code easy to read and work with, so query string ? mark in url is not good
    # name = request.args.get('name', name)
    name = 'Katie, Laura'
    return "Hello from {}.".format(name)

##think how to add float numbers
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
    # return "{} + {} = {}".format(num1, num2, int(num1)+int(num2))
    # return "{} + {} = {}".format(num1, num2, num1+num2)

app.run(debug=True, port=5000, host='127.0.0.1')
