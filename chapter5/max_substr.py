# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: max_substr.py
# Python  : python3.6
# Time    : 19-1-23 12:43

"""
面试题48：最长不含重复字符的子字符串
题目：请从字符串中找出一个最长的不包含重复字符的子字符串，
计算该最长子字符串的长度。假设字符串中只包含a~z的字符。
例如，在字符串‘arabcacfr‘中，最长的不包含重复字符的
子字符串是’acfr‘，长度为4.
"""

def max_substr(s):
    """
    递归公式：
    令f(i)表示已第i个字符结尾的子串最大长度
    如果第i个字符不在前一个最大子串中，则
    f(i) = f(i-1) + 1
    否则f(i)等于两个重复字符间的距离
    :param s:
    :return:
    """
    if not s:
        return ''
    temp = s[0]
    max_len = [0 for _ in range(len(s))]
    # 26个字母，每个字母在字符串中的索引
    positions = [-1 for _ in range(26)]
    positions[ord(s[0])-ord('a')] = 0
    max_len[0] = 1
    for i in range(1, len(s)):
        pre_index = positions[ord(s[i]) - ord('a')]
        if pre_index + len(temp) < i:
            max_len[i] = max_len[i-1] + 1
            temp += s[i]
        else:
            max_len[i] = i - pre_index
            temp = s[pre_index+1:i+1]
        positions[ord(s[i]) - ord('a')] = i
    return max(max_len)

if __name__ == '__main__':
    print(max_substr('aradbceacfr'))
