# Binary tree operations
from collections import deque

# TreeNode definition
class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

# Tree construction from an iterable
# Traversal in Level order to construct nodes
class BinaryTree:
    def __init__(self, vals):
        if not vals:
            self.first = Node()
        else:
            vals  = deque(vals)
            popval = vals.popleft()
            self.first = Node(None if popval=="null" else popval)
            dq = deque()
            dq.append(self.first)
            while True:
                curr = dq.popleft()
                if len(vals):
                    popval = vals.popleft()
                    curr.left = None if popval=="null" else Node(popval)
                    if curr.left:
                        dq.append(curr.left)
                else:
                    break
                if len(vals):
                    popval = vals.popleft()
                    curr.right = None if popval=="null" else Node(popval)
                    if curr.right:
                        dq.append(curr.right)
                else:
                    break
        
    def getRoot(self):
        return self.first

# Traverses the tree and prints all paths (Root -> Leaf)
def printPaths(root, path=[]):
    if not root:
        return
    path.append(root.val)
    if root.left is None and root.right is None:
        print(path)
    else:
        if root.left is not None:
            printPaths(root.left, path)
        if root.right is not None:
            printPaths(root.right, path)
    path.pop()
    return

# Traverses the tree (Root -> Leaf) and prints all paths whose sum is a given value
def hasSum(root, sum_, path=[]):
    if not root:
        return
    path.append(root.val)
    if root.left is None and root.right is None and sum_==root.val:
        print(path)
    else:
        sum_ -= root.val
        if root.left is not None:
            hasSum(root.left, sum_, path)
        if root.right is not None:
            hasSum(root.right, sum_, path)
    path.pop()
    return

def addPaths(root,  path=[], nums=[]):
    if not root:
        return
    path.append(root.val)
    if not (root.left or root.right):
        # print(path)
        nums.append("".join(map(str, path)))
    else:
        if root.left:
            addPaths(root.left, path, nums)
        if root.right:
            addPaths(root.right, path, nums)
    path.pop()


# Driver code
if __name__ == "__main__":
    # arr = [0,1,2,3,4,5,6,7,7,"null",9]
    arr = [5,4,8,11,"null",13,4,7,2,"null","null",5,1]
    first = BinaryTree(arr).getRoot()
    # print(first.val)
    print("------All paths--------")
    printPaths(first, [])
    print("-----Does path contain sum---------")
    hasSum(first, 22, [])
    print("------Calculate sum of path string--------")
    nums = []
    addPaths(first, [], nums)
    print(sum(map(int, nums)))
    print("--------------")
