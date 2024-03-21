"""
最大容量问题
输入一个数组 ，其中的每个元素代表一个垂直隔板的高度。数组中的任意两个隔板，
以及它们之间的空间可以组成一个容器。
"""

def maxArea(arr: list[int]):
    left = 0
    right = len(arr) -1
    area = 0
    while left < right:
        temp = min(arr[left], arr[right]) * (right-left)
        area = max(area, temp)
        if arr[left] < right:
            left += 1
        else:
            right -= 1
    return area


if __name__ == "__main__":
    arr = [3, 8, 5, 2, 7, 7, 3, 4]
    print(maxArea(arr))