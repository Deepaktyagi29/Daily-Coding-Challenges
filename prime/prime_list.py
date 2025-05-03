class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def primeList(self, head):
        primes = self.sieve(10010)
        pset = set(primes)
        curr = head
        while curr:
            if curr.val in pset:
                curr = curr.next
                continue
            i = 1
            while True:
                if (curr.val - i) in pset:
                    curr.val = curr.val - i
                    break
                if (curr.val + i) in pset:
                    curr.val = curr.val + i
                    break
                i += 1
            curr = curr.next
        return head

    def sieve(self, n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n + 1, i):
                    is_prime[j] = False
        return [i for i, val in enumerate(is_prime) if val]

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

values = [10, 15, 20, 25]
head = create_linked_list(values)
sol = Solution()
new_head = sol.primeList(head)
print_linked_list(new_head)
