#!/usr/bin/env python
'''
Shell Doctest module.

:Copyright: (c) 2009, the Shell Doctest Team All rights reserved.
:license: BSD, see LICENSE for more details.

def _print(arg):
    print(arg)

def test():
    """Print `TEST`
    """
    _print("TEST")

def echo(msg=None):
    """Print <message>, Default `None`
    """
    _print(msg)

if __name__ == "__main__":
    import base_app
    base_app.start_app(**vars())
'''

import commands
import inspect
import sys

from commandlineapp import CommandLineApp

class BaseApp(CommandLineApp):
    def __init__(self, *argv, **kwargv):
        if sys.argv[0].endswith('ipython'):
            sys.argv = sys.argv[1:]
            self._app_name = sys.argv[0]
            kwargv.update({'command_line_options': sys.argv[1:]})
        super(BaseApp, self).__init__(*argv, **kwargv)

    def main(self, *argv):
        sub_command = dict(enumerate(argv)).get(0, "main")
        try:
            getattr(self, "command_%(sub_command)s" % vars())(*(argv[1:]))
        except AttributeError:
            if self.debugging:
                raise
            print "ERROR:  sub-command %(sub_command)s not recognized" % vars()
            self.command_help()
        sys.exit(0)

    def command_help(self):
        """Displays sub-command help message.
        """
        prefix = "command_"
        methods = inspect.getmembers(self.__class__, inspect.ismethod)
        print "%s [<options>] sub-command [argv...]\n" % self._app_name
        print "SUB-COMMANDS:\n"
        for method_name, method in methods:
            if method_name.startswith(prefix):
                print " "*4, method_name[len(prefix):],
                for arg in method.im_func.func_code.co_varnames[1:method.im_func.func_code.co_argcount]:
                    if not arg.startswith("_"):
                        format = "<%s>"
                        if method.im_func.func_defaults and method.im_func.func_defaults[0]:
                            format = "[<%s=%s>]" % ("%s", method.im_func.func_defaults[0])
                        print format % arg,
                else:
                    print ""
                print " "*8, method.__doc__ or ""

    def command_main(self):
        raise NotImplementedError

    def option_handler_help(self):
        super(BaseApp, self).option_handler_help()
        self.command_help()

    def run(self):
        try:
            super(BaseApp, self).run()
        except SystemExit, e:
            if str(e) not in ["", "0"]: raise

def create_method(attribute):
    def method(self, *argv, **kwargv):
        if attribute.func_code.co_varnames[0] == 'self':
            argv = (self,) + argv
        return attribute(*argv, **kwargv)
    method.__name__ = "command_%s" % attribute.__name__
    method.__doc__ = attribute.__doc__
    return method

def set_method(cls, attribute):
    method = create_method(attribute)
    setattr(cls, method.__name__, method)
    return cls

def update_app(app, *attributes):
    for attribute in attributes:
        app = set_method(app, attribute)
    return app

def create_app(*attributes):
    attr_dict = dict((m.__name__, m) for m in map(create_method, attributes))
    return type('App', (BaseApp,), attr_dict)

def start_app(*argv, **kwargv):
    if not argv and not kwargv:
        kwargv = sys._getframe(1).f_globals
    if argv:
        argv = [i for i in argv if not i.__name__.startswith("_")]
    app = create_app(*argv)
    for k,v in kwargv.items():
        try:
            if v.__module__ == "__main__" and not k.startswith("_"):
                v.__name__ = k
                app = update_app(app, v)
        except AttributeError:
            pass
    if "main" not in [a.__name__ for a in argv] + kwargv.keys():
        app.command_main = app.command_help
    app().run()

if __name__ == "__main__":
    BaseApp().run()

