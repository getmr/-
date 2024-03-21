from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    # DFS + 回溯
    # 针对每一个首字符，找所有可能的字符串
    rows, cols = len(board), len(board[0])
    def dfs(r, c, k):
        # TODO: 递归终止条件
        if k == len(word):
            return True
        for (rr, cc) in ((r + 1, c), (r-1, c), (r, c+1), (r, c-1)):
            if 0 <= rr < len(board) and 0 <= cc < len(board[0]) and board[rr][cc] == word[k]:
                cur, board[rr][cc] = board[rr][cc], "/"
                if dfs(rr, cc, k+1):
                    board[rr][cc] = cur
                    return True
                board[rr][cc] = cur
        return False

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                cur, board[r][c] = board[r][c], "/"
                if dfs(r, c, 1):
                    board[r][c] = cur
                    return True
                board[r][c] = cur

    # 没有找到有效路径， 返回False
    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(exist(board, word))
    print(board)
    word = "SEE"
    print(exist(board, word))
    word = "ABCB"
    print(exist(board, word))
