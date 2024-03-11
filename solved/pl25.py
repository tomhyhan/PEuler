# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"
        
# class Solution:
#     def move_node(self, node, k):
#         while k > 0:
#             node = node.next
#             if node is None:
#                 return None
#             k -= 1
#         return node

#     def reverseKGroup(self, head, k: int):
#         matchings = []
#         if k == 1:
#             return head
#         for i in range(k):
#             if i >= k-i-1:
#                 break
#             left = self.move_node(head, i)
#             right = self.move_node(head, k-i-1)
#             matchings.append([left, right])    
#         while True:
#             did_step = False
#             for i in range(len(matchings)):
#                 left, right = matchings[i]
#                 left.val, right.val = right.val, left.val, 
#                 new_left = self.move_node(left,k)
#                 new_right = self.move_node(right,k)
#                 if new_left is None or new_right is None:
#                     did_step = True
#                 matchings[i] = [new_left, new_right]
#             if did_step:
#                 return head

class Solution:
    def move_node(self, head, k, node_left):
        if node_left < k:
            return head
        
        prev = None
        next_ = None
        cnt = 0
        current = head

        while cnt < k:
            next_ = current.next 
            current.next = prev
            prev, current = current, next_ 
            node_left -= 1
            cnt += 1
        
        if current:
            head.next = self.move_node(current, k, node_left)

        return prev
    
    def reverseKGroup(self, head, k: int):
        node_left = 0
        current = head
        while current:
            current = current.next
            node_left += 1

        return self.move_node(head, k, node_left)
    
# [1,2,3,4,5]
s = Solution()
node = ListNode(1)
current = node
for i in range(2,5):
    current.next = ListNode(i)
    current = current.next

node = s.reverseKGroup(node, 4)
print(node.val)
print(node.next)
print(node.next.next)
print(node.next.next.next)
