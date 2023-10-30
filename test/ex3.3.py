def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch),'branches must be tree'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left,right = fib_tree(n-2),fib_tree(n-1)
        return tree(label(left)+label(right),[left,right])

def is_leaf(tree):
    return not branches(tree)

def count_leaves(t):
    """count the leaves of tree T"""
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])
    
def leaves(tree):
    """return a list containing the leaf labels of tree
    >>> leaves(fib_tree(5))
    [1,0,1,0,1,1,0,1]
    """
    if is_leaf(tree):
        return[label[tree]]
    else:
        return sum(leaves(b) for b in branches(tree))
    
def print_tree(t,indent=0):
    print('  '*indent + str(label(t)))
    for b in branches(t):
        print_tree(b,indent+1)
        
    


    