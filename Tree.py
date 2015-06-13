__author__ = 'bhavinpatel'

class Node:

    def __init__(self, left= None,
                       right=None,
                       parent=None,
                       data=None):
        self._left     = left
        self._right    = right
        self._parent = parent
        if data is not None:
            self.data = data
        else:
            raise ValueError( "data needs value")

class Tree:

    def __init__(self, root):
        self._root = root
        self._current_node = root

    def addLeft(self , left_node):
        self._current_node._left = left_node

    def addRight(self, right_node):
        self._current_node._right = right_node

    def printRoot(self):
        print "\n Root : " + self._root.data

    def printTree(self , root):

        if root is not None:
            self.printTree( root._left)
            print root.data
            self.printTree( root._right)

    def printRightTreeFirst(self , root):

        if root is not None:
            self.printRightTreeFirst( root._right)
            print root.data
            self.printRightTreeFirst( root._left)

    def findDepth(self):
        current = self._root
        depth = 1
        while ( current._right is not None) :
            depth = depth + 1
            current = current._right
        print "Tree Depth " + str(depth)


class CourseTree(Tree):

    def insert(self , course = None , preReq=None):

        if int(self._root.data) == int(preReq):
            print "Never Ends"

        if preReq is not None:
            self.findAndAdd( find=course, right= Node( data = preReq) , current= self._root )

    def findAndAdd(self, find=None, right=None, left=None , current=None):

        if current is not None and find is not None:

            self._current_node = current

            print "\n current " + str(self._current_node.data)
            print "\n find " + str(find)

            if int(self._current_node.data) == int(find) :
                print "\n adding data"
                if right is not None:
                    self._current_node._right = right
                    print "\n adding right node"
                if left is not None:
                    self._current_node._left  = left
                    print "\n adding left node"

            self.findAndAdd( find = find , right = right , left = left , current = self._current_node._left)
            self.findAndAdd( find = find , right = right , left = left , current = self._current_node._right)



if __name__ == "__main__":

    t = Tree( Node(data='root'))
    t.printRoot()
    t.addLeft( Node(data="left"))
    t.addRight( Node(data = "right"))

    t.printTree(t._root)

    c = CourseTree (Node( data='0'))
    c.insert( course = 0 , preReq= 1)
    c.insert( course = 1 , preReq= 2)

    print "\n printing tree "
    c.printRightTreeFirst(c._root)

    c.findDepth()
