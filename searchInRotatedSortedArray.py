#neetcode 18
class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        # loop to get the index of the target
        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # to check if the left side is sorted
            if nums[mid] >= nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:  # to check if the right side is sorted
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    sol = Solution()
    answer = sol.search(nums, target)
    print(answer)