import os
import json
from flask import Flask, redirect, render_template, request


app = Flask(__name__)
users = []
    
def write_to_file(filename, data):
    """handle the process of writing data to text files"""
    with open(filename, "a") as file:
        file.writelines(data)

@app.route ('/', methods=["GET", "POST"])
def index():
    """Creates a username and checks this is a unique username. If it is a unique name the name gets added to users.txt"""
    if request.method == "POST":
        with open("data/users.txt", "r") as file:
            lines = file.read().split()
        print(lines)
        
        if request.form["username"] in lines:
            return "<h3>username already in use</h3>"
        else:
            write_to_file("data/users.txt", request.form["username"] + "\n")
            user =  request.form["username"] + "/1"
            return redirect(user)
    return render_template("index.html") 

@app.route('/<username>/<question_number>')
def questions(username, question_number):
    question = {}
    
    with open("data/questions.json","r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["question"] == question_number:
                question = obj
                
    return render_template("quiz.html", question=question)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)