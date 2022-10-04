class LinkedList:
    def __init__(self, all_nodes):
        self.firstPointer = 0
        self.endPointer = int
        self.allNodes = all_nodes


    def add_node(self, new_node):
        n = input("Where is your number?")
        #find where it needs to go
        #given temp value
        if n < 1:
            self.allNodes[n].linknodes(self.allNodes(n + 1))

        else:
            self.allNodes[n].linknodes(self.allNodes(n - 1))
            self.allNodes[n].linknodes(self.allNodes(n + 1))



class Nodes:
    def __init__(self, name):
        self.links = []
        self.name = name

    def link_nodes(self, linking_node):
        self.links += linking_node
        linking_node.linknodes(self)
