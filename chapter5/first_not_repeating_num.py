# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: first_not_repeating_char.py
# Python  : python3.6
# Time    : 19-1-24 22:21

"""
面试题50：第一个只出现一次的字符
题目一：字符串中第一个只出现一次的字符
在字符串中找出第一个只出现一次的字符。
如输入“abaccdeff"则输出b
"""

def find_char(s):
    if not s:
        return None
    char_count = dict()
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    for c in s:
        if char_count[c] == 1:
            return c
    return None

"""
相关题目：判断两个字符串是否为变位词
在英语中，如果两个单词中出现的字母相同，
并且每个字母出现的次数也相同，那么这两个
单词互为变位词(anagram),例如，silent
与listen,evil与live等互为变位词
"""
def is_anagram(s1, s2):
    if not (s1 and s2):
        return False
    char_dict = dict()
    for s in s1:
        char_dict[s] = char_dict.get(s, 0) + 1
    for s in s2:
        if s not in char_dict:
            return False
        char_dict[s] = char_dict[s] - 1
        if char_dict[s] == 0:
            char_dict.pop(s)
    return char_dict == {}

if __name__ == '__main__':
    print(find_char('abaccdeff'))
    print(is_anagram('listen', 'silence'))