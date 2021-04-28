from __future__ import print_function, division

# 2 rows and 2 columns

def top_bottom():
    print('+', end=" ")
    print ("- "*4, end=" ")
    print("+", end=" ")
    print ("- "*4, end=" ")
    print("+")

           
def side():
    print("|" + (" "*10) + "|", end=" ")
    print((" "*9) + "|")
    
def do_four(f):
    f()
    f()
    f()
    f()

def draw_grid(): 
    top_bottom()
    do_four(side)
    top_bottom()
    do_four(side)
    top_bottom()

draw_grid();
print("--------------------------")
print()

#for 4 rows and columns:
## Folling book example for 4 

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def beam():
    print("+ - - - - ", end=" ")

def print_beams():
    do_four(beam)
    print("+")

def post():
    print("|         ", end=" ")

def print_posts():
    do_four(post)
    print("|")

def do_row():
    print_beams()
    do_four(print_posts)


def do_grid():
    do_twice(do_row)
    print_beams()

do_grid()


    