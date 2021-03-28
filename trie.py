
class Node:

    def __init__(self):
    	# A simple node can have up to 4 neighbours
        self.neighbours = {}
        self.last = False

class Trie:

    def __init__(self):
        self.root = Node()

    #Receive a word at add it to its structure
    def add_word(self, word):

        root_node = self.root
        for character in word:
            if character not in root_node.neighbours:
                root_node.neighbours[character] = Node()

            root_node = root_node.neighbours[character]
        root_node.last = True
