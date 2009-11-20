#!/usr/bin/env python
"""
"""

from binascii import hexlify
import doctest
import inspect
import os
import socket
import sys
import time
import traceback
import unittest

import paramiko

TRANSPORT_POOL = dict()

class ResponseTimeout(Exception):
    def __init__(self, info=None):
        self.info = info or dict()

    def __str__(self):
        return "Responnse timeout: %(connection)s '%(cmd)s'" % self.info

def make_transport(hostname, port, username):
    global TRANSPORT_POOL
    pool_name = (hostname, port, username)
    if pool_name in TRANSPORT_POOL:
        return TRANSPORT_POOL[pool_name]
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((hostname, port))
    except Exception, e:
        print '*** Connect failed:', e
        traceback.print_exc()
        sys.exit(1)
    transport = paramiko.Transport(sock)
    try:
        transport.start_client()
    except paramiko.SSHException:
        print '*** SSH negotiation failed.'
        sys.exit(1)
    agent_keys = paramiko.Agent().get_keys()
    if len(agent_keys) == 0:
        return
    for key in agent_keys:
        print 'Trying ssh-agent key %s' % hexlify(key.get_fingerprint()),
        try:
            transport.auth_publickey(username, key)
            print '... success!'
        except paramiko.SSHException, e:
            print '... nope.', e
    TRANSPORT_POOL[pool_name] = transport
    return transport

def connect(transport):
    try:
        channel = transport.open_session()
    except:
        transport.close()
    channel.settimeout(10)
    return channel

def disconnect(transport):
    transport.close()

class Connection(object):
    channel = None

    def __init__(self, host, username=None, shell=None):
        if ":" in host:
            hostname, port = host.split(":")
            port = int(port)
        else:
            hostname, port = host, 22
        self.hostname = hostname
        self.port = port
        self.username = username or os.environ["USER"]
        self.shell = shell or '/bin/bash -s'

    def __call__(self, *argv, **kwargv):
        if not self.channel:
            self.connect()
            self.open()
        return self.command(*argv, **kwargv)

    def connect(self):
        self.channel = connect(
            make_transport(self.hostname, self.port, self.username))

    def disconnect(self):
        if not self.channel:
            return
        disconnect(self.channel.get_transport())
        self.channel = None

    def open(self):
        self.channel.exec_command(self.shell)

    def close(self):
        if not self.channel:
            return
        self.command("exit", None)
        self.channel = None

    def wait(self, ready, go, timeout=None):
        if timeout == None:
            timeout = 3 #default 3 sec
        if timeout:
            timeout = timeout * 100
        else:
            timeout = 1
        for i in xrange(int(timeout)):
            if ready():
                break
            time.sleep(0.01)
        else:
            invoker = sys._getframe(1).f_locals
            invoker = dict(
                connection = invoker["self"],
                cmd = invoker["cmd"].replace("\n", r"\n"))
            raise ResponseTimeout, invoker
        return go()

    def command(self, cmd, response=True, timeout=None):
        if not cmd.endswith("\n"):
            cmd = "%(cmd)s\n" % vars()
        self.wait(
            self.channel.send_ready,
            lambda: self.channel.send(cmd),
        )
        if response in [False, None]:
            return
        result = None
        try:
            result = self.wait(
                self.channel.recv_ready,
                lambda: self.channel.recv(1024),
                timeout,
            )
        except socket.timeout:
            pass
        return result

    def __str__(self):
        hostname = self.hostname
        port = self.port
        username = self.username
        shell = self.shell
        format = "%(username)s@%(hostname)s:%(port)s %% %(shell)s"
        return format % vars()

class DocTestFailure(AssertionError):
    def __init__(self, example, got, optionflags):
        self.example = example
        self.got = got
        self.optionflags = optionflags

    def __str__(self):
        msg = """ %(connection)s
Failed example:
    %(cmd)s
%(diff)s
"""
        checker = doctest.OutputChecker()
        connection = self.example.connection
        cmd = self.example.cmd
        diff = checker.output_difference(self.example, self.got, self.optionflags)
        return msg % vars()

class TestCase(unittest.TestCase):
    def tearDown(self):
        for _name, attr in inspect.getmembers(self):
            if isinstance(attr, Connection):
                attr.close()

    def assertOutput(self, connection, cmd, want, optionflags=None, timeout=None):
        optionflags = optionflags or 0
        got = connection(cmd, timeout=timeout)
        checker = doctest.OutputChecker()
        result = checker.check_output(want, got, optionflags)
        if result == True:
            return
        _connection, _cmd, _want = connection, cmd, want
        class Example(object):
            connection = _connection
            cmd = _cmd
            want = _want
        raise DocTestFailure, (Example, got, optionflags)

