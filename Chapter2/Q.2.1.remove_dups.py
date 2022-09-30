from LinkedList import LinkedList
# Question: Write code to remove duplicates from an unsorted linked list. 

# Clarification: What are we given? Head? Tail + head?
#                Is it double linked list ?
#                Do we have to do it in place?
#                Which copy of a single element should I keep?

# Plan: Brute force -> For each node, each if it has duplicates remove it.
#                   -> Takes O(n^2) time. 

# Hash map: Store each element in hash map. If it is seen again, take the pointer to
# the next one until hit tail.
# Time complexity O(N), Space O(N)

def remove_dups(myList):

    if myList.head == None:
        return myList
    
    elif myList.next == None:
        return myList
    
    elements = {}

    ptr = myList.head
    elements[ptr.value] =1

    while ptr.next != None:
        if ptr.next.value not in elements:
            elements[ptr.value] = 1
            ptr = ptr.next
        else:
            ptr.next = ptr.next.next

    return myList

# FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?

# Plan: Brute force O(N^2) time O(1) space

def remove_dups_followup(myList):

    if myList.head == None:
        return myList
    
    elif myList.next == None:
        return myList
    
    first = myList.head

    while first != None:
        second = first.next
        prev = first
        while second != None:
            if first.value == second.value:
                prev.next= second.next
            else:
                prev = prev.next
            second = second.next
        first = first.next


