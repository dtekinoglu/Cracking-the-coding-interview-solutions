# Question: Implement a function to check if a linked list is a palindrome. 

# Clarify: Is additional data structure allowed?

# Plan:Reverse and Compare 
# Our first solution is to reverse the linked list and compare the reversed list to the original list.

def isPalindrome(ll):

    cur = ll.head
    aList =[]

    while cur:
        aList.append(cur.value)
        cur = cur.next
    
    cur = ll.head

    while cur:
        elem = aList.pop()
        if cur.value != elem:
            return False
        cur = cur.next
    
    return True

