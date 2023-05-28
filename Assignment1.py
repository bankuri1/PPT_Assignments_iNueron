#!/usr/bin/env python
# coding: utf-8

# ### Assignment1

# ### <aside>
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# You can return the answer in any order.
# 
# **Example:**
# Input: nums = [2,7,11,15], target = 9
# Output0 [0,1]
# 
# **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1][
# 

# In[3]:


def twoSum(nums, target):
   

    num_lst = list(range(len(nums)))

    for indx, num in enumerate(num_lst):
        for num_other in num_lst[indx+1:]:
            if nums[num] + nums[num_other] == target:
                return [num, num_other]
            else: 
                continue
    return None


# In[4]:


nums=[2,7,11,15]
target=9
twoSum(nums,target)


# ### <aside>
# Q2. Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# 
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# 
# - Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# - Return k.
# 
# **Example :**
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_*,_*]
# 
# **Explanation:** Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)[
# </aside>
# 

# In[10]:


def arr(nums,val):
    count=0
    num_list=list(range(len(nums)))
    for i,num in enumerate(num_list):
        if nums[num]!=val:
            count=count+1
        else:
            continue
    return count


# In[13]:


nums=[2,3,3,2]
val=3
arr(nums,val)


# ### <aside>
# Q3. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# **Example 1:**
# Input: nums = [1,3,5,6], target = 5
# 
# Output: 2
# </aside>

# In[22]:


def searchInsert( nums, target):
       
        start = 0
        end = len(nums) - 1
        
      
        while (start <= end):
            
            mid = int((start + end)/2)
             
           
            if nums[mid] == target:
                return mid
            
           
            elif target > nums[mid]:
                start = mid + 1
                
            
            else:
                end = mid -1
      
        return end + 1


# In[25]:


nums = [1,3,4,6]
target = 5
searchInsert(nums,target)


# In[27]:


nums = [1,3,5,6]
target = 5
searchInsert(nums,target)


# ### <aside>
# 💡 **Q4.** You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# 
# Increment the large integer by one and return the resulting array of digits.
# 
# **Example 1:**
# Input: digits = [1,2,3]
# Output: [1,2,4]
# 
# **Explanation:** The array represents the integer 123.
# 
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# 
# </aside>

# In[49]:


def increment(nums):
    i=len(nums)-1
    print(i)
    while i >=0 and nums[i]==9 :
        i=i-1
   
    if i==-1 :
        result=[0]*(len(nums)+1)
        result[0]=1
        return result
    else:
        result=[0]*(len(nums))
        result[i]=nums[i]+1
        for j in range(i-1,-1,-1):
            result[j]=nums[j]
    return result
        
        


# In[50]:


nums=[9,9,9,8]
increment(nums)


# In[51]:


nums=[9,9,9,9]
increment(nums)


#  ### <aside>
# 💡 **Q5.** You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# 
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# 
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# 
# **Example 1:**
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# 
# **Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# 
# </aside>

# In[106]:


def twoArray(nums1, m, nums2, n):
       
        i = int(m - 1)
        j = int(n - 1)
        k = int(m + n - 1)
        
        while (k >= 0):
            if i>=0 and j>=0:
                if(nums2[j] > nums1[i]):
                    nums1[k] = nums2[j]
                    k -= 1
                    j -= 1
                else:
                    nums1[k] = nums1[i]
                    k -= 1
                    i -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                break
        return nums1


# In[107]:


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
twoArray(nums1,m,nums2,n)


# ### <aside>
# Q6.Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# 
# **Example 1:**
# Input: nums = [1,2,3,1]
# 
# Output: true
# 
# </aside>

# In[145]:


def arr(nums):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums),1):
           
            if nums[i]==nums[j]:
                return True
                
           
        
    return False
        


# In[150]:


nums = [1,2,9,10,3]
arr(nums)


# In[151]:


nums = [1,2,3,1]
arr(nums)


# ### <aside>
# Q7. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# **Example 1:**
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# </aside>

# In[172]:


def ele(nums):
    count=0
    k=0
    for i in range(len(nums)):
        if nums[i]!=0:
            k=k+1
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[count]=nums[i]
            count=count+1
    count=k
  
    while count < len(nums):
        nums[count] = 0
        count += 1

    return nums  


# In[173]:


nums= [0,1,0,3,12]
ele(nums)


# ### <aside>
# Q8.You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# 
# You are given an integer array nums representing the data status of this set after the error.
# 
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
# 
# **Example 1:**
# Input: nums = [1,2,2,4]
# Output: [2,3]
# 
# </aside>

# In[177]:


def missing(nums):
    for i in range(len(nums)):
        if nums[i]==nums[i+1]:
            return [nums[i],nums[i]+1]


# In[178]:


nums = [1,2,2,4] 
missing(nums)


# In[ ]:




