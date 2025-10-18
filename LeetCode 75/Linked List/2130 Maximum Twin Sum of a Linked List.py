# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        i = 0
        node = head
        stack_f = []
        stack_s = []

        while node:
            stack_f.append(node.val)
            i += 1
            node = node.next
            
        # print(i)
        # print(type(stack_f[0]))
            # else:
            #     stack_s.append(node.val)
            #     j += 1

        stack_s = stack_f[(i//2):]
        stack_f = stack_f[:(i//2)]

        # print(list(reversed(stack_s)))
        # print(stack_f)

        return max(list(map(lambda x, y: x + y, stack_f, list(reversed(stack_s)))))
