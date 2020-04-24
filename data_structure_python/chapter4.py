# -*- coding: utf-8 -*-

#普通迭代实现
def fib(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0,1]

    temp = [0,1]
    for i in range(2,n):
        temp.append(temp[i-2]+temp[i-1])

    return temp


# 递归实现
def fib_recursion(n):
    if n<2 :
        return n
    return fib_recursion(n-1)+fib_recursion(n-2)



#根据数字字符和符号字符四则运算结果
def cal(num1,num2,str):
    if str == "+":
        return int(num1)+int(num2)
    if str == "-":
        return int(num1)-int(num2)
    if str == "*":
        return int(num1)*int(num2)
    if str == "/" and num2 != 0 :
        return int(num1)//int(num2)
    else:
        return 0


#后缀表达式计算
#利用python的数组的函数模拟栈操作
#空栈 l = []
#进栈 l.append(ele)
#出栈 l.pop(ele)
#后缀表达式 9_3_1_-_3_*_+_10_2_/_+
def cal_suffix(string):
    split_str = string.split('_')
    stack = []
    for s in split_str:
        print(s)
        if s.isnumeric():
            stack.append(s)
        else:
            temp1 = stack.pop()
            temp2 = stack.pop()
            stack.append(cal(temp2,temp1,s))
    return stack[0]


#判断运算符号优先级
def lower(str1,str2):
    level1 = 1 if str1 in ["*","/"] else 0
    level2 = 1 if str2 in ["*","/"] else 0
    print("str level")
    print(str1)
    print(level1)
    print(str2)
    print(level2)
    return level1<=level2

#中缀表达式转后缀表达式，规则见chapter4.md
#mid: 9+(3-1)*3+10/2
#suffix: 9_3_1_-_3_*_+_10_2_/_+
def convert_mid_to_suffix(string):
    import re
    stack = []
    output = ""
    while len(string)>0:
        # print("whlile" + output)
        # print("stack:%s" % stack)
        # print("string:%s" % string)
        # print("first_ele:%s" % first_ele)
        first_ele = string[0:1]
        if first_ele.isnumeric():
            match = re.search('(\d+)',string)
            ele = match.group(0)
            output += "_"+ele
            string = string.replace(str(ele), "", 1)
        else:
            if len(stack) == 0:
                stack.append(first_ele)
            elif first_ele == "(":
                stack.append(first_ele)
            elif first_ele != ")" and lower(stack[-1],first_ele):
                stack.append(first_ele)
            else:
                if first_ele == ")":
                    while stack[-1] != "(":
                        last_ele = stack.pop()
                        output += '_'+last_ele
                    stack.pop()
                else:
                    while len(stack)>0:
                        last_ele = stack.pop()
                        output += '_' + last_ele
                    stack.append(first_ele)
            string = string.replace(str(first_ele), "", 1)
        if len(string) == 0:
            while len(stack) > 0:
                last_ele = stack.pop()
                output += '_' + last_ele
    return output[1:]


if __name__ == "__main__":
    #n=40
    #print(fib(n))
    #print(fib_recursion(10)) # 递归运算时间更长

    #target = "9_3_1_-_3_*_+_10_2_/_+"
    #print(cal_suffix(target))

    mid ="9+(3-1)*3+10/2"
    print(convert_mid_to_suffix(mid))