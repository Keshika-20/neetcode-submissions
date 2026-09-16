class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=sorted(nums)
        n=len(arr)
        result=[]
        for i in range(n):
            if i>0 and arr[i]==arr[i-1]:
                continue
            left=i+1
            right=n-1
            while(left<right):
                s=arr[i]+arr[left]+arr[right]
                if(s>0):
                    right-=1
                elif(s<0):
                    left+=1
                else:
                    result.append([arr[i],arr[left],arr[right]])
                    left+=1
                    right-=1
                    while(left<right and arr[left]==arr[left-1]):
                        left+=1
                    while(left<right and arr[left]==arr[left-1]):
                        right-=1
        return result