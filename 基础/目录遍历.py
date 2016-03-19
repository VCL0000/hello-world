import os


def dirlist(path):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)  # join()拼接路径
        if os.path.isdir(filepath):
            dirlist(filepath)
        print(filepath)


# path = input("请输入路径：")
# dirlist(path)

path = input("请输入路径：")
#g=walk(path)   会自动向下遍历
# g.next()  向下遍历再解析相当于toString
for path, dir, filelist in os.walk(path):
    for filename in filelist:
        files = os.path.join(path, filename)
        print(files)
