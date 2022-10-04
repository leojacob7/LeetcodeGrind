from typing import List, Optional
from ast import List


class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def insert(self, insertVal):
        newNode = ListNode(insertVal)
        if self.head is None:
            self.head = newNode
            return

        tempNode = self.head
        while tempNode.next is not None:
            tempNode = tempNode.next
        tempNode.next = newNode

    def reverseBetween(self, head: Optional[ListNode], first: int, second: int) -> Optional[ListNode]:
        startNode = head

        iter = 1
        # start
        startPrev = head
        while startNode:
            if iter == first:
                break
            iter += 1
            startPrev = startNode
            startNode = startNode.next

        if startNode == None:
            return head

        secondIter = 1
        endNode = self.head
        while endNode:
            if secondIter == second:
                break
            secondIter += 1
            endNode = endNode.next
        if endNode == None:
            return head

        prevNode = endNode.next
        tempNode = head
        curr = startNode
        currIndex = first

        # print(curr.val, curr.next.val)
        flag = 0
        while curr:
            if flag == 1:
                break
            if currIndex == second:
                flag = 1

            tempNode = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = tempNode
            currIndex += 1
        print(startPrev.val == head.val, startPrev.val, head.val)
        if first == 1:
            head = prevNode
            # print("printing nodes", head.val)
            # while prevNode:
            #     print(">>", prevNode.val)
            #     prevNode = prevNode.next
            return head
        else:
            print("outside")
            startPrev.next = endNode
            return head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        firstCurr = list1
        secondCurr = list2
        tempNode = ListNode()
        tempNodeIndex = tempNode
        while firstCurr and secondCurr:
            print(firstCurr.val, secondCurr.val, tempNodeIndex.val)
            if firstCurr.val <= secondCurr.val:
                tempNodeIndex.next = firstCurr
                firstCurr = firstCurr.next
            else:
                tempNodeIndex.next = secondCurr
                secondCurr = secondCurr.next
            tempNodeIndex = tempNodeIndex.next

        if firstCurr == None:
            tempNodeIndex.next = secondCurr
        else:
            tempNodeIndex.next = firstCurr
        return tempNode.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        curr = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        beforeSlow = None
        while slow:
            tempNode = slow.next
            if tempNode is None:
                beforeSlow = slow
            slow.next = prev
            prev = slow
            slow = tempNode
        curr = head
        slow = beforeSlow
        i = 0
        while slow is not None:
            if i == 20:
                break
            i += 1
            t1, t2 = curr.next, slow.next
            curr.next = slow
            slow.next = t1
            slow = t2
            curr = t1

        return head


# [4,-2,-4,0,-2,-2,-1,-2]
#  1, 2, 3,4, 5, 6, 7, 8
# [4,-2,0,-4,-2,-2,-1,-2]
LL1 = LinkedList(ListNode())
LL2 = LinkedList(ListNode())
inputArr = [1, 2, 3, 4]

for i in inputArr:
    LL1.insert(i)

head = LL1.head
nodes = (LL1.reorderList(head))
i = 0
while nodes:
    if i == 10:
        break
    i += 1
    print(">>>", nodes.val)
    nodes = nodes.next
