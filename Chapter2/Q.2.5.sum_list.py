from linked_list import LinkedList

# Sum Lists: You have two numbers represented by a linked list, where each node contains a single 
#digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a 
#function that adds the two numbers and returns the sum as a linked list. 
#EXAMPLE 
#Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. 
#Output: 2 -> 1 -> 9. That is, 912. 


def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = NumericLinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(result % 10)
        carry = result // 10

    if carry:
        ll.add(carry)

    return ll

# O(N) time, O(N) space



class NumericLinkedList(LinkedList):
    @classmethod
    def generate_from_integer(cls, integer):
        integer_parts = [int(c) for c in str(integer)]
        integer_parts.reverse()
        return cls(integer_parts)

    def numeric_value(self):
        number = 0
        for place, node in enumerate(self):
            number += node.value * 10**place
        return number

#FOLLOW UP 
#Suppose the digits are stored in forward order. Repeat the above problem. 
#Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. 
#Output: 9 -> 1 -> 2. That is, 912. 

# Plan: 1. Reverse the lists and call the function above.
#       2. Use stack.

def sum_lists_followup(l1, l2):
    s1 = []
    cur1= l1.head

    while cur1:
        s1.append(cur1.value)
        cur1 = cur1.next

    s2 = []
    cur2= l2.head

    while cur2:
        s2.append(cur2.value)
        cur2 = cur2.next

    s3 = []
    carry = 0

    while len(s1) != 0 and len(s2) != 0:
        num = s1.pop() + s2.pop() + carry
        s3.append(num%10)
        carry = num//10

    
    if len(s1) != 0:
        s3.append(s1.pop()+carry)
        carry = 0
    
    elif  len(s2) != 0:
        s3.append(s2.pop()+carry)
        carry = 0
    
    ll = NumericLinkedList()

    while len(s3) != 0:
        num = s3.pop()
        ll.add(num)
    return ll
    

        

test_cases = (
    # all values can either be list of integer or integers
    # a, b, expected_sum
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    (0, 0, 0),
    ([], [], 0),
    ([3, 2, 1], [3, 2, 1], [6, 4, 2]),
    (123, 123, 246),
    (123, 1, 124),
    (1, 123, 124),
)

testable_functions = (
    sum_lists,
)


def test_numeric_linked_list():
    ll = NumericLinkedList.generate_from_integer(321)
    assert ll.numeric_value() == 321


def test_linked_list_addition():
    for f in testable_functions:
        for a, b, expected in test_cases:
            print(f"{f.__name__}: {a}, {b}, {expected}")
            if isinstance(a, int):
                ll_a = NumericLinkedList.generate_from_integer(a)
            else:
                ll_a = NumericLinkedList(a.copy())

            if isinstance(b, int):
                ll_b = NumericLinkedList.generate_from_integer(b)
            else:
                ll_b = NumericLinkedList(b.copy())
            result = f(ll_a, ll_b)
            if isinstance(expected, int):
                assert result.numeric_value() == expected
            else:
                assert result.values() == expected


def example():
    ll_a = LinkedList.generate(4, 0, 9)
    ll_b = LinkedList.generate(3, 0, 9)
    print(ll_a)
    print(ll_b)
    #print(sum_lists(ll_a, ll_b))
    print(sum_lists_followup(ll_a, ll_b))


if __name__ == "__main__":
    example()