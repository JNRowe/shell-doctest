====================
shellunittest module
====================

Reference
=========

:Required paramiko:

    Shell-DoctestのUnitTestモジュールでは、paramikoを利用しています。

:transport:

    paramikoモジュールのtransportです。

:channel:

    paramikoモジュールのchannelです。

:Connection:

    channelにshellを開いた状態で、channelを保持します。

:UnitTest:

    setUpメソッドの定義はありません。

    tearDownメソッドは、データメンバのConnectionインスタンスをすべて閉じます。

    assertOutputメソッドは、Connectionでのコマンドの実行結果をdoctestモジュールを使って比較します。


Example:

.. code-block:: python
  :linenos:

  from doctest import ELLIPSIS

  from shelldoctest.shellunittest import Connection, TestCase

  host = "localhost:22"

  class Example(TestCase):
      c1 = Connection(host)
      c2 = Connection(host)

      def test(self):
          self.assertOutput(self.c1, "pwd", "/.../...\n", ELLIPSIS)
          self.c1("cd /", None)
          self.assertOutput(self.c2, "pwd", "/.../...\n", ELLIPSIS)
          self.assertOutput(self.c1, "pwd", "/\n")


Classes
-------

.. autoclass:: shelldoctest.shellunittest.Connection

    hostには、'hostname:port'の形式でSSH接続先のサーバを指定します。
    portには、ポートを指定します。
    ':port'は省略できます。
    portのデフォルトは22です。
    usernameには、ログインするUserNameを指定します。
    デフォルトは、環境変数のUSERを取ります。
    shellには、channelにshellを開くときに送信するコマンドを指定します。
    usernameのデフォルトは、'/bin/bash -s'です。

  .. automethod:: shelldoctest.shellunittest.Connection.__call__

    commandメソッドのラッパーです。
    __call__メソッドが初めて呼び出されたときに、channelを生成してshellを開きます。

  .. automethod:: shelldoctest.shellunittest.Connection.close

    channelを閉じます。
    channelに"exit"コマンドを送信します。

  .. automethod:: shelldoctest.shellunittest.Connection.command

    channelにコマンドを送信して、そのレスポンスを受信します。
    cmdには、channelに送信するコマンドを指定します。
    responseには、送信したコマンドのレスポンスを期待するか否かのフラグを指定します。
    たとえば、'cd'コマンドの様に標準出力への出力がないコマンドを送信するときには、Falseを指定します。
    デフォルトは、Trueです。
    timeoutには、cmdに指定するコマンドを実行してからレスポンスを受信するまでの待ち時間を指定します。
    timeoutは、最終的にConnectionインスタンスのwaitメソッドに渡します。

  .. automethod:: shelldoctest.shellunittest.Connection.connect

    channelインスタンスを生成して、channelデータメンバに設定します。

  .. automethod:: shelldoctest.shellunittest.Connection.disconnect

    channelデータメンバに関連するtransportを閉じます。

  .. automethod:: shelldoctest.shellunittest.Connection.open

    channelインスタンスにshellを開きます。

  .. automethod:: shelldoctest.shellunittest.Connection.wait

    timeoutに指定された間sleepしてから、go()を返すメソッドです。
    channelにコマンドを送信してから、レスポンスを受信できる状態に処理が進むまで待つときに呼び出します。
    readyには、sleepを解除してよい状態を示すフラグを返す呼び出し可能なオブジェクトを指定します。
    bool(ready())が、Trueを返せばsleepを解除し、Falseを返せばsleepを継続します。
    goには、sleepを解除した後に呼び出す呼び出し可能なオブジェクトを指定します。
    timeoutには、sleepする時間を秒単位で指定します。
    timeout時間を経過すると、ResponseTimeout例外を送出します。
    デフォルトは、3秒です。
    timeoutは、時間的に正確ではありません。
    実際には、0.01秒間sleepしてからreadyをチェックするループを、timeout*100回繰り返します。

.. autoclass:: shelldoctest.shellunittest.TestCase

  .. automethod:: shelldoctest.shellunittest.TestCase.assertOutput

    assertOutputメソッドは、Connectionにコマンドを送り、その実行結果をdoctestモジュールを使って比較します。
    比較した結果が相違であった場合には、DocTestFailure例外を送出します。
    connectionには、データメンバのConnectionインスタンスを指定します。
    cmdには、connectionへ送信するコマンドを指定します。
    wantには、期待するレスポンスを指定します。
    optionflagsには、doctestのオプションフラグを指定します。
    optionflagsは、現在のところオプションフラグの合計を数値で指定します。
    timeoutには、cmdに指定するコマンドを実行してからレスポンスを受信するまでの待ち時間を秒単位で指定します。
    timeoutは、最終的にConnectionインスタンスのwaitメソッドに渡します。

  .. automethod:: shelldoctest.shellunittest.TestCase.tearDown

    データメンバのConnectionインスタンスをすべて閉じます。


Functions
---------

.. autofunction:: shelldoctest.shellunittest.make_transport

    paramikoモジュールのtransportインスタンスを生成して、返します。
    hostname、port、usernameの組み合わせごとに、transportを生成します。
    transportを開始するための時間やリソースを節約するために再利用して、既に生成してあるtransportインスタンスを返します。
    hostnameには、SSH接続先のサーバを指定します。
    portには、ポートを指定します。
    portのデフォルトは22です。
    usernameには、ログインするUserNameを指定します。
    usernameのデフォルトは、環境変数のUSERを取ります。

.. autofunction:: shelldoctest.shellunittest.connect

    渡されたtransportに対してchannelを生成して、返します。
    transportには、make_transportで生成したtransportインスタンスを指定します。
    1つのtransportに対して複数のchannelを開くことができます。
    channelに送ったコマンドの実行プロセスが終了すると、channelも終了状態になります。

.. autofunction:: shelldoctest.shellunittest.disconnect

    渡されたtransportを閉じます。
    transportには、make_transportで生成したtransportインスタンスを指定します。


Exceptions
----------

.. autoclass:: shelldoctest.shellunittest.ResponseTimeout

.. autoclass:: shelldoctest.shellunittest.DocTestFailure


----

.. automodule:: shelldoctest.shellunittest

