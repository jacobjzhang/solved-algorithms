"""
 https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list
 
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    if head is None:
        return Node(data, None)
    else:
        current = head
        # PrintNodes(current)
        while current.next is not None:
            current = current.next
        
        # at this point, there is no current.next
        # so we define it as the newest add
        current.next = Node(data, None)
        return head

def PrintNodes(head):
    if head is not None:
        print('Node ', head.data)
        PrintNodes(head.next)