import os
from flask import Flask, redirect, render_template, request


app = Flask(__name__)
users = []
    
def write_to_file(filename, data):
    """handle the process of writing data to text files"""
    with open(filename, "a") as file:
        file.writelines(data)

def select_user_name():
    with open("data/users.txt", "r") as file:
        lines = file.read()
    print(lines)

    if "Jo" in lines:
        print("already in use")
    else:
        print("not working")

@app.route ('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        with open("data/users.txt", "r") as file:
            lines = file.read()
        print(lines)
        
        if request.form["username"] in lines:
            return render_template("index.html") 
        else:
            write_to_file("data/users.txt", request.form["username"] + "\n")
            return redirect(request.form["username"])
    return render_template("index.html") 

@app.route('/<username>')
def user(username):
    """display users score"""
    return render_template("quiz.html")
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)