# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the 
# intersecting node. Note that the intersection is defined based on reference, not value. That is, if the 
# kth node of the first linked list is the exact same node (by reference) as the jth node of the second 
# linked list, then they are intersecting


# What if both lists are empty? Do they intersect?
# One list is empty and other is not?
# We are checking pointer locations, not the values of nodes.

# Plan: Observe that if lists intersect, the last node is same. O(N+M)

def check_intersection(l1,l2):

    cur1 = l1.head
    cur2 = l2.head

    if not (cur1 and cur2): # Assuming that we should return FALSE in these cases.
        return False


    while cur1.next:
        cur1 = cur1.next


    while cur2.next:
        cur2 = cur2.next
    
    return cur1 == cur2

# How to find the intersection point? 
# It is a single linkedlist, you cant go back from the last node.
# Plan: If the lengths of the lists are the same, traverse through them at the same time.
# If not, chop off the longer one by difference of lengths and traverse through them at the same time.

def chop_and_traverse(l1,l2,diff):

    cur1 = l1.head
    cur2 = l2.head

    while diff!=0:
        diff -=1
        cur1 = cur1.next
    
    while cur1:
        if cur1 == cur2:
            return cur1
        cur1 = cur1.next
        cur2 = cur2.next
    
    return False


def find_intersect(l1,l2):
    length1 = len(l1)
    length2 = len(l2)

    if length1 == 0 or length2 == 0:
        return False

    if length1 >= length2:
        return chop_and_traverse(l1,l2,length1-length2)
    return chop_and_traverse(l2,l1,length2-length1)
