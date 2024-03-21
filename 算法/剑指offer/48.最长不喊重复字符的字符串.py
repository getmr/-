"""
最长不含重复字符的子字符串
题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。假设字符串中只包含'a'~'z'的字符。
例如，在字符串"arabcacfr"中，最长的不含重复字符的子字符串是"acfr"，长度为4。
"""

# 方法一：动态规划
def get_longest_substring(s):
    if not s:
        return 0
    length = len(s)
    max_length = 0
    pre_length = 0
    position = [-1] * 26
    for i in range(length):
        pre_index = position[ord(s[i]) - ord('a')]
        if pre_index < 0 or i - pre_index > pre_length:
            pre_length += 1
        else:
            if pre_length > max_length:
                max_length = pre_length
            pre_length = i - pre_index
        position[ord(s[i]) - ord('a')] = i
    if pre_length > max_length:
        max_length = pre_length
    return max_length


# 方法二：滑动窗口
def get_longest_substring2(s):
    if not s:
        return 0
    length = len(s)
    max_length = 0
    start = 0
    position = {}
    for i in range(length):
        if s[i] in position and position[s[i]] >= start:
            start = position[s[i]] + 1
        position[s[i]] = i
        max_length = max(max_length, i - start + 1)
    return max_length


# 方法三：滑动窗口
def get_longest_substring3(s):
    if not s:
        return 0
    length = len(s)
    max_length = 0
    start = 0
    position = [-1] * 26
    for i in range(length):
        pre_index = position[ord(s[i]) - ord('a')]
        if pre_index >= start:
            start = pre_index + 1
        position[ord(s[i]) - ord('a')] = i
        max_length = max(max_length, i - start + 1)
    return max_length


if __name__ == '__main__':
    print(get_longest_substring("arabcacfr"))  # 4
    print(get_longest_substring2("arabcacfr"))  # 4
    print(get_longest_substring3("arabcacfr"))  # 4
