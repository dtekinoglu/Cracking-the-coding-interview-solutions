from linked_list import LinkedList
# Question: Loop Detection: Given a circular linked list, implement an algorithm 
# that returns the node at the beginning of the loop. 

# What if is is an empty list? or with one element? What to return?

# Plan: If I move two pointers with different speeds, do they intersect?

# Let slow move 1 node and fast 2 nodes at a time. They must eventually meet in the loop.
# Assume fast hop over the slow (i) and go to (i+1). Then, they should have met in i-1.
# After they enter to the loop, fast come closer by 1 at each step.

# Where do they collide?
# Assume length of non-loop part is k.
# When slow enters to loop, fast moves 2k. k inside the loop. 
# So fast will be k % len(loop) node of the loop.
# len(loop) - k%len(loop) will be the collision point. which is k%len(loop) before the start of the loop.

# Now, put a pointer to the head. Move collision point and this one together. 
# They will collide at the start of the loop.

def detect_loop(ll):

    fast = ll.head
    slow = ll.head

    while fast != None and fast.next != None:  # No need to check slow since it will be behind if no loop.
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    
    if fast == None or fast.next == None:
        return None
    
    cur = ll.head
    while cur != slow:
        cur = cur.next
        slow = slow.next
    return cur

# Time O(N), space O(1)

def test_loop_detection():
    looped_list = LinkedList(["A", "B", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    tests = [
        (LinkedList(), None),
        ((LinkedList((1, 2, 3))), None),
        (looped_list, loop_start_node),
    ]

    for ll, expected in tests:
        assert detect_loop(ll) == expected

if __name__ == "__main__":
    test_loop_detection()
