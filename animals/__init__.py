#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pkgutil
import animals
import inspect
import importlib

package = animals
print globals()['package']
print __name__
base_class = animals.animal.Animal
for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
    print "Found submodule %s (is a package: %s)" % (modname, ispkg)
    module = importlib.import_module(__name__ + '.' + modname)
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and isinstance(obj, base_class):
            print name
