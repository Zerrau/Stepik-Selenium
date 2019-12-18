"""def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
        f"expected  {expected_result} got  {actual_result}" """


def test_substring(full_string, substring):
    assert substring not in full_string
    print("expected '{}' to be substring of '{}'".format(substring, full_string))

# c = test_substring(a, b)
# print(c)
# print('expected \'substring\' to be substring of \'full_string\'')
# print('Here is \'some text in quotes\'. Here is text without quotes.')
