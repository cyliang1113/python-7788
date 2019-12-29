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


def pageType(file, offset):
    s = offset + 24;
    file.seek(s)
    data = file.read(2)
    key = (data.hex());

    map = {
        "45bf": "B+树叶子节点页",
        "0002": "undo log页",
        "0003": "索引节点页",
        "0004": "insert buffer空闲列表页",
        "0000": "最新分配页",
        "0005": "insert buffer位图页",
        "0006": "系统页",
        "0007": "事务系统数据页",
        "0008": "File Space Header页",
        "0009": "扩展描述页",
        "000a": "BLOB页",
    }
    print("页类型: " + key + ", " + str(map.get(key)));


file_name = 'C:/Users/leon/Desktop/test1/user_user.ibd'
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
        pageType(file, offset)
