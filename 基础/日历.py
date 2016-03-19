import calendar
import time
print("输入年月生成日历")
y = int (input("输入年份"))
s = int(input("输入月份"))
cal = calendar.month(y,s)
print("日历为：")
print(cal)
