#Reference :https://www.youtube.com/watch?v=OTtbG8lNNW8&ab_channel=Michelle%E5%B0%8F%E6%A2%A6%E6%83%B3%E5%AE%B6
class Solution:
    def twoSum(self, nums, target):
        
        #建立空字典
        dict = {}
        
        for i in range(len(nums)): #檢查nums[]所有值
            if target - nums[i] not in dict: #如果target - nums[i]的值不在dict
                dict[nums[i]] = i #將其存到dict[]
            else:
                return [dict[target-nums[i]], i] #最後return 結果
