"""
[#test command]
$ ./shell-doctest --verbose=2 test test
Module:test/test-issues.py
Label:issue2
Label:None
Module:test/test.sh.py
Label:#non-python-file
Module:test/test0.py
Label:None
Label:#TEST1
Label:#TEST2
Module:test/test1.py
Label:None
Label:#TEST3
Label:#TEST4
Label:#TEST5
Label:#TEST6
Label:#TEST7
Label:#@IP-ADDR
Label:#USER@IP-ADDR

[#--dry-run option]
$ ./shell-doctest --dry-run test '#TEST1'|wc
5       7      51

[#labels command]
$ ./shell-doctest labels
[#test command] test.py:1:
[#--dry-run option] test.py:22:
[#labels command] test.py:26:
[issue2] test/test-issues.py:1:
[#non-python-file] test/test.sh.py:1:
[#TEST1] test/test0.py:9:
[#TEST2] test/test0.py:13:
[#TEST3] test/test1.py:9:
[#TEST4] test/test1.py:15:
[#TEST5] test/test1.py:19:
[#TEST6] test/test1.py:24:
[#TEST7] test/test1.py:31:
[#@IP-ADDR] test/test1.py:36:
[#USER@IP-ADDR] test/test1.py:43:
"""

import doctest
import unittest

from shelldoctest.shellunittest import Connection, TestCase
from shelldoctest.shellunittest import DocTestFailure, ResponseTimeout

host = "localhost:22"

class MyTest(TestCase):
    c = Connection(host)

    def test_raise_DocTestFailure(self):
        self.assertRaises(DocTestFailure, self.assertOutput, self.c, "pwd", "")

class MyTest2(TestCase):
    c = Connection(host)
    c1 = Connection(host)

    def test_muluti_connections(self):
        self.assertOutput(self.c, "pwd", "/.../...\n", doctest.ELLIPSIS)
        self.c("cd /", None)
        self.assertOutput(self.c1, "pwd", "/.../...\n", doctest.ELLIPSIS)
        self.assertOutput(self.c, "pwd", "/\n")

    def test_remake_connection(self):
        self.assertOutput(self.c, "pwd", "/.../...\n", doctest.ELLIPSIS)

    def test_timeout(self):
        self.assertRaises(ResponseTimeout, self.c, "sleep 10", "dummy", timeout=0.01)

if __name__ == "__main__":
    unittest.main()

