print("读取文件替换查找指定内容后替换保存")
rr = input("读取的文件")
tt = input("查找的内容")
tt2 = input("替换的内容")
ww = input("写入的文件")

fp1 = open(rr, "r")
fp2 = open(ww, "w")

for s in fp1.readlines():
    fp2.write(s.replace(tt, tt2))

fp1.close()
fp2.close()
