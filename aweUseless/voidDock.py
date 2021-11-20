#!/usr/bin/env python3
#via: https://zhuanlan.zhihu.com/p/142514129

class VoidDuck:
    """a void, versatile, useless and quiet duck, called in any way, return nothing, raise nothing"""
    def __init__(self, *args, **kwargs):
        pass

    def __getattr__(self, item):
        return self
    
    def __call__(self, *args, **kwargs):
        return self

    def __bool__(self):
        return False
