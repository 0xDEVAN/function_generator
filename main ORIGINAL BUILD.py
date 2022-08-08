from flask import Flask
from utility_functions import function_generator  

app = Flask(__name__)

@function_generator.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@function_generator.route("/create")
def generate_function():
    return __name__

@function_generator.route('/run')
def my_view_func(name):
    return name

@function_generator.route('/update')
def my_view_func(name):
    return name

@function_generator.route('/delete')
def my_view_func(name):
    return name