from LinkedList import LinkedList

# Question: Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

# Clarification: If size of list smaller than k? What if k =1, k=0?
# Plan: Start 2 pointers pointing the first element. 
# Move the first k steps.
# Then start the second. When first ptr hit the tail, return the value of second ptr.
# Time O(N), space O(1)


def return_kth_to_last(myList, k):
    
    step = 0
    first = myList.head
    second = first

    while step < k:
        if first == None:
            return None
        first = first.next
        step+=1
    
    while first != None:
        second = second.next
        first = first.next
    
    return second.value



