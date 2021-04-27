from __future__ import print_function, division

def do_twice(f, value):
    f(value)
    f(value)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f, value):
    do_twice(f, value)
    do_twice(f,value)

  

do_four(print,  "spam")




