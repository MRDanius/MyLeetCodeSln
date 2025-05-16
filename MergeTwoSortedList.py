# class Solution():
#     def mergeTwoLists(self, list1, list2):
# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
       
# class ListNode: 
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# node1 = ListNode(1)
# node2 = ListNode(2) 

# node1.next = node2
# node3 = ListNode(4)

# node2.next = node3 

# head = node1
# current = head 

# while current:
#     print(current.val)
#     current = current.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to simplify the merging process
        dummy = ListNode()
        current = dummy
        tail = ListNode(0)
        tail.next = dummy 
        while list1 and list2:
            if list1.val <=  list2.val:
                current.next = list1
                list1 = list1.next
             



