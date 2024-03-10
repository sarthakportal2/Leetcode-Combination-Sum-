class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      #using Dynamic Programming (DP) approach
      #min rumtime(30ms) T(C(N)) =O(n**2) and S(C(N))=O(N) as it reuires contiguous memory allocation iterating at its each level 
        dp=[[] for _ in range(1+target)]#List Declare
        for c in candidates:#Candadates Iteration
            for t in range(1,target+1):#target Iteration
                if c>t:continue#go to Next out of the iteration(target)
                if c==t:dp[t].append([c])#appending the candiates in target's inintalized list
                for l in dp[t-c]:dp[t].append(l+[c])#Appedning the prev candidate val in current target val within next iteration
        
        return dp[-1]#printing the output list 
