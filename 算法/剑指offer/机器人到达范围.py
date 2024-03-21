class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 方法2: 经典DFS, 递归+visit集合
        v = {(0, 0)}

        def getSum(x):
            # 求数位和, 即循环累加模10的结果然后除以10即可
            res = 0
            while x:
                res += x % 10
                x //= 10
            return res
            # 注意: 这里也可以将数字转换成字符串, 然后逐位字符转int求sum
            # return sum([int(c) for c in str(x)])

        def isValid(r, c):
            # 判断某个下标是否有效: 是否在方格内/行列数位和是否不大于k/是否被访问过
            return 0 <= r < m and 0 <= c < n and getSum(r) + getSum(c) <= k and (r, c) not in v

        def dfs(r, c):
            for rr, cc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if isValid(rr, cc):
                    # 如果邻居有效的话, 将其加入集合中, 递归调用dfs该邻居
                    v.add((rr, cc))
                    dfs(rr, cc)
        # 初始从起点开始dfs
        dfs(0, 0)
        return len(v)
