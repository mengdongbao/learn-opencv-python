import numpy as np

n1 = np.array([1,2,3])
n2 = np.array([.1,.2,.3])
n3 = np.array([[1,2],[3,4]])
# print(n1)
# print(n2)
# print(n3)
# print(n3.dtype)
# print(type(n3[0]))

# nd1 = [1,2,3]
# nd2 = np.array(nd1, ndmin=3)
# print(nd2)

# 用空填充
# print(np.empty((2,3)))
# 用 0 填充
# print(np.zeros((3,3), np.uint8))

# 用 1 填充
# print(np.ones([3,3], np.uint8))

# 随机数组 [1, 100)
# print(np.random.randint(1, 100, (3,2)))

# 数组运算
# n1 = np.array(
#     [
#         [1,2],
#         [3,4]
#     ]
#     )
# n2 = np.array(
#     [
#         [5,6], 
#         [7,8]
#     ]
#     )
# print(n1 + n2)
# print(n1 * n2)
# print(n1 >= n2)

# 数组复制
n1 = np.array([1,2], np.uint8)
n2 = np.copy(n1)
n1[0] = 3
print(n1, n2)
