import json

stu = {'name': 'Jack', 'age': 23}

file_name = 'stu.json'
with open(file_name, 'w') as f_obj:
    json.dump(stu, f_obj)
