#!/usr/bin/env python3

import sys
import importlib
import doctest

def test_module(doctest_name, module_name, verbose=False):

    if module_name.endswith('.py'):
        module_name, dot, ext = module_name.rpartition('.')
    module = importlib.import_module(module_name)

    res = doctest.testfile(doctest_name,
                           globs=module.__dict__,
                           verbose=verbose,
                           optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    if res.failed == 0:
        print(module_name, 'OK')
    else:
        print('{0} attempted: {1.attempted} failed: {1.failed}'.format(module_name, res))


if __name__ == '__main__':

    args = sys.argv[:]
    if '-v' in args:
        args.remove('-v')
        verbose = True
    else:
        verbose = False

    if len(args) == 3:
        doctest_name, module_name = args[1:]
    else:
        print('Usage: deck_runner.py <doctest_filename> <module_filename> [-v]')
        sys.exit()

    test_module(doctest_name, module_name, verbose)
