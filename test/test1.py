"""
Shell Doctest module.

:Copyright: (c) 2009, the Shell Doctest Team All rights reserved.
:license: BSD, see LICENSE for more details.

$ echo TEST
TEST

[#TEST3]
$ LANG=C date -r 0 -u
. date
Thu Jan  1 00:00:00 UTC 1970
...

[#TEST4]
$ LANG=C $
(...)bash: $: command not found

[#TEST5]
$ echo STDOUT; exit 1 STDERR
(1)bash: line 0: exit: too many arguments
STDOUT

[#TEST6]
@localhost
$ hostname
. whoami
. exit 1
(255)ssh: connect to host localhost port 22: Connection refused

[#TEST7]
root@localhost
$ REMOTE COMMAND
(255)ssh: connect to host localhost port 22: Connection refused

[#@IP-ADDR]
@127.0.0.1
$ hostname
. whoami
. exit 1
(255)ssh: connect to host 127.0.0.1 port 22: Connection refused

[#USER@IP-ADDR]
root@127.0.0.1
$ REMOTE COMMAND
(255)ssh: connect to host 127.0.0.1 port 22: Connection refused
"""
