def twoSum(nums, target):
    comps = {}
    
    for i in range(len(nums)):
        currNum = nums[i]
        
        diff = target - currNum
        
        if currNum in comps:
            return [comps[currNum], i]
        
        comps[diff] = i