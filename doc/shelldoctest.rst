===================
shelldoctest module
===================

test/test.sh:

.. literalinclude:: ../test/test.sh
   :language: bash
   :lines: 1-6
   :linenos:

::

    $ shell-doctest test test/test.sh Example

    $ shell-doctest --dry-run test test/test.sh Example
    [Example] test/test.sh.py:1:
    $ echo MSG1; echo MSG2 >&2; exit 1
    ----
    (1)MSG2
    MSG1

    $ shell-doctest --verbose=3 test test/test.sh Example
    New verbose level is 3
    Module:test/test.sh.py
    Label:Example
    Trying:
        echo MSG1; echo MSG2 >&2; exit 1
    Expecting:
        (1)MSG2
        MSG1
    ok
    1 items passed all tests:
       1 tests in test.test
    1 tests in 1 items.
    1 passed and 0 failed.
    Test passed.

