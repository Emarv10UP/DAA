class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge_sort(left: int, right: int):
            if left >= right:
                return
            
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            
            # Optimization: Skip merge step if already in order
            if nums[mid] <= nums[mid + 1]:
                return
            
            # Merge the two sorted halves into temporary buffer
            i, j, k = left, mid + 1, left
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1
            
            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1
                
            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1
                
            # Copy back to the main array
            nums[left:right + 1] = temp[left:right + 1]

        temp = [0] * len(nums)
        merge_sort(0, len(nums) - 1)
        return nums
