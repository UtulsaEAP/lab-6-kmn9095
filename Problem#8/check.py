def in_order(nums):
    # Check if the list is empty or has only one element (already sorted)
    if len(nums) <= 1:
        return True
    
    # Iterate through the list from index 1 to the end
    for i in range(1, len(nums)):
        # Compare the current element with the previous one
        if nums[i] < nums[i - 1]:
            # Not in order
            return False
        
    # Check if the list is sorted in descending order
    descending = all(nums[i] >= nums[i - 1] for i in range(1, len(nums)))
    
    if descending:
        return True  # In order (descending)
    else:
        return True  # In order (ascending)

if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
