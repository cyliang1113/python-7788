import json

stu = {'name': 'Jack', 'age': 23}

file_name = 'stu.json'
with open(file_name, 'r+') as file:
    print(file.read())
    json.dump(stu, file)
    print(file.read())
