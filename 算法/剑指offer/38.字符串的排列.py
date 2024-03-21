"""
字符串的排列
题目：输入一个字符串，打印出该字符串中字符的所有排列。
例如输入字符串abc，则打印出由字符a、b、c所能排列出来的所有字符串
abc、acb、bac、bca、cab和cba。
"""

# 解法1：递归
# 递归的思路是：把字符串分为两部分，一部分是字符串的第一个字符，另一部分是第一个字符以后的所有字符。
# 然后把第一个字符和它后面的字符逐个交换。
# 例如：abc
# 第一步：a和a交换，得到a+bc，然后对bc进行全排列
# 第二步：a和b交换，得到b+ac，然后对ac进行全排列
# 第三步：a和c交换，得到c+ba，然后对ba进行全排列
# 第四步：bc进行全排列，得到bc和cb
# 第五步：ac进行全排列，得到ac和ca
# 第六步：ba进行全排列，得到ba和ab
# 最后得到abc、acb、bac、bca、cab和cba
# 递归的终止条件是：当只有一个字符时，不需要交换，直接输出即可。
# 递归的时间复杂度是O(n!)，空间复杂度是O(n)
def permutation(s):
    if not s:
        return []
    res = []
    res.append(s)
    permutation_helper(list(s), 0, res)
    return res

def permutation_helper(s, start, res):
    if start == len(s)-1:
        print("".join(s))
    else:
        for i in range(start, len(s)):
            s[i], s[start] = s[start], s[i]
            if i != start:
                res.append("".join(s))
            permutation_helper(s, start+1, res)
            s[i], s[start] = s[start], s[i]


# 解法2：字典序排列
# 字典序排列的思路是：先对字符串进行排序，然后找到下一个排列。
# 例如：abc
# 第一步：abc
# 第二步：acb
# 第三步：bac
# 第四步：bca
# 第五步：cab
# 第六步：cba
# 字典序排列的时间复杂度是O(n!)，空间复杂度是O(1)
def permutation2(s):
    if not s:
        return []
    res = []
    s = sorted(s)
    res.append(''.join(s))
    while True:
        s = next_permutation(s)
        if s:
            res.append(''.join(s))
        else:
            break
    return res

def next_permutation(s):
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i+1]:
        i -= 1
    if i < 0:
        return []
    j = len(s) - 1
    while j >= 0 and s[j] <= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    s[i+1:] = s[i+1:][::-1]
    return s

if __name__ == "__main__":
    s = "abc"
    print(permutation(s))
    # Expected output: ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']
    print(permutation2(s))
    # Expected output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']