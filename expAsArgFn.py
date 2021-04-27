def do_twice(f, value):
    f(value)
    f(value)

def print_twice(bruce):
    print(bruce)
    print(bruce)


do_twice(print_twice, 'spam')

