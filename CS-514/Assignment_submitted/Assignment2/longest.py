class Depth:
    def __init(n):
        n.l = 0 

def longest(tree):
    length = Depth()
    return _longest(tree, length)
         
 
def _longest(tree, length):
 
    leftl = Depth()
    rightl = Depth()
    if tree == []:
        length.l = 0
        return 0
 
    left_len = _longest(tree[0], leftl)
    right_len = _longest(tree[2], rightl)
 
 
    length.l = max(leftl.l, rightl.l) + 1
 
    return max(leftl.l + rightl.l , max(left_len, right_len))
 

if __name__ == '__main__':
    tree = ([[], 1, []])
    # tree = [[], 1, []]
    # tree = [[[], 1, []], 2, [[], 3, []]]
    print(tree)    
    print(longest(tree))
    tree = ([[[], 1, []], 2, [[], 3, []]])
    print(tree)    
    print(longest(tree))
    tree = [[[], 1, []], 2, [[], 3, []]]
    print(tree)    
    print(longest(tree))
    tree = [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]
    print(tree)    
    print(longest(tree))