from linked_list import LinkedList

# Question: Implement a function to check if a linked list is a palindrome. 

# Clarify: Is additional data structure allowed?

# Plan:Reverse and Compare 
# Our first solution is to reverse the linked list and compare the reversed list to the original list.
# Time O(N), space O(N)

# Improvement: We can only push half of the list to stack and compare whether it is the same as the remaining halg.

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

def example():
    ll_a = LinkedList.generate(3, 1, 2)
    ll_b = LinkedList.generate(3, 0, 9)
    print(ll_a, isPalindrome(ll_a))
    print(ll_b,isPalindrome(ll_b))



if __name__ == "__main__":
    example()