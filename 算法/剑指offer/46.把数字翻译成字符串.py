"""
把数字翻译成字符串
题目：给定一个数字，我们按照如下规则把它翻译为字符串：
0翻译成“a”，1翻译成“b”，……，11翻译成“l”，……，25翻译成“z”。
一个数字可能有多个翻译。例如，12258有5种不同的翻译，
分别是“bccfi”、“bwfi”、“bczi”、“mcfi”和“mzi”。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
"""

def get_translation_count(num):
    if num < 0:
        return 0
    num_str = str(num)
    length = len(num_str)
    counts = [0] * length
    for i in range(length - 1, -1, -1):
        count = 0
        if i < length - 1:
            count = counts[i + 1]
        else:
            count = 1
        if i < length - 1:
            digit1 = int(num_str[i])
            digit2 = int(num_str[i + 1])
            converted = digit1 * 10 + digit2
            if converted >= 10 and converted <= 25:
                if i < length - 2:
                    count += counts[i + 2]
                else:
                    count += 1
        counts[i] = count
    return counts[0]

# 递归实现
def get_translation_count2(num):
    if num < 0:
        return
    
    def dnf(num):
        nonlocal cnt
        if num < 26:
            cnt += 1
            if num < 10:
                return
            else:
                dnf(num // 10)
        else:
            if num < 100:
                dnf(num // 10)
            else:
                if num % 100 < 26:
                    dnf(num // 100)
                dnf(num // 10)

    cnt = 0
    dnf(num)
    return cnt


    

if __name__ == '__main__':
    # print(get_translation_count(12258))  # 5
    print(get_translation_count2(12258))  # 5
    print(get_translation_count2(0))  # 1
    print(get_translation_count2(1))  # 1
    print(get_translation_count2(25))  # 2
    print(get_translation_count2(26))  # 1