class Solution:
    def leaders(self, arr):
        # code here
        leader = []
        max_right = float('-inf')
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>=max_right:
                leader.append(arr[i])
                max_right = arr[i]
        leader.reverse()
        return leader
