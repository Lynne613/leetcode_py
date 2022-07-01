class Solution:
    def twoSum(self, nums, target):
        
        #建立空字典
        dict = {}
        
        for i in range(len(nums)): #檢查nums[]所有值
            if target - nums[i] not in dict: #如果target - nums[i]的值不在dict
                dict[nums[i]] = i #將其存到dict[]
            else:
                return [dict[target-nums[i]], i] #最後return 結果
