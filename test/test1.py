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
[...]bash: $: command not found

[#3]
$ exit 1
[256]

[#4]
@localhost
$ hostname
. whoami
. exit 1
[256]<HOSTNAME>
<USERNAME>

[#5]
root@localhost
$ REMOTE COMMAND
[...]Received disconnect from ::1: 2: Too many authentication failures for root
"""
