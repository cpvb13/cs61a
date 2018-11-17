""" Lab 07: Recursive Objects """
def gen_inf(lst):
    while True:
        for elem in lst:
            yield elem
    
# Q4
def link_to_list(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    if link:
        link_list = [link.first] 

        while link.rest:
            link = link.rest
            link_list += [link.first]
        return link_list
    else:
        return []
    #return [link.first] + link_to_list(link.rest)

# Q5
def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    result = Link.empty
    while n:
        result = Link(n%10,result)
        n = n//10
    return result

# Q6
def cumulative_sum(t):
    """Mutates t so that each node's label becomes the sum of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    cumulative_b = [cumulative_sum(b) for b in t.branches]
    sub_sum = sum([b.label for b in t.branches])
    t.label += sub_sum
    # for b in t.branches:
    #     cumulative_sum(b)
    # t.label = sum([b.label for b in t.branches]) + t.label


# Q7
def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    #first check the length of branches aka #
    #print( len(t.branches))      

    def bst_max(t):
        if t.is_leaf():
            return t.label
        elif len(t.branches) == 2:
            return bst_max(t.branches[1])
        else:
            return bst_max(t.branches[0])

    def bst_min(t):
        if t.is_leaf():
            return t.label
        return bst_max(t.branches[0])
    

    if t.is_leaf():
        return True
    
    elif len(t.branches) == 2:
        if t.label < bst_min(t):
            return False
        if t.label > bst_max(t):
            return False
        
    bst_list = [is_bst(branch) for branch in t.branches] 
    return False not in bst_list

###Solution
    # def bst_min(t):
    #     """Returns the min of t, if t has the structure of a valid BST."""
    #     if t.is_leaf():
    #         return t.label
    #     return min(t.label, bst_min(t.branches[0]))

    # def bst_max(t):
    #     """Returns the max of t, if t has the structure of a valid BST."""
    #     if t.is_leaf():
    #         return t.label
    #     return max(t.label, bst_max(t.branches[-1]))

    # if t.is_leaf():
    #     return True
    # if len(t.branches) == 1:
    #     c = t.branches[0]
    #     return is_bst(c) and (bst_max(c) <= t.label or bst_min(c) > t.label)
    # elif len(t.branches) == 2:
    #     c1, c2 = t.branches
    #     valid_branches = is_bst(c1) and is_bst(c2)
    #     return valid_branches and bst_max(c1) <= t.label and bst_min(c2) > t.label
    # else:
    #     return False




# Q8

def in_order_traversal(t):
    """
    Generator function that generates an "in-order" traversal, in which we 
    yield the value of every node in order from left to right, assuming that each node has either 0 or 2 branches.

    For example, take the following tree t:
            1
        2       3
    4     5
         6  7

    We have the in-order-traversal 4, 2, 6, 5, 7, 1, 3

    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5, [Tree(6), Tree(7)])]), Tree(3)])
    >>> list(in_order_traversal(t))
    [4, 2, 6, 5, 7, 1, 3]
    """

    
    if t.is_leaf():
        yield t.label
    else:
        node,left,right = t,t.branches[0],t.branches[1]
        yield from in_order_traversal(left)
        yield node.label
        yield from in_order_traversal(right)

def contents(t):
    if t is BTree.empty:
        return []
    else:
        return contents(t.left) + [t.label] + contents(t.right)
# Linked List Class
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.second
    3
    >>> s.first = 5
    >>> s.second = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# Tree Class
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """
    m = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return lnk
        m *= lnk.first    
    return Link(m,multiply_lnks([x.rest for x in lst_of_lnks]))


# a = Link(2, Link(3, Link(5)))
# b = Link(6, Link(4, Link(2)))
# c = Link(4, Link(1, Link(0, Link(2))))

def remove_duplicates(lnk):
    # while lnk is not Link.empty and lnk.rest is not Link.empty:
    #     if link.first == link.rest.first:
    #         lnk.rest = lnk.rest.rest
    #     else:
    #         lnk = lnk.rest

    n = list()
    while lnk.rest != Link.empty:
        if lnk.first not in n:
            n.append(lnk.first)
            lnk = lnk.rest 
        else:
            lnk.first = lnk.rest


def quick_sort(lst):
    if len(lst)<=1:
        return lst
    pivot = lst[0]
    less = [x for x in lst if x<pivot]
    more = [x for x in lst if x>pivot]
    return quick_sort(less)+[pivot]+quick_sort(more)

# t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
# t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
# t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
# t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
# t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
# t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
# t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])    
# print(t1)
# print()

# print(t2)
# print()

# print(t3)
# print()

# print(t4)
# print()

# print(t5)
# print()

# print(t6)
# print()

# print(t7)
# print()


