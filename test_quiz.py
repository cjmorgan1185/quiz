"""from app import app
import unittest"""
import json

""" opens usernames and checks name is not already in list"""
with open("data/users.txt", "r") as file:
    lines = file.read().split()
print(lines)

if "Christ" in lines:
    print("already in use")
else:
    print("ok to use")
        
"""opens questions and stores them in a dictionary"""
question = {}

with open("data/questions.json","r") as json_data:
    data = json.load(json_data)
    for obj in data:
        if obj["question"] == "1":
            question = obj
print(question)

"""chekcs the answer to the question is correct"""

if "The A-Team" == question['answer']:
    print("correct")
else:
    print("incorrect")


        
""" class testApp(unittest.TestCase):
    def test_username_created_and_saved(self):
        username = "Chris"

if __name__ == '__main__':
    unittest.main()"""