# 22200849

import importlib

rotateR = getattr(importlib.import_module("1"), "rotateR")


def rotateR2(s):
    return rotateR(rotateR(s))


print(rotateR2("Thor"))
