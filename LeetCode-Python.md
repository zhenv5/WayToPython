# LeetCode-Python

<!-- create time: 2015-09-19 17:20:23  -->

<!-- This file is created from $MARBOO_HOME/.media/starts/default.md
本文件由 $MARBOO_HOME/.media/starts/default.md 复制而来 -->

### Compare Version Numbers

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

0.0 < 1.0.0 = 1.0

#### Solutions

```Python
def compareVersion(self, version1, version2):
    v1, v2 = self.helper(version1), self.helper(version2)
    return 1 if v1 > v2 else (-1 if v1 < v2 else 0)

def helper(self, v):
    v = map(int, v.split("."))
    # tackle tailing 0 case: 1.0.0 vs 1
    i = len(v)-1
    while i >= 0 and v[i] == 0:
        i -= 1
    return v[:i+1]
```

#### Highlight

* map
* compare two lists

### Single Number

Description:

Given an array of integers, every element appears twice except for one. Find that single one.

Your algorithm should have a linear runing time complexity. Can you implement it without using extra memory.

How to solve it:

* using a set
* using a dict
* bitwise operation
* sum difference
* reduce,lambda functions

```Python
def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res

def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)

def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)

def singleNumber(self, nums):
    return reduce(operator.xor, nums)
```