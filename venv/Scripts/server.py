# import flask to created the server
from flask import Flask
import json

# create the app
app = Flask(__name__)

# this is our first enpoint
@app.get("/") # / - means root
def home():
   return "Hello from flask"
@app.get("/about")
def about():
   # return your name on a json format
   name2 = {"name":"Jefferson Turla"}
   return json.dumps(name2)

@app.get("/greet/<name>")
def greet(name):
   return f"""
   <h1 style='color:lightblue;text-align:center'>
   Hello {name}
   </h>
   """

@app.get("/square/<int:number>")
def square(number):
   return f"""
   <p style='font-size:30px'>The square of {number} is {number*number}
   </p>
   """

@app.get("/farewell/<name>")
def farewell(name):
   return f"""
   <p style=font-weight:bold>
   Have a good one, {name}
   </p>
   """

# when i save my code, the changes will be applied
app.run(debug=True)

