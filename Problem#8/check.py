def in_order(nums):
    # Type your code here.
    num_list = []
    new_list = nums.copy()

    for _ in range(0, len(new_list)):
        num_list.append(min(new_list))
        new_list.remove(min(new_list))
    
    if num_list == nums:
        return(True)
    
    print(num_list)
    print(nums)
    

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