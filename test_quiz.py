"""from app import app
import unittest """


with open("data/users.txt", "r") as file:
    lines = file.read()
print(lines)

if "Jo" in lines:
    print("already in use")
else:
    print("not working")
        
        
"""
class testApp(unittest.TestCase):
    def test_username_created_and_saved(self):
        username = "Chris"

if __name__ == '__main__':
    unittest.main()
"""