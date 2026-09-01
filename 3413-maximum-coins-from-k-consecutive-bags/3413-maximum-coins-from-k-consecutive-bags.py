from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort(key=lambda x: x[0])
        n = len(coins)

        l = [c[0] for c in coins]
        r = [c[1] for c in coins]
        val = [c[2] for c in coins]

        # prefix[i] = total coins in segments[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + val[i] * (r[i] - l[i] + 1)

        def window_sum(s: int, e: int) -> int:
            """Coins covered by the closed window [s, e]."""
            # first segment whose r >= s (could contain s, or be just after a gap)
            i = bisect_left(r, s)
            # last segment whose l <= e
            j = bisect_right(l, e) - 1

            if i > j or i == n:
                return 0

            total = prefix[j + 1] - prefix[i]

            # trim the part of segment i that lies before s
            if l[i] < s:
                total -= (s - l[i]) * val[i]

            # trim the part of segment j that lies after e
            if r[j] > e:
                total -= (r[j] - e) * val[j]

            return total

        best = 0
        for i in range(n):
            # window whose left edge aligns with this segment's start
            best = max(best, window_sum(l[i], l[i] + k - 1))
            # window whose right edge aligns with this segment's end
            best = max(best, window_sum(r[i] - k + 1, r[i]))

        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumCoins([[8, 10, 1], [1, 3, 2], [5, 6, 4]], 4))  # 10
    print(sol.maximumCoins([[1, 10, 3]], 2))  # 6