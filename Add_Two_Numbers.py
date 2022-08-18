'''
1. Traverse through the lists and compute the number, then add and finally serve it to the listnode()

Runtime 146 ms
Memory	14 MB

'''
'''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        k1, k2, n1, n2 = 0, 0, 0, 0
        while l1:
            n1 += l1.val * 10 ** k1
            l1 = l1.next
            k1 += 1
        while l2:
            n2 += l2.val * 10 ** k2
            l2 = l2.next
            k2 += 1
        num = n1 + n2
        ans = cur = ListNode(0)
        if num == 0: return ans
        while num:
            cur.next = ListNode(num % 10)
            num //= 10
            cur = cur.next
        return ans.next
'''

'''
2. Adding them simultaneously and use carry if the number is too big

Runtime 92 ms	
Memory	13.9 MB

'''

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = cur = ListNode(0)
        add = 0
        while l1 or l2:
            val = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + add
            add = val // 10
            cur.next = ListNode(val % 10)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if add:
            cur.next = ListNode(add)
        return ans.next


'''
3. Converting them to strings, then to int and add them and serve to listnode()

Runtime 153 ms	
Memory	13.9 MB

'''
'''
        value_1, value_2 = "", ""
        final_result = 0
        while l1:
            value_1 = str(l1.val) + value_1
            l1 = l1.next
        
        while l2:
            value_2 = str(l2.val) + value_2
            l2 = l2.next
            
        final_result = int(value_1) + int(value_2)
        
        dummy = temp = ListNode()
        
        for i in reversed(str(final_result)):
            temp.next = ListNode(int(i))
            temp = temp.next
        
        return dummy.next
'''