import os
import json
from datetime import datetime
from flask import Flask, redirect, render_template, request


app = Flask(__name__)
correct = []
incorrect = []

def write_to_file(filename, data):
    """handle the process of writing data to text files"""
    with open(filename, "a") as file:
        file.writelines(data)

@app.route ('/', methods=["GET", "POST"])
def index():
    """adds scoreboard to home page"""
    sorted_scores = []
    name = []
    score = []
    time = []
    
    with open("data/scoreboard.txt", "r") as f:
            data = f.read().split(",")
            #print(data)
            #print(len(data))
            
            
            for i in range(0, len(data)-2, 3):
                name.append(data[i])
                score.append(data[i+1])
                time.append(data[i+2])
            #print(name, score, time)

            
            final = zip(name, score, time)
            sorted_scores = sorted(final, key=lambda final: final[1], reverse=True)
            #print(sorted_scores)
            name, score, time = zip(*sorted_scores)
            
    """Creates a username and checks this is a unique username. If it is a unique name the name gets added to users.txt"""
    
    if request.method == "POST":
        with open("data/users.txt", "r") as file:
            lines = file.read().split()
        
        if request.form["username"] in lines:
            return "<h3>username already in use</h3>"
        else:
            write_to_file("data/users.txt", request.form["username"] + "\n")
            user =  request.form["username"] + "/1"
            return redirect(user)
    return render_template("index.html", name=name, time=time, score=score, x=len(data)) 

            
@app.route('/<username>/<question_number>', methods=['GET', 'POST'])
def questions(username, question_number):
    question = {}
    
    with open("data/questions.json","r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["question"] == question_number:
                question = obj
                
    if request.method == "POST":
        
        if request.form["answer"] == question["answer"]:
            new = int(question_number) + 1
            correct.append(question["answer"])
            #open('data/incorrect_answers.txt', 'w').close()
            write_to_file("data/{0}_incorrect_answers.txt".format(username),"")
            write_to_file("data/{0}_correct_answers.txt".format(username), request.form["answer"] + "\n")
            return redirect(username + '/' + str(new))
        else:
            write_to_file("data/{0}_incorrect_answers.txt".format(username), request.form["answer"] + "\n")
            with open("data/{0}_incorrect_answers.txt".format(username), "r") as file:
                data = file.read().splitlines()
                incorrect_answers = data
            #print(incorrect_answers)
            return render_template("quiz.html", question=question, incorrect_answers = data)
        
    if int(question_number) > 5:
        
        with open("data/{0}_correct_answers.txt".format(username), "r") as file:
            correct_answers = file.read().splitlines()
        with open("data/{0}_incorrect_answers.txt".format(username), "r") as file:
            incorrect_answers = file.read().splitlines()
        
        user_score = len(correct_answers)*5-len(incorrect_answers)
        write_to_file("data/scoreboard.txt", username + "," + str(user_score) + ",{0},\n".format(datetime.now().strftime("%d-%m-%y %H:%M")))
        os.remove("data/{0}_correct_answers.txt".format(username))
        os.remove("data/{0}_incorrect_answers.txt".format(username))
        return redirect(username + "/scores")
    

                
    return render_template("quiz.html", question=question)
    
@app.route('/<username>/scores')
def scores(username):
    
    
    
    sorted_scores = []
    name = []
    score = []
    time = []
    
    with open("data/scoreboard.txt", "r") as f:
            data = f.read().split(",")
            #print(data)
            #print(len(data))
            
            
            for i in range(0, len(data)-2, 3):
                name.append(data[i])
                score.append(data[i+1])
                time.append(data[i+2])
            #print(name, score, time)

            
            final = zip(name, score, time)
            sorted_scores = sorted(final, key=lambda final: final[1], reverse=True)
            #print(sorted_scores)
            name, score, time = zip(*sorted_scores)

            
    return render_template("scoreboard.html",username=username, name=name, time=time, score=score, x=len(data))

    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)