# encoding=utf-8

def init_dict():
    rome_num = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    return rome_num


def get_num():
    change_num = eval(input("请输入1~3999的整数:\n"))
    return change_num


def translate_num(change_num):
    rome_num = init_dict()
    changed_num = []
    if change_num // 1000 >= 1:
        for i in range(change_num // 1000):
            changed_num.append("M")
        change_num = change_num % 1000
        if change_num % 900 >= 0 and change_num // 900 >= 1:
            changed_num.append("CM")
            change_num = change_num - 900
    else:
        if change_num % 900 >= 0 and change_num // 900 >= 1:
            changed_num.append("CM")
            change_num = change_num - 900
    if change_num // 500 >= 1:
        for i in range(change_num // 500):
            changed_num.append("D")
        change_num = change_num % 500
    else:
        if change_num % 400 >= 0 and change_num // 400 >= 1:
            changed_num.append("CD")
            change_num = change_num - 400
    if change_num / 100 >= 1:
        for i in range(change_num // 100):
            changed_num.append("C")
        change_num = change_num % 100
    else:
        if change_num % 90 >= 0 and change_num // 90 >= 1:
            changed_num.append("XC")
            change_num = change_num - 90
    if change_num / 50 >= 1:
        for i in range(change_num // 50):
            changed_num.append("L")
        change_num = change_num % 50
    else:
        if change_num % 40 >= 0 and change_num // 40 >= 1:
            changed_num.append("XL")
            change_num = change_num - 40

    if change_num / 10 != 0:
        for i in range(change_num // 10):
            changed_num.append("X")
        change_num = change_num % 10
        if change_num % 10 == 9:
            changed_num.append("IX")
            change_num = change_num - 9
    if change_num / 5 != 0:
        if change_num % 5 != 4:
            for i in range(change_num // 5):
                changed_num.append("V")
            change_num = change_num % 5
        else:
            changed_num.append("IV")
            change_num = change_num - 4

    if change_num / 1 != 0:
        for i in range(change_num // 1):
            changed_num.append("I")
    return changed_num


def main():
    print(translate_num(get_num()))


if __name__ == '__main__':
    main()
