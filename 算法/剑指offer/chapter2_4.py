# 替换空格
"""
题目： 请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入"We are happy."，则输出"We%20are
%20happy."。
"""
# 解题思路：先遍历一遍字符串，统计出字符串中空格的总数，然后计算出替换后的字符串的总长度，最后从后往前替换字符串。
# 时间复杂度：O(n)
# 空间复杂度：O(n)
def replace_space(s: str) -> str:
    if not s:
        return ""
    count = 0
    for char in s:
        if char == " ":
            count += 1
    new_length = len(s) + count * 2
    new_str = [0] * new_length
    i = len(s) - 1
    j = new_length - 1
    while i >= 0:
        if s[i] != " ":
            new_str[j] = s[i]
            j -= 1
        else:
            new_str[j] = "0"
            new_str[j-1] = "2"
            new_str[j-2] = "%"
            j -= 3
        i -= 1
    return "".join(new_str)