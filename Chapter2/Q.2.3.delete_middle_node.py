from LinkedList import LinkedList

# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but 
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to 
# that node. 
#EXAMPLE 
#lnput:the node c from the linked list a->b->c->d->e->f 
#Result: nothing is returned, but the new linked list looks like a ->b->d->e->f

# Clarification: We are given a pointer to that node? Or a value?

# Plan: copy the data from the next node over to the current node, and then to delete the 
# next node. 

def delete_middle(middleNode):

    if middleNode == None or middleNode.next == None:
        return False

    nextNode = middleNode.next
    middleNode.value = nextNode.value
    middleNode.next = nextNode.next.next
    return True

# O(1) time and space

# Note that this problem cannot be solved if the node to be deleted is the last node in the linked list. 
# You could, for example, consider marking the node as dummy
    

