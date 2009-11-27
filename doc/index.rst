.. Shell Doctest documentation master file, created by
   sphinx-quickstart on Sat Nov 21 10:00:12 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Shell Doctest's documentation!
=========================================

Shell-Doctest is Doctest tool and UnitTest module for shell command response,
written by ENDOH takanao and licensed under the BSD license.

Shell-Doctestは、shellコマンドのレスポンステストに利用できるツールとUnitTestモジュールを提供します。
ライセンスは、修正BSDライセンスです。

Shell-DoctestのUnitTestは、paramikoを利用しています。
Shell-DoctestのUnitTestモジュールを使うには、paramikoをインストールしてください。

Shell-Doctestは、2つのモジュールと、1つのユーティリティコマンドを提供します。

- shelldoctest:   shellコマンドの表記形式に対応したdoctestモジュールです。
- shellunittest:  shellコマンドを実行して、shellのレスポンスを検査するTestCaseを提供します。
- shell-doctest:  shelldoctestのテストを実行するユーティリティコマンドです。

Examples
--------

shell-doctestとshellunittestのサンプルです。

shelldoctest:

.. literalinclude:: ../test/test.sh
   :language: bash
   :lines: 1-6

shellunittest:

.. literalinclude:: ../test.py
   :language: python
   :pyobject: Example


Contents
--------

.. toctree::
   :maxdepth: 2
   :glob:

   *


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

