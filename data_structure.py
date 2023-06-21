#Karla Martinez 
#CS302 Karla Fant 

from reservation import * 
from restaraunt import * 
from camping import * 
from hotel import * 

#File holding the binary searchg tree 
#node will hold the object being passed in 
#tree will organize by venue names

#the node that will be used in the tree 
#data is the object that is being passed in 
class node: 
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None


class tree: 
    def __init__(self):
        self.root = None 
    
    #will insert the object into a node and place it into the tree 
    #this is the wrapper 
    def insert(self, ressy):
        object = ressy
        if(self.root == None):
            self.root = node(object)
            return 
        return self.insert_2(self.root, object)
    
    #main insert function working with the object handed over in 
    #the wrapper 
    def insert_2(self, root, object):
        if(root == None):
            return node(object)
        name = object.get_venue()
        if(name < root.data.get_venue()):
        #if(object < root.data):
            root.left = self.insert_2(root.left, object)
        if(name > root.data.get_venue()):
        #if(object > root.data):
            root.right = self.insert_2(root.right, object)
        if(name == root.data.get_venue()):
            root.right = self.insert_2(root.right, object)
        return root
    
    #will display the tree
    #wrapper for dipslay 
    def display_(self):
        if(self.root == None):
            print("empty")
            return 0
        self.display_2(self.root)
        return 1
    
    #main displkay function working with the "private"
    def display_2(self, root):
        if(root == None):
            return 0
        self.display_2(root.left)
        root.data.display()
        self.display_2(root.right)
        return 0

    #to remove a node in the tree 
    #will hole the rest of the tree so it isnt "lost"
    def removing(self, node):
        current = node 
        while(current.left != None):
            current = current.left 
        return current 
    
    #wrapper to delete the node 
    def delete(self, venue_name):
        if(self.root == None ):
            return 
        self.root = self.delete_(self.root, venue_name)

    #main function doing the actual deleting 
    def delete_(self, root, venue_name):
        if(root == None):
            return root 
        if(venue_name < root.data.get_venue()):
            root.left = self.delete_(root.left, venue_name)
        
        if(venue_name > root.data.get_venue()):
            root.right = self.delete_(root.right, venue_name)

        if(root.left == None):
            return root.right
        if(root.right == None):
            return root.left 
        
        root.data = self.removing(root.right).data 
        root.right = self.delete_(root.right, root.data.get_venue())
        return root 
    
    def retrieve(self, venue_name):
        return self.retrieve_(self.root, venue_name)
    
    def retrieve_(self, root, venue_name):
        if(root == None):
            print("Not found")
            return None
        if(venue_name < root.data.get_venue()):
            return self.retrieve_(root.left, venue_name)
        if(venue_name > root.data.get_venue()):
            return self.retrieve_(root.right, venue_name)
        return root











