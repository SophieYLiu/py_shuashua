# DFS + Mem - this is like top down DP: (n is num of coins)
# without mem, O(n^k) where k is the max steps to get to bottom of tree, it is related to the min face value and target amount
# with mem, O(n*amount) coz there are these much states computed

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(rem, mem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if rem in mem:
                return mem[rem]

            min_step = float('inf')
            for coin in coins:
                temp = dfs(rem-coin, mem)
                if temp != -1:
                    min_step = min(temp + 1, min_step)  # 注意这里
            mem[rem] = -1 if min_step == float('inf') else min_step
            return mem[rem]
        
        return dfs(amount, collections.defaultdict(int))

# DFS + Mem(另一种写法，去掉lru_cache就是without mem的写法)
		@lru_cache(None)
		def dfs(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0

            min_step = float('inf')
            for coin in coins:
                temp = dfs(rem-coin)
                if temp != -1:
                    min_step = min(temp + 1, min_step)
            return min_step if min_step != float('inf') else -1


# DP (bottom up)
	def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [float('inf')]*(amount+1)
        mem[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    mem[i] = min(mem[i], mem[i-coin]+1)
        return mem[amount] if mem[amount] != float('inf') else -1

