import math

v = 1.0
print("计算器版本：", v)

print("本计算器支持的算法有: + - * / ^ 开方 log sin cos tan ")

a = int(input("请输入第一个数据："))
o = input("请输入运算符")
b = int(input("请输入第二个数据,不需要是请输入任意值："))


def jia(x, y):
    return print(x, o, b, "=", x + y)


def jian(x, y):
    return print(x, o, b, "=", x - y)


def cheng(x, y):
    return print(x, o, b, "=", x * y)


def chu(x, y):
    return print(x, o, b, "=", x / y)


def chengfang(x, y):
    return print(x, o, b, "=", x ** y)


def kaifang(x, y):
    return print(x, o, "=", math.sqrt(x))


def laole(x, y):
    return print(x, o, y, "=", math.log(x, y))


def sin(x, y):
    return print(x, o, "=", math.sin(x))


def cos(x, y):
    return print(x, o, "=", math.cos(x))


def tan(x, y):
    return print(x, o, "=", math.tan(x))


def operator(a, o, b):
    if o == "+":
        jia(a, b)
    elif o == "-":
        jian(a, b)
    elif o == "*":
        cheng(a, b)
    elif o == "/":
        chu(a, b)
    elif o == "^":
        chengfang(a, b)
    elif o == "开方":
        kaifang(a, b)
    elif o == "log":
        laole(a, b)
    elif o == "sin":
        sin(a, b)
    elif o == "cos":
        cos(a, b)
    elif o == "tan":
        tan(a, b)
    else:
        print("运算符有错")
        pass


operator(a, o, b)
