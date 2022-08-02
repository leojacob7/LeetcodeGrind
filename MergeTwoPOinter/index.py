def insertPos(position, nums, element, leng):
    # print("Input at insertPos", position, nums, element, leng, len(nums))
    print()
    index = len(nums) - 1
    if position != leng-1:
        while index > position:
            nums[index] = nums[index - 1]
            index -= 1
        print("nums after shifting", nums, position, element)
        nums[position] = element
    else:
        nums.append(element)
    return nums


def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j = 0, 0
    while i < m and j < n:
        if(nums1[i] < nums2[j]):
            i += 1
        if(nums1[i] > nums2[j]):
            print("inserting before", nums1)
            nums1 = insertPos(i, nums1, nums2[j], m + n)
            print("inserting here", nums1, i, j)
            j += 1
            # i += 1
        if nums1[i] == nums2[j]:
            print(nums1[i], nums2[j])
            nums1 = insertPos(i, nums1, nums2[j], m + n)
            # print("here", nums1)
            # i += 1
            j += 1

    print("nums result", nums1, i, m, j, n)
    if(j < n):
        while j != n:
            print("nums1", nums1, i, m, j, n)
            # if(i > m):
            #     nums1.append(nums2[j])
            # else:

            i += 1
            nums1 = insertPos(i, nums1, nums2[j], m + n)
            j += 1
    if n == 0:
        nums1 = nums1[:m]
    print("Result", nums1)


merge([1, 0],
      1,
      [2, 5, 6],
      3)
