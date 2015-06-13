__author__ = 'bhavinpatel'


from pprint import pprint

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
        return str(depth)


class CourseTree(Tree):

    def insert(self , course = None , preReq=None):

        if int(self._root.data) == int(preReq):
            return True # never ends

        if preReq is not None:
            self.findAndAdd( find=course, right= Node( data = preReq) , current= self._root )


    def findAndAdd(self, find=None, right=None, left=None , current=None):

        if current is not None and find is not None:

            self._current_node = current

            #print "\n current " + str(self._current_node.data)
            #print "\n find " + str(find)

            if int(self._current_node.data) == int(find) :
                #print "\n adding data"
                if right is not None:
                    self._current_node._right = right
                    #print "\n adding right node"
                if left is not None:
                    self._current_node._left  = left
                    #print "\n adding left node"

            self.findAndAdd( find = find , right = right , left = left , current = self._current_node._left)
            self.findAndAdd( find = find , right = right , left = left , current = self._current_node._right)


class Course:

    def __init__(self,inputData=None):

        self.testCases = {}

        if inputData is None:
            self.parseRawInput()
        #self._inputData = "".join(inputData)


        #self.parseInput()

    def parseInput(self):

        lines = self._inputData.split("\n")
        line_no = 0
        self.NoOfTestCases = int(lines[line_no])

        for testNo in range( self.NoOfTestCases ):
            line_no += 1
            ( N , R ) = lines[line_no].split()
            self.testCases[testNo] = {  "NoOfCourses" : int(N),
                                        "NoOfPreReq"  : int(R) }
            line_no += 1
            ( U , V ) = lines[line_no].split()
            self.testCases[testNo]["courseTree"] = CourseTree(  Node( data = int(U) ) )

            r = self.testCases[testNo]["courseTree"].insert( course = int(U) , preReq= int(V) )

            if r is True:
                self.testCases[testNo]["result"] = "Never Ends"



            #print ("\n *  %s %s r(%s)") %( str(U), str(V), str(r))

            for preReqNo in range( int(R) - 1):
                line_no += 1
                (U , V) = lines[ line_no ].split()
                #print ("\n i(%s) %s %s") %(  str(line_no),str(U), str(V))

                r = self.testCases[testNo]["courseTree"].insert( course= int(U), preReq=int(V))
                if r is True:
                    self.testCases[testNo]["result"] = "Never Ends"


    def parseRawInput(self):

        tc = raw_input()
        self.NoOfTestCases = int(tc)

        for testNo in range( self.NoOfTestCases ):
            l = raw_input()
            ( N , R ) = l.split()
            self.testCases[testNo] = {  "NoOfCourses" : int(N),
                                        "NoOfPreReq"  : int(R) }
            l = raw_input()
            ( U , V ) = l.split()
            self.testCases[testNo]["courseTree"] = CourseTree(  Node( data = int(U) ) )

            r = self.testCases[testNo]["courseTree"].insert( course = int(U) , preReq= int(V) )

            if r is True:
                self.testCases[testNo]["result"] = "Never Ends"

            for preReqNo in range( int(R) - 1):
                l = raw_input()
                (U , V) = l.split()

                r = self.testCases[testNo]["courseTree"].insert( course= int(U), preReq=int(V))
                if r is True:
                    self.testCases[testNo]["result"] = "Never Ends"



    def showSchedule(self):
        for testNo in range ( self.NoOfTestCases):
            # self.testCases[testNo]["courseTree"].printRightTreeFirst( self.testCases[testNo]["courseTree"]._root )
            if self.testCases[testNo].has_key("result"):
                print "Case %s: %s" %( str( testNo +1 ) , str( self.testCases[testNo]["result"]) )
            else :
                print "Case %s: %s semester(s)" %( str( testNo +1 ) , str(self.testCases[testNo]["courseTree"].findDepth() ) )


if __name__ == "__main__":

    c = Course()
    c.showSchedule()