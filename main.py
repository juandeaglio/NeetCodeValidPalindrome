import unittest
import re


def run_tests(tested_function, test_cases):
    for test in test_cases:
        try:
            assert test['expected'] == tested_function(test['input'])
            print(f"Test passed for expected {test['expected']} for input {test['input']}")
        except AssertionError:
            print(f"Test failed for expected {test['expected']} for input {test['input']}")


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s = re.sub(r'[^a-z0-9]', '', s)

        for i in range(0, len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False

        return True


long_test_case = ""
for i in range(0, 100000):
    if i % 3 == 0:
        long_test_case += ' '
    elif i % 3 == 1:
        long_test_case += 'a'
    else:
        long_test_case += 'b'

long_test_case += long_test_case[::-1]

test_cases = [
    {'input': 'a', 'expected': True},
    {'input': 'ab', 'expected': False},
    {'input': 'a,b a', 'expected': True},
    {'input': ' ', 'expected': True},
    {'input': long_test_case, 'expected': True},
]

run_tests(Solution().isPalindrome, test_cases)

