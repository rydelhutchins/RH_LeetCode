class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        val = 3
        [3, 3, 4, 5, 6, 3, 4]
         L
         R
            L
            R
               L
               R
               L
                  R
               L
                     R
                  L
                        R
                  L
                           R
        """

        l = 0
        for r in range(0, len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l
            
