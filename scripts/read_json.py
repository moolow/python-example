import json

myList = [1, 2, 'Hello']
myDict = {'list': myList, 'a': 10}

# Serialize obj to a JSON formatted str.
print(json.dumps(myList)) # '[1, 2, "Hello"]'
print(json.dumps(myDict)) # '{"list": [1, 2, "Hello"], "a": 10}'
