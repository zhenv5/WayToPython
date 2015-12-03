class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def search(root,key):

    if not root:
        return False
    if root.value == key:
        return True
    if key < root.value:
        return search(root.left,key)
    else:
        return search(root.right,key)

def add(root,key):

    if not root:
        return BST(key)

    if key < root.value:
        if root.left == None:
            root.left = BST(key)
        else:
            add(root.left,key)
    elif key > root.value:
        if root.right == None:
            root.right = BST(key)
        else:
            add(root.right,key)
    else:
        print "cannot add a duplicate value"

def minValueNodeInRight(root):
	if not root:
		return None
	cur = root
	while not cur.left:
		cur = cur.left
	return cur

def delete(root,key):
    if not root:
    	return None
    if key < root.value:
    	root.left = delete(root.left,key)
    elif key > root.value:
    	root.right = delete(root.right,key)
    else:
    	if not root.left:
    		return root.right
    	if not root.right:
    		return root.left
    	
    	temp = minValueNodeInRight(root.right)

    	root.value = temp.value

    	root.right = delete(root.right,temp.value)

    return root

def findCommonNode(root1,root2):

    if not root1 or not root2:
        return False
    if root1.value == root2.value:
        return True
    elif root1.value > root2.value:
        return findCommonNode(root1.left,root2) or findCommonNode(root1,root2.right)
    else:
        return findCommonNode(root1.right,root2) or findCommonNode(root1,root2.left)

def printBST(root):

    if not root:
        return
    printBST(root.left)
    print root.value
    printBST(root.right)



root = BST(1)

add(root,0)
add(root,3)
add(root,4)
add(root,5)
add(root,10)

root1 = BST(4)
add(root1,3)
add(root1,2)
add(root1,6)
add(root1,5)
add(root1,10)



printBST(root)
delete(root,0)
printBST(root)
#print findCommonNode(root,root1)

#print search(root,2)
#printBST(root)
