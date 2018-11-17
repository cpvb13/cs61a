HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    #>>> street(1488)
    #51
    return w(inter) - avenue(inter)

def avenue(inter):
    #>>> avenue(1438)
    #7
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7) #1438
    >>> ess_a_bagel = intersection(51, 3) #1488
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    return abs(street(a)-street(b))+abs(avenue(a)-avenue(b))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    return [int(s[i]**0.5) for i in range(len(s)) if (s[i]**0.5)==round(s[i]**0.5)]

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    def g_helper(x):
        if x <= 3:
            return x
        return g(x - 1) + 2 * g(x - 2) + 3 * g(x - 3)
    return g_helper(n)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4) #1*3+ 2*2 + 3*1 
    10
    >>> g_iter(5) #1*3+ 2*2 + 3*1   + 2*3  + 3*2
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True

    G(n) = [G(n - 1)] +     [2 * G(n - 2)]    +     [3 * G(n - 3)],  if n > 3

    """
    if n <= 3:
        return n

    x = 0
    a,b,c = 3,2,1
    while x < n-3: #anything above 3 should iterate and update to g(n)
        a,b,c = a+2*b+3*c,a,b
        x+=1
        #print(a,b,c)
    return a



def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """

    def check_change(coin,amount):
        if amount<1: 
            return 0
        elif amount == 1: #only one way once amount is 1
            return 1
        return check_change(coin,amount-coin) + check_change(2*coin,amount-coin) #double coin value
    return check_change(1,amount) #start with a 1cent coin



def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2 
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3

    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    

    def how_to_move(disks,start,end,helper):
        if disks == 1:
            return print_move(start, end)            
        

        elif disks ==2:
            print_move(start, helper)
            print_move(start, end)
            print_move(helper, end)

        if disks%2==0 and disks != 2: #even
            flip = True

            for n in range(disks//2):
                if flip:
                    a,b,c = print_move(start, helper),print_move(start, end),print_move(helper, end)
                else:
                    a,b,c = print_move(start, end),print_move(end, start),print_move(end, helper)
                flip = not flip
            print_move(start, end)

        

        if disks%2==1: #odd
            flip = True
            d = disks
            while d>=2:
                if flip:
                    a,b,c = print_move(start, end),print_move(start, helper),print_move(end, helper)
                else:
                    a,b,c = print_move(start, end),print_move(helper, start),print_move(helper, end)
                flip = not flip
                d-=1
            return print_move(start, end)
        else:
            return None
            #pattern is alternate between topmost smallest/biggest piece

    return how_to_move(n,start,end,6-start-end)
"""
This is how i worked through the problem...
Look For Pattern! s = start, e = end, h = helper ... s+e+h = 6
    >>> move_stack(1, 1, 3) n is odd
    Move the top disk from rod 1 to rod 3 -se

    >>> move_stack(2, 1, 3) n is even
    Move the top disk from rod 1 to rod 2 -sh
    Move the top disk from rod 1 to rod 3 -se
    Move the top disk from rod 2 to rod 3 -he

    >>> move_stack(3, 1, 3) n is odd
    Move the top disk from rod 1 to rod 3- se
    Move the top disk from rod 1 to rod 2- sh 
    Move the top disk from rod 3 to rod 2- eh
    Move the top disk from rod 1 to rod 3- se
    Move the top disk from rod 2 to rod 1- hs
    Move the top disk from rod 2 to rod 3- he
    Move the top disk from rod 1 to rod 3- se

    """
###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
