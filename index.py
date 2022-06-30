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


print(twoNumberSum(array, targetResult))


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


# Problem No. 2

def validateSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

# Problem No. 3

# O(nlogn) time | o(n) space


def sortedSquaredArray(array):
    squares = [0 for _ in array]

    for num in range(len(array)):
        value = array[num]
        squares[num] = value * value

    squares.sort()
    return squares

# Problem No. 4


def tournamentWinner(competitions, results):
    teams = {"": 0}
    i = 0
    currentBestTeam = ""
    while i < len(competitions):
        homeTeam = str(competitions[i][0])
        awayTeam = str(competitions[i][1])
        if results[i] == 1:
            if homeTeam in teams:
                teams[homeTeam] += 3
            else:
                teams[homeTeam] = 3
                currentBestTeam = homeTeam if teams[currentBestTeam] < teams[homeTeam] else currentBestTeam

        else:
            if awayTeam in teams:
                teams[awayTeam] += 3
            else:
                teams[awayTeam] = 3
            currentBestTeam = awayTeam if teams[currentBestTeam] < teams[awayTeam] else currentBestTeam
        i += 1

    return currentBestTeam

# Problem No. 5


def nonConstructibleChange(coins):
    coins.sort()
    minimum_change = 0
    for coin in coins:
        if coin > minimum_change + 1:
            break
        minimum_change += coin
    return minimum_change + 1

#Problem No. 6

def findClosestValueInBst(tree, target, closest = None):
    if tree is None:
        return closest
    if closest is None or abs(target - closest) > abs(target - tree.value):
            closest = tree.value
    if target < tree.value:
        return findClosestValueInBst(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBst(tree.right, target, closest)
    else:
        return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#Problem No. 7

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    stack = [(root, 0)]
    branchSumValues = []
    while len(stack) > 0:
        current, sumValue = stack.pop()
        if current.left is None and current.right is None:
            branchSumValues.append(sumValue+current.value)

        if current.left is not None:
            stack.append((current.left, sumValue+current.value))
        if current.right is not None:
            stack.append((current.right, sumValue+current.value))
            
    branchSumValues.reverse()
    return branchSumValues



#Problem No. 8

def nodeDepths(root):
    stack = [root]
    node_depth_sum = [0]

    output = 0

    while len(stack) > 0:
        curr_node = stack.pop()
        curr_sum = node_depth_sum.pop()
        output += curr_sum

        if curr_node.right is not None:
           stack.append(curr_node.right)
           node_depth_sum.append(curr_sum + 1)

        if curr_node.left is not None:
           stack.append(curr_node.left)
           node_depth_sum.append(curr_sum + 1)
    return output



class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None