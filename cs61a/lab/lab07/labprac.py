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
    if len(t.branches)>2:
        return False
    elif len(t.branches) == 0:
        return True
    
    def bst_left(b,t_max,labels):
        #print(b,t_max,)
        if b.branches[0].label > t_max:
        	return False
        else:
        	return True

    def bst_right(b,t_min,labels):
       	if b.branches[0].label < t_min:
       		return False
       	else:
       		return True

    for b in t.branches: 
        # if len(b.branches)>2: #kinda repeating base case...
        #     return False    
        labels = [b.label] #parent node
        #print(isinstance(b.branches[0],Tree),'in')
        labels.extend([b_.label for b_ in b.branches]) #add child node(s)
        #print('l',labels)
        
        if len(b.branches) == 2:
            if b.branches[0].label != min(labels):
            #print('min')
                return False  
            if b.branches[1].label != max(labels):
                return False
            #print(b.branches[0],'-', min(labels))              
            #print(b.branches[1],'-', max(labels))
            # if b.branches[0] == [] and b.branches[1] == []:
            #     return True
        elif len(b.branches) == 1:   
            if b is t.branches[0]: #if its the left branch
                bst_left(b,t.label,labels)
                	
            elif b is t.branches[1]:
                bst_right(b,t.label,labels)
            else:
                return True
        return is_bst(b)
        # else:
        #     return False
