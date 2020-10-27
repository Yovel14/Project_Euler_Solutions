'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109


'''


def searchRange(nums, target):#solution using binary search
    def Find(a):#find possible ocurence of a
        length = len(nums)
        low = 0
        high = length-1
        possible_occurrence = length
        while low <=high:
            mid = low +(high-low)//2
            if nums[mid]>=a:
                possible_occurrence = mid
                high = mid-1
                continue
            else: low  = mid+1
        return possible_occurrence
    #note if target not in nums returns the same value as find(targer+1)
    FirstPos = Find(target)#find first occurence of target
    LastPos = Find(target+1)-1#find first occurence of target+1 and than remove one from the index to get last occurence of target
    return [FirstPos,LastPos] if FirstPos<=LastPos else [-1,-1]
