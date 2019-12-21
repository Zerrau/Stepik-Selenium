# -*- coding: utf-8 -*-

# формат вывода строки f-strings
str1 = 1
str2 = "two"
str3 = "third"
print(
    f"Let's count together! '{str1}', then goes {str2}, and then {str3}")


def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
        f"expected  {expected_result} got  {actual_result}"


def test_substring(full_string, substring):
    if substring == full_string:
        print()
        return
    if substring not in full_string:
        print('expected', "'{}'".format(substring), 'to be substring of', "'{}'".format(full_string))
    if full_string in substring:
        print(full_string, substring)
