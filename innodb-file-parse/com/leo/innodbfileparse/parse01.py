import os.path as path


def pageNo(file, offset):
    s = offset + 4;
    file.seek(s)
    data = file.read(4)
    print("页编号: " + data.hex())

def beforePage(file, offset):
    s = offset + 8;
    file.seek(s)
    data = file.read(4)
    print("前一页编号: " + data.hex())

def afterPage(file, offset):
    s = offset + 12;
    file.seek(s)
    data = file.read(4)
    print("后一页编号: " + data.hex())


file_name = 'C:/Users/youliang.chen/Desktop/test1/user.ibd'
page_size = 16;  # 页大小16K
size = int(path.getsize(file_name) / 1024)
page_count = int(size / page_size)
print("文件大小: " + str(size) + "K")
print("页大小: " + str(page_size) + "K")
print("页数量: " + str(page_count))

with open(file_name, "rb") as file:
    for i in range(page_count):
        print("----------------------------------------")
        offset = i * page_size * 1024
        pageNo(file, offset)
        beforePage(file, offset)
        afterPage(file, offset)
