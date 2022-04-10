import os
import json

# Access to the files
os.chdir(os.path.dirname(__file__))

# Open json file
with open('data.json', 'r') as f:
    data = json.load(f)
