'''
(size of each row can be different)
Eg1
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Eg2
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
'''
class Solution(object):
    def findDiagonalOrder(self, nums):
        res = []
        for i, r in enumerate(nums):
            for j, a in enumerate(r):
                if len(res) <= i + j:
                    res.append([])
                res[i + j].append(a)
        return [a for r in res for a in reversed(r)]


'''
Zigzag

so 2 key facts:
1. Diagonals are defined by the sum of indicies in a 2 dimensional array
2. The snake phenomena can be achieved by reversing every other diagonal level, therefore check if divisible by 2
'''

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        d={}
		#loop through matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
				#if no entry in dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
				#If you've already passed over this diagonal, keep adding elements to it!
                    d[i+j].append(matrix[i][j])
		# we're done with the pass, let's build our answer array
        ans= []
		#look at the diagonal and each diagonal's elements
        for entry in d.items():
			#each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
			#snake time, look at the diagonal level
            if entry[0] % 2 == 0:
				#Here we append in reverse order because its an even numbered level/diagonal. 
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans
        