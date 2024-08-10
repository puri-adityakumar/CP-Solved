# https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1

class Solution:

    #Function to rotate a linked list.
    def rotate(self, head, k):
        temp = head

        while(temp.next):
            temp = temp.next
        for i in range(k):
            new = head
            head = head.next
            new.next = None
            temp.next = new
            temp = temp.next
        return head

