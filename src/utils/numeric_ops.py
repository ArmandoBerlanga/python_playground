def find_max(nums):
    maximum = nums[0]

    for i in range (1, len(nums)):
        if nums [i] > maximum:
            maximum = nums [i]

    return maximum

def findMedianSortedArrays(nums1, nums2):
    
    if len(nums1) == 0 and len(nums2) == 0:
        return 0
    elif len(nums2) == 0:
        nums1.__add__(nums2)
    else:
        for n in nums2:
            nums1.append(n)

    nums1.sort()

    mitad = int(round(len(nums1)/2, 1))
    if (len(nums1) % 2 != 0):
        return nums1[mitad]

    else:
        return (nums1[mitad] + nums1[mitad-1])/2