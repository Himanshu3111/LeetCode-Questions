class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Kind 1: each number is followed by (number + 1)
        is_asc = all(nums[(i + 1) % n] == (nums[i] + 1) % n for i in range(n))
        # Kind 2: each number is followed by (number - 1)
        is_desc = all(nums[(i + 1) % n] == (nums[i] - 1) % n for i in range(n))

        if not is_asc and not is_desc:
            return -1

        p = nums.index(0)           # position of 0

        if is_asc:
            if p == 0:
                return 0            # already sorted
            return min(p, n - p + 2)

        r = nums.index(n - 1)       # position of the biggest number
        return min(n - p, r + 1)
