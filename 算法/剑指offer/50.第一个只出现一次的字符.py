"""
第一个只出现一次的字符
题目：在字符串中找出第一个只出现一次的字符。如输入“abaccdeff”，则输出b。
"""

def first_not_repeating_char(s):
    if not s:
        return None
    char_count = dict()
    for i in s:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    for i in s:
        if char_count[i] == 1:
            return i
    return None



if __name__ == "__main__":
    print(first_not_repeating_char("abaccdeff"))  # b
    print(first_not_repeating_char("aabbcc"))  # ""
    print(first_not_repeating_char("a"))  # a
    print(first_not_repeating_char(""))  # ""
    print(first_not_repeating_char(None))  # ""