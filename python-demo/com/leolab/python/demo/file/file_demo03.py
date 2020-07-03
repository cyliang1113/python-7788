import os.path as path
import os

file_name = './binFile'

if os.path.exists(file_name):
    os.remove(file_name)

with open(file_name, "w") as file:
    pass

with open(file_name, "rb+") as file:
    file.write(b"1234567899abcdef")
    print(file.read(1))
    file.seek(5)
    print(file.read(1))
    file.seek(16)
    print(file.read(1))