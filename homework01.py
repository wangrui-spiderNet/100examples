# coding=UTF-8

'''
【程序2】
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
　　　于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
　　　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
　　　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
　　　100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
1.程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。　　　　　　
2.程序源代码：
'''

sellary = int(raw_input("请输入利润(万):"))
a = 10
b = 20
c = 40
d = 60
e = 100
list = [a, b, c, d, e]


def calculate(num, list):
    if num < list[0]:
        return num * 0.1
    if list[0] < num and num <= list[1]:
        return list[0] * 0.1 + (num - list[0]) * 0.075
    if list[1] < num and num <= list[2]:
        return list[1] * 0.075 + (num - list[1]) * 0.05
    if list[2] < num and num <= list[3]:
        return list[2] * 0.05 + (num - list[2]) * 0.03
    if list[3] < num and num <= list[4]:
        return list[3] * 0.03 + (num - list[3]) * 0.015
    else:
        return list[4] * 0.015 + (num - list[4]) * 0.01


print ('应得工资:', calculate(sellary, list))
