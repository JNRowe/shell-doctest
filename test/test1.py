"""
Shell Doctest module.

:Copyright: (c) 2009, the Shell Doctest Team All rights reserved.
:license: BSD, see LICENSE for more details.

$ echo TEST
TEST

[#1]
$ LANG=C date -r 0 -u
. date
Thu Jan  1 00:00:00 UTC 1970
...

[#2]
$ LANG=C $
(...)bash: $: command not found

[#3]
$ echo STDOUT; exit 1 STDERR
(1)bash: line 0: exit: too many arguments
STDOUT

[#4]
@localhost
$ hostname
. whoami
. exit 1
(255)ssh: connect to host localhost port 22: Connection refused

[#5]
root@localhost
$ REMOTE COMMAND
(255)ssh: connect to host localhost port 22: Connection refused
"""
