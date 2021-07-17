class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #main idea:
        #create a dictionary of format: {-sum : [(index1, index2), (index1, index2), ...]}
        #-sum because that's our target value
        #create and return a set of triplets that fulfill requirements
        
        #edge cases:
        if len(set(nums)) == 1 and len(nums) > 2:
            if nums[0] == 0:
                return [[0,0,0]]
            else:
                return []
        
        if len(set(nums)) == 3:
            myset = set(nums)
            myret = []
            mysum = 0
            for num in myset:
                mysum += num
            if mysum == 0:
                myret.append(myset)
            
            if 0 in myset and [0,0,0] not in myret and nums.count(0) > 2:
                myret.append([0,0,0])
            return myret
        
        pairs = {}
        
        #create the list of pairs w/ indices O(n^2)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                psum = -(nums[i] + nums[j])
                if psum in pairs:
                    #retrieve, update, and replace the list of index pairs
                    plist = pairs[psum]
                    plist.append((i, j))
                    pairs[psum] = plist
                else:
                    #put a new list in for psum
                    pairs.update({psum : [(i, j)]})
            
        triplets = set()
            
        #print(pairs)
            
        #create a list of triplets that fulfill conditions O(n * len(pairs[pnum])) (worst case n^3, but should not really happen)
        for i in range(0, len(nums)):
            if nums[i] in pairs:
                pairlist = pairs[nums[i]]
                for pair in pairlist:
                    #check that the indices don't match
                    if i != pair[0] and i != pair[1]:
                        #check that values don't match
                        if ((nums[pair[0]], nums[pair[1]], nums[i]) not in triplets
                            and (nums[pair[0]], nums[i], nums[pair[1]]) not in triplets
                            and (nums[pair[1]], nums[pair[0]], nums[i]) not in triplets
                            and (nums[pair[1]], nums[i], nums[pair[0]]) not in triplets
                            and (nums[i], nums[pair[0]], nums[pair[1]]) not in triplets
                            and (nums[i], nums[pair[1]], nums[pair[0]]) not in triplets):
                            
                            triplets.add((nums[pair[0]], nums[pair[1]], nums[i]))
        #print(triplets)
        
        return triplets

#runtime: O(n^3) (usually faster)
#memory: O(n^2)