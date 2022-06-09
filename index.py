# Problem No. 1 Solution 1

# 0(n^2) time | 0(1) space
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetResult = 10

def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
    	  for j in range(i + 1, len(array)):
              if array[i] + array[j] == targetSum:
                  return [array[i], array[j]]
    return []

print(twoNumberSum(array,targetResult))


# Problem No. 1 Solution 2

# 0(nLog(n)) time | O(1) space
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetResult = 10


def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
