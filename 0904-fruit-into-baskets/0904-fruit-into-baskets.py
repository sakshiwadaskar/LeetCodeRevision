class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        # keep baskets in the map
          # - increase count of visiting fruit if you can fit in your basket
        # count of map should not exceed > 2

        count_map = {} # fruit_type -> count
        i = 0
        res = 0
        for j in range(len(fruits)):
            count_map[fruits[j]] = 1 + count_map.get(fruits[j], 0)

            while len(count_map) > 2:
                count_map[fruits[i]] -= 1
                if count_map[fruits[i]] == 0:
                    del count_map[fruits[i]]
                i += 1

            res = max(res, (j - i + 1))
            j += 1

        return res

        