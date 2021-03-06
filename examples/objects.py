from numba import double, autojit

class MyClass(object):
    def mymethod(self, arg):
        return arg * 2
    
@autojit(locals=dict(mydouble=double)) # specify types for local variables
def call_method(obj):
    print obj.mymethod("hello")   # object result
    mydouble = obj.mymethod(10.2) # native double
    print mydouble * 2            # native multiplication
    
call_method(MyClass())
