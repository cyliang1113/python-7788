import json

file_name = 'stu.json'
with open(file_name) as f_obj:
    stu = json.load(f_obj)
print(stu)
