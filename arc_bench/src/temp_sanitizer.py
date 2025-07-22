import json
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

data['test'][0]['output'] = None 

print(json.dumps(data))