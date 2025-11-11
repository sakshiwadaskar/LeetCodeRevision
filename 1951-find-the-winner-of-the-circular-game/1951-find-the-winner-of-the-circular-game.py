class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque(range(1, n + 1))

        while len(q) > 1:
            for i in range(k-1):
                val = q.popleft()
                q.append(val)

            q.popleft()


        return q[0]