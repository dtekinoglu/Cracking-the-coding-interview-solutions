# Question: : Write code to partition a linked list around a value x, such that all nodes less than x come 
#before all nodes greater than or equal to x. If x is contained within the list the values of x only need 
#to be after the elements less than x (see below). The partition element x can appear anywhere in the 
#"right partition"; it does not need to appear between the left and right partitions. 


#EXAMPLE 
#Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5] 
#Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

# Clarification:
# - What is the input? Head and x?
# - What if empty linkedlist? Linkedlist with 1 element?
# - Am I allowed to use additional data structure? Or in-place?

# Observation: x's must be in the right partition

#Plan : Two pointers, 1 pointing the first element of left partition
#                     1 pointing the first element of right partition
#                     Create left half and right half
#                     Create a pointer from last element of left half to last element of right half

# O(N) time, O(1) space

def partition(myList, x):

    if myList.head == None or myList.head.next == None:
        return myList.head

    left = myList.head
    right = myList.head

    while left != None:
        if left.value >= x:
            left = left.next

    while right != None:
        if right.value >= x:
            right = right.next
    
    if left == None or right == None:
        return myList.head
    
    tailLeft = left
    headLeft = left
    while left.next != None:
        if left.next.value < x:
            tailLeft.next = left.next
            tailLeft = tailLeft.next
            left = left.next
        else:
            left = left.next

    tailRight = right
    headRight = right
    while right.next != None:
        if right.next.value >= x:
            tailRight.next = right.next
            tailRight = tailRight.next
            right = right.next
        else:
            right = right.next
    
    tailLeft.next = headRight
    headRight.next = None

    return headLeft