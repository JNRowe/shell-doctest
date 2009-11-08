"""
[#test command]
$ ./shell-doctest --verbose=2 test test
Module:test/issue2.py
Label:None
Label:None
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

[#--dry-run option]
$ ./shell-doctest --dry-run test '#TEST1'|wc
5       7      51

[#labels command]
$ ./shell-doctest labels
[#test command] test.py:1:
[#--dry-run option] test.py:18:
[#labels command] test.py:22:
[#TEST1] test/test0.py:9:
[#TEST2] test/test0.py:13:
[#TEST3] test/test1.py:9:
[#TEST4] test/test1.py:15:
[#TEST5] test/test1.py:19:
[#TEST6] test/test1.py:24:
[#TEST7] test/test1.py:31:
"""
