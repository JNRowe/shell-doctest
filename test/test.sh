[Example]
$ echo MSG1
. echo MSG2 >&2
. exit 1
(1)MSG2
MSG1

[#non-python-file]
$ echo TEST
. echo TEST
TEST
TEST
