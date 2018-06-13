"""from app import app
import unittest"""
import json
from random import randint

with open("data/users.txt", "r") as file:
    lines = file.read().split()
print(lines)

if "Christ" in lines:
    print("already in use")
else:
    print("ok to use")
        

question = {}

with open("data/questions.json","r") as json_data:
    data = json.load(json_data)
    for obj in data:
        if obj["question"] == 1:
            question = obj
print(question)


        
""" class testApp(unittest.TestCase):
    def test_username_created_and_saved(self):
        username = "Chris"

if __name__ == '__main__':
    unittest.main()"""