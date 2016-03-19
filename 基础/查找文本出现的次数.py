import re

file = input("查找的文件")
ss = input("查找的内容")
fp = open(file, "r")
count = 0
for s in fp.readlines():
    li = re.findall(ss, s)
    if len(li) > 0:
        count = count + len(li)

print("search", count, ss)
fp.close()
